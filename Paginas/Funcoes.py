import streamlit as st
import Controllers.AtividadeController as AtividadeController
import streamlit.components.v1 as components
from datetime import date
from models.Atividade import *
from .Cadastrar import *
from datetime import date


def cadastrar_atividade_pesquisa_calcular(opcao_categoria):
    data = date.today()
    input_ch_valida_final = 0
    with st.form(key='cadastrar_atividades_pesquisa', clear_on_submit=True):

        input_opcao_subcategoria = st.selectbox('Subcategorias', [
            'Selecione', '[1]-Participação individual ou em grupo de Projetos de Pesquisa realizados...', '[2]-Participação em projetos de pesquisa (CNPq, CAPES, FAPESP e/ou...'])
        input_ra_titular_atividade = st.text_input(
            label="Insira o seu RA", max_chars=13)
        input_opcao_categoria = opcao_categoria

        input_descricao_atividade = st.text_input(
            label='Insira a descrição da atividade', max_chars=70)

        input_carga_horaria = st.number_input(
            label='Insira a Carga Horaria', step=1, format='%d')
        input_carga_horaria_minima = st.number_input(
            label='Insira a carga horaria minima', step=1, format='%d')
        input_peso_atividade = st.number_input(
            label='Insira o peso da atividade')

        # calculo--
        if input_carga_horaria >= input_carga_horaria_minima:
            carga_horaria_valida = input_carga_horaria*input_peso_atividade
        else:
            carga_horaria_valida = 0
        input_ch_valida_final = carga_horaria_valida

        input_button_submit_pesquisa = st.form_submit_button(
            "Cadastrar Atividade")

    if input_button_submit_pesquisa:
        Atividade_Pesquisa.ra_titular_atividade = input_ra_titular_atividade
        Atividade_Pesquisa.data_atividade = data
        Atividade_Pesquisa.categoria_atividade = input_opcao_categoria
        Atividade_Pesquisa.subcategoria_atividade = input_opcao_subcategoria
        Atividade_Pesquisa.descricao_atividade = input_descricao_atividade
        Atividade_Pesquisa.ch_valida_final = input_ch_valida_final

        AtividadeController.incluir_Atividade_pesquisa(Atividade_Pesquisa)
        st.success(
            'A atividade foi cadastrada com sucesso!!')


# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-
# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-


