import React from 'react';

export default function ERickCard({ erick, onBook, selected, disabled }) {
  const full = erick.passengers.length >= erick.capacity;
  const dropoffs = erick.passengers.map((p) => p.dropoff);
  const uniqueDropoffs = Array.from(new Set(dropoffs));
  const statusLabel =
    erick.status === 'enroute' ? 'En route' : erick.status === 'idle' ? 'Idle' : 'Boarding';

  return (
    <article
      className={`erickcard ${full ? 'erickcard--full' : ''} ${selected ? 'erickcard--active' : ''}`}
      onClick={() => !full && !disabled && onBook?.(erick.id)}
    >
      <div className="erickcard__head">
        <span className="erickcard__id">{erick.id}</span>
        <span className={`erickcard__status ${erick.status === 'enroute' ? 'erickcard__status--enroute' : ''}`}>
          {statusLabel}
        </span>
      </div>
      <div>
        <div className="erickcard__driver">{erick.driverName}</div>
        <div className="muted" style={{ fontSize: 11, letterSpacing: '0.04em' }}>
          Driver · Fleet ID {erick.id}
        </div>
      </div>
      <div className="erickcard__body">
        <div className="erickcard__fill">
          {erick.passengers.length}<em>/{erick.capacity}</em>
        </div>
        <div style={{ textAlign: 'right' }}>
          <div className="panel__eyebrow">Seats filled</div>
        </div>
      </div>

      {uniqueDropoffs.length > 0 && (
        <ul className="erickcard__dropoffs">
          {uniqueDropoffs.map((d) => (
            <li key={d}>{d}</li>
          ))}
        </ul>
      )}

      <div className="erickcard__foot">
        <span className="muted" style={{ fontSize: 11, letterSpacing: '0.04em' }}>
          {full ? 'Capacity lock (4/4)' : `${erick.capacity - erick.passengers.length} seat${erick.capacity - erick.passengers.length === 1 ? '' : 's'} open`}
        </span>
        <button
          className="erickcard__book"
          disabled={full || disabled}
          onClick={(e) => {
            e.stopPropagation();
            onBook?.(erick.id);
          }}
        >
          {full ? 'Full' : 'Book seat'}
        </button>
      </div>
    </article>
  );
}
