import React from 'react';
import RoleSwitch from './RoleSwitch.jsx';
import { useStore } from '../state/store.jsx';

export default function TopBar() {
  const { state } = useStore();
  const { walletBalance, activeBooking } = state.student;
  const isHeld = Boolean(activeBooking);

  return (
    <header className="topbar">
      <div className="brand">
        <div className="brand__mark" aria-hidden="true">E</div>
        <div className="brand__wordmark">
          <strong>E-Rick Campus</strong>
          <small>IIT Roorkee · Group 2 prototype</small>
        </div>
      </div>

      <div className="topbar__right">
        <span className={`wallet-pill ${isHeld ? 'wallet-pill--held' : ''}`}>
          <span className="wallet-pill__label">Wallet</span>
          <span className="wallet-pill__num">
            ₹{walletBalance}
            {isHeld ? ' · ₹5 held' : ''}
          </span>
        </span>
        <RoleSwitch />
      </div>
    </header>
  );
}
