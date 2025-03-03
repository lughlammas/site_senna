document.addEventListener('DOMContentLoaded', () => {
    alert('Dê play e sinta o Groove do Jazz de Senna 🎷🔥'); // <- Essa belezinha aqui

    const imagens = [
        { src: "assets/ayrton1.jpg", titulo: "O Kart de Lata que Virou Lenda", link: "pages/1 - O Kart de Lata que Virou Lenda.html" },
        { src: "assets/ayrton2.jpg", titulo: "Primeira Vitória na F1 — Estoril 1985", link: "pages/2 - Primeira Vitória na F1 — Estoril 1985.html" },
        { src: "assets/ayrton3.jpg", titulo: "A Magia na Chuva — Donington 1993", link: "pages/3 - A Magia na Chuva — Donington 1993.html" },
        { src: "assets/ayrton4.jpg", titulo: "A Volta Perfeita em Mônaco", link: "pages/4 - A Volta Perfeita em Mônaco.html" },
        { src: "assets/ayrton5.jpg", titulo: "Senna e Prost — Guerra de Gigantes", link: "pages/5 - Senna e Prost — Guerra de Gigantes.html" },
        { src: "assets/ayrton6.jpg", titulo: "Brasil em Lágrimas — Interlagos 1991", link: "pages/6 - Brasil em Lágrimas — Interlagos 1991.html" },
        { src: "assets/ayrton7.jpg", titulo: "Ayrton Off-Track — O Homem por Trás do Mito", link: "pages/7 - Ayrton Off-Track — O Homem por Trás do Mito.html" },
        { src: "assets/ayrton8.jpg", titulo: "O Capacete Amarelo — Símbolo Imortal", link: "pages/8 - O Capacete Amarelo — Símbolo Imortal.html" },
        { src: "assets/ayrton9.jpg", titulo: "O Último Ato — Imola 1994", link: "pages/9 - O Último Ato — Imola 1994.html" },
        { src: "assets/ayrton10.jpg", titulo: "O Legado Inquebrável", link: "pages/10 - O Legado Inquebrável.html" }
    ];

    const imagensGrid = document.querySelector('.imagens-grid');
    const audio = document.getElementById('background-audio');
    const toggleButton = document.getElementById('toggle-audio');

    let isPlaying = false;

    // Tenta iniciar o áudio automaticamente no mute (Chrome friendly)
    audio.volume = 0;
    const autoPlayPromise = audio.play();

    if (autoPlayPromise !== undefined) {
        autoPlayPromise.then(() => {
            console.log('🎷 Autoplay funcionou (milagre!)');
            audio.volume = 1; // Som normal após start
            isPlaying = true;
            toggleButton.innerText = '🎷 Jazz Off';
        }).catch(() => {
            console.warn('🚫 Autoplay bloqueado, esperando interação');
        });
    }

    // Botão manual de controle (caso autoplay falhe)
    toggleButton.addEventListener('click', () => {
        if (isPlaying) {
            audio.pause();
            toggleButton.innerText = '🎷 Jazz On';
        } else {
            audio.volume = 1; // Garante volume certo
            audio.play().catch(err => console.warn('Erro ao dar play:', err));
            toggleButton.innerText = '🎷 Jazz Off';
        }
        isPlaying = !isPlaying;
    });

    // Popula a galeria dinamicamente
    imagens.forEach(imagem => {
        const container = document.createElement('div');
        container.classList.add('foto');

        container.innerHTML = `
            <a href="${imagem.link}">
                <img src="${imagem.src}" alt="${imagem.titulo}">
                <div class="hover-text">${imagem.titulo}</div>
            </a>
        `;

        imagensGrid.appendChild(container);
    });
});
