class Livro:
    def __init__(self, isbn, titulo, autor, ano_publicacao):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = int(ano_publicacao)
        self.disponivel = True
        self.quem_pegou_id_aluno = None

    def __str__(self):
        status = 'Disponível' if self.disponivel else f"Emprestado para: {self.quem_pegou_id_aluno}"
        return f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano_publicacao} | {status}"


class Aluno:
    def __init__(self, id_aluno, nome):
        self.id_aluno = id_aluno
        self.nome = nome
        self.livros_emprestado_isbns = []

    def __str__(self):
        livros_isbns = ", ".join(self.livros_emprestado_isbns) if self.livros_emprestado_isbns else "Nenhum livro emprestado"
        return f"ID Aluno: {self.id_aluno} | Nome: {self.nome} | Livros Emprestados (ISBNs): [{livros_isbns}]"


ARQUIVO_LIVROS = "livros.csv"
ARQUIVO_ALUNOS = "alunos.csv"

acervo_biblioteca = []
alunos_cadastrados = []


def adicionar_livro():
    print("\n--- Adicionar Novo Livro ---")
    isbn = input("Digite o ISBN do livro: ")

    for livro_existente in acervo_biblioteca:
        if livro_existente.isbn == isbn:
            print("Erro: Já existe um livro com esse ISBN.")
            return

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")

    try:
        ano_publicacao_int = int(ano_publicacao)
        if ano_publicacao_int <= 0:
            print("Erro: Ano de publicação inválido.")
            return
    except ValueError:
        print("Erro: Ano de publicação deve ser um número.")
        return

    novo_livro = Livro(isbn, titulo, autor, ano_publicacao_int)
    acervo_biblioteca.append(novo_livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")


def listar_todos_os_livros():
    print("\n--- Todos os Livros no Acervo ---")
    if not acervo_biblioteca:
        print("Nenhum livro cadastrado.")
        return
    for livro in acervo_biblioteca:
        print(livro)


def cadastrar_aluno():
    print("\n--- Cadastrar Novo Aluno ---")
    id_aluno = input("Digite o ID (matrícula) do aluno: ")

    for aluno_existente in alunos_cadastrados:
        if aluno_existente.id_aluno == id_aluno:
            print("Erro: Já existe um aluno com este ID.")
            return

    nome = input("Digite o nome do aluno: ")
    novo_aluno = Aluno(id_aluno, nome)
    alunos_cadastrados.append(novo_aluno)
    print(f"Aluno '{nome}' cadastrado com sucesso!")


def listar_alunos():
    print("\n--- Alunos Cadastrados ---")
    if not alunos_cadastrados:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos_cadastrados:
        print(aluno)


def salvar_dados_livros():
    with open(ARQUIVO_LIVROS, "w") as arquivo:
        for livro in acervo_biblioteca:
            disponivel_str = "1" if livro.disponivel else "0"
            quem_pegou_str = livro.quem_pegou_id_aluno if livro.quem_pegou_id_aluno else ""
            linha = f"{livro.isbn},{livro.titulo},{livro.autor},{livro.ano_publicacao},{disponivel_str},{quem_pegou_str}\n"
            arquivo.write(linha)
    print("Dados dos livros salvos com sucesso!")


def salvar_dados_alunos():
    with open(ARQUIVO_ALUNOS, "w") as arquivo:
        for aluno in alunos_cadastrados:
            isbns_str = ";".join(aluno.livros_emprestado_isbns)
            linha = f"{aluno.id_aluno},{aluno.nome},{isbns_str}\n"
            arquivo.write(linha)
    print("Dados dos alunos salvos com sucesso!")


def carregar_dados_alunos():
    try:
        with open(ARQUIVO_ALUNOS, "r") as arquivo:
            for linha_csv in arquivo:
                linha_csv = linha_csv.strip()
                if not linha_csv:
                    continue
                partes = linha_csv.split(",", 2)
                id_aluno = partes[0]
                nome = partes[1]
                aluno_carregado = Aluno(id_aluno, nome)

                if len(partes) > 2 and partes[2]:
                    isbns_str = partes[2]
                    aluno_carregado.livros_emprestado_isbns = [isbn.strip() for isbn in isbns_str.split(";") if isbn.strip()]

                alunos_cadastrados.append(aluno_carregado)
        print("Dados dos alunos carregados.")
    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO_ALUNOS}' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados dos alunos: {e}")


