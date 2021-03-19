<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!--Configuração de Codificação de Caracteres-->
    <meta charset="utf-8">
    <!--Configuração de Compatibilidade de Browsers-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Configuração de Escalonamento para Device Mobile-->
    <meta name="viewport" content="width=device-width">
    <!--Configuração da Unidade Organizacional do CME da Barra Brasil-->
    <meta property="creator.productor" content="http://estruturaorganizacional.dados.gov.br/id/unidade-organizacional/241245">
    <!--Estilos da página-->
    <link href="css/estilos.css" rel="stylesheet">
    <!--Incorporação da fonte Noto Serif da Google-->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap" rel="stylesheet" type="text/css">
    <!--Incorporação da fonte awsome para ícones da página-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!--Inclusão do ícone do CME na aba do Browser-->
    <link rel="shortcut icon" href="img/favicon.png">
    <!--Título da Página na aba do Browser-->
    <title>Centro de Microscopia Eletrônica</title>
    <!--Carregando as Bibliotecas do Google Charts-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <!--Configuração Local do Google Charts-->
    <script type="text/javascript" src="js/charts.js"></script>
</head>

<!--Início do Menu de Navegação-->
<nav class="menu">
    <!--Link de direcionamento da barra de acessibilidade para menu-->
    <a name="nav" id="nav"></a>
    <!--Início da Lista de Links do Menu de 1° Nível-->
    <ul>
        <!--Link para Página Incial-->
        <li><a href="index.php">Página Inicial</a></li>
        <!--Link para Páginas da Organização do Centro de Microscopia Eletrônica-->
        <li class="sub-menu"><a href="#">CME</a>
            <!--Início da Lista de Links do Menu de 2° Nível-->
            <ul>
                <!--Link para Página da Chefia do Centro de Microscopia Eletrônica-->
                <li><a href="direcao.php">Chefia</a></li>
                <!--Link para Página do Corpo de Conselheiros do Centro de Microscopia Eletrônica-->
                <li><a href="conselho.php">Conselho</a></li>
                <!--Link para Página da Equipe Técnica do Centro de Microscopia Eletrônica-->
                <li><a href="equipe_tecnica.php">Equipe Técnica</a></li>
                <!--Link para Página do Regimento Interno do Centro de Microscopia Eletrônica-->
                <li><a href="regimento.php">Regimento</a></li>
                <!--Link para Página da Descrição do Funcionamento do Centro de Microscopia Eletrônica-->
                <li><a href="#">Funcionamento</a></li>
                <!--Link para Página da História do Centro de Microscopia Eletrônica-->
                <li><a href="#">Histórico</a></li>
                <!--Link para Página de Descrição da Missão e Visão do Centro de Microscopia Eletrônica-->
                <li><a href="#">Missão e Visão</a></li>
                <!--Link para Página de Disponibilização do Logtipo do Centro de Microscopia Eletrônica-->
                <li><a href="#">Logotipo</a></li>
                <!--Link para Página do Planejamento Estratégico do Centro de Microscopia Eletrônica-->
                <li><a href="#">Planejamento Estratégico</a></li>
            </ul>
            <!--Final da Lista de Links do Menu de 2° Nível-->
        </li>
        <!--Link para Página de Trabalhos Desenvolvidos com Auxílio do Centro de Microscopia Eletrônica-->
        <li><a href="#">Produção Científica</a></li>
        <!--Link para Página de Orientações aos Usuários-->
        <li class="sub-menu"><a href="#">Orientações aos Usuários</a>
            <!--Início da Lista de Links do Menu de 2° Nível-->
            <ul>
                <!--Link para Página de Normas para Usuários do Centro de Microscopia Eletrônica-->
                <li><a href="#">Normas</a></li>
                <!--Link Alternativo para Página do Sistema Interno de Gerenciamento do Centro de Microscopia Eletrônica-->
                <li><a href="#">Sistema de Gerenciamento</a></li>
                <!--Link para Página de Perguntas Frequêntes do Centro de Microscopia Eletrônica-->
                <li><a href="#">Perguntas Frequentes</a></li>
            </ul>
            <!--Final da Lista de Links do Menu de 2° Nível-->
        </li>
        <!--Link para Página da Infraestrutura do Centro de Microscopia Eletrônica-->
        <li class="sub-menu"><a href="#">Infraestrutura</a>
            <!--Início da Lista de Links do Menu de 2° Nível-->
            <ul>
                <!--Link para Página dos Equipamentos do Centro de Microscopia Eletrônica-->
                <li><a href="#">Equipamentos</a></li>
                <!--Link para Página dos Laboratórios do Centro de Microscopia Eletrônica-->
                <li><a href="#">Laboratórios</a></li>
                <!--Link para Página dos Equipamentos do Centro de Microscopia Eletrônica-->
                <li><a href="#">Tabelas de Serviços e Preços</a></li>
            </ul>
            <!--Final da Lista de Links do Menu de 2° Nível-->
        </li>
        <!--Link para Galeria de Imagens-->
        <li><a href="#">Galeria</a></li>
        <!--Link para Softwares Úteis para Microscopia-->
        <li><a href="#">Softwares Úteis</a></li>
    </ul>
    <!--Final da Lista de Links do Menu-->
</nav>
<!--Final do Menu de Navegação-->
<div class="menu-toggle"><i class="fa fa-bars" aria-hidden="true"></i></div>

<script>
    var menuTogle = document.querySelector('.menu-toggle');
    var menu = document.querySelector('.menu');

    menuTogle.addEventListener("click", (e) => {
        e.stopPropagation();
        if (menu.classList == "menu") {
            menu.classList.add("on");
        } else {
            menu.classList.remove("on");
        }
    });
</script>