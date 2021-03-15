//Seleciona o Header do HTML
var backgroundImage = document.querySelector('header');

//Array de endereços de imagens
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

//Carrega imagem randomicamente
var bg = images[Math.floor(Math.random() * images.length)];
//Insere a imagem carregada no estilo da página
backgroundImage.style.backgroundImage = "url(" + bg + ")";


var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}