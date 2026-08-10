import csv

NOME_ARQUIVO = "livros.csv"


# Carrega os livros salvos no arquivo CSV
def carregar_livros():
    livros = []

    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                livro = {
                    "titulo": linha["titulo"],
                    "autor": linha["autor"],
                    "ano": int(linha["ano"]),
                    "isbn": linha["isbn"],
                    "status": linha["status"]
                }

                livros.append(livro)

    except FileNotFoundError:
        livros = []

    return livros


# Salva todos os livros no arquivo CSV
def salvar_livros(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]

    with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(livros)