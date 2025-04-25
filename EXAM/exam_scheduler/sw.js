const CACHE_NAME = 'exam-scheduler-v1';
const urlsToCache = [
  '/',
  '/manifest.json',
  'exam_scheduler\\icons\\android-launchericon-192-192.png',
  'exam_scheduler\\icons\\android-launchericon-512-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
