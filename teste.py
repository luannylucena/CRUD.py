
banco_de_dados = []
#Nome, sobrenome, telefone, profissao e data de nascimento

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

menu()
menu()

def criar_registro(banco_de_dados):
    dados_usuario = [] 
    nome = input('Nome: ').capitalize()
    sobrenome = input('Sobrenome: ').capitalize()
    telefone = input("Telefone: ") #
    profissao = input("Profissão: ").capitalize()
    data_nascimento = input("Data de nascimento: ")
    dados_usuario.append(nome)
    dados_usuario.append(sobrenome) #aassim por diante. 
    dados_usuario.append(telefone)
    dados_usuario.append(profissao)
    dados_usuario.append(data_nascimento)
    banco_de_dados.append(dados_usuario) 

criar_registro(banco_de_dados)

def ler_registro(banco_de_dados):
    name = input("Digite o nome ou a profissão para buscar o registro: ")

    for dados_usuario in banco_de_dados:
        if dados_usuario[0] == name:
            print(f"Nome: {dados_usuario[0]}")
            print(f"Sobrenome: {dados_usuario[1]}")
            print(f"Telefone: {dados_usuario[2]}")
            print(f"Profissão: {dados_usuario[3]}")
            print(f"Data de nascimento: {dados_usuario[4]}")

        elif dados_usuario[3] == name: 
            print(f"Nome: {dados_usuario[0]}")
            print(f"Sobrenome: {dados_usuario[1]}")
            print(f"Telefone: {dados_usuario[2]}")
            print(f"Profissão: {dados_usuario[3]}")
            print(f"Data de nascimento: {dados_usuario[4]}")
        else:
            print("nome não encontrado")

ler_registro(banco_de_dados)

def atualizar_registro(banco_de_dados):
    telefone = input("Digite o telefone do registro que deseja atualizar: ")
    encontrado = False

    for dados_usuario in banco_de_dados:
        if dados_usuario[2] == telefone:
            print("Registro encontrado.")
            nome = input("Nome: ").capitalize()
            sobrenome = input("Sobrenome: ").capitalize()
            profissao = input("Profissão: ").capitalize()
            data_nascimento = input("Data de nascimento: ")

            dados_usuario[0] = nome
            dados_usuario[1] = sobrenome
            dados_usuario[3] = profissao
            dados_usuario[4] = data_nascimento

            print("Registro atualizado.")
            encontrado = True

    if not encontrado:
        print("Registro não encontrado.")

def deletar_registro(banco_de_dados):
    telefone = input("Digite o telefone do registro que deseja deletar: ")
    encontrado = False

    for dados_usuario in banco_de_dados:
        if dados_usuario[2] == telefone:
            banco_de_dados.remove(dados_usuario)
            print("Registro deletado.")
            encontrado = True
            break

    if not encontrado:
        print("Registro não encontrado.")



