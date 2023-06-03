"""
Você foi contratado para trabalhar no RH de um empresa Multinacional como trainee! Na sua primeira semana, você vai trabalhar no RH.

Sua primeira demanda é criar um sistema que cumpra os seguintes requisitos:

    Seu sistema deverá armazenar os registros dos funcionários. Os registros são, no mínimo: Nome, sobrenome, telefone, profissao e data de nascimento.

    Seu sistema deve ser capaz de fazer as operações básicas de um banco de dados: Criar, Ler, atualizar e deletar, ou seja:

    Criar: deve ser possível receber novos registros pelo usuario e armazenar no seu sistema (CHECK)

    Ler: O usuário deve conseguir encontrar o registro completo, procurando pelo nome ou pela profissao. 
    Sejam apresentados os dados de forma que o nome tenha as primeiras letras maiusculas. 
    O numero deve ser apresentado no formato "(dd)1234-5678". E apresentar de forma mais visual possivel.

    atualizar: O usuario deve conseguir atualizar o registro, buscando pelo numero de telefone

    deletar: O usuario deve conseguir deletar o registro buscando pelo numero do telefone

    Cada operação deverá ser chamada por uma função própria

    Deverá ser possível chamar uma unica função chamada menu() que vai permitir ao usuario a chamar as diferentes operações

Bonus 1

Quando for chamada a operação de leitura, mostrar quantos dias faltam para o aniversário pro colaborador daquele registro. Dica: use a lib datetime

Bonus 2

Receber o CEP do colaborador e armazenar seu endereco.

def recebe_cep_retorna_endereco(cep:str) -> list:
  import requests
  cep = cep.replace("-", "").replace(".", "").replace(" ", "")
  if len(cep) == 8:
      link = f'https://viacep.com.br/ws/{cep}/json/'
      requisicao = requests.get(link)
      dic_requisicao = requisicao.json()
      uf = dic_requisicao['uf']
      cidade = dic_requisicao['localidade']
      bairro = dic_requisicao['bairro']
      logradouro = dic_requisicao['logradouro']
      return([uf, cidade, bairro, logradouro])
  else:
      raise Exception('CEP Inválido')

"""

#nome = input("Digite seu nome: ")

#o lista append vai inserir dados novos dentro da lista
# fazer um while edindo o inpur pro usuário, pedir os dados na ordem e acada inout é uma append pra lista nova. 

banco_de_dados = []

#função para receber o input do usuário e add essas informações dentro do 'dados_usuario'

def criar_dados(banco_de_dados):
    dados_usuario = [] #inicio para garantir que toda chamada desa função ela vai ta vazia. em python vc tem que inicializar as funções, coloco só pra dizer que ela existe
    nome = input('nome: ').capitalize()
    sobrenome = input('sobrenome: ').capitalize()
    telefone = input("telefone: ")
    profissão = input("profissão: ").capitalize()
    data_nascimento = input("data de nascimento: ")
    dados_usuario.append(nome)
    dados_usuario.append(sobrenome) #aassim por diante. 
    banco_de_dados.append(dados_usuario) 

#TRATAR O FORMATO DO NUMERO DE TELEFONE (PESQUISAR)


#função que vai add os dados dentro dos dados usuário. A ultima execução dela vai ser add os dados do usuario dentro do banco de dados. 

for dados_usuario in banco_de_dados:
    if dados_usuario[0] == name:
        print(f"Nome: {dados_usuario[0]}")
        print(f"Telefone: {dados_usuario[1]}")
        print(f"Data de nascimento: {dados_usuario[2]}")

    elif dados_usuario[3] == name: #aqui eu procuro pela profissão caso nao ache pelo nome. pq le pode procurar pelo nome OU pela profissão
        print(f"Nome: {dados_usuario[0]}")
        print(f"Telefone: {dados_usuario[1]}")
        print(f"Data de nascimento: {dados_usuario[2]}")
    else:
        print("nome não encontrado")




#FALTA DELETAR E ATUALIZAR. (PROCURAR FUNÇÃO UPDATE) (PARADELETAR É .DROP)

#toda as funções recebem bancos de dados e o menu tb! 
"""

def menu():
    while True:
        print("===== MENU =====")
        print("1. Criar registro")
        print("2. Ler registro")
        print("3. Atualizar registro")
        print("4. Deletar registro")
        print("0. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            criar_registro()
        elif opcao == "2":
            ler_registro()
        elif opcao == "3":
            atualizar_registro()
        elif opcao == "4":
            deletar_registro()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")

# Chamada da função menu para iniciar o sistema
menu()

"""