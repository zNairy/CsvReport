-- 5 editoras que mais tem livros

select EDITORA.CodEditora as "Código Editora", EDITORA.Nome as "Nome Editora",
count(LIVRO.Editora) as "Livros Publicados" from LIVRO
right join EDITORA on EDITORA.CodEditora = LIVRO.Editora
group by EDITORA.CodEditora
order by count(LIVRO.Editora) desc
limit 5;