# Usando uma imagem base oficial do Python
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para o container
COPY .. /app

# Comando para iniciar o servidor
CMD ["python", "simulador_cliente.py"]
