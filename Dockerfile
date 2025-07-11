# Use uma versão de Python estável e bem suportada pelas bibliotecas de dados
FROM python:3.11-slim

# Atualiza pacotes e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app/src

# Copia o requirements (se existir)
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]