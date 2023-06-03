banco_de_dados = []

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Criar registro")
        print("2. Ler registro")
        print("3. Atualizar registro")
        print("4. Deletar registro")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            criar_registro(banco_de_dados)
        elif opcao == "2":
            ler_registro(banco_de_dados)
        elif opcao == "3":
            atualizar_registro(banco_de_dados)
        elif opcao == "4":
            deletar_registro(banco_de_dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def criar_registro(banco_de_dados):
    dados_usuario = []
    nome = input('Nome: ').capitalize()
    sobrenome = input('Sobrenome: ').capitalize()
    telefone = input("Telefone: ")
    profissao = input("Profissão: ").capitalize()
    data_nascimento = input("Data de nascimento: ")
    dados_usuario.append(nome)
    dados_usuario.append(sobrenome)
    dados_usuario.append(telefone)
    dados_usuario.append(profissao)
    dados_usuario.append(data_nascimento)
    banco_de_dados.append(dados_usuario)

def ler_registro(banco_de_dados):
    name = input("Digite o nome ou a profissão para buscar o registro: ").lower()

    for dados_usuario in banco_de_dados:
        if dados_usuario[0].lower() == name or dados_usuario[3].lower() == name:
            print(f"Nome: {dados_usuario[0]}")
            print(f"Sobrenome: {dados_usuario[1]}")
            print(f"Telefone: ({dados_usuario[2][:2]}){dados_usuario[2][2:6]}-{dados_usuario[2][6:]}")
            print(f"Profissão: {dados_usuario[3]}")
            print(f"Data de nascimento: {dados_usuario[4]}")
            break
    else:
        print("Registro não encontrado.")

def atualizar_registro(banco_de_dados):
    telefone = input("Digite o telefone do registro que deseja atualizar: ")
  
    for dados_usuario in banco_de_dados:
        if dados_usuario[2] == telefone:
            print("Registro encontrado.")
            nome = input("Novo nome: ").capitalize()
            sobrenome = input("Novo sobrenome: ").capitalize()
            profissao = input("Nova profissão: ").capitalize()
            data_nascimento = input("Nova data de nascimento: ")

            dados_usuario[0] = nome
            dados_usuario[1] = sobrenome
            dados_usuario[3] = profissao
            dados_usuario[4] = data_nascimento

            print("Registro atualizado.")
            break

        else:
            print("Registro não encontrado.")

def deletar_registro(banco_de_dados):
    telefone = input("Digite o telefone do registro que deseja deletar: ")
        
    for dados_usuario in banco_de_dados:
        if dados_usuario[2] == telefone:
            banco_de_dados.remove(dados_usuario)
            print("Registro deletado.")
            break

        else:
            print("Registro não encontrado.")

menu()