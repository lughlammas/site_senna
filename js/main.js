
document.addEventListener('DOMContentLoaded', () => {
    const imagensGrid = document.querySelector('.imagens-grid');

    for (let i = 1; i <= 10; i++) {
        const link = document.createElement('a');
        link.href = `pages/curiosidade${i}.html`;
        link.dataset.title = `Curiosidade ${i}`;

        const img = document.createElement('img');
        img.src = `assets/Ayrton${i}.jpg`;
        img.alt = `Ayrton Senna ${i}`;

        link.appendChild(img);
        imagensGrid.appendChild(link);
    }
});
