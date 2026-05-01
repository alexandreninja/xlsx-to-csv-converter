<h1 align="left">XLSX to CSV Converter</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/Pandas-data%20analysis-blue" />
  <img src="https://img.shields.io/badge/Streamlit-app-red" />
  <img src="https://img.shields.io/badge/Docker-ready-blue" />
  <img src="https://img.shields.io/badge/Status-active-success" />
</p>

Projeto simples em Python para converter arquivos `.xlsx` em `.csv`, agora com interface gráfica via Streamlit.

---

## 🧠 Versão

### 🚀 v1.1.0

**Novidades desta versão:**

- Interface gráfica com Streamlit  
- Upload de arquivos via navegador  
- Pré-visualização dos dados  
- Download do arquivo convertido  
- Histórico de conversões na sessão  
- Reset inteligente da aplicação  

---

## 🎯 Objetivo

Este projeto foi criado como parte da minha transição de Marketing Analytics para Ciência de Dados, com foco em:

- automação de processos  
- manipulação de dados  
- execução local segura (LGPD)  
- construção de aplicações reais  

---

## ⚙️ O que o projeto faz

- Lê arquivos `.xlsx`
- Converte para `.csv`
- Normaliza automaticamente os nomes dos arquivos
- Permite uso via terminal ou interface gráfica
- Processa dados localmente (sem envio externo)

---

## 🧰 Tecnologias usadas

- Python  
- Pandas  
- OpenPyXL  
- Streamlit  
- Docker  
- Docker Compose  

---

## 🖥️ Como rodar o projeto (PASSO A PASSO)

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/alexandreninja/xlsx-to-csv-converter.git
cd xlsx-to-csv-converter
```

---

### 2️⃣ Criar ambiente virtual (recomendado)

```bash
python -m venv venv
```

#### Ativar o ambiente:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como usar

### 🔹 Interface gráfica (RECOMENDADO)

```bash
streamlit run app.py
```

Depois abra no navegador:

http://localhost:8501

👉 Você poderá:

- enviar arquivo `.xlsx`
- visualizar os dados
- baixar o `.csv`

---

### 🔹 Via script (modo tradicional)

```bash
python xlsx_to_csv.py
```

---

### 🔹 Via Docker

```bash
docker compose run --rm converter
```

---

## 🔒 Segurança

Todos os dados são processados localmente.  
Nenhuma informação é enviada para serviços externos.

---

## 📂 Estrutura do projeto

```bash
.
├── assets/               # Imagens e arquivos visuais do projeto
├── xlsx/                 # Arquivos de entrada
├── csv/                  # Arquivos convertidos
├── app.py                # Interface Streamlit
├── xlsx_to_csv.py        # Script principal
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🔮 Próximas melhorias

<ul>
  <li>Upload de múltiplos arquivos</li>
  <li>Escolha de pasta via interface</li>
  <li>Melhor tratamento de erros</li>
  <li>Persistência de histórico</li>
  <li>Deploy em ambiente controlado</li>
</ul>

---
<img src="assets/ninja-logo.png" width="120" align="left"/>

**Alexandre NINJA**  
Marketing Analytics → Ciência de Dados  
*Transformando dados em decisões — sem perder o propósito.*

<br clear="left"/>
