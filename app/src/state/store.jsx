import React, { createContext, useContext, useReducer, useMemo } from 'react';
import {
  INITIAL_ERICKS,
  INITIAL_STUDENT,
  INITIAL_ADMIN_STATS,
  LOCATIONS,
} from '../data/mockData.js';

// ---------- initial state ----------
const initialState = {
  role: 'student',
  student: INITIAL_STUDENT,
  ericks: INITIAL_ERICKS,
  locations: LOCATIONS,
  adminStats: INITIAL_ADMIN_STATS,
  toasts: [],
  actionLog: [],
};

// ---------- helpers ----------
const BOOKING_HOLD_MS = 60 * 1000;
const CANCELLATION_FEE = 5;
const BASE_FARE = 10;

const uid = (prefix = 'id') =>
  `${prefix}-${Math.random().toString(36).slice(2, 9)}`;

const withToast = (state, toast) => ({
  ...state,
  toasts: [...state.toasts, { id: uid('t'), createdAt: Date.now(), ttlMs: 5000, ...toast }],
});

// ---------- reducer ----------
function reducer(state, action) {
  const logged = { ...action, _at: Date.now() };
  const log = [...state.actionLog.slice(-49), logged];

  switch (action.type) {
    case 'SWITCH_ROLE':
      return { ...state, role: action.role, actionLog: log };

    case 'BOOK_SEAT': {
      const { erickId, studentId, dropoff } = action;
      const erick = state.ericks.find((e) => e.id === erickId);
      if (!erick) return state;
      if (erick.passengers.length >= erick.capacity) {
        return withToast(
          { ...state, actionLog: log },
          { tone: 'error', title: 'Vehicle full', body: `${erickId} is at capacity.` }
        );
      }
      const bookingId = uid('bk');
      const passenger = {
        id: bookingId,
        name: state.student.name,
        dropoff,
        status: 'booked',
        studentId,
        deadline: Date.now() + BOOKING_HOLD_MS,
      };
      const ericks = state.ericks.map((e) =>
        e.id === erickId ? { ...e, passengers: [...e.passengers, passenger] } : e
      );
      const student = {
        ...state.student,
        activeBooking: { bookingId, erickId, dropoff, deadline: passenger.deadline },
      };
      return { ...state, ericks, student, actionLog: log };
    }

    case 'CANCEL_BOOKING': {
      const { bookingId, reason } = action;
      let found = null;
      const ericks = state.ericks.map((e) => {
        const keep = e.passengers.filter((p) => p.id !== bookingId);
        if (keep.length !== e.passengers.length) {
          found = e;
        }
        return { ...e, passengers: keep };
      });
      if (!found) return state;

      let student = { ...state.student, activeBooking: null };
      let toasts = state.toasts;

      if (reason === 'timeout') {
        student = {
          ...student,
          walletBalance: Math.max(0, student.walletBalance - CANCELLATION_FEE),
          reputationNoShows: [...student.reputationNoShows, Date.now()],
        };
        toasts = [
          ...toasts,
          {
            id: uid('t'),
            createdAt: Date.now(),
            ttlMs: 5000,
            tone: 'error',
            title: 'Booking cancelled',
            body: `₹${CANCELLATION_FEE} deducted - you didn't reach in time.`,
          },
        ];
      } else {
        toasts = [
          ...toasts,
          {
            id: uid('t'),
            createdAt: Date.now(),
            ttlMs: 4000,
            tone: 'neutral',
            title: 'Booking cancelled',
            body: `Seat released on ${found.id}.`,
          },
        ];
      }
      return { ...state, ericks, student, toasts, actionLog: log };
    }

    case 'MARK_REACHED': {
      const { bookingId } = action;
      const ericks = state.ericks.map((e) => {
        const hit = e.passengers.find((p) => p.id === bookingId);
        if (!hit) return e;
        const passengers = e.passengers.map((p) =>
          p.id === bookingId ? { ...p, status: 'boarded', deadline: undefined } : p
        );
        const allBoarded = passengers.every((p) => p.status === 'boarded');
        return {
          ...e,
          passengers,
          status: allBoarded && passengers.length === e.capacity ? 'enroute' : 'boarding',
        };
      });
      let student = state.student;
      if (state.student.activeBooking?.bookingId === bookingId) {
        student = { ...student, activeBooking: { ...student.activeBooking, deadline: null, locked: true } };
      }
      return { ...state, ericks, student, actionLog: log };
    }

    case 'ADD_OFFLINE_PASSENGER': {
      const { erickId, name, dropoff } = action;
      const erick = state.ericks.find((e) => e.id === erickId);
      if (!erick) return state;
      if (erick.passengers.length >= erick.capacity) {
        return withToast(
          { ...state, actionLog: log },
          {
            tone: 'error',
            title: 'Vehicle at capacity (4/4)',
            body: 'Cannot add offline passenger - seat unavailable.',
          }
        );
      }
      const ericks = state.ericks.map((e) =>
        e.id === erickId
          ? {
              ...e,
              passengers: [
                ...e.passengers,
                { id: uid('off'), name, dropoff, status: 'boarded', offline: true },
              ],
            }
          : e
      );
      return withToast(
        { ...state, ericks, actionLog: log },
        { tone: 'success', title: 'Passenger added', body: `${name} → ${dropoff}.` }
      );
    }

    case 'WALLET_TOPUP': {
      const student = {
        ...state.student,
        walletBalance: state.student.walletBalance + action.amount,
      };
      return withToast(
        { ...state, student, actionLog: log },
        { tone: 'success', title: 'Wallet topped up', body: `+₹${action.amount}` }
      );
    }

    case 'COMPLETE_RIDE': {
      const { erickId, studentId, fare = BASE_FARE } = action;
      const erick = state.ericks.find((e) => e.id === erickId);
      if (!erick) return state;
      const passenger = erick.passengers.find((p) => p.studentId === studentId);
      const ericks = state.ericks.map((e) =>
        e.id === erickId
          ? {
              ...e,
              passengers: e.passengers.filter((p) => p.studentId !== studentId),
              status: e.passengers.length - 1 === 0 ? 'idle' : e.status,
            }
          : e
      );
      const student = {
        ...state.student,
        walletBalance: Math.max(0, state.student.walletBalance - fare),
        activeBooking: null,
        rideHistory: [
          { id: uid('rh'), from: erick.driverName, to: passenger?.dropoff || ' - ', fare, at: Date.now() },
          ...state.student.rideHistory,
        ].slice(0, 10),
      };
      const adminStats = {
        ...state.adminStats,
        completedRides: state.adminStats.completedRides + 1,
        revenueToday: state.adminStats.revenueToday + fare,
      };
      return { ...state, ericks, student, adminStats, actionLog: log };
    }

    case 'TICK_TIMERS': {
      // Expire bookings whose deadline has passed.
      const now = Date.now();
      let timedOutBooking = null;
      const ericks = state.ericks.map((e) => {
        const keep = e.passengers.filter((p) => {
          if (p.status === 'booked' && p.deadline && p.deadline <= now) {
            timedOutBooking = p;
            return false;
          }
          return true;
        });
        return keep.length === e.passengers.length ? e : { ...e, passengers: keep };
      });

      // Expire toasts.
      const toasts = state.toasts.filter((t) => now - t.createdAt < (t.ttlMs || 5000));

      if (timedOutBooking) {
        const student = {
          ...state.student,
          walletBalance: Math.max(0, state.student.walletBalance - CANCELLATION_FEE),
          reputationNoShows: [...state.student.reputationNoShows, now],
          activeBooking: state.student.activeBooking?.bookingId === timedOutBooking.id
            ? null
            : state.student.activeBooking,
        };
        return {
          ...state,
          ericks,
          student,
          toasts: [
            ...toasts,
            {
              id: uid('t'),
              createdAt: now,
              ttlMs: 5000,
              tone: 'error',
              title: 'Cancelled - ₹5 deducted',
              body: `You didn't board within 60s. Seat released.`,
            },
          ],
        };
      }
      if (toasts.length === state.toasts.length && ericks === state.ericks) return state;
      return { ...state, ericks, toasts };
    }

    case 'DISMISS_TOAST':
      return { ...state, toasts: state.toasts.filter((t) => t.id !== action.id) };

    case 'PUSH_TOAST':
      return withToast(state, action.toast);

    default:
      return state;
  }
}

// ---------- context ----------
const StoreContext = createContext(null);

export function StoreProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  const value = useMemo(() => ({ state, dispatch }), [state]);
  return <StoreContext.Provider value={value}>{children}</StoreContext.Provider>;
}

export function useStore() {
  const ctx = useContext(StoreContext);
  if (!ctx) throw new Error('useStore must be used inside StoreProvider');
  return ctx;
}

export const BOOKING_HOLD_MS_EXPORT = BOOKING_HOLD_MS;
export const CANCELLATION_FEE_EXPORT = CANCELLATION_FEE;
