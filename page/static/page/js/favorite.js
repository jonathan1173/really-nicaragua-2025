document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('favorite-btn');
  const url = btn.getAttribute('data-url');

  // Verificar si ya está en favoritos
  axios.get('/users/is-favorite/', { params: { url: url } })
    .then(response => {
      if (response.data.favorite) {
        btn.textContent = 'Quitar favorito';
        btn.classList.remove('bg-blue-500');
        btn.classList.add('bg-red-500');
      } else {
        btn.textContent = 'Agregar favorito';
        btn.classList.remove('bg-red-500');
        btn.classList.add('bg-blue-500');
      }
    });
  
  // Toggle favoritos
  btn.addEventListener('click', function () {
    const title = btn.getAttribute('data-title');

    axios.get('/users/toggle-favorite/', {
      params: {
        url: url,
        title: title
      }
    })
    .then(response => {
      const added = response.data.status === 'added';
      btn.textContent = added ? 'Quitar favorito' : 'Agregar favorito';

      // Cambiar color
      if (added) {
        btn.classList.remove('bg-blue-500');
        btn.classList.add('bg-red-500');
      } else {
        btn.classList.remove('bg-red-500');
        btn.classList.add('bg-blue-500');
      }
    })
    .catch(error => {
      console.error('Error toggling favorite:', error);
    });
  });
});
