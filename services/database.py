import pyodbc


# Preencher os campos abaixo com os dados do seu banco de dados, e alterar o nome das tabelas no resto do programa.


server = ''
database = ''
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
