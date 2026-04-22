// Initial state for the E-Rick Campus prototype.
// IIT Roorkee destination list - confirmed April 2026.
export const LOCATIONS = [
  // Hostels (14)
  { id: 'azad-bhawan', name: 'Azad Bhawan', group: 'Hostels' },
  { id: 'ravindra-bhawan', name: 'Ravindra Bhawan', group: 'Hostels' },
  { id: 'govinda-bhawan', name: 'Govinda Bhawan', group: 'Hostels' },
  { id: 'himalaya-bhawan', name: 'Himalaya Bhawan', group: 'Hostels' },
  { id: 'vivekananda-bhawan', name: 'Vivekananda Bhawan', group: 'Hostels' },
  { id: 'vigyan-bhawan', name: 'Vigyan Bhawan', group: 'Hostels' },
  { id: 'jawahar-bhawan', name: 'Jawahar Bhawan', group: 'Hostels' },
  { id: 'sarojini-bhawan', name: 'Sarojini Bhawan', group: 'Hostels' },
  { id: 'kasturba-bhawan', name: 'Kasturba Bhawan', group: 'Hostels' },
  { id: 'rajeev-bhawan', name: 'Rajeev Bhawan', group: 'Hostels' },
  { id: 'cautley-bhawan', name: 'Cautley Bhawan', group: 'Hostels' },
  { id: 'rajendra-bhawan', name: 'Rajendra Bhawan', group: 'Hostels' },
  { id: 'radhakrishnan-bhawan', name: 'Radhakrishnan Bhawan', group: 'Hostels' },
  { id: 'ganga-bhawan', name: 'Ganga Bhawan', group: 'Hostels' },
  // Academic Departments (16)
  { id: 'metallurgical-engineering', name: 'Metallurgical Engineering', group: 'Academic Departments' },
  { id: 'chemical-engineering', name: 'Chemical Engineering', group: 'Academic Departments' },
  { id: 'hydrology', name: 'Hydrology', group: 'Academic Departments' },
  { id: 'earthquake-engineering', name: 'Earthquake Engineering', group: 'Academic Departments' },
  { id: 'earth-sciences', name: 'Earth Sciences', group: 'Academic Departments' },
  { id: 'civil-engineering', name: 'Civil Engineering', group: 'Academic Departments' },
  { id: 'architecture-planning', name: 'Architecture & Planning', group: 'Academic Departments' },
  { id: 'mechanical-east-block', name: 'Mechanical - East Block', group: 'Academic Departments' },
  { id: 'mechanical-west-block', name: 'Mechanical - West Block', group: 'Academic Departments' },
  { id: 'electrical-engineering', name: 'Electrical Engineering', group: 'Academic Departments' },
  { id: 'ece', name: 'ECE', group: 'Academic Departments' },
  { id: 'cse', name: 'CSE', group: 'Academic Departments' },
  { id: 'chemical-sciences', name: 'Chemical Sciences', group: 'Academic Departments' },
  { id: 'physics', name: 'Physics', group: 'Academic Departments' },
  { id: 'hss', name: 'HSS', group: 'Academic Departments' },
  { id: 'biotechnology', name: 'Biotechnology', group: 'Academic Departments' },
  // Gates (4)
  { id: 'main-gate', name: 'Main Gate', group: 'Gates' },
  { id: 'back-gate', name: 'Back Gate', group: 'Gates' },
  { id: 'south-gate', name: 'South Gate', group: 'Gates' },
  { id: 'solani-gate', name: 'Solani Gate', group: 'Gates' },
  // Campus Facilities (9)
  { id: 'apj-block', name: 'APJ Block', group: 'Campus Facilities' },
  { id: 'gb-block', name: 'GB Block', group: 'Campus Facilities' },
  { id: 'central-library', name: 'Central Library', group: 'Campus Facilities' },
  { id: 'doms', name: 'DOMS', group: 'Campus Facilities' },
  { id: 'institute-hospital', name: 'Institute Hospital', group: 'Campus Facilities' },
  { id: 'campus-temple', name: 'Campus Temple', group: 'Campus Facilities' },
  { id: 'sac-student-activity-centre', name: 'SAC (Student Activity Centre)', group: 'Campus Facilities' },
  { id: 'mac-multi-activity-centre', name: 'MAC (Multi-Activity Centre)', group: 'Campus Facilities' },
  { id: 'icc-indoor-complex', name: 'ICC (Indoor Complex)', group: 'Campus Facilities' },
];

