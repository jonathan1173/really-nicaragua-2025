addEventListener('click', e => {

    const color = ['color1', 'color2', 'color3'];
    const animationDuration = 1500;

    for (let i = 0; i < 3; i++) {
        // crea el circulo para renderizarlo luego en el dom 
        const circle = document.createElement('div');
        circle.className = 'ripple';
        circle.classList.add(color[i]);

        // da las propiedades al circulo 

        circle.style.width = '20px';
        circle.style.height = '20px';
        circle.style.position = 'absolute';
        circle.style.left = `${e.pageX}px`;
        circle.style.top = `${e.pageY}px`;

        circle.style.zIndex = '1000';

        circle.style.animationDelay = `${i * 250}ms`
        document.body.appendChild(circle);

        setTimeout(() => circle.remove(), animationDuration + i * 200);

    }
});
