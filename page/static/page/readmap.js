const waitForMap = setInterval(() => {
  if (typeof simplemaps_countrymap !== "undefined" && simplemaps_countrymap.hooks) {
    clearInterval(waitForMap);
    simplemaps_countrymap.hooks.click_state = function (id) {
      const estado = simplemaps_countrymap_mapdata.state_specific[id];
      if (estado && estado.name) {
        
        
        console.log("redirigiendo");
        const targetUrl = `http://127.0.0.1:8000/home/maps/${estado.name.toLowerCase()}`;
        console.log(targetUrl);
        window.location.href = targetUrl;

      }
    };
  }
}, 100);
