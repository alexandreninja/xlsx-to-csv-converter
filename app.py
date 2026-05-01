# ================================
# IMPORTAÇÕES
# ================================
import streamlit as st

# Importa a função do "motor" (xlsx_to_csv.py)
from xlsx_to_csv import converter_arquivo_upload


# ================================
# CONFIGURAÇÃO DA PÁGINA
# ================================
st.set_page_config(
    page_title="XLSX to CSV Converter",
    layout="centered"
)


# ================================
# ESTADO DA SESSÃO (MEMÓRIA)
# ================================

# Histórico de conversões
if "historico" not in st.session_state:
    st.session_state.historico = []

# Controle de arquivos já processados (evita duplicação)
if "arquivos_processados" not in st.session_state:
    st.session_state.arquivos_processados = set()

# Controle do uploader (permite resetar o componente)
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# ================================
# INTERFACE (TÍTULO E DESCRIÇÃO)
# ================================
st.title("XLSX to CSV Converter")

st.write("Converta arquivos Excel (.xlsx) para CSV de forma simples e segura.")

st.markdown("---")

st.info("Seus dados são processados localmente. Nenhuma informação é enviada para a internet. 🔒")

st.markdown("---")


# ================================
# UPLOAD DE ARQUIVO
# ================================
st.markdown("### 📤 Envie seu arquivo")

uploaded_file = st.file_uploader(
    "Selecione um arquivo .xlsx para converter:",
    type=["xlsx"],
    key=f"uploader_{st.session_state.uploader_key}"
)

st.caption("Clique no botão acima para selecionar um arquivo `.xlsx`. Tamanho máximo: 200 MB por arquivo.")


# ================================
# PROCESSAMENTO DO ARQUIVO
# ================================
if uploaded_file is not None:

    # Confirmação visual
    st.success(f"Arquivo carregado: {uploaded_file.name}")

    try:
        # Spinner de carregamento (UX)
        with st.spinner("🔄 Convertendo arquivo..."):

            # ================================
            # CHAMADA DO MOTOR (xlsx_to_csv.py)
            # ================================
            df, csv, nome_csv = converter_arquivo_upload(uploaded_file)

        # ================================
        # HISTÓRICO (EVITA DUPLICAÇÃO)
        # ================================
        if uploaded_file.name not in st.session_state.arquivos_processados:

            st.session_state.historico.append({
                "Arquivo original": uploaded_file.name,
                "Arquivo convertido": nome_csv,
                "Linhas": len(df),
                "Status": "Sucesso"
            })

            st.session_state.arquivos_processados.add(uploaded_file.name)

        # ================================
        # FEEDBACK DE SUCESSO
        # ================================
        st.success("✅ Conversão realizada com sucesso!")

        # ================================
        # PRÉ-VISUALIZAÇÃO DOS DADOS
        # ================================
        st.subheader("📊👀 Pré-visualização dos dados")

        st.dataframe(df.head())

        # ================================
        # BOTÃO DE DOWNLOAD
        # ================================
        st.download_button(
            label="📥 Baixar arquivo CSV",
            data=csv,
            file_name=nome_csv,
            mime="text/csv"
        )

    # ================================
    # TRATAMENTO DE ERRO
    # ================================
    except Exception as e:
        st.error("❌ Erro ao processar o arquivo.")
        st.error(f"Detalhes do erro: {str(e)}")


# ================================
# HISTÓRICO DA SESSÃO
# ================================
st.markdown("---")

st.subheader("🕘 Histórico da sessão")

if st.session_state.historico:

    st.dataframe(st.session_state.historico, use_container_width=True)

    # ================================
    # BOTÃO LIMPAR HISTÓRICO + RESET
    # ================================
    if st.button("🧹 Limpar histórico"):

        st.session_state.historico = []
        st.session_state.arquivos_processados = set()

        # Incrementa a chave para resetar o uploader
        st.session_state.uploader_key += 1

        # Recarrega o app
        st.rerun()

else:
    st.info("Nenhuma conversão realizada nesta sessão.")