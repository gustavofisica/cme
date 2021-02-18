google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawTooltipCharts);

// Set up data for visible chart.
var primaryData = [
    ['Microscópio Eletrônico de Transmissão JEOL JEM 1200EX-II', 22.4],
    ['Microscópio Eletrônico de Varredura JEOL JSM 6360-LV', 111.3],
    ['Microscópio Eletrônico de Varredura TESCAN VEGA3 LMU', 19.2],
    ['Microscópio Eletrônico de Varredura FEI Quanta 450 FEG', 1.9],
    ['Microscópio Raman Confocal Witec alpha 300R', 6.4],
    ['Microscópio de Força Atômica Shimadzu SPM 9500 J3', 2.4],
    ['Microscópio Eletrônico de Varredura de Bancada FEI Phenom', 2.4]
];

// Set up data for your tooltips.
var tooltipData = [
    ['Cursos',
    'Microscópio Eletrônico de Transmissão JEOL JEM 1200EX-II', 
    'Microscópio Eletrônico de Varredura JEOL JSM 6360-LV', 
    'Microscópio Eletrônico de Varredura TESCAN VEGA3 LMU', 
    'Microscópio Eletrônico de Varredura FEI Quanta 450 FEG',
    'Microscópio Raman Confocal Witec alpha 300R', 
    'Microscópio de Força Atômica Shimadzu SPM 9500 J3',
    'Microscópio Eletrônico de Varredura de Bancada FEI Phenom'],
    ['Química',             12.5,   98.7,   25.3,   0.6,    3.3,    2.8,    1.2],
    ['Física',              13.0,   90.7,   17.1,   0.8,    2.8,    3.4,    1.2],
    ['Botânica',            9.3,    93.0,   15.8,   0.9,    1.8,    3.8,    1.2],
    ['Biologia Celular',    14.9,   97.5,   17.1,   1.3,    4.4,    5.1,    1.2],
    ['PIPE',                14.3,   98.7,   13.6,   2.1,    4.9,    5.7,    1.2],
    ['Engenharia Mecânica', 18.2,   16.5,   0.0,    2.2,    5.2,    2.3,    1.2]
];

var primaryOptions = {
    legend: 'none',
    tooltip: {isHtml: true} // This MUST be set to true for your chart to show.
};

var tooltipOptions = {
    title: 'Detalhe de Utilização por Curso',
    pieSliceText: 'value'
};

// Draws your charts to pull the PNGs for your tooltips.
function drawTooltipCharts() {

    var data = new google.visualization.arrayToDataTable(tooltipData);
    var view = new google.visualization.DataView(data);

    // For each row of primary data, draw a chart of its tooltip data.
    for (var i = 0; i < primaryData.length; i++) {

        // Set the view for each event's data
        view.setColumns([0, i + 1]);

        var hiddenDiv = document.getElementById('hidden_div');
        var tooltipChart = new google.visualization.PieChart(hiddenDiv);

        google.visualization.events.addListener(tooltipChart, 'ready', function() {

        // Get the PNG of the chart and set is as the src of an img tag.
        var tooltipImg = '<img src="' + tooltipChart.getImageURI() + '">';

        // Add the new tooltip image to your data rows.
        primaryData[i][2] = tooltipImg;

        });
        tooltipChart.draw(view, tooltipOptions);
    }
    drawPrimaryChart();
}

function drawPrimaryChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Event');
    data.addColumn('number', 'Highest Recent Viewership');

    // Add a new column for your tooltips.
    data.addColumn({
        type: 'string',
        label: 'Tooltip Chart',
        role: 'tooltip',
        'p': {'html': true}
    });

    // Add your data (with the newly added tooltipImg).
    data.addRows(primaryData);

    var visibleDiv = document.getElementById('visible_div');
    var primaryChart = new google.visualization.BarChart(visibleDiv);
    primaryChart.draw(data, primaryOptions);

}