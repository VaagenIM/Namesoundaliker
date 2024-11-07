const cacheName = "Namesoundaliker";  
const assets = ["/"];  // Eventuelle ekstra sider som "kan fungere offline", ikke nødvendig
self.addEventListener("install", (installEvent) => {  
  installEvent.waitUntil(  
    caches.open(cacheName).then((cache) => {  
      cache.addAll(assets);  
    })  
  );  
});