import sqlite3

def criando_bd():
    conexao = sqlite3.connect('funcionarios.db')

    cursor = conexao.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS funcionarios(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cargo TEXT NOT NULL,
                salario REAL NOT NULL
            );    
        """
    )

    conexao.close()

escolha = -1


def inserir():
    nome = input("Nome do funcionário: ")
    idade = int(input("Idade do funcionário: "))
    cargo = input("Cargo do funcionário: ")
    salario = float(input("Salário do funcionário: "))

    conexao = sqlite3.connect('funcionarios.db')
    cursor = conexao.cursor()

    cursor.execute(
        """
            INSERT INTO funcionarios(nome, idade, cargo, salario)
            VALUES (?, ?, ?, ?);
        """,
        (nome, idade, cargo, salario)
    )

    conexao.commit()
    conexao.close()
    print("Funcionário inserido com sucesso!")

def visualizar():
    conexao = sqlite3.connect('funcionarios.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios;")
    funcionarios = cursor.fetchall()

    for funcionario in funcionarios:
        print(funcionario)

    conexao.close()
def atualizar():
    id_atualizar = int(input("ID do funcionário a ser atualizado: "))
    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))
    novo_cargo = input("Novo cargo: ")
    novo_salario = float(input("Novo salário: "))

    conexao = sqlite3.connect('funcionarios.db')
    cursor = conexao.cursor()

    cursor.execute(
        """
            UPDATE funcionarios
            SET nome = ?, idade = ?, cargo = ?, salario = ?
            WHERE id = ?;
        """,
        (novo_nome, nova_idade, novo_cargo, novo_salario, id_atualizar)
    )

    conexao.commit()
    conexao.close()
    print("Funcionário atualizado com sucesso!")

def deletar():
    id_deletar = int(input("ID do funcionário a ser deletado: "))

    conexao = sqlite3.connect('funcionarios.db')
    cursor = conexao.cursor()

    cursor.execute(
        """
            DELETE FROM funcionarios
            WHERE id = ?;
        """,
        (id_deletar,)
    )

    conexao.commit()
    conexao.close()
    print("Funcionário deletado com sucesso!")
criando_bd()
while True:
    print("Menu de opções:")
    print("1. Inserir dados")
    print("2. Visualizar dados cadastrados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        inserir()
    elif escolha == 2:
        visualizar()
    elif escolha == 3:
        atualizar()
    elif escolha == 4:
        deletar()
    elif escolha == 5:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida!")