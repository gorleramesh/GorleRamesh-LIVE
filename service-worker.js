// Installing service worker
const CACHE_NAME  = 'Gorle Ramesh';

/* Add relative URL of all the static content you want to store in
 * cache storage (this will help us use our app offline)*/
let resourcesToCache = ["./index.html", "./images/Cloudy.svg","./images/mainback.png","./images/phone.png", "./illus/light.svg","./illus/clear.svg","./illus/ramesh.svg","./illus/learnyt.svg","./illus/light.svg","./illus/shiny.svg", "./styles.css"];

self.addEventListener("install", e=>{
    e.waitUntil(
        caches.open(CACHE_NAME).then(cache =>{
            return cache.addAll(resourcesToCache);
        })
    );
});
