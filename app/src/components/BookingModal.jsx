import React, { useState } from 'react';
import { useStore } from '../state/store.jsx';

const BASE_FARE = 10;

export default function BookingModal({ erickId, onClose }) {
  const { state, dispatch } = useStore();
  const erick = state.ericks.find((e) => e.id === erickId);
  const [dropoff, setDropoff] = useState(state.locations[0]?.name ?? '');

  if (!erick) return null;
  const seatsLeft = erick.capacity - erick.passengers.length;
  const canBook = seatsLeft > 0 && !state.student.activeBooking;

  const onConfirm = () => {
    dispatch({
      type: 'BOOK_SEAT',
      erickId,
      studentId: state.student.id,
      dropoff,
    });
    onClose();
  };

  return (
    <div className="modal-scrim" role="dialog" aria-modal="true" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal__eyebrow">Confirm booking · {erickId}</div>
        <div className="modal__title">Reserve one seat with {erick.driverName}</div>
        <div className="modal__subtitle">
          Reach the vehicle within 60 seconds of confirming.
          If you don't board in time, ₹5 will be deducted and the seat released to the next student.
        </div>

        <div className="modal__field">
          <label htmlFor="dropoff">Drop-off</label>
          <select
            id="dropoff"
            value={dropoff}
            onChange={(e) => setDropoff(e.target.value)}
          >
            {Array.from(new Set(state.locations.map((l) => l.group))).map((group) => (
              <optgroup key={group} label={group}>
                {state.locations
                  .filter((l) => l.group === group)
                  .map((l) => (
                    <option key={l.id} value={l.name}>{l.name}</option>
                  ))}
              </optgroup>
            ))}
          </select>
        </div>

        <div className="modal__fare">
          <span className="modal__fare-label">Flat fare</span>
          <span className="modal__fare-amt">₹{BASE_FARE}</span>
        </div>

        {!canBook && (
          <div className="off-pax__err" style={{ marginBottom: 12 }}>
            {state.student.activeBooking
              ? 'You already have an active booking.'
              : 'No seats available on this vehicle.'}
          </div>
        )}

        <div className="modal__actions">
          <button className="btn-ghost" onClick={onClose}>Cancel</button>
          <button
            className="btn-primary"
            onClick={onConfirm}
            disabled={!canBook}
          >
            Confirm · Start 60s hold
          </button>
        </div>
      </div>
    </div>
  );
}
