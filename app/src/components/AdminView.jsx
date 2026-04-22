import React, { useMemo } from 'react';
import { useStore } from '../state/store.jsx';
import CampusMap from '../data/campusMap.jsx';

export default function AdminView() {
  const { state } = useStore();

  const stats = useMemo(() => {
    const totalCapacity = state.ericks.reduce((a, e) => a + e.capacity, 0);
    const totalPax = state.ericks.reduce((a, e) => a + e.passengers.length, 0);
    const fill = totalCapacity ? (totalPax / totalCapacity) * 100 : 0;
    const leakage =
      state.ericks.reduce((a, e) => a + e.passengers.filter((p) => p.offline).length, 0);
    const leakagePct =
      totalPax > 0 ? (leakage / totalPax) * 100 : state.adminStats.leakagePercent;

    return {
      completedRides: state.adminStats.completedRides,
      avgWaitMin: state.adminStats.avgWaitMin,
      revenueToday: state.adminStats.revenueToday,
      leakagePct: leakagePct.toFixed(1),
      emptyReturnPercent: state.adminStats.emptyReturnPercent,
      fill: fill.toFixed(0),
    };
  }, [state.ericks, state.adminStats]);

  return (
    <div style={{ padding: 32 }}>
      <div className="reveal reveal-0" style={{ marginBottom: 24 }}>
        <span className="panel__eyebrow">Operations dashboard · today</span>
        <h1 style={{ fontSize: 40, letterSpacing: '-0.02em', marginTop: 6 }}>
          E-Rick Campus · aggregate view
        </h1>
        <div className="muted" style={{ marginTop: 4 }}>
          Live fleet signal · four vehicles · IIT Roorkee
        </div>
      </div>

      {/* KPI tiles */}
      <div className="admin-grid">
        {[
          { label: 'Completed rides', value: stats.completedRides, unit: 'today', delta: '+12 vs. yesterday' },
          { label: 'Avg. wait', value: stats.avgWaitMin, unit: 'min', delta: '−0.8 min' },
          { label: 'Revenue', value: `₹${stats.revenueToday}`, unit: 'today', delta: '+₹240' },
          { label: 'Leakage', value: `${stats.leakagePct}%`, unit: 'offline fares', delta: '−1.9 pts', good: true },
          { label: 'Empty return', value: `${stats.emptyReturnPercent}%`, unit: 'of trips', delta: '+0.5 pts', good: false },
        ].map((s, i) => (
          <div key={s.label} className={`stat-tile reveal reveal-${Math.min(5, i + 1)}`}>
            <span className="stat-tile__label">{s.label}</span>
            <span className="stat-tile__value">{s.value}</span>
            <span className="stat-tile__unit">{s.unit}</span>
            <span className={`stat-tile__delta ${s.good === false ? 'stat-tile__delta--bad' : ''}`}>
              {s.delta}
            </span>
          </div>
        ))}
      </div>

      <div className="admin-two">
        <section className="panel reveal reveal-4">
          <div className="panel__head">
            <div>
              <span className="panel__eyebrow">Fleet</span>
              <h2 className="panel__title">Vehicles · current state</h2>
            </div>
            <span className="panel__eyebrow">{stats.fill}% FILL</span>
          </div>
          <table className="fleet-table">
            <thead>
              <tr>
                <th>Fleet ID</th>
                <th>Driver</th>
                <th>Zone</th>
                <th>Pax</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {state.ericks.map((e) => (
                <tr key={e.id}>
                  <td className="num">{e.id}</td>
                  <td>{e.driverName}</td>
                  <td className="muted">{e.homeZone}</td>
                  <td className="num">{e.passengers.length}/{e.capacity}</td>
                  <td>
                    <span className={`fleet-table__pill fleet-table__pill--${e.status}`}>
                      {e.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <section className="panel reveal reveal-5">
          <div className="panel__head">
            <div>
              <span className="panel__eyebrow">Live map</span>
              <h2 className="panel__title">Fleet positions</h2>
            </div>
          </div>
          <CampusMap ericks={state.ericks} />
          <div className="mapwrap__caption">
            <div className="mapwrap__legend">
              <span><span className="legend-dot legend-dot--accent" /> Available</span>
              <span><span className="legend-dot" style={{ background: 'var(--error)' }} /> Full</span>
            </div>
            <div>Snapshot · refresh every 1s</div>
          </div>
        </section>
      </div>

      <div className="erick-select-hint" style={{ marginTop: 32 }}>
        Leakage computed from offline passenger ratio · empty-return % from static mock · all
        other numbers derived live from the action log.
      </div>
    </div>
  );
}
