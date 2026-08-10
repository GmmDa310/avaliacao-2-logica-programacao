# Sistema de Gerenciamento de Biblioteca

Projeto individual da disciplina de Lógica de Programação.

## Descrição

Este programa controla um catálogo de livros usando Python. O catálogo será
salvo no arquivo `livros.csv`, para que os dados continuem disponíveis quando
o programa for aberto novamente.

## Como executar

1. Instale o Python 3.
2. Abra o terminal dentro da pasta do projeto.
3. Execute:

```text
python main.py
```

## Funcionalidades

- Cadastrar livros;
- Emprestar livros;
- Devolver livros;
- Listar livros;
- Buscar por título ou autor;
- Ordenar por título, autor ou ano;
- Salvar e carregar os dados em arquivo CSV.

## Requisitos técnicos aplicados

- **Menu principal:** está na função `mostrar_menu()` e é controlado por
  `if`, `elif` e `else` dentro da função `main()`.
- **Repetição:** o `while` da função `main()` mantém o sistema aberto até a
  opção `7 - Sair`.
- **Funções:** o programa foi dividido em funções pequenas, como
  `cadastrar_livro()`, `buscar_livro()` e `listar_livros()`. Elas recebem
  parâmetros e algumas retornam valores.
- **Lista de dicionários:** a variável `livros` é uma lista e cada livro é um
  dicionário com título, autor, ano, ISBN e status.
- **Persistência:** `carregar_livros()` lê o arquivo no início e
  `salvar_livros()` atualiza o catálogo depois de cada alteração e também
  quando o programa termina.
- **Biblioteca padrão:** foi utilizado somente o módulo `csv`, que já faz parte
  do Python. Não é necessário instalar pacotes com `pip`.
- **Ordenação:** a função `ordenar_livros()` usa `sorted()` e exibe uma nova
  lista, sem alterar a ordem original do catálogo.

## Organização dos arquivos

```text
biblioteca/
├── main.py
├── livros.csv
└── README.md
```

## Evolução do desenvolvimento

O projeto foi desenvolvido em etapas. Cada tarefa foi registrada em um commit
separado para mostrar a evolução do código.

### Etapa 1 — Estrutura inicial

Commit:

```text
cria estrutura inicial do projeto de biblioteca
```

Foram criados `main.py`, `livros.csv`, `README.md` e as funções iniciais de
leitura e escrita do arquivo CSV.

### Etapa 2 — Cadastro e validações

Commit:

```text
adiciona cadastro e validacao de livros
```

Foi adicionada a função de cadastro, com título, autor, ano e ISBN. Também
foram incluídas a validação de campos vazios, a validação do ano e a
verificação de ISBN repetido.

### Etapa 3 — Empréstimo e devolução

Commit:

```text
adiciona emprestimo e devolucao de livros
```

Foram adicionadas as funções de empréstimo e devolução. O status do livro muda
entre `Disponível` e `Emprestado`, com mensagens para situações inválidas.

### Etapa 4 — Listagem e busca

Commit:

```text
adiciona listagem e busca de livros
```

Foi adicionada a listagem organizada de todos os livros e a busca por título
ou autor, aceitando letras maiúsculas e minúsculas.

### Etapa 5 — Ordenação, menu e documentação

Commit:

```text
finaliza menu ordenacao e documentacao
```

Foi finalizado o menu principal, com `while`, `if`, `elif` e `else`. Também
foi incluída a ordenação por título, autor ou ano e a documentação inicial.

### Etapa 6 — Correção da persistência

Commit:

```text
corrige persistencia imediata no arquivo CSV
```

Foi corrigido o salvamento dos dados. Agora o arquivo `livros.csv` é
atualizado imediatamente depois de cadastrar, emprestar ou devolver um livro.
O programa também continua salvando ao escolher a opção de sair.

Além disso, linhas inválidas do CSV são ignoradas com uma mensagem, e o
programa informa quando ocorre um erro ao salvar.

## Como consultar a evolução no Git

Para ver o histórico resumido:

```text
git log --oneline
```

Para estudar uma etapa específica:

```text
git show CODIGO-DO-COMMIT
```

Para voltar temporariamente a uma versão anterior:

```text
git checkout CODIGO-DO-COMMIT
```

Para retornar à versão final:

```text
git checkout main
```

## Preparação para a defesa oral

- `carregar_livros()` recupera os dados do CSV quando o programa começa.
- `salvar_livros()` atualiza o catálogo no CSV depois das alterações e antes
  de encerrar.
- `buscar_por_isbn()` evita ISBN repetido e localiza livros para empréstimo ou
  devolução.
- `cadastrar_livro()` cria um dicionário e adiciona esse dicionário à lista.
- `emprestar_livro()` e `devolver_livro()` alteram somente o status do livro.
- `buscar_livro()` percorre a lista com `for` e aceita parte do título ou autor.
- `ordenar_livros()` usa `sorted()` para mostrar uma cópia ordenada.
- `main()` usa `while` para repetir o menu e `if/elif/else` para chamar cada
  funcionalidade.

Uma alteração simples para demonstrar ao vivo é mudar uma mensagem exibida,
adicionar uma opção de busca ou incluir um novo campo no dicionário e no CSV.