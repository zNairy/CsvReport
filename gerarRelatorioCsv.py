#!/usr/bin/ python3

__autor__ = 'Naamã Costa'
__github__  = 'https://github.com/zNairy/'

from csv import writer
from database import credentials
from mysql.connector import connect


# args: namefile: nome do arquivo de saida | content: resultado da busca feita no banco
def salvarRelatorioCsv(namefile, content):
    with open(f'{namefile}.csv', 'w', newline='') as relatorio: # abrindo arquivo de saída csv
        writer(relatorio).writerows(content) # escrevendo todas as linhas do conteúdo

def main():

    with connect(**credentials) as database: # criando instância da conexão com o banco
        
        # verificando se a conexão com o banco foi bem sucedida
        if database.is_connected():
            cursor = database.cursor() # criando instância do cursor

            # primeira query -- 10 livros mais caros
            cursor.execute("""
                select Cod as 'Código Livro', Titulo,
                AUTOR.CodAutor as 'Código Autor', AUTOR.Nome as 'Nome Autor', Valor as 'Preço Livro',
                EDITORA.CodEditora as 'Código Editora', EDITORA.Nome as 'Nome Editora' from LIVRO
                join AUTOR on AUTOR.CodAutor = LIVRO.Autor
                join EDITORA on EDITORA.CodEditora = LIVRO.Editora
                order by LIVRO.Valor desc
                limit 10;
            """)

            result = cursor.fetchall() # resgatando o conteúdo da busca
            result.insert(0, cursor.column_names) # inserindo o header da consulta no começo do resultado para escrita

            # salvando o resultado em um relatório no formato csv
            salvarRelatorioCsv('relatorio-dezLivrosMaisCaros', result)

            # segunda query -- 5 editoras que mais tem livros
            cursor.execute("""
                select EDITORA.CodEditora as 'Código Editora', EDITORA.Nome as 'Nome Editora',
                count(LIVRO.Editora) as 'Livros Publicados' from LIVRO
                right join EDITORA on EDITORA.CodEditora = LIVRO.Editora
                group by EDITORA.CodEditora
                order by count(LIVRO.Editora) desc
                limit 5;
            """)

            result = cursor.fetchall() # resgatando o conteúdo da busca
            result.insert(0, cursor.column_names) # inserindo o header da consulta no começo do resultado para escrita

            # salvando o resultado em um relatório no formato csv
            salvarRelatorioCsv('relatorio-TopCincoEditoras', result)


if __name__ == '__main__':
    main()
