//Função Seleciona o Header do HTML
var backgroundImage = document.querySelector('header');

var images = [
    'img/header/MEV_Espiculas_Bio.png',
    'img/header/MET_NanoTubo_Fis.png',
    'img/header/MET_Polimero_Qui.png',
    'img/header/MEV_Inseto_Bio.png',
    'img/header/MEV_Inseto_Pan_Bio.png',
    'img/header/MEV_Planta_Bio.png',
    'img/header/MEV_Planta_Pan_Bio.png',
    'img/header/MEV_Planta_Transv_Bio.png'
];

var bg = images[Math.floor(Math.random() * images.length)];

backgroundImage.style.backgroundImage = "url(" + bg + ")";

//Função do Menu Responsivo
var menuTogle = document.querySelector('.menu-toggle');
var bar = document.querySelector('.menu-toggle i');
var menuUl = document.querySelector('.menu ul');

menuTogle.addEventListener("click", (e) => {

    if (menuUl.classList == "") {
        menuUl.classList.toggle("on");
        bar.classList.remove("fa-bars");
        bar.classList.add("fa-times");
    } else {
        menuUl.classList.toggle("on");
        bar.classList.remove("fa-times");
        bar.classList.add("fa-bars");
    }
});

//Função do Slider

var portifolio = document.querySelector('.portifolio');
if (portifolio != null) {
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        if (n > slides.length) {
            slideIndex = 1
        }
        if (n < 1) {
            slideIndex = slides.length
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
    }
}

//Função da galeria de imagens
let modal = document.querySelector('.modal');
let imagem = document.querySelectorAll('.galeria img');
let imagemModal = document.querySelector('.imagem-modal');
let textoModal = document.querySelector('.descricao-modal');
let imagemModalGaleria = document.querySelector('.imagem-modal-portifolio');
let textoAmostraModal = document.querySelector('.portifolio-amostra');
let textoEquipamentoModal = document.querySelector('.portifolio-decricao-equipamento');
let textoDescricaoModal = document.querySelector('.portifolio-decricao-texto');
let pesquisadorDescricaoModal = document.querySelector('.descricao-pessoas-pesquisador');
let departamentoDescricaoModal = document.querySelector('.descricao-pessoas-departamento');
let tecnicoDescricaoModal = document.querySelector('.descricao-pessoas-tecnico');
let cargoTecnicoDescricaoModal = document.querySelector('.descricao-pessoas-tecnico-cargo');
let botaoFecharModal = document.querySelector('.fechar-modal')


if (imagemModal != null) {
    imagem.forEach(imagem => {
        imagem.addEventListener('click', () => {
            modal.classList.add('abrir');
            let srcModal = imagem.getAttribute("data-original");
            imagemModal.src = srcModal;
            let altTexto = imagem.alt;
            textoModal.textContent = altTexto;
        });
    });
} else if (imagemModalGaleria != null) {
    imagem.forEach(imagem => {
        imagem.addEventListener('click', () => {
            modal.classList.add('abrir');
            let srcModal = imagem.getAttribute("data-original");
            let amostraModal = imagem.getAttribute("data-amostra");
            let equipamentoModal = imagem.getAttribute("data-equipamento");
            let descricaoModal = imagem.getAttribute("data-descricao");
            let pesquisadorModal = imagem.getAttribute("data-pesquisador");
            let departamentoModal = imagem.getAttribute("data-departamento");
            let tecnicoModal = imagem.getAttribute("data-tecnico");
            let cargoModal = imagem.getAttribute("data-cargo");
            imagemModalGaleria.src = srcModal;
            textoAmostraModal.textContent = amostraModal;
            textoEquipamentoModal.textContent = equipamentoModal;
            textoDescricaoModal.textContent = descricaoModal;
            pesquisadorDescricaoModal.textContent = pesquisadorModal;
            departamentoDescricaoModal.textContent = departamentoModal;
            tecnicoDescricaoModal.textContent = tecnicoModal;
            cargoTecnicoDescricaoModal.textContent = cargoModal;
        });
    });
}

modal.addEventListener('click', fecharModal);
if (botaoFecharModal != null) {
    botaoFecharModal.addEventListener('click', removeAbrirModal);
};
document.addEventListener('keydown', (e) => {
    if (e.keyCode == 27) {
        removeAbrirModal();
    }
});

function fecharModal(e) {
    if (e.target.classList.contains('modal')) {
        removeAbrirModal();
    }
}

function removeAbrirModal() {
    modal.classList.remove('abrir');
}