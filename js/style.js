//Dinâmica do Cabeçalho Fixo
function init(){
	var cabecalho = document.querySelector('header');
	var cabecalhoEspaco = document.querySelector('.cabecalho-espaco');
	var cabecalhoOffset = cabecalho.offsetTop;
	
	function verificaCabecalho(){
		var scrollTop = window.scrollY;
		var cabecalhoAltura = cabecalho.offsetHeight;
		
		if(scrollTop >= cabecalhoOffset){
			// Rolagem da página passou do elemento
			cabecalho.classList.add("header-fixo");
			
			
			//ativa o cabecalho-espaco para ocupar o espaço perdido
			cabecalhoEspaco.style.height = cabecalhoAltura + 'px';
			
		} else {
			//Retira a classe adicional do elemento
			cabecalho.classList.remove("header-fixo");
			
			//retira o cabecalho-espaco
			cabecalhoEspaco.style.height = 0;
		}
	}
	
	window.addEventListener('scroll', verificaCabecalho);
	window.addEventListener('resize', verificaCabecalho);
}

window.addEventListener('load',init);

//Habilita do Alto Contraste da Barra Brasil
var body = document.querySelector('body');
var altoContraste = document.querySelector('#contrast')
	
function verificaBody(){
	// Verifica se a classe do body é contraste
	if(body.classList != "contraste"){
		// Se não for contraste, incluí a classe contraste
		body.classList.add("contraste");

	} else{
		//Se o contraste estiver definido, retira a classe
		body.classList.remove("contraste");
	}
}

altoContraste.addEventListener('click', verificaBody);