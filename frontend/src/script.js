    var map = L.map('map').setView([-8.283, -35.976], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Mapa'
    }).addTo(map);

    L.marker([-8.283, -35.976]).addTo(map)
        .bindPopup('Casa disponível')
        .openPopup();

//Carrossel
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

let current = 0;

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active');
        dots[i].classList.remove('active');
    });

    slides[index].classList.add('active');
    dots[index].classList.add('active');
}

function nextSlide() {
    current = (current + 1) % slides.length;
    showSlide(current);
}

dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
        current = i;
        showSlide(current);
    });
});

setInterval(nextSlide, 4000);
