import streamlit as st
import pandas as pd
import pickle

# Carregando o modelo treinado

with open("modelo_treinado.pkl", "rb") as file:
    modelo = pickle.load(file)

def calcula_consumo(consumo):
    dados = pd.DataFrame({'consumo': [consumo]})
    valor = modelo.predict(dados)[0][0]
    print(f"Valor calculado pelo modelo: {valor}")
    return valor

# Configuração da página
st.set_page_config(
    page_title="Econect",
    page_icon="🍃"
)

# titulo da aplicação

st.title("Previsão de preço com base no consumo")
st.divider()

menu = st.sidebar

consumo = menu.number_input('Digite o consumo em kW:', min_value=0.0, format="%.2f")

# Opções para escolha da fonte de energia

opcoes = ["Solar", "Eólica", "Maremotriz", "Geotérmica", "Hidráulica"]
tipo = menu.selectbox('Selecione o tipo de energia: ', options = opcoes)

# Botão para fazer o cálculo

btn_preco = menu.button("Calcular valor")

if btn_preco:
    if consumo <= 0:
        st.erro("Não é possível fazer a conta para valores menores ou igual a zero", icon="❌")
    else:
        valor = calcula_consumo(consumo)

        fatores = {
            "Solar": 200.25,
            "Eólica": 205.65,
            "Geotérmica": 210.80,
            "Maremotriz": 220.10,
            "Hidráulica": 208.75
        }

        fator_multiplicacao = fatores.get(tipo, 1)
        valor_total = valor * fator_multiplicacao

        st.write(f"O valor da energia de {consumo:.2f} kW com energia {tipo} é de R${valor_total:,.2f}")
        st.success("O valor foi calculado com sucesso", icon="✔️")