# E-Rick Campus  - Team E prototype

Interactive Vite + React prototype of a campus E-Rickshaw mobility app for IIT Roorkee. Built as the demo artifact for the TQM course project final presentation.

## Setup

```
cd deliverables/app
npm install
npm run dev -- --port 5174 --host 127.0.0.1
```

Open `http://127.0.0.1:5174/` in a desktop-sized browser window (minimum 1000px wide; mobile not supported in v1).

Requires Node 20+.

## Tour of the three views

Use the **Demo view** toggle in the top-right (Student / Driver / Admin).

### Student
- Live campus map with four E-ricks as terracotta pentagons.
- Tap any E-rick (on the map or in the list) to open the booking modal.
- Pick a drop-off from the IIT Roorkee location list, confirm. A 60-second countdown ring starts; ₹5 is visually "held" in the wallet pill.
- If the countdown hits zero without boarding, ₹5 is deducted from the wallet and the seat is released automatically.
- Full vehicles (ER-02, 4/4) are visually locked with a maroon accent and a disabled "Full" button, demonstrating the capacity rule from the driver's perspective.

### Driver
- Manifest for the selected vehicle (switch via dropdown or by tapping a marker on the map).
- "Mark reached" on a booked passenger triggers a 5-second undoable toast before the status is committed.
- "Add offline passenger" field blocks at 4/4 with an explicit error message.
- "Complete ride" bills each boarded passenger ₹10 and updates both the wallet and the admin counters.

### Admin
- Aggregate KPI tiles: completed rides (live counter), avg wait, revenue today, leakage %, empty-return %.
- Fleet table showing all four vehicles and their current state.
- Same campus map for situational awareness.

## Notes

- Drop-off locations use the **IIT Roorkee destination list (April 2026)** — 43 locations across Hostels, Academic Departments, Gates, and Campus Facilities (see `src/data/mockData.js`).
- State lives in a single `useReducer` in `src/state/store.jsx`; every dispatched action is logged to a ring buffer for future replay/inspection.
- Typography: Fraunces (display serif) + IBM Plex Sans (UI). Loaded via Google Fonts in `index.html`.
- No UI library; all styles are hand-written in `src/styles.css` against CSS variables.

## File tree

```
deliverables/app/
├── README.md
├── package.json
├── vite.config.js
├── index.html
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── styles.css
    ├── state/store.jsx
    ├── data/{mockData.js, campusMap.jsx}
    ├── hooks/useCountdown.js
    └── components/…
```
