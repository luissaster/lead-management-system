# 1. Imagem base: Um Linux enxuto com Python 3.9 já instalado
FROM python:3.9-slim

# 2. Define variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 4. Copia o arquivo de dependências para o contêiner
COPY requirements.txt /app/

# 5. Instala as dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copia o código da sua aplicação para dentro do contêiner
# (Será feito após criarmos o projeto Django)
COPY ./app /app