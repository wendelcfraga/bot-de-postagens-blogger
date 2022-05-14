# bot-de-postagens-blogger
Um robô simples que faz postagens na plataforma blogger utilizando WebScraping e a API Blogger v.3 do Google.


## 🚀 Começando

Uma ferramenta que depois de buscar por conteúdo na internet elabora uma postagem e envia para o blogger.

Consulte o **Autor** caso tenha alguma dúvida.

### 📋 Pré-requisitos

> Python3


### 🔧 Instalação e Configuração

Primeiro clone o repositório e instale as dependências digitando o seguinte comando:

> pip install -r requeriments.txt

* edite o script de acordo com a sua necessidade;
* coloque suas credenciais do google no arquivo > "client_secrets.json";
* coloque sua api do wordtracker no arquivo ` "keys.json" `;
* coloque o id do seu blog no espaço indicado no arquivo ` "keys.json" `; 
* coloque sua chave de api e id do Google Custom Search no arquivo ` "keys.json" `;
* por fim digite o comando:

> python blogger.py 


## 📦 Desenvolvimento

* Autor: **Wendel Fraga** - *Trabalho Completo* - [WendelFraga](https://github.com/wendelfraga)
* Use essa POC como bem entender.

## 🛠️ Construído com


* [python-oauth2](https://python-oauth2.readthedocs.io/en/latest/) - Biblioteca para autenticação da conta Google.
* [wikipedia](https://wikipedia.readthedocs.io/en/latest/) - Biblioteca que facilita o recolhimento de informações da Wikipédia.
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Usada para realizar o scraping.
* [GoogleCloudPlatform](https://console.cloud.google.com/) - APIS do Google.


