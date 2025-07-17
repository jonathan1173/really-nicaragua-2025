window.addEventListener('load', function () {
  if (typeof simplemaps_countrymap !== 'undefined') {
    simplemaps_countrymap.load();
  }
});


const waitForMap = setInterval(() => {
  if (typeof simplemaps_countrymap !== "undefined" && simplemaps_countrymap.hooks) {
    clearInterval(waitForMap);
    simplemaps_countrymap.hooks.click_state = function (id) {
      const estado = simplemaps_countrymap_mapdata.state_specific[id];
      if (estado && estado.name) {
        

        console.log("redirigiendo");
        const baseUrl = window.location.origin;
        const targetUrl = `${baseUrl}/home/maps/${estado.name}`;
        console.log(targetUrl);
        window.location.href = targetUrl;

      }
    };
  }
}, 100);