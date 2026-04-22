import React, { useEffect } from 'react';
import { useStore } from '../state/store.jsx';

export default function ToastStack() {
  const { state, dispatch } = useStore();
  return (
    <div className="toastwrap" role="status" aria-live="polite">
      {state.toasts.map((t) => (
        <ToastItem
          key={t.id}
          toast={t}
          onClose={() => dispatch({ type: 'DISMISS_TOAST', id: t.id })}
        />
      ))}
    </div>
  );
}

function ToastItem({ toast, onClose }) {
  useEffect(() => {
    if (!toast.ttlMs) return;
    const id = setTimeout(() => {
      onClose();
      toast.onExpire?.();
    }, toast.ttlMs);
    return () => clearTimeout(id);
  }, [toast.id, toast.ttlMs]);

  const toneClass =
    toast.tone === 'error'
      ? 'toast--error'
      : toast.tone === 'success'
      ? 'toast--success'
      : '';
  return (
    <div className={`toast ${toneClass}`}>
      <span className="toast__tag" />
      <div>
        <div className="toast__title">{toast.title}</div>
        {toast.body && <div className="toast__body">{toast.body}</div>}
      </div>
      {toast.undoLabel && (
        <button
          className="toast__undo"
          onClick={() => {
            toast.onUndo?.();
            onClose();
          }}
        >
          {toast.undoLabel}
        </button>
      )}
      <button className="toast__close" aria-label="Dismiss" onClick={onClose}>×</button>
    </div>
  );
}
