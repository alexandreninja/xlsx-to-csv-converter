import pandas as pd
import os
import re

def normalizer_nome(nome_arquivo):
    # Converte nome para lowercase e remove caracteres especiais
    # Remove extensão
    nome = nome_arquivo.replace('.xlsx', '')
    # Converte para lowercase
    nome = nome.lower()
    # Subistitui espacos e caracteres especiais para hífen
    nome = re.sub(r'[^a-z0-9]', '-', nome)
    # Remove hífens duplicados
    nome = re.sub(r'-+', '-', nome)
    # Remove hífens no início e no fim
    nome = nome.strip('-')
    return nome

def converter_xlsx_para_csv(pasta_xslx, pasta_csv):
    # Cria pasta de saída se não existir
    os.makedirs(pasta_csv, exist_ok=True)

    # Lista todos os arquivos xlsx na pasta
    for arquivo in os.listdir(pasta_xslx):
        if arquivo.endswith('.xlsx'):
            caminho_xlsx = os.path.join(pasta_xslx, arquivo)

            # Lê o arquivo Excel
            df = pd.read_excel(caminho_xlsx)

            # Normaliza o nome do arquiv
            nome_normalizado = normalizer_nome(arquivo)
            caminho_csv = os.path.join(pasta_csv, f'{nome_normalizado}.csv' )

            # Salva como CSV
            df.to_csv(caminho_csv, index=False, encoding='utf-8')
            print(f'Convertido: {arquivo} -> {nome_normalizado}.csv')

# Executa a conversão
pasta_xslx = 'xlsx'
pasta_csv = 'csv'
converter_xlsx_para_csv(pasta_xslx, pasta_csv)            
