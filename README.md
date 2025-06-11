# 📚 Sistema de Gerenciamento de Biblioteca

Este é um sistema simples de gerenciamento de biblioteca desenvolvido em Python. Ele permite o cadastro de livros e alunos, empréstimo e devolução 
de livros, além de persistência dos dados em arquivos CSV.

## 🚀 Funcionalidades

- Cadastro de livros com ISBN, título, autor e ano de publicação
- Cadastro de alunos com ID (matrícula) e nome
- Empréstimo de livros para alunos
- Devolução de livros
- Listagem de todos os livros ou apenas os disponíveis
- Listagem de alunos cadastrados
- Salvamento e carregamento automático dos dados em arquivos CSV

## 🛠️ Tecnologias utilizadas

- Python 3
- Manipulação de arquivos `.csv`
- Interface de texto via terminal

## 💾 Estrutura de Arquivos

- `livros.csv`: contém os dados dos livros cadastrados e seus status (disponível ou emprestado).
- `alunos.csv`: contém os dados dos alunos e os ISBNs dos livros emprestados.

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado:
   ```bash
   python --version

CLONE ESSE REPOSITÓRIO :

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

EXECUTE O PROGRAMA :

python biblioteca.py



 EXEMPLO DE USO : 


  SISTEMA DE BIBLIOTECA

1. Cadastrar Livro
2. Listar Livros Disponíveis
3. Listar Todos os Livros
4. Cadastrar Aluno
5. Listar Alunos
6. Emprestar Livro
7. Devolver Livro
8. Salvar e Sair

Escolha uma opção:


