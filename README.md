# TrackCash-First-Step

<h1 align="center">
  <img alt="TackCash" title="TackCash" src="https://sistema.trackcash.com.br/images/logo/logo_trackcash_vert.png" width="300px" />
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

### Extra

Para criar uma melhor interação do usuário com a interface foi implementada a leitura de dados, desta forma o usuário agora pode entrar com as datas que irão definir o início e término do período de tempo. Uma verificação utilizando Regex para confirmar o formato da data esperado (dd/mm/YYYY) e a verificação que a data final é depois da data inicial.

### Observações

* Nas opções de configuração do selenium a flag headless está  setada com o valor False, configuração padrão, para melhor entender o passo a passo das instruções passadas para a realização da tarefa.
* No código pode ser visto o uso de diversos delays, isto se deve a latência da conexão utilizada durante os teste com o script, foram necessários para que o browser pudesse atualizar os estados do componente da página ou carregar a página.
* A acreção da leitura de datas ainda tem muito a ser melhorada para ter melhores aspectos de UX e também é necessário a criação de testes automatizados.

