import React, { useEffect } from 'react';
import { useCountdown } from '../hooks/useCountdown.js';
import { useStore } from '../state/store.jsx';

export default function CountdownTimer({ deadline, bookingId }) {
  const { dispatch } = useStore();
  const { mmss, percent, secondsLeft, expired } = useCountdown(deadline);

  useEffect(() => {
    if (expired && bookingId) {
      dispatch({ type: 'CANCEL_BOOKING', bookingId, reason: 'timeout' });
    }
  }, [expired, bookingId, dispatch]);

  const urgent = secondsLeft <= 15;
  const angleFrac = Math.max(0, Math.min(1, percent));

  return (
    <div
      className={`countdown ${urgent ? 'countdown--urgent' : ''}`}
      style={{ ['--p']: angleFrac }}
      aria-label={`Countdown: ${mmss} remaining`}
    >
      <div className="countdown__inner">
        <div className="countdown__mmss">{mmss}</div>
        <div className="countdown__label">Board in</div>
      </div>
    </div>
  );
}
