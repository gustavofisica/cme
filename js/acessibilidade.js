//Habilita do Alto Contraste da Barra Brasil
var body = document.querySelector('body');
var altoContraste = document.querySelector('#alto-contraste')
	
function verificaBody(){
	// Verifica se a classe do body não é "contraste"
	if(body.classList != "contraste"){
		// Se não for contraste, requisita uma confirmação para pessoas autistas
		var retorno = confirm("Ei, espera um momento.\nVamos falar de autismo?\nA função que você acaba de habilitar ativa o Alto Contraste da página que pode ser desconfortável para pessoas autistas.\nNossa preocupação é oferecer a melhor experiência ao usuário.\nPortanto se você for autista ou estiver acompanhando uma pessoa autista, pode cancelar essa ação.\nMas se for uma pessoa de baixa visão, essa função foi pensada em você! Nessa caso, basta clicar em Ok.");
		// Se o usuário confirma a alteração de contraste, efetua-se a troca de classe do body
		if(retorno == true){
			// Inclusão da classe "contraste" no body do HTML
			body.classList.add("contraste");
		}
	// Se o "contraste" estiver definido na classe do body
	} else{
		// Retira a classe o valor da classe do html
		body.classList.remove("contraste");
	}
}

// Chama a função verificaBody se o link ALTO CONTRASTE foi clicado
altoContraste.addEventListener('click', verificaBody);