def cadastrar_atividade_aperfeicoamento_calcular(opcao_categoria):
    data = date.today()
    input_ch_valida_final = 0
    input_pontuacao_maxima = 0
    input_resposta = 0

    with st.form(key='cadastrar_atividade_aperfeicoamento_calcular', clear_on_submit=True):

        input_opcao_subcategoria = st.selectbox('Subcategorias', [
            'Selecione', '[1]-Participação como apresentador de trabalho científico (comunicação oral...', '[2]-Participação como ouvinte em Congressos, Seminários, Simpósios e...', '[3]-Participação como ouvinte em sessões de defesas de Tese de Doutorado...', '[4]-Participação como ouvinte em sessões de defesas de Trabalho de...', '[5]-Participação em eventos culturais complementares, tais como Feiras...', '[6]-Participação em sessões de lançamento de livros e/ou sessões de...', '[7]-Participação em oficinas, palestras e minicursos da área do saber...', '[8]-Participação em cursos de extensão e/ou capacitação realizados...', '[9]-Participação em Comissão Organizadora de eventos científicos...', '[10]-Participação, no âmbito interno, como membro discente eleito para a...', '[11]-Participação em eventos educativos organizados por entidades públicas...', '[12]-Participação em cursos a distância, de instituições de ensino pública ou...', '[13]-Atividades de representação discente, tais como representante de sala...', '[14]-Atividade Social – trabalho voluntário...'])
        input_ra_titular_atividade = st.text_input(
            label="Insira o seu RA", max_chars=13)
        input_opcao_categoria = opcao_categoria

        input_descricao_atividade = st.text_input(
            label='Insira a descrição da atividade', max_chars=70)

        input_carga_horaria = st.number_input(
            label='Insira a Carga Horaria', step=1, format='%d')
        input_carga_horaria_minima = st.number_input(
            label='Insira a carga horaria minima', step=1, format='%d')
        input_peso_atividade = st.number_input(
            label='Insira o peso da atividade')
        input_resposta = st.selectbox(
            'Existe pontuação Máxima?', ['Sim', 'Não'])

        input_pontuacao_maxima = st.number_input(
            label='Insira a pontuação máxima', step=1, format='%d')

        # calculo--# ---------------------------------------------------------------

        if (input_carga_horaria_minima > 0 and input_carga_horaria_minima > input_carga_horaria):
            carga_horaria_valida = input_carga_horaria * \
                ((input_peso_atividade/10)*input_carga_horaria)

        else:
            if input_carga_horaria >= input_carga_horaria_minima:
                carga_horaria_valida = input_carga_horaria*input_peso_atividade
            else:
                carga_horaria_valida = 0
        if input_pontuacao_maxima <= carga_horaria_valida and input_resposta == 'Sim':
            carga_horaria_valida = input_pontuacao_maxima

        # calculo--# ---------------------------------------------------------------

        # ---------------------------------------------------------------------------
        # submit
        input_ch_valida_final = carga_horaria_valida
        input_button_submit_pesquisa = st.form_submit_button(
            "Cadastrar Atividade")
    # atribuindo o conteudo do submit nos atributos e e chamando o insert do banco de dados
    if input_button_submit_pesquisa:
        Atividade_Pesquisa.ra_titular_atividade = input_ra_titular_atividade
        Atividade_Pesquisa.data_atividade = data
        Atividade_Pesquisa.categoria_atividade = input_opcao_categoria
        Atividade_Pesquisa.subcategoria_atividade = input_opcao_subcategoria
        Atividade_Pesquisa.descricao_atividade = input_descricao_atividade
        Atividade_Pesquisa.ch_valida_final = input_ch_valida_final

        AtividadeController.incluir_Atividade_pesquisa(Atividade_Pesquisa)
        st.success(
            'A atividade foi cadastrada com sucesso!!')

# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-
# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-


def cadastrar_atividade_doacao_alimento_calcular(opcao_categoria):
    data = date.today()
    input_ch_valida_final = 0
    with st.form(key='cadastrar_atividade_doacao_alimento_calcular', clear_on_submit=True):

        input_opcao_subcategoria = st.selectbox('Subcategorias', [
            'Selecione', '[1]-Participação em ações sociais com o intuito de doar alimentos, produtos de higiene pessoal...'])
        input_ra_titular_atividade = st.text_input(
            label="Insira o seu RA", max_chars=13)
        input_opcao_categoria = opcao_categoria

        input_descricao_atividade = st.text_input(
            label='Insira a descrição da atividade', max_chars=70)

        input_participacao_doacoes = st.number_input(
            label='Insira a quantidade de participações em doações', step=1, format='%d')

        # input_participacao_doacoes
        # calculo
        carga_horaria_valida = input_participacao_doacoes*5
        if carga_horaria_valida >= 20:
            carga_horaria_valida = 20

        input_ch_valida_final = carga_horaria_valida

        input_button_submit_pesquisa = st.form_submit_button(
            "Cadastrar Atividade")

    if input_button_submit_pesquisa:
        Atividade_Pesquisa.ra_titular_atividade = input_ra_titular_atividade
        Atividade_Pesquisa.data_atividade = data
        Atividade_Pesquisa.categoria_atividade = input_opcao_categoria
        Atividade_Pesquisa.subcategoria_atividade = input_opcao_subcategoria
        Atividade_Pesquisa.descricao_atividade = input_descricao_atividade
        Atividade_Pesquisa.ch_valida_final = input_ch_valida_final

        AtividadeController.incluir_Atividade_pesquisa(Atividade_Pesquisa)
        st.success(
            'A atividade foi cadastrada com sucesso!!')


# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-
# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-


