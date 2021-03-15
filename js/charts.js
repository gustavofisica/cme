google.charts.load('current', {packages: ['corechart']}); // Roda a biblioteca do Google Charts mais recente

var dadosSecundarios = [
    ['Cursos',
        'TEM JEOL JEM 1200EX-II',
        'SEM JEOL JSM 6360-LV',
        'SEM TESCAN VEGA3 LMU',
        'SEM FEI Quanta 450 FEG',
        'Raman Witec alpha 300R',
        'AFM Shimadzu SPM 9500 J3',
        'SEM FEI Phenom'],
    ['Química', 12.5, 98.7, 25.3, 0.6, 3.3, 2.8, 1.2],
    ['Física', 13.0, 90.7, 17.1, 0.8, 2.8, 3.4, 1.2],
    ['Botânica', 9.3, 93.0, 15.8, 0.9, 1.8, 3.8, 1.2],
    ['Biologia Celular', 14.9, 97.5, 17.1, 1.3, 4.4, 5.1, 1.2],
    ['PIPE', 14.3, 98.7, 13.6, 2.1, 4.9, 5.7, 1.2],
    ['Engenharia Mecânica', 18.2, 16.5, 0.0, 2.2, 5.2, 2.3, 1.2]
];

google.charts.setOnLoadCallback(desenharGraficoSecundario);

function desenharGraficoSecundario(){

    var data = new google.visualization.arrayToDataTable(dadosSecundarios);
    var view = new google.visualization.DataView(data);

    for (let index = 0; index < dadosPrimarios.length; index++) {

        view.setColumns([0, index + 1]);

        var graficoEscondido = document.getElementById('grafico-escondido');
        var graficoSecundario = new google.visualization.PieChart(graficoEscondido);

        google.visualization.events.addListener(graficoSecundario, 'ready', function(){

            var imagemGraficoSecundario = '<img src="' + graficoSecundario.getImageURI() + '">';

            dadosPrimarios[index][3] = imagemGraficoSecundario;
        });

        graficoSecundario.draw(view, opcoesSecundaria);
        
    }

    var opcoesSecundaria = {
        'title': 'Distribuição por Cursos'
    }

    desenharGrafico();
}


var dadosPrimarios = [
    ['TEM JEOL JEM 1200EX-II', 2000, 'color: #934849'],
    ['SEM JEOL JSM 6360-LV', 500, 'color: #1B1BBD'],
    ['SEM TESCAN VEGA3 LMU', 230, 'color: #258325'],
    ['SEM FEI Quanta 450 FEG', 50, 'color: #FF90A3'],
    ['Raman Witec alpha 300R', 900,'color: #E31616'],
    ['AFM Shimadzu SPM 9500 J3', 260, 'color: #E7E722'],
    ['SEM FEI Phenom', 200, 'color: #C5A5CF']
]; // Elenca os dados do Gráfico

google.charts.setOnLoadCallback(desenharGrafico);

function desenharGrafico(){
    var tabela = new google.visualization.DataTable(); //Constroí a planilha de dados
    tabela.addColumn('string', 'Equipamento'); //Insere a primeira coluna
    tabela.addColumn('number', 'Horas de Uso'); // Insere a segunda coluna
    tabela.addColumn({type: 'string', role: 'style'}); //Insere a regra de cor do dado no gráfico

    tabela.addColumn({
        type: 'string',
        label: 'Tooltip Chart',
        role: 'tooltip',
        'p': {'html': true}
    });

    tabela.addRows(dadosPrimarios); // Insere as linhas que estão na variável dados

    var opcoes = {
        'tooltip': {isHtml: true},
        'title': 'Estatísticas CME',
        'legend': 'none',
        'height': 500,
        'width': 600
    }; // Carrega as opções para a construção do gráfico

    var grafico = new google.visualization.BarChart(document.getElementById('grafico')); //Identifica o tipo de gráfico e onde ele deve ser desenhado no HTML
    grafico.draw(tabela, opcoes); // Desenha o gráfico com os dados da tabela com as opções elencadas
} //Função que carrega os dados