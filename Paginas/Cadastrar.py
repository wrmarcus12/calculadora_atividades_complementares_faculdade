import streamlit as st
import Controllers.AtividadeController as AtividadeController
from datetime import date
from models.Atividade import *
from Paginas.Funcoes import *
from models.Atividade import *
import streamlit.components.v1 as components
import pandas as pd
import time


def Cadastrar_Atividade():
    st.title("Escolha a Categoria da Atividade")
    opcao_categoria = st.selectbox('Categorias', ['Selecione', 'Atividades de Pesquisa', 'Atividades de Aperfeiçoamento e Enriquecimento Cultural',
                                                  'Atividades de Doação de Alimentos', 'Atividades de Iniciação á Docência', 'Atividades de Divulgação Científica e Publicações'])

    if opcao_categoria == 'Atividades de Pesquisa':
        cadastrar_atividade_pesquisa_calcular(opcao_categoria)
    elif opcao_categoria == 'Atividades de Aperfeiçoamento e Enriquecimento Cultural':
        cadastrar_atividade_aperfeicoamento_calcular(opcao_categoria)
    elif opcao_categoria == 'Atividades de Doação de Alimentos':
        cadastrar_atividade_doacao_alimento_calcular(opcao_categoria)
    elif opcao_categoria == 'Atividades de Iniciação á Docência':
        cadastrar_atividade_docencia_calcular(opcao_categoria)
    elif opcao_categoria == 'Atividades de Divulgação Científica e Publicações':
        cadastrar_atividade_divulgacao_calcular(opcao_categoria)


def Consultar_Atividade():
    soma_atual = 0
    valor_atribuido = 80
    st.title("Para continuar, digite o seu RA")
    second_input_ra_titular_atividade = st.text_input(
        label="Insira o número", max_chars=13)
    botao_pesquisar = st.button(label='Pesquisar', key=None, help=None,
                                on_click=None, args=None, kwargs=None)
    st.write('\n\n')
    if botao_pesquisar:
        contador = 0
        lista = []
        for item in AtividadeController.Consultar_Atividade_pesquisa():
            if second_input_ra_titular_atividade == item.ra_titular_atividade:
                contador += 1
                lista.append([item.ra_titular_atividade, item.data_atividade,
                              item.categoria_atividade, item.subcategoria_atividade, round(item.ch_valida_final)])
                soma_atual += round(item.ch_valida_final)

        dff = pd.DataFrame(
            lista,
            columns=['Ra', 'Data', 'Categoria',
                     'Subcategoria', 'Carga Horaria Valida']
        )
        st.write(
            '\n\nNeste número de Registro foram encontrados {} resultado(s).     \n\n\n\n\n'.format(contador))
        st.table(dff)
        st.write('\n')


def Calcular_Atividade():

    # ------------------------------------------------------------------------------------------------------------------------------
    #
    st.subheader(
        "Para calcular o seu progresso digite o seu RA e a carga horária total de AACC do seu curso")
    terceiro_input_ra_titular_atividade = st.text_input(
        label="Insira o número do Ra", max_chars=13)
    input_carga_total_curso = st.number_input(
        label='Insira a Carga Horária Total do Curso', step=1, format='%d')
    botao_pesquisar_buscar = st.button(label='Buscar', key=None, help=None,
                                       on_click=None, args=None, kwargs=None)
    st.write('\n\n')

    soma_atual = 0

    st.write('\n\n')
    if botao_pesquisar_buscar:
        contador = 0
        lista = []
        for item in AtividadeController.Consultar_Atividade_pesquisa():
            if terceiro_input_ra_titular_atividade == item.ra_titular_atividade:
                contador += 1
                lista.append([item.ra_titular_atividade, item.data_atividade,
                              item.categoria_atividade, item.subcategoria_atividade, round(item.ch_valida_final)])
                soma_atual += round(item.ch_valida_final)

        percentual = (soma_atual/input_carga_total_curso)*100
        st.subheader('Seu progresso atual é de:  \t{}%'.format(
            round(percentual, 2)))
        minha_barra = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            minha_barra.progress(i+1)
            if i >= percentual:
                break

        somax = input_carga_total_curso-soma_atual

        if somax <= 0:
            st.write('Você possui um total de {} hora(s). Você já completou sua carga horária! Parabéns!'.format(
                soma_atual))
        else:
            st.write('Você possui um total de {} hora(s). Restam {} hora(s) para concluir sua carga horária total.'.format(
                soma_atual, somax))


def Deletar_Atividade():
    st.title('Digite o número do RA')
    quarto_input_ra = st.text_input(
        label="Insira o número", max_chars=13)

    botao_pesquisar_buscar_delete = st.button(label='Buscar', key=None, help=None,
                                              on_click=None, args=None, kwargs=None)
    st.write('\n\n')
    if botao_pesquisar_buscar_delete:
        contador = 0
        lista = []
        for item in AtividadeController.Consultar_Atividade_pesquisa():
            if quarto_input_ra == item.ra_titular_atividade:
                soma_atual = 0
                contador += 1
                lista.append([item.ra_titular_atividade, item.data_atividade,
                              item.categoria_atividade, item.subcategoria_atividade, round(item.ch_valida_final)])
                soma_atual += round(item.ch_valida_final)

        dff = pd.DataFrame(
            lista,
            columns=['Ra', 'Data', 'Categoria',
                     'Subcategoria', 'Carga Horaria Valida']
        )

        st.table(dff)
        st.write('\n')

    st.subheader('Deseja excluir todas as atividades desse registro?')
    botao_confirmacao_delete = st.button(label='Sim, Deletar', key=None, help=None,
                                         on_click=None, args=None, kwargs=None)
    if botao_confirmacao_delete:
        Ra_value = quarto_input_ra
        AtividadeController.Deletar_Atividade_pesquisa(Ra_value)
        st.success('As atividades foram deletadas! Atualize a página')
