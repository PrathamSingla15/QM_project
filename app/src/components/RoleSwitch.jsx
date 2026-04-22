import React from 'react';
import { useStore } from '../state/store.jsx';

const ROLES = [
  { id: 'student', label: 'Student' },
  { id: 'driver', label: 'Driver' },
  { id: 'admin', label: 'Admin' },
];

export default function RoleSwitch() {
  const { state, dispatch } = useStore();
  return (
    <div className="roleswitch">
      <span className="roleswitch__label">Demo view</span>
      <span className="roleswitch__demo-note">not in prod</span>
      <div className="roleswitch__group" role="tablist" aria-label="Role selector">
        {ROLES.map((r) => (
          <button
            key={r.id}
            role="tab"
            aria-pressed={state.role === r.id}
            className="roleswitch__btn"
            onClick={() => dispatch({ type: 'SWITCH_ROLE', role: r.id })}
          >
            {r.label}
          </button>
        ))}
      </div>
    </div>
  );
}