def carregar_dados_livros():
    try:
        with open(ARQUIVO_LIVROS, "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",", 5)
                if len(partes) >= 5:
                    isbn, titulo, autor, ano, disponivel_str = partes[:5]
                    quem_pegou = partes[5] if len(partes) > 5 else ""
                    livro = Livro(isbn, titulo, autor, ano)
                    livro.disponivel = disponivel_str == "1"
                    livro.quem_pegou_id_aluno = quem_pegou if quem_pegou else None
                    acervo_biblioteca.append(livro)
        print("Dados dos livros carregados.")
    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO_LIVROS}' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados dos livros: {e}")


def buscar_livros_por_isbn(isbn_procurado):
    for livro in acervo_biblioteca:
        if livro.isbn == isbn_procurado:
            return livro
    return None


def buscar_aluno_por_id(id_aluno_procurado):
    for aluno in alunos_cadastrados:
        if aluno.id_aluno == id_aluno_procurado:
            return aluno
    return None


def emprestar_livro():
    print("\n--- Emprestar Livro ---")
    isbn_livro = input("Digite o ISBN do livro: ")
    id_aluno = input("Digite o ID do aluno: ")

    livro = buscar_livros_por_isbn(isbn_livro)
    aluno = buscar_aluno_por_id(id_aluno)

    if not livro:
        print("Erro: Livro não encontrado.")
        return
    if not aluno:
        print("Erro: Aluno não encontrado.")
        return
    if not livro.disponivel:
        print(f"Erro: Livro '{livro.titulo}' já está emprestado.")
        return

    livro.disponivel = False
    livro.quem_pegou_id_aluno = aluno.id_aluno
    aluno.livros_emprestado_isbns.append(livro.isbn)

    print(f"Livro '{livro.titulo}' emprestado para '{aluno.nome}' com sucesso!")


def devolver_livro():
    print("\n--- Devolver Livro ---")
    isbn_livro = input("Digite o ISBN do livro: ")
    livro = buscar_livros_por_isbn(isbn_livro)

    if not livro:
        print("Erro: Livro não encontrado.")
        return
    if livro.disponivel:
        print("Erro: Este livro já está disponível.")
        return

    id_aluno = livro.quem_pegou_id_aluno
    aluno = buscar_aluno_por_id(id_aluno)

    livro.disponivel = True
    livro.quem_pegou_id_aluno = None

    if aluno and livro.isbn in aluno.livros_emprestado_isbns:
        aluno.livros_emprestado_isbns.remove(livro.isbn)

    print(f"Livro '{livro.titulo}' devolvido com sucesso!")


def listar_livros_disponiveis():
    print("\n--- Livros Disponíveis ---")
    disponiveis = [livro for livro in acervo_biblioteca if livro.disponivel]
    if not disponiveis:
        print("Nenhum livro disponível.")
        return
    for livro in disponiveis:
        print(livro)


def exibir_menu():
    print("\n" + "="*30)
    print("  SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1. Cadastrar Livro")
    print("2. Listar Livros Disponíveis")
    print("3. Listar Todos os Livros")
    print("4. Cadastrar Aluno")
    print("5. Listar Alunos")
    print("6. Emprestar Livro")
    print("7. Devolver Livro")
    print("8. Salvar e Sair")  
    print("="*30)
    return input("Escolha uma opção: ")

def main():
    carregar_dados_livros()
    carregar_dados_alunos()

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            adicionar_livro()
        elif escolha == '2':
            listar_todos_os_livros()
        elif escolha == '3':
            listar_livros_disponiveis()
        elif escolha == '4':
            cadastrar_aluno()
        elif escolha == '5':
            listar_alunos()
        elif escolha == '6':
            emprestar_livro()
        elif escolha == '7':
            devolver_livro()
        elif escolha == '8':
            salvar_dados_livros()
            salvar_dados_alunos()
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
