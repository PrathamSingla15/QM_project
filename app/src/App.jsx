import React, { useEffect } from 'react';
import { useStore } from './state/store.jsx';
import TopBar from './components/TopBar.jsx';
import StudentView from './components/StudentView.jsx';
import DriverView from './components/DriverView.jsx';
import AdminView from './components/AdminView.jsx';
import ToastStack from './components/Toast.jsx';

export default function App() {
  const { state, dispatch } = useStore();

  // Global 1s tick - drives countdown expirations + toast GC.
  useEffect(() => {
    const id = setInterval(() => dispatch({ type: 'TICK_TIMERS' }), 1000);
    return () => clearInterval(id);
  }, [dispatch]);

  return (
    <div className="app">
      <TopBar />
      {state.role === 'student' && <StudentView />}
      {state.role === 'driver' && <DriverView />}
      {state.role === 'admin' && <AdminView />}

      <footer className="footnote">
        Prototype v0.1 · Group 2 · TQM 2026 · IIT Roorkee destination list (April 2026).
      </footer>

      <ToastStack />
    </div>
  );
}
