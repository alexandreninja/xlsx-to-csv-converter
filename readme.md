<h1 align="left">XLSX to CSV Converter</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/Pandas-data%20analysis-blue" />
  <img src="https://img.shields.io/badge/Streamlit-app-red" />
  <img src="https://img.shields.io/badge/Docker-ready-blue" />
  <img src="https://img.shields.io/badge/Status-active-success" />
</p>

Conversor de arquivos `.xlsx` para `.csv` com interface gráfica via Streamlit.

---

## 🧠 Versão

### 🚀 v1.1.0

**Novidades desta versão:**

- Interface gráfica com Streamlit  
- Upload de arquivos via navegador  
- Pré-visualização dos dados  
- Download do arquivo convertido  
- Histórico de conversões na sessão  
- Execução via Docker simplificada  

---

## 🚀 Como rodar o projeto (RECOMENDADO)

### 🐳 Via Docker (mais simples)

#### 1️⃣ Instale o Docker Desktop

https://www.docker.com/products/docker-desktop/

#### 2️⃣ Clone o projeto

```bash
git clone https://github.com/alexandreninja/xlsx-to-csv-converter.git
cd xlsx-to-csv-converter
```

#### 3️⃣ Rode o projeto

```bash
docker compose up --build
```

#### 4️⃣ Acesse no navegador

```text
http://localhost:8501
```

💡 Pronto! Você já pode usar o conversor sem instalar Python ou bibliotecas.

---

## 🖥️ O que você pode fazer na interface

- 📤 Enviar arquivos `.xlsx`  
- 👀 Visualizar os dados  
- 📥 Baixar o `.csv` convertido  
- 🕘 Acompanhar histórico da sessão  

---

## 🔒 Segurança

Todos os dados são processados localmente.  
Nenhuma informação é enviada para a internet.

---

## ⚙️ Outras formas de execução (opcional)

### 🔹 Via Python

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

### 🔹 Script direto (modo antigo)

```bash
python xlsx_to_csv.py
```

---

## 📂 Estrutura do projeto

```bash
.
├── assets/               # Imagens e arquivos visuais
├── xlsx/                 # Arquivos de entrada
├── csv/                  # Arquivos convertidos
├── app.py                # Interface Streamlit
├── xlsx_to_csv.py        # Lógica de conversão
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
  <li>Versão executável (.exe)</li>
</ul>

---
<img src="assets/ninja-logo.png" width="120" align="left"/>

**Alexandre NINJA**  
Marketing Analytics → Ciência de Dados  
*Transformando dados em decisões — sem perder o propósito.*

<br clear="left"/>