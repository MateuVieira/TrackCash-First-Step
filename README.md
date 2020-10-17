# TrackCash-First-Step

<h1 align="center">
  <img alt="TackCash" title="TackCash" src="https://scontent-gru2-2.cdninstagram.com/v/t51.2885-19/s320x320/75487952_484171055518655_7311530687218057216_n.jpg?_nc_ht=scontent-gru2-2.cdninstagram.com&_nc_ohc=099peI-odLgAX_zbfBM&oh=29e463dac08cd8f05f4b2511dbc85bbf&oe=5FB200AE" width="300px" />
</h1>

### Tech

Este projeto foi feito utilizando as seguintes tecnologias:

* Python - version 3.8.5
* time
* selenium - version 3.141.0

### Inicializar

Dentro do diretório raiz deste repositorio, rodar o comando para executar o script:

```sh
$ python3 firstStep.py
```

### Descrição

Este projeto foi proposto como um teste para a avaliação das habilidades com o uso da linguagem de programação Python e o uso da biblioteca Selenium para realizar Web Scraping. O objetivo deste projeto é fazer o login utilizando as credenciais fornecidas na página do marketplace, depois redirecionar a página para o dashboard de gerência de informações de pedidos.

É pedido que se selecione um período de tempo para carregar os dados de pedidos, para este projeto o período estipulado foi de 1 de janeiro de 2018 até 1 de fevereiro de 2018. Após os dados foram atualizados na página, temos de clicar em um botão com a opção de exportar os dados no formato de excel.

O componente para seleção do período de tempo foi implementado utilizando react-daterange-picker, o que impossibilita a entrada de dados no componente Input do Form. A metodologia encontrada para resolver esse problema foi de emular os cliques do mouse nos elementos para a entrada do valor, assim criando um algoritmo para realizar cada ação.

Outro possível metodologia é analisar os requests feitos pela página com os dados para query para busca do período de tempo escolhido, desta maneira não seria mais necessário realizar a emulação dos comando para a escolha do período de tempo.

Quando clicamos no botão para exportar como Excel um popup aparece na tela avisando que o arquivo foi enviado para um email.

#### credenciais

* desenvolvimento@comprenet.com.br
* tecnol@gia2@17
