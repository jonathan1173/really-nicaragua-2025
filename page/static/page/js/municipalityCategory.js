document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll('button[data-name]');
  const contentContainer = document.getElementById('content-container');
  const municipality = document.getElementById('municipality-data').dataset.municipality;

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const category = button.getAttribute('data-name');

      axios.get(`/home/maps/${municipality}/options`, {
        params: { category: category }
      })
      .then(response => {
        const data = response.data;

        if (data.content) {
          contentContainer.innerHTML = `
            <div class="bg-white p-4 rounded shadow">
              <h4 class="text-2xl font-bold text-gray-800 mb-2">${data.category}</h4>
              <div class="text-gray-700">${data.content}</div>
            </div>
          `;
        } else {
          contentContainer.innerHTML = `<p class="text-gray-500 italic">No hay contenido disponible para esta categoría.</p>`;
        }
      })
      .catch(() => {
        contentContainer.innerHTML = `<p class="text-red-500">Error al cargar contenido.</p>`;
      });
    });
  });
});


