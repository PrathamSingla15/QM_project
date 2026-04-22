/**
 * ux_review.cjs — Final UX polish screenshot pass.
 * Usage: node ux_review.cjs before|after
 */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE_URL = 'http://127.0.0.1:5173/';
const PASS = process.argv[2] || 'before';
if (!['before', 'after'].includes(PASS)) {
  console.error('Usage: node ux_review.cjs before|after');
  process.exit(2);
}
const OUT_DIR = path.join(__dirname, 'ux_review', PASS);
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

function wait(ms) { return new Promise((r) => setTimeout(r, ms)); }

async function freshLoad(page) {
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  // Wait for Google fonts so Fraunces doesn't fall back mid-screenshot.
  await page.evaluate(() => document.fonts.ready);
  await wait(700);
}

async function shot(page, name) {
  const p = path.join(OUT_DIR, name);
  await page.screenshot({ path: p, fullPage: true });
  console.log('  ->', p);
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1400, height: 900 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();

  // --- 01 Student initial ---
  console.log('01 Student initial');
  await freshLoad(page);
  await page.waitForSelector('article.erickcard', { timeout: 10000 });
  await shot(page, '01_student_initial.png');

  // --- 02 Booking modal open ---
  console.log('02 Booking modal open');
  await freshLoad(page);
  await page.waitForSelector('article.erickcard', { timeout: 10000 });
  // ER-01 is the first non-disabled Book button.
  await page.locator('button.erickcard__book:not([disabled])').first().click();
  await page.waitForSelector('.modal', { timeout: 5000 });
  await wait(400);
  await shot(page, '02_booking_modal_open.png');

  // --- 03 Booking modal dropdown expanded ---
  console.log('03 Booking modal dropdown expanded');
  // Native <select> can't be popped in headless. Turn it into an inline listbox
  // by adding size attribute so optgroups are visible in the screenshot.
  await page.$eval('#dropoff', (el) => {
    el.setAttribute('size', '12');
    el.style.height = 'auto';
  });
  await wait(300);
  await shot(page, '03_booking_modal_dropdown.png');
  // Revert so next interactions behave normally.
  await page.$eval('#dropoff', (el) => el.removeAttribute('size'));
  // Close modal
  await page.keyboard.press('Escape');
  await wait(300);

  // --- 04 Countdown active ---
  console.log('04 Countdown active (after confirm)');
  await freshLoad(page);
  await page.locator('button.erickcard__book:not([disabled])').first().click();
  await page.waitForSelector('.modal', { timeout: 5000 });
  // Pick a specific dropoff so the booking subtitle is interesting.
  await page.selectOption('#dropoff', { label: 'Central Library' }).catch(() => {});
  await page.locator('button.btn-primary', { hasText: 'Confirm' }).click();
  await wait(800);
  await shot(page, '04_countdown_active.png');

  // --- 05 Countdown expired ---
  console.log('05 Countdown expired (force via page.evaluate)');
  // Rather than wait 60s, rewind the active booking deadline into the past
  // by mutating the internal timer. We can't easily reach the reducer from
  // the page, but the reducer's TICK_TIMERS compares p.deadline <= now,
  // so we set the system clock forward by mocking Date.now. Simpler: wait
  // on the actual TICK loop by advancing DATE via context.
  // Instead, trigger a user-driven cancel with reason:'timeout' by
  // dispatching a manual action through a global handle. We don't have a
  // debug handle. Fallback: monkey-patch Date.now in-page, then wait ~1.2s.
  await page.evaluate(() => {
    const realNow = Date.now;
    // Jump 65s forward; next TICK_TIMERS will expire the booking.
    const offset = 65_000;
    Date.now = () => realNow() + offset;
    // Fire a synthetic visibility tick to ensure requestAnimationFrame/
    // setInterval keep working.
  });
  // Wait for the app's 1s tick + useCountdown 200ms to pick it up.
  await wait(1500);
  await shot(page, '05_countdown_expired.png');
  // Reset Date.now in-page for subsequent captures (though we freshLoad next).
  await page.evaluate(() => { /* next freshLoad wipes the patch */ });

  // --- 06 Capacity-full card (ER-02) ---
  console.log('06 Capacity full ER-02');
  await freshLoad(page);
  await page.waitForSelector('article.erickcard', { timeout: 10000 });
  // Hover the ER-02 card to show its state clearly.
  const er02 = page.locator('article.erickcard').filter({ hasText: 'ER-02' }).first();
  await er02.scrollIntoViewIfNeeded();
  await er02.hover().catch(() => {});
  await wait(400);
  await shot(page, '06_capacity_full_er02.png');

  // --- 07 Wallet after top-up ---
  console.log('07 Wallet after top-up');
  await freshLoad(page);
  await page.locator('button.btn-primary', { hasText: 'Top up' }).first().click();
  await wait(400);
  await shot(page, '07_wallet_after_topup.png');

  // --- 08 Driver manifest ---
  console.log('08 Driver manifest');
  await freshLoad(page);
  await page.locator('button[role="tab"]', { hasText: 'Driver' }).click();
  await wait(700);
  await shot(page, '08_driver_manifest.png');

  // --- 09 Driver mark-reached undo toast ---
  console.log('09 Driver reached undo toast');
  // Driver view defaults to ER-04 (3 passengers, all boarded) — switch to ER-01
  // which has 2 boarded passengers seeded; no pending. To show the undo flow
  // we need a booked passenger: create one first as a student.
  await freshLoad(page);
  // Book as student first to create a pending passenger on ER-01.
  await page.locator('button.erickcard__book:not([disabled])').first().click();
  await page.waitForSelector('.modal', { timeout: 5000 });
  await page.locator('button.btn-primary', { hasText: 'Confirm' }).click();
  await wait(500);
  // Switch to Driver, pick ER-01.
  await page.locator('button[role="tab"]', { hasText: 'Driver' }).click();
  await wait(500);
  // Switch vehicle to ER-01 via the manifest select.
  await page.locator('.driver-select').selectOption('ER-01').catch(() => {});
  await wait(500);
  // Click Mark reached on the pending passenger.
  const reachedBtn = page.locator('button.btn-primary', { hasText: 'Mark reached' }).first();
  await reachedBtn.click();
  await wait(400);
  await shot(page, '09_driver_reached_undo.png');

  // --- 10 Driver add-offline form ---
  console.log('10 Driver add-offline form');
  await freshLoad(page);
  await page.locator('button[role="tab"]', { hasText: 'Driver' }).click();
  await wait(600);
  await page.locator('input[placeholder="Student name"]').fill('Aisha T.');
  await page.locator('.off-pax select').selectOption({ index: 3 });
  await wait(400);
  await shot(page, '10_driver_add_form.png');

  // --- 11 Driver add-offline full-block ---
  console.log('11 Driver add-offline full-block (ER-02)');
  await freshLoad(page);
  await page.locator('button[role="tab"]', { hasText: 'Driver' }).click();
  await wait(500);
  await page.locator('.driver-select').selectOption('ER-02');
  await wait(400);
  // ER-02 is 4/4; the form should show the locked copy.
  await page.locator('.off-pax').scrollIntoViewIfNeeded();
  await wait(300);
  await shot(page, '11_driver_add_fullblock.png');

  // --- 12 Admin KPIs ---
  console.log('12 Admin KPIs');
  await freshLoad(page);
  await page.locator('button[role="tab"]', { hasText: 'Admin' }).click();
  await wait(700);
  await shot(page, '12_admin_kpis.png');

  await context.close();

  // --- 13 Narrow viewport 1000x800 ---
  console.log('13 Narrow viewport 1000x800');
  const narrowCtx = await browser.newContext({
    viewport: { width: 1000, height: 800 },
    deviceScaleFactor: 2,
  });
  const narrowPage = await narrowCtx.newPage();
  await narrowPage.goto(BASE_URL, { waitUntil: 'networkidle' });
  await narrowPage.evaluate(() => document.fonts.ready);
  await wait(700);
  await narrowPage.screenshot({
    path: path.join(OUT_DIR, '13_overflow_check_narrow.png'),
    fullPage: true,
  });
  console.log('  ->', path.join(OUT_DIR, '13_overflow_check_narrow.png'));

  await browser.close();
  console.log('\nDone. Output in', OUT_DIR);
}

main().catch((err) => {
  console.error('ux_review failed:', err);
  process.exit(1);
});
