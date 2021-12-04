from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import Controllers.AtividadeController as AtividadeController
from models.Atividade import *
import streamlit.components.v1 as components
import pandas as pd
from datetime import date
from models.Atividade import *
from Paginas.Cadastrar import *
from Paginas.Funcoes import *


##########
# Menu e home
st.sidebar.title('Categorias')
# Pagina_Aluno = st.sidebar.selectbox(
# 'Aluno', ['Selecione', 'Cadastro', 'Login'])
Pagina_Atividade = st.sidebar.selectbox(
    'Atividade', ['Selecione', 'Cadastrar Atividade', 'Consultar Atividade', 'Calcular Horas Restantes', 'Excluir Atividade'])

# if Pagina_Aluno == 'Selecione' and Pagina_Atividade == 'Selecione':


if Pagina_Atividade == 'Selecione':
    st.title(
        "Seja Bem-Vindo!\n\n\n Logo ao lado esquerdo estão as opções da calculadora!")

if Pagina_Atividade == 'Cadastrar Atividade':
    Cadastrar_Atividade()

if Pagina_Atividade == 'Consultar Atividade':
    Consultar_Atividade()

if Pagina_Atividade == 'Calcular Horas Restantes':
    Calcular_Atividade()

if Pagina_Atividade == 'Excluir Atividade':
    Deletar_Atividade()
