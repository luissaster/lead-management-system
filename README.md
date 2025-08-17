# Sistema de Leads

Aplicação web para registro de leads, construída com Django e integrada a um workflow de automação no n8n. Toda a infraestrutura é containerizada com Docker e orquestrada com Docker Compose.

## Pré-requisitos

Antes de começar, certifique-se de ter o Docker instalado em sua máquina:
* [Docker](https://www.docker.com/get-started/)

## Executando o projeto

Siga os passos abaixo para rodar o ambiente localmente.

### 1. Clonar o repositório
```bash
git clone https://github.com/luissaster/sistema-de-leads.git
cd sistema-de-leads
```

### 2. Configurar as variáveis de ambiente

O projeto utiliza um ```.env``` para lidar com as configurações. Crie uma cópia do arquivo de exemplo:

```bash
cp .env.example .env
```
Abra o arquivo ```.env``` e preencha as variáveis.

⚠️ Atenção: a variável ```N8N_WEBHOOK_URL``` só pode ser definida após o n8n estar rodando.

Exemplo inicial:

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

# Variável do n8n (defina após o passo 3)
N8N_WEBHOOK_URL=http://challenge_n8n:5678/webhook/seu-id-unico # Altere para sua URL
```

### 3. Subir os serviços

Com as variáveis de ambiente configuradas, inicie todos os serviços com o Docker Compose:

```bash
docker-compose up -d --build
```

Este comando irá construir a imagem da aplicação Django, baixar as imagens do Postgres e n8n, e iniciar os três serviços em segundo plano.

### 4. Configurar o webhook do n8n

* Acesse o n8n em: http://localhost:5678.
* Crie (ou importe) o workflow do arquivo ```workflow.json```.
* Copie a URL gerada no nó de webhook.
* Edite o arquivo ```.env``` e substitua o valor da variável:

```env
N8N_WEBHOOK_URL=http://challenge_n8n:5678/webhook/seu-id-unico
```

* Reinicie os serviços para aplicar as mudanças:

```bash
docker-compose up -d
```

## Acesso aos serviços

Após a conclusão dos passos acima, os serviços estarão disponíveis nos seguintes endereços:

* Aplicação Django: http://localhost:8000
* Interface do n8n: http://localhost:5678