// Stylized campus positions (in the SVG 800x500 viewBox).
// These double as marker positions for the campus map component.
export const LOCATION_NODES = [
  { name: 'Main Gate', x: 110, y: 420, zone: 'south' },
  { name: 'Main Building', x: 230, y: 330, zone: 'south' },
  { name: 'Convocation Hall', x: 330, y: 400, zone: 'south' },
  { name: 'Lecture Hall Complex', x: 400, y: 260, zone: 'mid' },
  { name: 'Dept of CSE', x: 540, y: 300, zone: 'mid' },
  { name: 'Dept of Civil', x: 600, y: 220, zone: 'mid' },
  { name: 'Main Library (MGCL)', x: 470, y: 160, zone: 'north' },
  { name: 'Institute Canteen', x: 340, y: 150, zone: 'north' },
  { name: 'Health Centre', x: 220, y: 200, zone: 'mid' },
  { name: 'Rajendra Bhawan', x: 640, y: 400, zone: 'east' },
  { name: 'Govind Bhawan', x: 700, y: 330, zone: 'east' },
  { name: 'Cautley Bhawan', x: 720, y: 120, zone: 'north' },
  { name: 'Kasturba Bhawan', x: 580, y: 90, zone: 'north' },
  { name: 'Sarojini Bhawan', x: 420, y: 60, zone: 'north' },
  { name: 'Jwalamukhi Dining', x: 160, y: 120, zone: 'north' },
];

// Main arteries between zones - thick accent lines.
export const ARTERIES = [
  ['Main Gate', 'Main Building'],
  ['Main Building', 'Convocation Hall'],
  ['Main Building', 'Lecture Hall Complex'],
  ['Lecture Hall Complex', 'Main Library (MGCL)'],
  ['Lecture Hall Complex', 'Dept of CSE'],
  ['Dept of CSE', 'Dept of Civil'],
  ['Main Library (MGCL)', 'Institute Canteen'],
  ['Institute Canteen', 'Jwalamukhi Dining'],
  ['Dept of Civil', 'Cautley Bhawan'],
  ['Main Library (MGCL)', 'Kasturba Bhawan'],
  ['Kasturba Bhawan', 'Sarojini Bhawan'],
  ['Dept of CSE', 'Govind Bhawan'],
  ['Govind Bhawan', 'Rajendra Bhawan'],
  ['Convocation Hall', 'Rajendra Bhawan'],
  ['Main Building', 'Health Centre'],
];

// Seed E-ricks. Each passenger: { id, name, dropoff, status: 'booked' | 'boarded' }
export const INITIAL_ERICKS = [
  {
    id: 'ER-01',
    driverName: 'Rakesh K.',
    driverPhotoSeed: 'rakesh',
    location: { x: 140, y: 410 },
    capacity: 4,
    passengers: [
      { id: 'p-er01-1', name: 'Nisha R.', dropoff: 'Central Library', status: 'boarded' },
      { id: 'p-er01-2', name: 'Karan J.', dropoff: 'CSE', status: 'boarded' },
    ],
    status: 'boarding',
    homeZone: 'south',
  },
  {
    id: 'ER-02',
    driverName: 'Suresh P.',
    driverPhotoSeed: 'suresh',
    location: { x: 460, y: 170 },
    capacity: 4,
    passengers: [
      { id: 'p-er02-1', name: 'Priya S.', dropoff: 'Central Library', status: 'boarded' },
      { id: 'p-er02-2', name: 'Ankit V.', dropoff: 'CSE', status: 'boarded' },
      { id: 'p-er02-3', name: 'Devika L.', dropoff: 'ECE', status: 'boarded' },
      { id: 'p-er02-4', name: 'Mohit B.', dropoff: 'MAC (Multi-Activity Centre)', status: 'boarded' },
    ],
    status: 'boarding',
    homeZone: 'north',
  },
  {
    id: 'ER-03',
    driverName: 'Arjun M.',
    driverPhotoSeed: 'arjun',
    location: { x: 700, y: 115 },
    capacity: 4,
    passengers: [
      { id: 'p-er03-1', name: 'Ishaan T.', dropoff: 'Ganga Bhawan', status: 'boarded' },
    ],
    status: 'idle',
    homeZone: 'north',
  },
  {
    id: 'ER-04',
    driverName: 'Manoj S.',
    driverPhotoSeed: 'manoj',
    location: { x: 400, y: 280 },
    capacity: 4,
    passengers: [
      { id: 'p-er04-1', name: 'Rhea G.', dropoff: 'Azad Bhawan', status: 'boarded' },
      { id: 'p-er04-2', name: 'Yash D.', dropoff: 'APJ Block', status: 'boarded' },
      { id: 'p-er04-3', name: 'Meera A.', dropoff: 'SAC (Student Activity Centre)', status: 'boarded' },
    ],
    status: 'boarding',
    homeZone: 'mid',
  },
];

export const INITIAL_STUDENT = {
  id: 'stu-1001',
  name: 'Aarav Sharma',
  walletBalance: 180,
  walletDebt: 0,
  reputationNoShows: [],
  activeBooking: null,
  rideHistory: [
    { id: 'rh-1', from: 'Main Gate', to: 'Dept of CSE', fare: 10, at: Date.now() - 1000 * 60 * 60 * 4 },
    { id: 'rh-2', from: 'Dept of CSE', to: 'Institute Canteen', fare: 8, at: Date.now() - 1000 * 60 * 60 * 23 },
  ],
};

export const INITIAL_ADMIN_STATS = {
  completedRides: 128,
  avgWaitMin: 4.2,
  revenueToday: 1840,
  leakagePercent: 6.8,
  emptyReturnPercent: 11.4,
};
