var campoEmail = document.querySelector('#email')
var sugestao = document.querySelector('#sugestao')

var domains = ['gmail.com', 'aol.com', 'ufpr.br'];
var secondLevelDomains = ['hotmail']
var topLevelDomains = ["com", "net", "org", "br"];

if (campoEmail != null) {
  campoEmail.addEventListener('blur', function () {
    Mailcheck.run({
      email: campoEmail.value,
      domains: domains, // optional
      topLevelDomains: topLevelDomains, // optional
      secondLevelDomains: secondLevelDomains, // optional
      suggested: function (suggestion) {
        sugestao.style.display = 'block';
        sugestao.textContent = 'Você quis dizer: ' + suggestion.full + ' ?';
        sugestao.parentNode.classList.add('contatoCampo--erro');
        campoEmail.classList.add('erro');
        sugestao.setAttribute('tabindex', '0');
        sugestao.setAttribute('role', 'alert');
      }
    });
  });
}