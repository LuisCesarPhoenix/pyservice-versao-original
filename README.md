Observação: Para melhor visualização, visualize em tela cheia

Documentação do pyService

Visão Geral
O pyService é um microsserviço que processa arquivos recebidos da API via RabbitMQ, realizando higienização, enriquecimento de 
dados, geração de relatórios e enviando os arquivos tratados de volta para o OwnCloud.

Fluxo de funcionamento:
a)Recebe mensagens do RabbitMQ para saber quais arquivos processar.
b)Baixa os arquivos do OwnCloud (pasta work/).
c)Higieniza e enriquece os dados, consultando o MongoDB.
d)Gera relatórios e dashboards (CSV/XLSX e PDF).
e)Envia os arquivos processados para o OwnCloud (pasta finalizado/).

Link do roadmap: https://roadmap.sh/r/pymicroservice 

1. Estrutura do Projeto
Diretórios e arquivos principais:

pyService/
├── .dockerignore
├── .env                            # Arquivo de variáveis de ambiente
├── .env                            # Arquivo exemplo de variáveis de ambiente
├── .gitignore
├── anotacoes_pyservice
├── docker-compose.yml              # Arquivo de configuração do Docker Compose
├── dockerfile                      # Dockerfile para containerização
├── main.py                         # Arquivo principal do serviço
├── README.md                       # Documentação do projeto
├── requirements.txt                # Dependências do Python
├── arquivos-para-consulta/ 
├── src/
│   ├── config/
│   │   ├── rabbitmq_config.py      # Configuração da conexão com RabbitMQ
│   │   ├── settings.py             # Configuração das variáveis de ambiente
│   ├── controllers/
│   │   ├── rabbitmq_controller.py  # Processamento de mensagens da fila
│   ├── models/
│   │   ├── data_schema.py          # Estrutura dos dados para enriquecimento
│   ├── routes/
│   ├── services/
│   │   ├── file_service.py         # Lógica de higienização e enriquecimento de dados
│   │   ├── rabbitmq_consumer.py    # Consumidor do RabbitMQ que escuta a fila
│   │   ├── report_service.py       # Geração de relatórios PDF e dashboards
│   ├── tests/
│   │   ├── send_test_message.py
│   ├── utils/
│   │   ├── rabbitmq_utils.py             # Envio e recebimento de mensagens do RabbitMQ
│   │   ├── owncloud_utils.py             # Conexão e manipulação de arquivos no OwnCloud
│   │   ├── mongo_utils.py                # Conexão e consultas ao MongoDB
├── storage/                        # Diretório para armazenar arquivos temporários e processados
│   ├── work/                       # Arquivos aguardando processamento
│   ├── finalizado/                 # Arquivos processados
├──

2. Como Tudo se Conecta?

a)A API recebe uma requisição POST /process com o nome do arquivo.
b)O processFile envia a solicitação para o RabbitMQ.
c)O pyService recebe a mensagem do RabbitMQ.
d)O pyService baixa o arquivo do OwnCloud, higieniza, enriquece e move para finalizado/.
e)O RabbitMQ confirma que o arquivo foi processado

3. Dependências do pyService

# Dependências principais
pika==1.3.2           # Conexão com RabbitMQ
pandas==2.1.4         # Manipulação e análise de dados
pymongo==4.5.0        # Conexão com MongoDB
matplotlib==3.8.0     # Geração de gráficos para relatórios
requests==2.31.0      # Requisições HTTP (se necessário)
owncloud==0.6         # Integração com OwnCloud
openpyxl==3.1.2       # Manipulação de arquivos Excel
reportlab==4.0.4      # Geração de PDFs

# Apenas necessário se estiver usando Flask como API
flask==3.0.0
flask-cors==4.0.0
OBS: Se não for usar uma API HTTP no pyService, remova flask e flask-cors.
O pyService está rodando via RabbitMQ, então Flask e Flask-Cors só é necessário se for usada uma API HTTP.

4. Instalando e Executando o pyService

4.1 Rodando localmente
a)Instale as dependências na pasta do projeto: 
/mnt/c/users/cesar/pyService$ pip install -r requirements.txt
b)Inicie o consumidor do RabbitMQ: 
python src/routes/rabbitmq_consumer.py

