import React from 'react';

export function EnRouteBanner({ erickId, driver }) {
  return (
    <div className="banner banner--accent">
      <span className="banner__eyebrow">EN ROUTE · LOCKED</span>
      <span className="banner__body">
        {erickId} with {driver} is en route. Cannot cancel without driver approval.
      </span>
    </div>
  );
}

export function ConnectionBanner() {
  return (
    <div className="banner banner--warn">
      <span className="banner__eyebrow">CONNECTION</span>
      <span className="banner__body">Offline · showing last-known fleet state.</span>
    </div>
  );
}
