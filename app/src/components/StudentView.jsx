import React, { useMemo, useState } from 'react';
import { useStore } from '../state/store.jsx';
import CampusMap from '../data/campusMap.jsx';
import ERickCard from './ERickCard.jsx';
import BookingModal from './BookingModal.jsx';
import CountdownTimer from './CountdownTimer.jsx';
import WalletPanel from './WalletPanel.jsx';
import { EnRouteBanner } from './Banner.jsx';

export default function StudentView() {
  const { state, dispatch } = useStore();
  const [selectedErick, setSelectedErick] = useState(null);
  const [bookingFor, setBookingFor] = useState(null);

  const activeBooking = state.student.activeBooking;
  const activeErick = activeBooking
    ? state.ericks.find((e) => e.id === activeBooking.erickId)
    : null;
  const enroute = activeErick?.status === 'enroute';

  const openBooking = (erickId) => {
    if (state.student.activeBooking) return;
    setBookingFor(erickId);
  };

  const cancelActive = () => {
    if (!activeBooking) return;
    dispatch({ type: 'CANCEL_BOOKING', bookingId: activeBooking.bookingId, reason: 'user' });
  };

  const sortedEricks = useMemo(
    () => [...state.ericks].sort((a, b) => a.id.localeCompare(b.id)),
    [state.ericks]
  );

  return (
    <div className="layout">
      {/* --- map column --- */}
      <section className="panel reveal reveal-0">
        <div className="panel__head">
          <div>
            <span className="panel__eyebrow">Live fleet · {state.ericks.length} vehicles</span>
            <h2 className="panel__title">Where is the next ride?</h2>
          </div>
          <span className="panel__eyebrow">UPDATED · just now</span>
        </div>
        <CampusMap
          ericks={state.ericks}
          selectedErickId={selectedErick}
          onSelectErick={(id) => {
            setSelectedErick(id);
            openBooking(id);
          }}
        />
        <div className="mapwrap__caption">
          <div className="mapwrap__legend">
            <span><span className="legend-dot legend-dot--ink" /> Landmark</span>
            <span><span className="legend-dot legend-dot--accent" /> E-rick available</span>
            <span><span className="legend-dot" style={{ background: 'var(--error)' }} /> Full</span>
          </div>
          <div>Stylized wayfinding - not to scale</div>
        </div>
      </section>

      {/* --- center column: booking + cards --- */}
      <section className="panel reveal reveal-1">
        <div className="panel__head">
          <div>
            <span className="panel__eyebrow">Book a seat</span>
            <h2 className="panel__title">Flat ₹10 · ride anywhere on campus</h2>
          </div>
        </div>

        {enroute && (
          <EnRouteBanner erickId={activeErick.id} driver={activeErick.driverName} />
        )}

        {activeBooking && activeErick && !enroute && (
          <div className="activebooking">
            <CountdownTimer
              deadline={activeBooking.deadline}
              bookingId={activeBooking.bookingId}
            />
            <div className="activebooking__meta">
              <div className="activebooking__hint">Active booking</div>
              <div className="activebooking__title">
                {activeErick.id} · {activeErick.driverName}
              </div>
              <div className="activebooking__sub">
                Drop-off: <strong>{activeBooking.dropoff}</strong>
              </div>
              <div className="activebooking__sub">
                Reach the vehicle within 60 seconds. Miss the window and ₹5 is deducted.
              </div>
              <div className="activebooking__actions">
                <button className="btn-danger" onClick={cancelActive}>Cancel booking</button>
              </div>
            </div>
          </div>
        )}

        <div className="vstack" style={{ gap: 12 }}>
          {sortedEricks.map((erick, i) => (
            <div key={erick.id} className={`reveal reveal-${Math.min(6, i + 1)}`}>
              <ERickCard
                erick={erick}
                selected={selectedErick === erick.id}
                onBook={openBooking}
                disabled={Boolean(activeBooking)}
              />
            </div>
          ))}
        </div>

        <div className="erick-select-hint">
          Tap any E-rick on the map or a card above to reserve a seat.
        </div>
      </section>

      {/* --- wallet column --- */}
      <WalletPanel />

      {bookingFor && <BookingModal erickId={bookingFor} onClose={() => setBookingFor(null)} />}
    </div>
  );
}
