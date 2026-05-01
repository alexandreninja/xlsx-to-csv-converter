# ================================
# IMPORTAÇÕES
# ================================
import pandas as pd
import os
import re


# ================================
# FUNÇÃO: NORMALIZAR NOME
# ================================
def normalizar_nome(nome_arquivo):
    # Remove extensão
    nome = nome_arquivo.replace(".xlsx", "")

    # Converte para minúsculo
    nome = nome.lower()

    # Substitui caracteres especiais por "-"
    nome = re.sub(r"[^a-z0-9]", "-", nome)

    # Remove hífens duplicados
    nome = re.sub(r"-+", "-", nome)

    # Remove hífens do início e fim
    nome = nome.strip("-")

    return nome


# ================================
# FUNÇÃO: CONVERTER ARQUIVO (STREAMLIT)
# ================================
def converter_arquivo_upload(arquivo_upload):
    # Lê o Excel enviado pelo usuário
    df = pd.read_excel(arquivo_upload)

    # Gera nome do CSV
    nome_csv = arquivo_upload.name.replace(".xlsx", ".csv")

    # Converte para CSV (em memória)
    csv = df.to_csv(index=False).encode("utf-8")

    # Retorna tudo para o Streamlit
    return df, csv, nome_csv


# ================================
# FUNÇÃO: CONVERSÃO EM LOTE (PASTAS)
# ================================
def converter_xlsx_para_csv(pasta_xlsx, pasta_csv):
    # Cria pasta de saída se não existir
    os.makedirs(pasta_csv, exist_ok=True)

    # Percorre arquivos
    for arquivo in os.listdir(pasta_xlsx):
        if arquivo.endswith(".xlsx"):
            caminho_xlsx = os.path.join(pasta_xlsx, arquivo)

            # Lê Excel
            df = pd.read_excel(caminho_xlsx)

            # Normaliza nome
            nome_normalizado = normalizar_nome(arquivo)

            # Caminho final
            caminho_csv = os.path.join(pasta_csv, f"{nome_normalizado}.csv")

            # Salva CSV
            df.to_csv(caminho_csv, index=False, encoding="utf-8")

            print(f"Convertido: {arquivo} -> {nome_normalizado}.csv")


# ================================
# EXECUÇÃO DIRETA (CLI)
# ================================
# Só roda quando executado diretamente (NÃO quando importado)
if __name__ == "__main__":
    pasta_xlsx = "xlsx"
    pasta_csv = "csv"
    converter_xlsx_para_csv(pasta_xlsx, pasta_csv)