import streamlit as st

st.title("🍔 ConradoGPT - Seu assistente da Cantina")
st.write("Pergunte sobre o cardápio, preços e opções saudáveis!")
# Força o navegador a desativar qualquer corretor ou auto-completar no campo de texto
st.markdown(
    """
    <style>
    input[data-testid="stChatInputTextArea"] {
        autocomplete: off !important;
        autocorrect: off !important;
        autocapitalize: off !important;
        spellcheck: false !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


CARDAPIO = {
    "salgados": "- Esfiha de carne (R$ 6,00)\n- Coxinha assada de frango (R$ 6,50)\n- Pão de queijo (R$ 4,00)",
    "doces": "- Salada de frutas (R$ 5,00)\n- Gelatina (R$ 3,00)\n- Cookie integral (R$ 4,50)",
    "bebidas": "- Suco natural de laranja (R$ 5,00)\n- Água mineral (R$ 3,00)\n- Suco de uva integrado (R$ 5,50)\n- Coca-cola 30 ml (R$ 10,00)"
}



FUNCAO ={
    "A minha função é tornar a cantina técnologica e garantir que você compre com um auxílio"
}
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou o ConradoGPT 🍔. Como posso te ajudar com o cardápio ou preços hoje?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso te ajudar hoje?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    texto_usuario = prompt.lower()
    
    # 1. Saudações
    if any(palavra in texto_usuario for palavra in ["olá", "ola", "oi", "bom dia", "boa tarde"]):
        resposta = "Olá! Tudo bem? 😊 Sou o ConradoGPT. Você gostaria de ver o nosso **cardápio** ou saber o preço de algum item específico?"
        
      
    # 2. Cardápio Completo
    elif any(palavra in texto_usuario for palavra in ["cardapio", "cardápio", "comer", "opções", "opcoes", "menu", "tudo"]):
        resposta = f"Aqui está o nosso cardápio completo de hoje! 😋\n\n**Salgados (Assados):**\n{CARDAPIO['salgados']}\n\n**Doces:**\n{CARDAPIO['doces']}\n\n**Bebidas:**\n{CARDAPIO['bebidas']}"
    
    
    
    elif any(palavra in texto_usuario for palavra in ["funcao", "função"]):
            resposta = f"Minha funÇão e te ajudar a entender o sistema e comprar melhor"
        
    elif any(palavra in texto_usuario for palavra in ["formas de pagamento", "forma", "Forma"]):
        resposta = f"Você pode pagar por Crédito, débito ou dinheiro físico (presencialmente na cantina ou por aqui)"
    
    
    
    
    # 3. Filtros por Categoria (Doces / Sêxtuplos do Corretor / Barato)
    elif any(palavra in texto_usuario for palavra in ["doce", "doces", "sêxtuplos", "sextuplos", "sobremesa"]):
        resposta = f"Essas são as nossas opções de doces saudáveis de hoje: 🍏\n\n{CARDAPIO['doces']}"
        
    elif any(palavra in texto_usuario for palavra in ["salgados", "salgado", "assados"]):
        resposta = f"Esses são os salgados assados disponíveis hoje: 🥐\n\n{CARDAPIO['salgados']}"
        
    elif "barato" in texto_usuario or "econômico" in texto_usuario:
        resposta = "Os nossos produtos mais baratos hoje são a **Água mineral** e a **Gelatina**, ambos por apenas **R$ 3,00**! 💸"

    # 4. Itens Específicos
    elif "coxinha" in texto_usuario:
        resposta = "A nossa Coxinha de frango é assada e super saudável! Custa **R$ 6,50** 🍗."
        
    elif "esfiha" in texto_usuario or "esfira" in texto_usuario:
        resposta = "Temos uma deliciosa esfiha de carne assada por **R$ 6,00** 🍕."
        
    elif any(palavra in texto_usuario for palavra in ["pão de queijo", "pao de queijo", "queijo", "quijo"]):
        resposta = "O pão de queijo quentinho sai por **R$ 4,00** 🧀."
        
    # 5. Proibições e Informações Gerais
   # elif any(palavra in texto_usuario for palavra in ["refrigerante", "coca", "frito", "fritura", "suco"]):
       # resposta = f"Não trabalhamos com fritos ou refrigerantes por regras de saúde da escola! 🍎 Nossos sucos naturais são:\n\n{CARDAPIO['bebidas']}"
        
    elif any(palavra in texto_usuario for palavra in ["saldo", "cartao", "cartão", "pagar", "recarga"]):
        resposta = "Para consultar o saldo do aluno ou fazer recargas, por favor procure a secretaria da escola ou acesse o portal dos pais 💳."
        
    else:
        resposta = "Sou o ConradoGPT, o assistente da cantina! 🍔 Tente perguntar sobre o **cardápio**, sobre os **doces**, o preço da **coxinha** ou qual o produto **mais barato**! ou qualquer dúvida que tiver!!"

    with st.chat_message("assistant"):
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
