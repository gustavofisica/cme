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
