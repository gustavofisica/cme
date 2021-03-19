var caixa = document.querySelector('.caixa');
var altoContraste = document.querySelector('#alto-contraste');
var imagensContraste = ["logo",
	"Icone-Sistema-CME",
	"Icone-Tabela-CME",
	"Icone-Normas-CME"
];

function trocaContraste() {
	var caixa = document.querySelector('.caixa');

	if (caixa.classList.contains("contraste")) {

		caixa.classList.remove("contraste");

		for (let i = 0; i < imagensContraste.length; i++) {
			var elemento = document.getElementById(imagensContraste[i]);
			elemento.src = "img/" + imagensContraste[i] + ".png";
		}

	} else {

		var retorno = confirm("Ei, espera um momento.\nA função que você acaba de habilitar ativa o Alto Contraste da página que pode ser desconfortável para pessoas autistas.\nNossa preocupação é oferecer a melhor experiência ao usuário.\nPortanto se você for autista ou estiver acompanhando uma pessoa autista, pode cancelar essa ação.\nMas se for uma pessoa de baixa visão, essa função foi pensada em você! Nessa caso, basta clicar em Ok.");

		if (retorno == true) {

			caixa.classList.add("contraste");

			for (let i = 0; i < imagensContraste.length; i++) {
				var elemento = document.getElementById(imagensContraste[i]);
				elemento.src = "img/" + imagensContraste[i] + "-contraste.png";
			}
		}
	}
}

altoContraste.addEventListener('click', trocaContraste);