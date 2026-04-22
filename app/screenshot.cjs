/**
 * screenshot.cjs — Playwright screenshot script for E-Rick Campus prototype
 * Usage: node screenshot.cjs
 */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE_URL = 'http://127.0.0.1:5175/';
const OUT_DIR = path.join(__dirname, 'screenshots');

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

async function wait(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1400, height: 900 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();

  // Helper: navigate fresh
  async function freshLoad() {
    await page.goto(BASE_URL, { waitUntil: 'networkidle' });
    await wait(600);
  }

  console.log('Loading page...');
  await freshLoad();

  // -----------------------------------------------------------------------
  // 1. Student map view (default state)
  // -----------------------------------------------------------------------
  console.log('01 — Student map view (default)');
  await wait(500);
  await page.screenshot({
    path: path.join(OUT_DIR, '01_student_map.png'),
    fullPage: true,
  });

  // -----------------------------------------------------------------------
  // 2. E-rick card detail — show cards in the booking column clearly
  //    Take a fresh load to avoid any leftover modal state
  // -----------------------------------------------------------------------
  console.log('02 — E-rick card detail (ER-01 card highlighted)');
  await freshLoad();
  // Wait for cards to render
  await page.waitForSelector('article.erickcard', { timeout: 10000 });
  await wait(300);
  // Screenshot the center column area (clip to card region)
  const centerSection = page.locator('.layout section:nth-child(2)');
  await centerSection.waitFor({ state: 'visible', timeout: 10000 });
  const box = await centerSection.boundingBox();
  if (box) {
    await page.screenshot({
      path: path.join(OUT_DIR, '02_erick_card_detail.png'),
      clip: {
        x: Math.max(0, box.x),
        y: Math.max(0, box.y),
        width: Math.min(800, box.width),
        height: Math.min(700, box.height),
      },
    });
  } else {
    // Fallback: full page
    await page.screenshot({ path: path.join(OUT_DIR, '02_erick_card_detail.png'), fullPage: true });
  }

  // -----------------------------------------------------------------------
  // 3. Booking modal — click Book seat to open modal with dropoff dropdown
  // -----------------------------------------------------------------------
  console.log('03 — Booking modal with drop-off dropdown');
  await freshLoad();
  const bookBtn = page.locator('button.erickcard__book:not([disabled])').first();
  await bookBtn.click();
  await wait(500);
  // Open the select dropdown to show options (click it so it's focused / open)
  const dropoffSelect = page.locator('#dropoff');
  await dropoffSelect.click();
  await wait(400);
  await page.screenshot({
    path: path.join(OUT_DIR, '03_booking_modal.png'),
    fullPage: true,
  });
  // Close modal
  await page.keyboard.press('Escape');
  await wait(300);

  // -----------------------------------------------------------------------
  // 4. Countdown active — after confirming a booking
  // -----------------------------------------------------------------------
  console.log('04 — Countdown active (after booking confirm)');
  await freshLoad();
  const bookBtn2 = page.locator('button.erickcard__book:not([disabled])').first();
  await bookBtn2.click();
  await wait(400);
  // Confirm the booking
  const confirmBtn = page.locator('button.btn-primary', { hasText: 'Confirm' });
  await confirmBtn.click();
  await wait(700);
  // Now we should see the countdown timer
  await page.screenshot({
    path: path.join(OUT_DIR, '04_countdown_active.png'),
    fullPage: true,
  });

  // -----------------------------------------------------------------------
  // 5. Wallet panel — scroll/crop to wallet area
  // -----------------------------------------------------------------------
  console.log('05 — Wallet panel');
  await freshLoad();
  // Scroll to wallet section (it's the rightmost panel)
  const walletPanel = page.locator('.wallet');
  await walletPanel.scrollIntoViewIfNeeded();
  await wait(400);
  // Get bounding box of the wallet section (parent panel)
  const walletSection = page.locator('section.panel').filter({ has: page.locator('.wallet') });
  const walletBox = await walletSection.boundingBox();
  if (walletBox) {
    await page.screenshot({
      path: path.join(OUT_DIR, '05_wallet_panel.png'),
      clip: {
        x: Math.max(0, walletBox.x - 20),
        y: Math.max(0, walletBox.y - 20),
        width: Math.min(500, walletBox.width + 40),
        height: Math.min(700, walletBox.height + 40),
      },
    });
  } else {
    await page.screenshot({ path: path.join(OUT_DIR, '05_wallet_panel.png'), fullPage: true });
  }

  // -----------------------------------------------------------------------
  // 6. Driver view — switch role via RoleSwitch
  // -----------------------------------------------------------------------
  console.log('06 — Driver view');
  await freshLoad();
  // Click "Driver" in the role switcher
  const driverRoleBtn = page.locator('button[role="tab"]', { hasText: 'Driver' });
  await driverRoleBtn.click();
  await wait(600);
  await page.screenshot({
    path: path.join(OUT_DIR, '06_driver_view.png'),
    fullPage: true,
  });

  // -----------------------------------------------------------------------
  // 7. Driver add offline passenger form
  // -----------------------------------------------------------------------
  console.log('07 — Driver Add Offline Passenger form');
  // We're already in driver view — just fill in the offline passenger form
  const nameInput = page.locator('input[placeholder="Student name"]');
  await nameInput.fill('Priyanka R.');
  await wait(300);
  const dropoffDriverSelect = page.locator('.off-pax select');
  await dropoffDriverSelect.selectOption({ index: 2 }); // pick any option
  await wait(300);
  await page.screenshot({
    path: path.join(OUT_DIR, '07_driver_add_passenger.png'),
    fullPage: true,
  });

  // -----------------------------------------------------------------------
  // 8. Admin view — switch to Admin role
  // -----------------------------------------------------------------------
  console.log('08 — Admin KPI dashboard');
  await freshLoad();
  const adminRoleBtn = page.locator('button[role="tab"]', { hasText: 'Admin' });
  await adminRoleBtn.click();
  await wait(700);
  await page.screenshot({
    path: path.join(OUT_DIR, '08_admin_view.png'),
    fullPage: true,
  });

  await browser.close();
  console.log('\nAll screenshots saved to:', OUT_DIR);
}

main().catch((err) => {
  console.error('Screenshot script failed:', err);
  process.exit(1);
});
