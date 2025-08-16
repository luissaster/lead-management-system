# Sistema de Leads

Aplicação web para registro de leads, construída com Django e integrada a um workflow de automação no n8n. Toda a infraestrutura é containerizada com Docker e orquestrada com Docker Compose.

## Pré-requisitos

Antes de começar, certifique-se de ter o Docker instalado em sua máquina:
* [Docker](https://www.docker.com/get-started/)

## Executando o projeto

Siga os passos abaixo rodar o ambiente localmente.

### 1. Clonar o repositório
```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Configurar as Variáveis de Ambiente
O projeto utiliza um ```.env``` para lidar com as configurações. Crie uma cópia do arquivo de exemplo:
```
cp .env.example .env
```
Agora, abra o arquivo ```.env``` e preencha as variáveis. Um exemplo de configuração para o ambiente local é:
```
# Variáveis do Django
SECRET_KEY='adicione-uma-chave-aleatoria-aqui'
DEBUG=1

# Variáveis do Banco de Dados
DB_NAME=challenge_db
DB_USER=challenge_user
DB_PASS=challenge_pass
DB_HOST=challenge_db
DB_PORT=5432

# Variável do n8n (será gerada pelo seu n8n local)
N8N_WEBHOOK_URL=http://challenge_n8n:5678/webhook/seu-id-unico
```
Importante: A ```N8N_WEBHOOK_URL``` deve ser obtida a partir do seu nó de Webhook no n8n após iniciar o ambiente.

### 3. Subir os serviços
Com as variáveis de ambiente configuradas, inicie todos os serviços com o Docker Compose:
```
docker-compose up -d --build
```
Este comando irá construir a imagem da aplicação Django, baixar as imagens do Postgres e n8n, e iniciar os três serviços em segundo plano.

### 4. Aplicar as migrações da Base de Dados
Após os servições estarem rodando, execute as migrações do Django para criar as tabelas na base de dados:
```
docker-compose exec challenge_web python manage.py migrate
```

## Acesso aos Serviços
Após a conclusão dos passos acima, os serviços estarão disponíveis nos seguintes endereços:
* Aplicação Django: http://localhost:8000
* Interface do n8n: http://localhost:5678

## Workflow do n8n
O arquivo ```workflow.json``` incluído neste repositório pode ser importado diretamente para a sua instância do n8n para recriar o fluxo de trabalho.