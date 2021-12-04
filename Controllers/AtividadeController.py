from typing import List
import services.database as db
from models.Atividade import *
import pyodbc
from Paginas import *


def incluir_Atividade_pesquisa(Atividade_Pesquisa):
    count = db.cursor.execute("""
  INSERT INTO ATIVIDADES_PESQUISA_CALCULADORA (RA, DATA, CATEGORIA, SUBCATEGORIA, DESCRICAO, CARGA_HORARIA_VALIDA)
  VALUES (?,?,?,?,?,?)""",
                              Atividade_Pesquisa.ra_titular_atividade, Atividade_Pesquisa.data_atividade, Atividade_Pesquisa.categoria_atividade, Atividade_Pesquisa.subcategoria_atividade, Atividade_Pesquisa.descricao_atividade, Atividade_Pesquisa.ch_valida_final).rowcount
    db.cnxn.commit()


def Consultar_Atividade_pesquisa():
    db.cursor.execute("SELECT * FROM ATIVIDADES_PESQUISA_CALCULADORA")
    costumerlist = []

    for row in db.cursor.fetchall():
        costumerlist.append(
            Atividade_Pesquisa(row[0], row[1], row[2], row[3], row[4], row[5]))
    return costumerlist


def Deletar_Atividade_pesquisa(Ra_value):

    delete_query = '''DELETE FROM ATIVIDADES_PESQUISA_CALCULADORA WHERE RA= '{}' '''.format(
        Ra_value)
    db.cursor.execute(delete_query)
    db.cnxn.commit()