def cadastrar_atividade_docencia_calcular(opcao_categoria):
    data = date.today()
    input_ch_valida_final = 0
    with st.form(key='cadastrar_atividade_docencia_calcular', clear_on_submit=True):

        input_opcao_subcategoria = st.selectbox('Subcategorias', [
            'Selecione', '[1]-Ministrar atividades de monitoria, como bolsista ou voluntário, em...', '[2]-Ministrar atividades de monitoria, como voluntário, em disciplinas do...'])
        input_ra_titular_atividade = st.text_input(
            label="Insira o seu RA", max_chars=13)
        input_opcao_categoria = opcao_categoria

        input_descricao_atividade = st.text_input(
            label='Insira a descrição da atividade', max_chars=70)

        input_quantidade_semestre = st.number_input(
            label='Insira a quantidade de semestres', step=1, format='%d')
        input_peso_atividade = st.number_input(
            label='Insira o peso da atividade')

        # calculo--
        carga_horaria_valida = input_quantidade_semestre*input_peso_atividade
        input_ch_valida_final = carga_horaria_valida

        input_button_submit_pesquisa = st.form_submit_button(
            "Cadastrar Atividade")

    if input_button_submit_pesquisa:
        Atividade_Pesquisa.ra_titular_atividade = input_ra_titular_atividade
        Atividade_Pesquisa.data_atividade = data
        Atividade_Pesquisa.categoria_atividade = input_opcao_categoria
        Atividade_Pesquisa.subcategoria_atividade = input_opcao_subcategoria
        Atividade_Pesquisa.descricao_atividade = input_descricao_atividade
        Atividade_Pesquisa.ch_valida_final = input_ch_valida_final

        AtividadeController.incluir_Atividade_pesquisa(Atividade_Pesquisa)
        st.success(
            'A atividade foi cadastrada com sucesso!!')


# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-
# *-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-**-*-*#*-*-*-**-*-*-*-*-*-**-*-


def cadastrar_atividade_divulgacao_calcular(opcao_categoria):
    data = date.today()
    input_ch_valida_final = 0
    with st.form(key='cadastrar_atividade_divulgacao_calcular', clear_on_submit=True):

        input_opcao_subcategoria = st.selectbox('Subcategorias', [
            'Selecione', '[1]-Publicação de artigo individual ou coletivo em Revista com indexação...', '[2]-Publicação de artigo individual ou coletivo em Jornal impresso com...', '[3]-Publicação de artigo em Revista ou em Jornal impresso com indexação...', '[4]-Publicação de resumo individual ou coletivo em eventos nacionais...', '[5]-Publicação de resumo individual ou coletivo em eventos internacionais...', '[6]-Publicação de trabalho individual ou coletivo em mídia eletrônica, digital...', '[7]-Participação em concursos literários, mostras culturais ou apresentações...', '[8]-Autoria única ou conjunta de trabalhos de pesquisa apresentados em...'])
        input_ra_titular_atividade = st.text_input(
            label="Insira o seu RA", max_chars=13)
        input_opcao_categoria = opcao_categoria

        input_descricao_atividade = st.text_input(
            label='Insira a descrição da atividade', max_chars=70)

        input_quantidade_artigos_resumos = st.number_input(
            label='Insira a quantidade de artigos ou resumos', step=1, format='%d')
        input_peso_atividade = st.number_input(
            label='Insira o peso da atividade')

        # calculo--
        carga_horaria_valida = input_quantidade_artigos_resumos*input_peso_atividade

        input_ch_valida_final = carga_horaria_valida

        input_button_submit_pesquisa = st.form_submit_button(
            "Cadastrar Atividade")

    if input_button_submit_pesquisa:
        Atividade_Pesquisa.ra_titular_atividade = input_ra_titular_atividade
        Atividade_Pesquisa.data_atividade = data
        Atividade_Pesquisa.categoria_atividade = input_opcao_categoria
        Atividade_Pesquisa.subcategoria_atividade = input_opcao_subcategoria
        Atividade_Pesquisa.descricao_atividade = input_descricao_atividade
        Atividade_Pesquisa.ch_valida_final = input_ch_valida_final

        AtividadeController.incluir_Atividade_pesquisa(Atividade_Pesquisa)
        st.success(
            'A atividade foi cadastrada com sucesso!!')
