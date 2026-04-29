
<h1 align="left">XLSX to CSV Converter</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/Pandas-data%20analysis-blue" />
  <img src="https://img.shields.io/badge/Docker-ready-blue" />
  <img src="https://img.shields.io/badge/Status-active-success" />
</p>

Projeto simples em Python para converter arquivos `.xlsx` em `.csv`, usando Pandas e Docker.

## Objetivo

Este projeto foi criado como parte da minha transição de Marketing Analytics para Ciência de Dados, com foco em automação de processos, manipulação de dados e uso de containers com Docker.

## O que o projeto faz

- Lê arquivos `.xlsx` dentro da pasta `xlsx`
- Converte cada arquivo para `.csv`
- Normaliza o nome dos arquivos
- Salva os arquivos convertidos na pasta `csv`

## Tecnologias usadas

- Python
- Pandas
- OpenPyXL
- Docker
- Docker Compose

## Como rodar com Docker (via Terminal)

```bash
docker compose run --rm converter
```

## Como rodar sem Docker (via Terminal)

```bash
pip install -r requirements.txt
python xlsx_to_csv.py
```

## Versão

1.0.0

## Próximas melhorias

- Permitir escolher a pasta de entrada e saída via terminal
- Criar interface com Streamlit
- Tratar erros de arquivos corrompidos
- Adicionar testes automatizados

## Estrutura do projeto

```bash
.
├── assets/               # Imagens e arquivos visuais do projeto
├── xlsx/                 # Arquivos de entrada
├── csv/                  # Arquivos convertidos
├── xlsx_to_csv.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Autor

<table>
  <tr>
    <td>
      <img src="assets/ninja-logo.png" width="120"/>
    </td>
    <td>
      <strong>Alexandre NINJA</strong><br/>
      Marketing Analytics → Ciência de Dados<br/>
      <em>Transformando dados em decisões — sem perder o propósito.</em>
    </td>
  </tr>
</table>