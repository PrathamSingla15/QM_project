import React, { useState } from 'react';
import { useStore } from '../state/store.jsx';

export default function AddOfflinePassenger({ erickId }) {
  const { state, dispatch } = useStore();
  const erick = state.ericks.find((e) => e.id === erickId);
  const [name, setName] = useState('');
  const [dropoff, setDropoff] = useState(state.locations[0]?.name ?? '');
  const [err, setErr] = useState('');

  if (!erick) return null;
  const full = erick.passengers.length >= erick.capacity;

  const onAdd = () => {
    if (!name.trim()) {
      setErr('Enter the passenger name first.');
      return;
    }
    if (full) {
      setErr('Vehicle at capacity (4/4). Cannot add another passenger.');
      return;
    }
    dispatch({
      type: 'ADD_OFFLINE_PASSENGER',
      erickId,
      name: name.trim(),
      dropoff,
    });
    setName('');
    setErr('');
  };

  return (
    <div className="off-pax">
      <div>
        <div className="off-pax__title">Add offline passenger</div>
        <div className="off-pax__capinfo">
          Capacity · {erick.passengers.length}/{erick.capacity}
          {full ? ' · LOCKED' : ''}
        </div>
      </div>
      <div className="off-pax__row">
        <input
          type="text"
          placeholder="Student name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={full}
        />
        <select
          value={dropoff}
          onChange={(e) => setDropoff(e.target.value)}
          disabled={full}
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
        <button
          className="btn-primary"
          onClick={onAdd}
          disabled={full}
          style={full ? { background: 'var(--error)', cursor: 'not-allowed' } : undefined}
        >
          {full ? 'Locked' : 'Add'}
        </button>
      </div>
      {err && <div className="off-pax__err">{err}</div>}
      {full && !err && (
        <div className="off-pax__err">Vehicle at capacity (4/4) - ride must depart before adding more.</div>
      )}
    </div>
  );
}
