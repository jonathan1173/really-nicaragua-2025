document.addEventListener("DOMContentLoaded", () => {
  const hamburgerButton = document.getElementById("hamburger-button")
  const navbarContent = document.querySelector(".navbar__content")

  if (hamburgerButton && navbarContent) {
    hamburgerButton.addEventListener("click", () => {
      // Toggle the 'is-open' class on both the button and the content
      hamburgerButton.classList.toggle("is-open")
      navbarContent.classList.toggle("is-open")
    })
  }
})
