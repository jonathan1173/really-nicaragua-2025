document.addEventListener("DOMContentLoaded", function () {
  const btnMenuToggle = document.getElementById("btn-menu-toggle");
  const navbarMenu = document.getElementById("navbar-menu");

  const btnSearchToggle = document.getElementById("btn-search-toggle");
  const searchMobile = document.getElementById("navbar-search-mobile");

  // Toggle menú hamburguesa móvil
  btnMenuToggle.addEventListener("click", () => {
    const isExpanded = btnMenuToggle.getAttribute("aria-expanded") === "true";
    btnMenuToggle.setAttribute("aria-expanded", !isExpanded);
    navbarMenu.classList.toggle("hidden");
  });

  // Toggle búsqueda móvil (solo si existe)
  if (btnSearchToggle && searchMobile) {
    btnSearchToggle.addEventListener("click", () => {
      const isVisible = searchMobile.style.display === "block";
      searchMobile.style.display = isVisible ? "none" : "block";
      btnSearchToggle.setAttribute("aria-expanded", !isVisible);
    });
  }
});
