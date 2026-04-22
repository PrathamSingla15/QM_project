import React, { useState, useMemo } from 'react';
import { useStore } from '../state/store.jsx';
import CampusMap from '../data/campusMap.jsx';
import AddOfflinePassenger from './AddOfflinePassenger.jsx';

export default function DriverView() {
  const { state, dispatch } = useStore();
  const [selectedId, setSelectedId] = useState('ER-04');
  const erick = state.ericks.find((e) => e.id === selectedId) || state.ericks[0];

  const boarded = erick.passengers.filter((p) => p.status === 'boarded');
  const pending = erick.passengers.filter((p) => p.status === 'booked');

  const pendingReached = (passenger) => {
    // optimistic mark with undo toast
    dispatch({ type: 'MARK_REACHED', bookingId: passenger.id });
    dispatch({
      type: 'PUSH_TOAST',
      toast: {
        tone: 'success',
        title: `Marked boarded · ${passenger.name}`,
        body: `Undo within 5s to revert.`,
        ttlMs: 5000,
        undoLabel: 'Undo',
        onUndo: () => {
          // Undo: remove the passenger (they never boarded)
          dispatch({ type: 'CANCEL_BOOKING', bookingId: passenger.id, reason: 'driver-undo' });
        },
      },
    });
  };

  const completeRide = () => {
    // Complete the ride: each boarded passenger → COMPLETE_RIDE
    boarded.forEach((p) => {
      dispatch({
        type: 'COMPLETE_RIDE',
        erickId: erick.id,
        studentId: p.studentId || p.id,
        fare: 10,
      });
    });
  };

  const stats = useMemo(() => {
    const all = state.ericks.reduce((acc, e) => acc + e.passengers.length, 0);
    const capacity = state.ericks.reduce((acc, e) => acc + e.capacity, 0);
    const fill = capacity ? Math.round((all / capacity) * 100) : 0;
    return { totalPax: all, fill, completed: state.adminStats.completedRides };
  }, [state.ericks, state.adminStats]);

  return (
    <div className="layout">
      <section className="panel reveal reveal-0">
        <div className="panel__head">
          <div>
            <span className="panel__eyebrow">Driver console · {erick.driverName}</span>
            <h2 className="panel__title">{erick.id} · {erick.passengers.length}/{erick.capacity} seats</h2>
          </div>
          <span className="panel__eyebrow">STATUS · {erick.status.toUpperCase()}</span>
        </div>
        <CampusMap
          ericks={state.ericks}
          selectedErickId={erick.id}
          onSelectErick={(id) => setSelectedId(id)}
        />
        <div className="mapwrap__caption">
          <div className="mapwrap__legend">
            <span><span className="legend-dot legend-dot--accent" /> Your vehicle</span>
            <span><span className="legend-dot" /> Other fleet</span>
          </div>
          <div>Tap a marker to switch vehicle</div>
        </div>
      </section>

      <section className="panel reveal reveal-1">
        <div className="panel__head">
          <div>
            <span className="panel__eyebrow">Manifest · {erick.id}</span>
            <h2 className="panel__title">Passengers onboard</h2>
          </div>
          <select
            className="driver-select"
            value={erick.id}
            onChange={(e) => setSelectedId(e.target.value)}
          >
            {state.ericks.map((e) => (
              <option key={e.id} value={e.id}>{e.id} · {e.driverName}</option>
            ))}
          </select>
        </div>

        <div className="driver-list">
          {pending.map((p) => (
            <div key={p.id} className="driver-pax">
              <div>
                <div className="driver-pax__name">{p.name}</div>
                <div className="driver-pax__dropoff">→ {p.dropoff}</div>
              </div>
              <span className="driver-pax__status driver-pax__status--booked">Reserved · holding</span>
              <button className="btn-primary" onClick={() => pendingReached(p)}>Mark reached</button>
            </div>
          ))}
          {boarded.map((p) => (
            <div key={p.id} className="driver-pax">
              <div>
                <div className="driver-pax__name">
                  {p.name} {p.offline && <em style={{ fontSize: 10, color: 'var(--muted)' }}>offline</em>}
                </div>
                <div className="driver-pax__dropoff">→ {p.dropoff}</div>
              </div>
              <span className="driver-pax__status driver-pax__status--boarded">Boarded</span>
            </div>
          ))}
          {erick.passengers.length === 0 && (
            <div className="muted" style={{ padding: 24, textAlign: 'center' }}>
              No passengers yet. Wait at the pickup zone or add an offline passenger.
            </div>
          )}
        </div>

        <div style={{ marginTop: 24 }}>
          <AddOfflinePassenger erickId={erick.id} />
        </div>

        <div style={{ display: 'flex', gap: 12, marginTop: 24, justifyContent: 'flex-end' }}>
          <button
            className="btn-primary"
            onClick={completeRide}
            disabled={boarded.length === 0}
            style={{ background: 'var(--accent)' }}
          >
            Complete ride · collect ₹{boarded.length * 10}
          </button>
        </div>
      </section>

      <section className="panel reveal reveal-2">
        <div className="panel__head">
          <div>
            <span className="panel__eyebrow">Today's summary</span>
            <h2 className="panel__title">Shift digest</h2>
          </div>
        </div>
        <dl className="driver-summary">
          <div>
            <dt>Fleet fill</dt>
            <dd>{stats.fill}<small style={{ fontSize: 14, color: 'var(--muted)' }}>%</small></dd>
          </div>
          <div>
            <dt>Pax onboard</dt>
            <dd>{stats.totalPax}</dd>
          </div>
          <div>
            <dt>Completed rides</dt>
            <dd>{stats.completed}</dd>
          </div>
          <div>
            <dt>Revenue · ₹</dt>
            <dd>{state.adminStats.revenueToday}</dd>
          </div>
        </dl>
        <div className="erick-select-hint" style={{ marginTop: 24 }}>
          Capacity rule: adding a 5th passenger is hard-blocked regardless of channel (app or offline).
        </div>
      </section>
    </div>
  );
}
