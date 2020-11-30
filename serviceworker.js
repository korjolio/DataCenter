// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/WebApp/css/estilos.css',
    '/static/WebApp/img/bg_main.jpg',
    '/static/WebApp/img/datacenter-banner1.jpg',
    '/static/WebApp/img/pp.jpg',
    '/static/WebApp/img/principal.jpg',
    '/static/WebApp/vendor/bootstrap/css/bootstrap.css',
    '/static/WebApp/vendor/bootstrap/css/bootstrap.css.map',
    '/static/WebApp/vendor/bootstrap/css/bootstrap.min.css',
    '/static/WebApp/vendor/bootstrap/css/bootstrap.min.css.map',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.bundle.js',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.bundle.js.map',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.bundle.min.js',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.bundle.min.js.map',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.js',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.js.map',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.min.js',
    '/static/WebApp/vendor/bootstrap/js/bootstrap.min.js.map',
    '/static/WebApp/vendor/font-awesome/css/font-awesome.css',
    '/static/WebApp/vendor/font-awesome/css/font-awesome.css.map',
    '/static/WebApp/vendor/font-awesome/css/font-awesome.min.css',
    '/static/WebApp/vendor/font-awesome/fonts/fontawesome-webfont.eot',
    '/static/WebApp/vendor/font-awesome/fonts/fontawesome-webfont.svg',
    '/static/WebApp/vendor/font-awesome/fonts/fontawesome-webfont.ttf',
    '/static/WebApp/vendor/font-awesome/fonts/fontawesome-webfont.woff',
    '/static/WebApp/vendor/font-awesome/fonts/fontawesome-webfont.woff2',
    '/static/WebApp/vendor/font-awesome/fonts/FontAwesome.otf',

];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
/*
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});
*/

self.addEventListener("fetch", function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result) {
            return caches.open(staticCacheName)
            .then(function(c) {
                c.put(event.request.url, result.clone())
                return result
            })
        })
        .catch(function(e) {
            return caches.match(event.request);
        })
    )
})