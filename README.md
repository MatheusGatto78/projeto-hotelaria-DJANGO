# HOTEL - projeto 🛎️

_Este é um sistema de gerenciamento de hotel desenvolvido com Django. Ele permite cadastrar quartos, clientes e realizar reservas de forma prática e eficiente. Ideal para pequenos e médios estabelecimentos hoteleiros._

> Caio Pietro Fernandes - N° 03
>  
> Daniel Fonseca Monteiro - N° 05
>  
> Daniele Amaral Santos - N° 07
> 
> Matheus Vinicius Gatto - N° 25
> 
> Murillo Henrique de Oliveira Rodrigues - N° 26
> 
___

### LINKS DE APOIO 🔗
> trello ->  https://trello.com/invite/b/681b9cad0a474cf0d867f30c/ATTI2d08f2b9d14cb3e36c715249d4d8fc7f9E196C58/hotelaria   
> notion -> https://lizard-tangerine-a45.notion.site/RASCUNHO-Hotelaria-1ec6cd955f7a80c5a5e2deb5d4149398?pvs=4
___

## 07/05  
  _O projeto começou com o professor dando ajuda com o passo a passo para preparar o django, o professor usou as etapas passadas na ultima aula, com isso seguimos o resto do dia configurando o Django, porque é uma parte trabalhosa, por isso o apoio do professor é necessário, acreditamos que a parte mais importante da preparação do "ambiente" são os comandos setados para criar de maneira correta o django:_    
###  _INICIANDO O AMBIENTE VIRTUAL_ (no terminal) 🔧

_Criar o ambiente virtual pelo terminal_
_Ctrl + Shift +_
```
python -m venv venv
```
_Entrar no ambiente virtual_
```
.\venv\Scripts\Activate.ps1
```
_INSTALANDO O DJANGO_
_No VSCode, dentro da pasta do projeto com Django, executar o comando_
```
pip install django
```
_Para conferir de todo o procedimento foi feito corretamente, execute:_
```
django-admin
```
- Criando o projeto
```
django-admin startproject "nome do projeto"
```
```
cd "nome do projeto"
```
```
python manage.py runserver
```
## Estrutura Inicial de um Projeto Django: Entendendo os Arquivos e Suas Funções

_Vamos revisar a estrutura do nosso projeto. Assim que criarmos nosso projeto, teremos o arquivo **`manage.py`** e a pasta com o mesmo nome do projeto, além dos demais arquivos.
Dentro dessa pasta, teremos o arquivo **`__init__.py`**, que estará vazio. Esse arquivo indica para o Python que essa pasta **`teste01`** faz parte de um módulo Python.
Os arquivos **`asgi.py`** e **`wsgi.py`** são os arquivos de configuração que, quando colocarmos o site em um servidor, o servidor saberá como lidar com esse projeto. Utilizaremos esses arquivos apenas no momento de fazer o **deploy** do projeto.
  No arquivo **`urls.py`**, é onde definiremos os links, os endereços das páginas do nosso site. Já o **`settings.py`** é onde iremos de fato configurar o projeto. É dentro desse arquivo que definiremos as configurações e as informações essenciais para o nosso site funcionar corretamente. 
Em cada aplicativo criado, também teremos alguns arquivos que serão gerados automaticamente. Entre eles, um arquivo **`__init__.py`** que também iniciará vazio e indicará que a pasta **loja** é um aplicativo do nosso projeto.
  A pasta **`migrations`** será responsável por gerenciar e registrar as modificações no banco de dados.
O **`admin.py`** será onde você configurará o que será exibido na tela de administração do site, ou seja, o que o usuário que é administrador do site visualizará ao acessá-lo.
No **`apps.py`**, você irá configurar e registrar os aplicativos referentes à aplicação **`nomedoaplicativo`**. Por padrão, o Django já irá criar o app referente à sua aplicação, e costumamos deixar apenas um app por aplicação mesmo.
O arquivo **`tests.py`**, como o próprio nome sugere, serve para que você execute os testes da sua aplicação.
Por fim, temos dois arquivos muito importantes: o **`models.py`** e o **`views.py`**. Esses arquivos são os que você mais utilizará e modificará.
No **`models.py`**, é onde você definirá as informações que serão registradas no seu sistema e no seu banco de dados. O **`views.py`** é onde definirá a lógica por trás do seu site, ou seja, onde você definirá as funções ou classes que serão executadas quando o usuário acessar um link específico do seu site._



## 21/05 🗒️
_Demos continuidade à parte principal do projeto, ainda com o apoio do professor. Estamos na etapa de configuração do sistema, incluindo a definição de quem será o administrador. Nesta aula, o foco foi configurar e preparar o código responsável por auxiliar os usuários na reserva dos quartos. De forma resumida, conseguimos implementar a seleção do quarto desejado pelo cliente, além de exibir se o quarto está reservado ou disponível. Aproveitamos também para definir o preço de cada quarto disponível no sistema._
___
## 28/05 🗒️
_Prosseguimos o projeto, pórem agora nao temos o apoio do professor, porque chegamos na parte que precisamos seguir sem a ajuda do professor, a ideia hoje é:_
- Terminar a parte de adicionar colaborador ✅
- Adicionar quartos no sistema ✅

## 28/05 🗒️
_Neste dia, demos continuidade ao que já havíamos iniciado anteriormente. Adiantamos algumas etapas em casa, o que nos ajudou a ganhar tempo quando chegamos na sala. Isso otimizou nosso trabalho e nos deu mais flexibilidade durante o encontro presencial.
Trabalhamos na funcionalidade de listagem dos quartos, que não conseguimos finalizar durante a aula no Senai, e também concluímos a parte de reservas. Agora estamos bem próximos de finalizar tudo.
Além disso, ajustamos a interface do site e alteramos as cores, deixando o visual mais personalizado e com a nossa identidade_


## 11/06 🗒️
_Hoje nós chegamos com o projeto ja "finalizado" a unica parte pendente é uma parte das reservas com as datas de liberação dos quartos, os que estão disponíveis ou não, acreditamos que ainda hoje antes do fim do dia, assim iremos mostrar e finalizar mais um projeto._


