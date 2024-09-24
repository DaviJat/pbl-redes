# Usando uma imagem base oficial do Python
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para o container
COPY .. /app

# Instalando as dependências necessárias
RUN pip install networkx

# Expondo a porta que o servidor usará
EXPOSE 61582

# Comando para iniciar o servidor
CMD ["python","-u", "servidor.py"]
