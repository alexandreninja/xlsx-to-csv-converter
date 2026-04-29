FROM python:3.11-slim

WORKDIR /app

# Copia o requirements.txt para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte
COPY . . 

# Define o comando padrão
CMD ["python", "xlsx_to_csv.py"]