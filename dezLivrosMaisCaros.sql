-- 10 livros mais caros

select Cod as "Código Livro", Titulo,
AUTOR.CodAutor as "Código Autor", AUTOR.Nome as "Nome Autor", Valor as "Preço Livro",
EDITORA.CodEditora as "Código Editora", EDITORA.Nome as "Nome Editora" from LIVRO
join AUTOR on AUTOR.CodAutor = LIVRO.Autor
join EDITORA on EDITORA.CodEditora = LIVRO.Editora
order by LIVRO.Valor desc
limit 10;