# Minha API COMPONETE_A

Este projeto foi pensado em atender a demanda de uma *Oficina_de_Peças* **VS Veiculos**, onde se realiza concerto e manutenção de veículos,
Componente_A(API principal) recebe dados de veículo do Componente_B(API externa) e peças do Componente_C(API externa).

```
    A oficina permite atender tanto CPF quanto CNPJ, o CPF se refere aos veículos que surgem de maneira aleatória, sendo possível seu cadastro,
    quanto ao CNPJ, os veículos são cadastrados atravéz de uma API externa com dados dos veículos fornecido pela Empresa. Nesse projeto a Empresa
    (API externa), é uma locadora de veículos.
```
Logo abaixo informa como executar a API.

---
## Como executar 


Após efetuar o download do repositório e com o VSCode aberto, abra a pasta Gerenciamento peças oficina, clicando em Arquivo/Abrir Pasta.
Em seguida clique com o botao direio do mouse em backend e com o esquerdo Abrir no Terminal Integrado.

> Não é obrigatório mas será recomendado usar o virtualenv, uma vez que o projeto foi elaborado com essa ferramenta.
 [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Digite o comando abaixo no terminal para instalar o virtualenv
```
python3 -m venv env
```

Com o env instalado agora iremos ativá-lo.
```
./env/Scripts/activate
```

agora iremos instalar todas as libs/bibliotecas python listadas no `requirements.txt` instaladas.
```
(env)$ pip install -r requirements.txt
```
>*Após instalar as libs é recomendado que faça uma atualização do comando* `pip`
>>python.exe -m pip install --upgrade pip

>*Instalação do Pandas para uso de recursos em forma de tabela no terminal*
>>pip3 install pandas

>*Instalação do requests*
>>pip3 install requests

Antes de iniciar o Docker é recomendável que execute o flask para criar o arquivo sqlite com as tabelas.
```
    flask run --host 0.0.0.0 --port 5000
```
Com o arquivo do banco criado, saia do flask com o comando abaixo.
```
    CTRL + C
```

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

>*Você pode instalar o docker para VSCode via terminal com o seguinte comando*
>>pip3 install docker

Vá até o diretório que contém o Dockerfile e o requirements.txt no terminal.
    Antes de criar a imagem é necessário criar uma rede para que haja comunicação entre conteiners;
        >>criar rede com o nome "oficina"
            ```
            >>>$ docker network create --driver=bridge oficina
            ```

>**Componente_A**;
>>Execute **como administrador** o seguinte comando para construir a imagem Docker da Componente_A(API principal):

```
$ docker build -t rest-a .
```

Para executar o container basta executar, **como administrador**, expecificando o nome e a rede.

```
$ docker run -d -p 5000:5000 --name peca-veiculo --network oficina -v /c/P/pucrio-mvp-sprint2-principaA-backend/database:/app/database rest-a
>>>obs: o comando anterior se refere ao mapeamento com o docker da pasta database que esta na maquina local(area de trabalho), para que a imagem que esta no docker com o banco db.sqlite3 consiga atualizar o mesmo banco na maquina local.
```
---
### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).

---
### *Como usar*

>OBS
Logo após a execução da API, uma página com a documentação será aberta em Swagger, Redoc ou RapiDoc, nesse exemplo falaremos da Swagger que servirá para a restante, pois o propósito delas são o mesmo, outro fato é a respeito das rotas, foi implementado 12 rotas, porém como requisito do MVP com apenas 7 rotas, onde 5 rotas são de joias (POST/veiculo, POST/update_veiculo, GET/veiculos, GET/veiculosapi, DELETE/veiculo) e 2 rotas de peças (GET/pecas, GET/pecasapi). Get/veiculosapi acessa dados da API externa(Empresa) e GET/pecasapi acessa dados da API externa(Pecas).
---

#### **GET/veiculosapi**

Com o Swagger aberto iremos a procura da rota GET/veiculosapi para consumir dados da API externa com dados de veiculos.
```
Clique em "Try it out", em seguida, clique em execute para buscar dados dos vjoia  como(nome_joia, modelo).
```

>Obs: *Os dados serão salvos no banco* com essa menssagem de confirmação via terminal e swagger.

>Cod:200 - Não há veículos cadastrados, retornará uma [].
>Cod:200 - veiculos encontrados.

---

#### **GET/pecasapi**

```
Clique em "Try it out", em seguida, clique em execute para buscar dados das pedra como(nome_peca, modelo_peca e cod_peca).
```

>Obs: *Os dados serão salvos no banco* com essa menssagem de confirmação via terminal e swagger.

>Cod:200 - Não há peças cadastrados, retornará uma [].
>Cod:200 - veiculos encontrados.

---







