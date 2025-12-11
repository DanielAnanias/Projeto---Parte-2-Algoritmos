validacao = 'PetPetSerttão352'

def validar_numero():
    numero = input('\nDigite o DDD e o número de telefone: ')
    if len(numero) < 11 or len(numero) > 11:
        return validar_numero()
    return(numero)
    
def validar_adm(validacao):
    user = input('\nDigite qual o tipo de usuário está sendo cadastrado: (Cliente/Admin) ').capitalize()
    if user == "Admin":
        codigo = input('\nDigite o Código de validação do ADM: ')
        if codigo != validacao:
            print('\nVocê não tem acesso ao perfil de ADM!!')
            return validar_adm()
        return(user)
    return(user)
        
def validar_senha():
        senha = input('\nCrie uma senha segura com caractéres especiais (@, #, $): ')
        if '@' not in senha and '#' not in senha and '$' not in senha or len(senha) < 8 or len(senha) > 12:
            return validar_senha()
        return(senha)
    
def validar_login(usuarios):
    login = input('Digite seu Usuário Login: ')
    senha = input('Digite sua senha: ')
    for log in usuarios:
        if log["login"] == login and log["senha"] == senha:
            print(f'\n\nBem vindo {log["nome"]}, o que podemos fazer pelo senhor hoje? ')
            logado = True
            tipo = log["user"]
            break
    if logado == False:
        print('\nUsuário não encontrado, login inválido')
    return(login, senha)

def validar_quantia_prod_comp(produtos, nome_prod):
    quantidade = int(input(f'\nQual a quantia deseja comprar do produto? '))
    if quantidade <= 0 or quantidade > produtos[nome_prod]["quantia"] or nome_prod not in {produtos["nome"]}:
        return validar_quantia_prod_comp()
    return(quantidade)

def validar_valor():
    valor = float(input('\nDigite qual será o valor: '))
    while valor <= 0:
        valor = float(input('\nDigite qual será o valor: '))
    return(valor)

def validar_horario():
    horarios = input('\nDigite quais serão os horário disponíveis: ').split()
    while len(horarios) <= 0 or len(horarios) > 18:
        horarios = input('Digite quais serão os horário disponíveis: ').split()
    return(horarios)

def validar_idade_CLT():
    idade = int(input('\nDigite qual a idade do funcionário: '))
    if idade < 18:
        print('\nNão pode contratar!!')
        return None

def validar_estudo_CLT(estuda, nome_CLT, setor, idade):
    if estuda == 'S' or estuda == 'SIM':
        local = input('\nOnde Estuda? ')
        ensino = input('\nQual o nível de Ensino? ')
        estudo = input('\nO que Estuda? ')

        contribuintes = {
            "nome": nome_CLT,
            "setor": setor,
            "idade": idade,
            "estudo": estudo,
            "local": local,
            "ensino": ensino
        }
    return(contribuintes)

def validar_VET():
    idade = int(input('\nDigite a idade: '))
    if idade < 23:
        print('\nIdade Insuficiente!!')
        return validar_VET()
    return(idade)

def validar_remove_P(produtos):
    posicao = int(input('\nDigite qual o indice você deseja remover: '))
    if posicao < 0 or posicao >= len(produtos):
        print('Inválido!')
        return validar_remove_P()
    return(posicao)

def validar_remove_S(servicos):
    posicao = int(input('\nDigite qual o indice você deseja remover: '))
    if posicao < 0 or posicao >= len(servicos):
        print('Inválido!')
        return validar_remove_S()
    return(posicao)

def validar_remove_PET(pets):
    lugar = int(input("\nDigite qual o indice do Pet você deseja remover:"))
    if lugar < 0 or lugar >= (len(pets)):
        print("\nInválido!")
        return validar_remove_PET()
    return(lugar)

def validar_remove_CLT(contribuintes):
    posicao = int(input('\nDigite qual o indice você deseja remover: '))
    if posicao < 0 or posicao >= len(contribuintes):
        print('\nInválido')
        return validar_remove_CLT()
    return(posicao)

def validar_atua_P(produtos):
    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
    if posicao < 0 or posicao >= len(produtos):
        print('\nInválido')
        return validar_atua_P()
    return(posicao)

def validar_atua_S(servicos):
    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
    if posicao < 0 or posicao >= len(servicos):
        print('\nInválido')
        return validar_atua_S()
    return(posicao)

def validar_atua_PET(pets):
    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
    if posicao < 0 or posicao >= len(pets):
        print('\nInválido')
        return validar_atua_S()
    return(posicao)

def validar_atua_CLT(contribuintes):
    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
    if posicao < 0 or posicao >= len(contribuintes):
        print('\nInválido')
        return validar_atua_S()
    return(posicao)

def validar_peso_P(produto):
    kg = int(input(f'\nQuantas quilogramas foram compradas de {produto}? '))
    if kg <= 0:
        return validar_peso_P()
    return(kg)

def validar_quantia_P():
    quantidade = int(input('\nQual a quantidade deste produto? '))
    if quantidade <= 0:
        return validar_quantia_P()
    return(quantidade)

def validar_indice_PET(pet):
    indice = int(input('\nDigite o índice que você deseja atualizar: '))
    if indice < 0 or indice >= len(pet):
        print('\nNão encontrado!!')
        return validar_indice_PET()
    return(indice)

def validar_indice_CLT(contribuintes):
    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
    if posicao < 0 or posicao >= len(contribuintes):
        print('\nInválido')
        return validar_indice_CLT()
    return(posicao)

def validar_KG(produto):
    kg = int(input(f'\nQuantas quilogramas foram compradas de {produto} do fornecedor? '))
    if kg <= 0:
        return validar_KG()
    return(kg)

def validar_P_existe(produtos):
    produto = input('\nDigite o nome do produto: ')
    if produto in produtos:
        print('Produto já cadastrado com este Nome')
        return validar_P_existe()
    return(produto)


# def validar_P_existe_pay(produtos):

#     nome_prod = input('\nDigite o nome do produto que deseja comprar: ')
#     for produto in produtos:
#         if produto["nome_P"] == nome_prod:
#             produto_enc = produto
#             break

#     if produto_enc is None:

#         return(f'Produto {nome_prod} não encontrado!!')
    
# def validar_estoque(nome_prod, produtos, quantidade):
#     for p in produtos:
#         if quantidade > nome_prod["quantia/KG"]:
#             return(f'Quantidade do estoque insufuciente, temos somente {nome_prod[p]["quantia/KG"]}')

def validar_cancel_S(agendamentos, nome):
    numero_servico = int(input('\nDigite qual o número do serviço deseja desmarcar: '))
    if nome == agendamentos[numero_servico]["nome_S"]:
        if numero_servico < 0 or numero_servico >= len(agendamentos):
            print('\nInválido')
            return validar_cancel_S()
        return(numero_servico)
    
def validar_idade_PET():
    idade = int(input('Qual a idade do seu Pet? '))
    if idade >= 14:
        return validar_idade_PET()
    return(idade)

def validar_AV1():
    escala = float(input('\nNuma escala de 0 à 10, qual a nota do nosso atendimento? '))
    if escala > 10 or escala < 0:
        return validar_AV1()
    return(escala)

def validar_AV2():
    escala_atend = float(input('\nNuma escala de 0 à 10, qual a nota do nosso sistema? '))
    if escala_atend > 10 or escala_atend < 0:
        return validar_AV1()
    return(escala_atend)

        
