#!/usr/bin/ python3

__author__ = 'Naamã Costa'
__github__  = '@zNairy | https://github.com/zNairy/'
__repository__ = 'https://github.com/zNairy/CsvReport'

from csv import writer
from database import credentials
from mysql.connector import connect
from mysql.connector.errors import ProgrammingError


def loadQueryFromFile(namefile):
    return open(namefile, 'r').read()

# args: namefile: nome do arquivo de saida | content: resultado da busca feita no banco
def salvarRelatorioCsv(namefile, content):
    with open(f'{namefile}.csv', 'w', newline='') as relatorio: # abrindo arquivo de saída csv
        writer(relatorio).writerows(content) # escrevendo todas as linhas do conteúdo

def main():

    try:
        with connect(**credentials) as database: # criando instância da conexão com o banco
        
            # verificando se a conexão com o banco foi bem sucedida
            if database.is_connected():
                cursor = database.cursor() # criando instância do cursor

                # primeira query -- 10 livros mais caros
                cursor.execute(loadQueryFromFile('dezLivrosMaisCaros.sql'))

                result = cursor.fetchall() # resgatando o conteúdo da busca
                result.insert(0, cursor.column_names) # inserindo o header da consulta no começo do resultado para escrita

                # salvando o resultado em um relatório no formato csv
                salvarRelatorioCsv('relatorio-dezLivrosMaisCaros', result)

                # segunda query -- 5 editoras que mais tem livros
                cursor.execute(loadQueryFromFile('cincoEditorasComMaisLivros.sql'))

                result = cursor.fetchall() # resgatando o conteúdo da busca
                result.insert(0, cursor.column_names) # inserindo o header da consulta no começo do resultado para escrita

                # salvando o resultado em um relatório no formato csv
                salvarRelatorioCsv('relatorio-cincoEditorasComMaisLivros', result)
    except ProgrammingError:
        print('Invalid credentials in .env file')

if __name__ == '__main__':
    main()
