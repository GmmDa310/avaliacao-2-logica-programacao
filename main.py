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


# Salva os livro no arquivo CSV
def salvar_livros(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]

    with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(livros)
     # Procura um livro pelo ISBN
def buscar_por_isbn(livros, isbn):
    for livro in livros:
        if livro["isbn"].lower() == isbn.lower():
            return livro

    return None


# Pede um texto e impede que o campo fique vazio
def pedir_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto
        else:
            print("Este campo não pode ficar vazio.")


# Pede um ano válido
def pedir_ano():
    while True:
        ano_digitado = input("Ano: ").strip()

        try:
            ano = int(ano_digitado)

            if ano > 0:
                return ano
            else:
                print("Digite um ano maior que zero.")

        except ValueError:
            print("Ano inválido. Digite apenas números.")


# Cadastra um livro novo
def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")

    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    ano = pedir_ano()
    isbn = pedir_texto("ISBN: ")

    if buscar_por_isbn(livros, isbn) is not None:
        print("Já existe um livro cadastrado com este ISBN.")
        return False

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "Disponível"
    }

    livros.append(novo_livro)

    print("Livro cadastrado com sucesso.")

    return True