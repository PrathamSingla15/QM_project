import React from 'react';
import { LOCATION_NODES, ARTERIES } from './mockData.js';

const NODE_INDEX = Object.fromEntries(LOCATION_NODES.map((n) => [n.name, n]));

// Major landmarks get bigger labels.
const MAJOR = new Set([
  'Main Library (MGCL)',
  'Main Gate',
  'Main Building',
  'Dept of CSE',
  'Convocation Hall',
]);

export default function CampusMap({ ericks, selectedErickId, onSelectErick }) {
  return (
    <svg className="mapsvg" viewBox="0 0 800 500" role="img" aria-label="Stylized IITR campus map">
      {/* subtle zonal tint behind the map for a "print" feel */}
      <defs>
        <pattern id="dots" width="8" height="8" patternUnits="userSpaceOnUse">
          <circle cx="1" cy="1" r="0.5" fill="#CEC6B4" opacity="0.6" />
        </pattern>
      </defs>
      <rect x="0" y="0" width="800" height="500" fill="url(#dots)" />

      {/* cartouche rectangle */}
      <rect
        x="16" y="16" width="768" height="468"
        fill="none" stroke="#CEC6B4" strokeWidth="1"
      />
      <rect
        x="22" y="22" width="756" height="456"
        fill="none" stroke="#CEC6B4" strokeWidth="1"
        strokeDasharray="2 3" opacity="0.5"
      />

      {/* compass rose */}
      <g transform="translate(746, 54)">
        <circle r="16" fill="#F6F2EA" stroke="#1B1A17" />
        <text y="-20" textAnchor="middle" fontFamily="IBM Plex Mono" fontSize="9" fill="#1B1A17" fontWeight="600">N</text>
        <line x1="0" y1="-10" x2="0" y2="10" stroke="#1B1A17" strokeWidth="0.8" />
        <line x1="-10" y1="0" x2="10" y2="0" stroke="#CEC6B4" strokeWidth="0.6" />
        <polygon points="0,-12 -3,0 0,-2 3,0" fill="#E85D2F" />
      </g>

      {/* scale bar */}
      <g transform="translate(40, 460)">
        <line x1="0" y1="0" x2="80" y2="0" stroke="#1B1A17" strokeWidth="1" />
        <line x1="0" y1="-4" x2="0" y2="4" stroke="#1B1A17" />
        <line x1="40" y1="-3" x2="40" y2="3" stroke="#1B1A17" />
        <line x1="80" y1="-4" x2="80" y2="4" stroke="#1B1A17" />
        <text x="0" y="14" fontFamily="IBM Plex Mono" fontSize="9" fill="#1B1A17">0</text>
        <text x="80" y="14" fontFamily="IBM Plex Mono" fontSize="9" fill="#1B1A17" textAnchor="end">200m</text>
        <text x="0" y="-10" fontFamily="IBM Plex Sans" fontSize="9" fill="#A39A87" letterSpacing="0.16em">SCALE</text>
      </g>

      {/* title */}
      <text x="40" y="48" fontFamily="Fraunces" fontSize="18" fontWeight="500" fill="#1B1A17">Campus wayfinding</text>
      <text x="40" y="62" fontFamily="IBM Plex Sans" fontSize="9" fill="#A39A87" letterSpacing="0.2em" textTransform="uppercase">TEAM E / REV.0.1 / APRIL 2026</text>

      {/* arteries (primary) */}
      <g>
        {ARTERIES.map(([a, b], i) => {
          const A = NODE_INDEX[a];
          const B = NODE_INDEX[b];
          if (!A || !B) return null;
          return (
            <line
              key={`art-${i}`}
              className="artery"
              x1={A.x} y1={A.y} x2={B.x} y2={B.y}
            />
          );
        })}
      </g>

      {/* decorative side paths (a few extra for atmosphere) */}
      <g>
        <path className="sidepath" d="M 180 250 Q 240 280 300 260" />
        <path className="sidepath" d="M 560 60 Q 620 80 680 80" />
        <path className="sidepath" d="M 500 420 Q 550 440 620 420" />
      </g>

      {/* nodes */}
      <g>
        {LOCATION_NODES.map((n) => {
          const r = MAJOR.has(n.name) ? 5.5 : 3.5;
          return (
            <g key={n.name} transform={`translate(${n.x}, ${n.y})`}>
              <circle className="node-bg" r={r} />
              {MAJOR.has(n.name) && (
                <circle r={r + 3} fill="none" stroke="#1B1A17" strokeWidth="0.5" opacity="0.35" />
              )}
              <text
                className={`node-label ${MAJOR.has(n.name) ? 'node-label--big' : ''}`}
                x={r + 5}
                y={4}
              >
                {n.name}
              </text>
            </g>
          );
        })}
      </g>

      {/* e-rick markers */}
      <g>
        {ericks.map((e) => {
          const full = e.passengers.length >= e.capacity;
          return (
            <g
              key={e.id}
              transform={`translate(${e.location.x}, ${e.location.y})`}
              onClick={() => onSelectErick?.(e.id)}
              style={{ cursor: 'pointer' }}
            >
              {/* pentagon marker */}
              <polygon
                className={`erick-marker ${full ? 'erick-full' : ''}`}
                data-selected={e.id === selectedErickId}
                points="0,-10 9.5,-3 6,8 -6,8 -9.5,-3"
              />
              <text className="erick-label" x="0" y="22" textAnchor="middle">{e.id}</text>
            </g>
          );
        })}
      </g>
    </svg>
  );
}
