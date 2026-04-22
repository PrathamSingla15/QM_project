import { useEffect, useState } from 'react';

/**
 * useCountdown - returns live countdown info for a given absolute deadline.
 *
 * @param {number|null|undefined} deadlineEpoch  timestamp (ms)
 * @returns {{ secondsLeft: number, mmss: string, percent: number, expired: boolean }}
 */
export function useCountdown(deadlineEpoch) {
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    if (!deadlineEpoch) return;
    const id = setInterval(() => setNow(Date.now()), 200);
    return () => clearInterval(id);
  }, [deadlineEpoch]);

  if (!deadlineEpoch) {
    return { secondsLeft: 0, mmss: '00:00', percent: 0, expired: true };
  }

  const msLeft = Math.max(0, deadlineEpoch - now);
  const secondsLeft = Math.ceil(msLeft / 1000);
  const mins = Math.floor(secondsLeft / 60);
  const secs = secondsLeft % 60;
  const mmss = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

  // percent = fraction remaining out of 60s max (for 60s holds).
  const percent = Math.min(1, msLeft / (60 * 1000));
  return { secondsLeft, mmss, percent, expired: msLeft === 0 };
}
