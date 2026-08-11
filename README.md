# Sistema de Gerenciamento de Biblioteca

Projeto individual da disciplina de Lógica de Programação.

## Sobre o código
Este programa foi feito em Python para controlar uma biblioteca. É possível cadastrar, emprestar, devolver, listar, buscar e ordenar livros.

Os dados ficam salvos no arquivo `livros.csv`, então não são perdidos quando o programa é fechado.


## Oque o código faz

* Cadastrar livros
* Emprestar livros
* Devolver livros
* Listar livros
* Buscar por título ou autor
* Ordenar por título, autor ou ano
* Salvar os dados no CSV

## Estrutura do código

```text
biblioteca/
├── main.py
├── livros.csv
└── README.md
```

## O que eu usei

* `if`, `elif` e `else`
* `while`
* Funções
* Listas e dicionários
* Arquivo CSV
* `sorted()` para ordenação

O programa usa apenas a biblioteca `csv`, que já vem com o Python.

## Histórico do desenvolvimento

O código foi feito em etapas, usando commits para registrar as mudanças.

**Etapa 1:** criação da estrutura inicial e leitura/escrita do CSV.

**Etapa 2:** criação do cadastro de livros e validações.

**Etapa 3:** criação das funções de empréstimo e devolução.

**Etapa 4:** criação da listagem e busca de livros.

**Etapa 5:** finalização do menu, ordenação e documentação.

**Etapa 6:** correção do salvamento imediato no arquivo CSV.

## Git

Para ver os commits do projeto:

```text
git log --oneline
```

Para ver uma alteração específica:

```text
git show CODIGO-DO-COMMIT
```