Agora, sempre que a API enviar um arquivo para o RabbitMQ, o pyService irá:
Baixar o arquivo do OwnCloud
Higienizar os dados e enriquecer com o MongoDB
Gerar relatórios e gráficos
Enviar o arquivo processado de volta para o OwnCloud

4.2 Rodando no Servidor
a)Atualize os pacotes e instale o Python: 
sudo apt update && sudo apt install -y python3 python3-pip
b)Instale as dependências manualmente: 
pip install pandas flask flask-cors pymongo pika openpyxl reportlab

5. Configuração do Docker

5.1 docker-compose.yml
version: "3.8"

services:
  pyservice:
    build: .
    container_name: pyservice
    env_file: .env
    depends_on:
      redis:
        condition: service_healthy  # Espera até que o Redis esteja pronto
    restart: always
    networks:
      - pyservice_default
    volumes:
      - pyservice_data:/app/data  # Volume persistente para dados do pyservice
      - .:/app  # <<<<<< ISSO MONTA SEU CÓDIGO LOCAL TODO DENTRO DO CONTAINER

  redis:
    image: "redis:latest"
    container_name: redis
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      retries: 5
      timeout: 3s
    networks:
      - pyservice_default

volumes:
  pyservice_data:
    # Define um volume chamado pyservice_data, usado para armazenar dados persistentes do pyservice.

networks:
  pyservice_default:
    external: true
    # Usa a rede externa pyservice_default para permitir a comunicação com RabbitMQ, MongoDB, etc.

5.2 Criando e Subindo os Containers
a)Execute:
docker network create pyservice_default  # Cria a rede necessária
docker-compose up -d                     # Sobe os containers em segundo plano

b)Para verificar os logs:
docker logs -f pyservice

6. Funções e Responsabilidades

a)Arquivos de Configuração e Infraestrutura:
docker-compose.yml → Configuração dos serviços no Docker (RabbitMQ, MongoDB, OwnCloud e pyService).
Dockerfile → Define a imagem do container para o pyService.
requirements.txt → Lista de dependências do Python.
.env → Variáveis de ambiente para configuração.
main.py → Arquivo principal que inicializa o serviço.

b)Configuração e Conexões:
src/config/settings.py → Configuração das variáveis de ambiente.
src/config/rabbitmq.py → Configuração da conexão com RabbitMQ (antes rabbitmqConfig.py).

c)Mensagens e Processamento no RabbitMQ:
src/utils/rabbitmq.py → Envio e recebimento de mensagens no RabbitMQ (integrou rabbitmqRoutes.py).

d)Serviços e Processamento de Arquivos:
src/services/rabbitmq_consumer.py → Consumidor do RabbitMQ que escuta a fila e encaminha mensagens para o processamento (antes 
estava em routes/).
src/controllers/rabbitmq_controller.py → Processa a mensagem recebida da fila e aciona os serviços de tratamento de arquivos.
src/services/file_service.py → Lógica de higienização e enriquecimento de dados.
src/services/report_service.py → Geração de relatórios PDF e dashboards.

e)Conexões com Outros Serviços:
src/utils/owncloud.py → Conexão e manipulação de arquivos no OwnCloud.
src/utils/mongo.py → Conexão e consultas ao MongoDB.

f)Modelos de Dados:
src/models/data_schema.py → Estrutura dos dados para enriquecimento.

7. Explicação dos Processos

7.1 Consumo de Mensagens do RabbitMQ
Objetivo: O pyService escuta mensagens do RabbitMQ para processar arquivos.
Arquivo: rabbitmq_consumer.py

import pika
import json
from services.file_service import process_file

def callback(ch, method, properties, body):
    message = json.loads(body)
    file_name = message.get("file_name")
    process_file(file_name)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="pyservice_queue")

channel.basic_consume(queue="pyservice_queue", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

Conclusão
O pyService automatiza a higienização e enriquecimento de dados.
Ele integra RabbitMQ, MongoDB e OwnCloud para processamento eficiente.
A API apenas encaminha os arquivos e o pyService faz o trabalho pesado.
