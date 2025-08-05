document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('favorite-btn');  // ID corregido
  const url = btn.getAttribute('data-url');
  const btnText = btn.querySelector('.btn-text'); // elemento texto

  axios.get('/users/is-favorite/', { params: { url: url } })
    .then(response => {
      if (response.data.favorite) {
        btnText.textContent = 'Quitar favorito';
        btn.classList.remove('bg-blue-700');
        btn.classList.add('bg-red-600');
      } else {
        btnText.textContent = 'Agregar favorito';
        btn.classList.remove('bg-red-600');
        btn.classList.add('bg-blue-700');
      }
    });

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
      btnText.textContent = added ? 'Quitar favorito' : 'Agregar favorito';

      if (added) {
        btn.classList.remove('bg-blue-700');
        btn.classList.add('bg-red-600');
      } else {
        btn.classList.remove('bg-red-600');
        btn.classList.add('bg-blue-700');
      }
    })
    .catch(error => {
      console.error('Error toggling favorite:', error);
    });
  });
});
