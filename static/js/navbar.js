document.addEventListener("DOMContentLoaded", function () {
  const btnMenuToggle = document.getElementById("btn-menu-toggle");
  const navbarMenu = document.getElementById("navbar-menu");
  const btnSearchToggle = document.getElementById("btn-search-toggle");
  const searchMobile = document.getElementById("navbar-search-mobile");

  // Función para cerrar todos los menús
  function closeAllMenus() {
    // Cerrar menú hamburguesa
    navbarMenu.classList.add("hidden");
    btnMenuToggle.setAttribute("aria-expanded", "false");
    
    // Cerrar búsqueda móvil
    if (searchMobile) {
      searchMobile.classList.add("hidden");
      btnSearchToggle.setAttribute("aria-expanded", "false");
    }
  }

  // Toggle menú hamburguesa móvil
  btnMenuToggle.addEventListener("click", (e) => {
    e.preventDefault();
    
    const isMenuExpanded = btnMenuToggle.getAttribute("aria-expanded") === "true";
    
    if (isMenuExpanded) {
      // Si el menú está abierto, cerrarlo
      navbarMenu.classList.add("hidden");
      btnMenuToggle.setAttribute("aria-expanded", "false");
    } else {
      // Si el menú está cerrado, cerrar búsqueda primero y luego abrir menú
      if (searchMobile) {
        searchMobile.classList.add("hidden");
        btnSearchToggle.setAttribute("aria-expanded", "false");
      }
      
      // Abrir menú
      navbarMenu.classList.remove("hidden");
      btnMenuToggle.setAttribute("aria-expanded", "true");
    }
  });

  // Toggle búsqueda móvil
  if (btnSearchToggle && searchMobile) {
    btnSearchToggle.addEventListener("click", (e) => {
      e.preventDefault();
      
      const isSearchExpanded = btnSearchToggle.getAttribute("aria-expanded") === "true";
      
      if (isSearchExpanded) {
        // Si la búsqueda está abierta, cerrarla
        searchMobile.classList.add("hidden");
        btnSearchToggle.setAttribute("aria-expanded", "false");
      } else {
        // Si la búsqueda está cerrada, cerrar menú primero y luego abrir búsqueda
        navbarMenu.classList.add("hidden");
        btnMenuToggle.setAttribute("aria-expanded", "false");
        
        // Abrir búsqueda
        searchMobile.classList.remove("hidden");
        btnSearchToggle.setAttribute("aria-expanded", "true");
        
        // Enfocar el input de búsqueda
        const searchInput = document.getElementById("search-navbar-mobile-input");
        if (searchInput) {
          setTimeout(() => {
            searchInput.focus();
          }, 100);
        }
      }
    });
  }

  // Cerrar menús al hacer clic fuera (opcional)
  document.addEventListener("click", (e) => {
    const isClickInsideNav = e.target.closest("nav");
    if (!isClickInsideNav) {
      closeAllMenus();
    }
  });

  // Cerrar menús al presionar Escape (opcional)
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeAllMenus();
    }
  });
});