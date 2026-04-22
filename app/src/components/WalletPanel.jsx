import React from 'react';
import { useStore } from '../state/store.jsx';

function formatTime(ts) {
  const d = new Date(ts);
  return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

export default function WalletPanel() {
  const { state, dispatch } = useStore();
  const { walletBalance, walletDebt, rideHistory, activeBooking } = state.student;
  const isHeld = Boolean(activeBooking);

  return (
    <section className="panel reveal reveal-3">
      <div className="panel__head">
        <div>
          <h2 className="panel__title">Wallet</h2>
        </div>
        <span className="panel__eyebrow">Prepaid · ₹</span>
      </div>

      <div className="wallet">
        <div>
          <div className="wallet__balance">
            <span className="wallet__currency">₹</span>
            <span className="wallet__amount">{walletBalance}</span>
          </div>
          {isHeld && (
            <div className="wallet__held">₹5 held · released on boarding or cancellation</div>
          )}
          {walletDebt > 0 && (
            <div className="wallet__debt">Debt outstanding: ₹{walletDebt}</div>
          )}
        </div>

        <div className="wallet__actions">
          <button
            className="btn-primary"
            onClick={() => dispatch({ type: 'WALLET_TOPUP', amount: 50 })}
          >
            Top up ₹50
          </button>
          <button
            className="btn-ghost"
            onClick={() => dispatch({ type: 'WALLET_TOPUP', amount: 100 })}
          >
            + ₹100
          </button>
        </div>

        <div>
          <div className="panel__eyebrow" style={{ marginBottom: 10 }}>
            Recent rides
          </div>
          <div className="wallet__history">
            {rideHistory.length === 0 && (
              <div className="muted" style={{ fontSize: 12 }}>No rides yet.</div>
            )}
            {rideHistory.slice(0, 6).map((r) => (
              <div key={r.id} className="wallet__history-item">
                <div>
                  <div>{r.from} → {r.to}</div>
                  <small>{formatTime(r.at)}</small>
                </div>
                <span>−₹{r.fare}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
