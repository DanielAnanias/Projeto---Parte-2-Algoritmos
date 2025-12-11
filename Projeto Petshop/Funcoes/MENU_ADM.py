from Funcoes import Validacoes



def cadastrar_produto(produtos):
    produto = Validacoes.validar_P_existe()
    classificacao = input('\nQual será o tipo de produto oferecido? ').capitalize()
    valor = Validacoes.validar_valor()

    if classificacao == 'Alimenticio':

        kg = Validacoes.validar_KG()

        produtos = {
            "nome_P": produto,
            "classificacao": classificacao,
            "valor": valor,
            "peso": kg
        }

        return(produtos)
    
    else:
        quantidade = Validacoes.validar_quantia_P()
        
        produtos = {
            "nome_P": produto,
            "classificacao": classificacao,
            "valor": valor,
            "quantia": quantidade
        }

        return(produtos)


def buscar_S(servicos):
    for s in servicos:
        print(s["nome_S"])
    busca = input('\nDigite qual produto deseja buscar: ').capitalize()
    print('\n -------------------------')
    for se in servicos:
        if busca in se: 
            print(f'\nNome: {se["nome_S"]} - Tipo: {se["tipo_S"]} - Valor: {se["valor_S"]} - Horários disponíveis: {se["horarios"]}')
    print('\n -------------------------')
    return(servicos)


def buscar_P(produtos):
    for p in produtos:
        print(p["nome_P"])
    busca = input('\nDigite qual produto deseja buscar: ').capitalize()
    print('\n -------------------------')
    for p in produtos:
        if busca in p: 
            print(f'\nNome: {p["nome_P"]} - Tipo: {p["tipo_P"]} - Valor: {p["valor_P"]} - Quantidade/KG: {p["quantia/KG"]}')
    print('\n -------------------------')
    return(produtos)


def listar_CLTs(contribuintes):
    print('\n\n -------------------------')
    for clt in contribuintes:
        print(f'Funcionário: {clt["nome_CLT"]} setor: {clt["setor"]} - Idade: {clt["idade"]} - Experiência: {clt["expert"]}')
    print('-------------------------\n\n')
    return(contribuintes)


def cadastrar_servico():
    servico = input('\n\nDigite o nome do serviço: ')
    classificacao = input('\nQual será o tipo de serviço oferecido? ')
    valor = Validacoes.validar_valor_S(valor)
    horarios = Validacoes.validar_horario(horarios)

    servicos = {
        "servico": servico,
        "classificacao": classificacao,
        "valor": valor,
        "horarios disponiveis": horarios
    }
    return(servicos)


def cadastrar_CLT():
    nome_CLT = input('\nDigite o Nome do Funcionário: ')
    setor = input('\nQual será o setor de trabalho? ')
    idade = Validacoes.validar_idade_CLT(idade)
    experiencia = input('\nQual a experiência na área: ')
    estuda = input('\nO(a) funcionário(a) estuda? (S/N): ').upper()
    
    if estuda == "S" or "SIM":

        Validacoes.validar_estudo_CLT()
    
    else:

        contribuintes = {
            "nome": nome_CLT, 
            "setor": setor, 
            "idade": idade, 
            "experiencia": experiencia, 
            "estudo": estuda
    }
    return(contribuintes)


def cadastrar_VET():
    nome_vet = input('\nDigite qual o Nome do(a) Veterinário(a): ')
    idade = Validacoes.validar_VET()
    experiencia = input('\nQual a experiência na área? ').capitalize()
    crmv = input('\nQual CRMV do Veterinário(a)? ').upper()
    salario = input('\nDigite qual será o Salário: ')

    contribuintes = {
        "nome_vet": nome_vet,
        "idade": idade,
        "experiencia": experiencia,
        "crmv": crmv,
        "salario": salario
    }

    return(contribuintes)


def remover_P(produtos):
    for posicao in range(len(produtos)):
        print(f'Indice: {posicao} - Nome do Produto: {produtos[posicao]["nome_P"]}')
    
    posicao = Validacoes.validar_remove_P()

    produtos.pop(posicao)

def remover_S(servicos):
    for indice in range(len(servicos)):
        print(f'Indice: {indice} - Nome do Produto: {servicos[indice]["nome_S"]}')

    indice = Validacoes.validar_remove_S()

    servicos.pop(indice)


def remover_Pet(pets):
    for lugar in range(len(pets)):
        print(f"\n\nIndice: {lugar} - Nome do Pet : {pets[lugar]["nome"]} - Dono: {pets[lugar]["dono"]}")

    lugar = Validacoes.validar_remove_PET()

    pets.pop(lugar)


def remover_CLT(contribuintes):
    for posicao in range(len(contribuintes)):
        print(f'\n\nIndice: {posicao} - Nome do contribuinte: {contribuintes[posicao]["nome_CLT"]}')

    posicao = Validacoes.validar_remove_CLT()

    contribuintes.pop(posicao)


def atualizar_P(produtos):
    for posicao in range(len(produtos)):
        print(f'Código {posicao} - Nome {produtos[posicao]["nome_P"]}')

    posicao = Validacoes.validar_atua_P()
    produto = input('\nDigite o nome do Produto: ').capitalize()
    classificacao = input('\nDigite o tipo de Produto: ').capitalize()
    valor = Validacoes.validar_valor()

    if classificacao == 'Alimenticia' or classificacao == 'Alimentícia':
        kg = Validacoes.validar_peso_P()

        dic_novo = {"nome_P": produto, "classe": classificacao, "preco": valor, "peso": kg}
        produtos[posicao] = dic_novo
        print(dic_novo)

        return(dic_novo)
    
    else:
        quantidade = Validacoes.validar_quantia_P()

        dic_novo = {"nome_P": produto, "classe": classificacao, "preco": valor, "quantia": quantidade}
        produtos[posicao] = dic_novo
        print(dic_novo)

        return(dic_novo)


def atualizar_S(servicos):
    for posicao in range(len(servicos)):
        print(f'\n\nCódigo {posicao} - Nome {servicos[posicao]["nome_S"]}')

    posicao = Validacoes.validar_atua_S()
    servico = input('\nDigite o nome do Serviço: ')
    classificacao = input('\nDigite o tipo de Serviço: ')
    descricao = input('\nDê uma breve Descrição do serviço')
    valor = Validacoes.validar_valor()

    dicio_new = {"nome_S": servico, "classe": classificacao, "descricao": descricao, "preco": valor}
    servicos[posicao] = dicio_new
    print(dicio_new)

    return(dicio_new)


def atualizar_PET(pet):
    for colocação in range(len(pet)):
        print(f'\n\nÍndice: {colocação} - Nome {pet[colocação]["nome_PET"]}')

    indice = Validacoes.validar_indice_PET()

    dono = input('\nNome do Dono: ')
    nome_pet = input('\nDigite qual o nome do Seu Pet: ')
    animal = input('\nQual o animal seu Pet é? ')
    raca = int(input('\nQual a raça é seu Pet? '))
    idade = int(input('\nQual a idade do seu Pet? '))
    peso = input('\nQual o peso do Pet? ')

    dic_Pet = {"dono": dono, "nome_PET": nome_pet, "animal": animal, "raca": raca, "idade": idade, "peso": peso}
    pet[indice] = dic_Pet
    print(dic_Pet)

    return(dic_Pet)


def atualizar_VET(contribuintes):
    for posicao in range(len(contribuintes)):
        print(f'\n\nCódigo {posicao} - Nome {contribuintes[posicao]["nome_CLT"]}')

    posicao = Validacoes.validar_indice_CLT()

    atuacao = input('\nQual a atuação do(a) Funcionário(a)? ').capitalize()

    if atuacao == "Veterinário" or atuacao == "Veterinario" or atuacao == "Veterinaria" or atuacao == "Veterinária":

        nome_vet = input('\nDigite qual o Nome do(a) Veterinário(a): ')
        idade = Validacoes.validar_VET()
        experiente = input('\nQual a experiência na área? ').capitalize()
        crmv = input('\nQual CRO do Veterinário(a)? ').upper()
        salario = input('\nDigite qual será o Salário: ')

        dic_vet_new = {"nome_VET": nome_vet, "idade": idade, "experiencia": experiente, "crmv": crmv, "salario": salario}
        contribuintes[posicao] = dic_vet_new
        print(dic_vet_new)

        return(dic_vet_new)
    
    
def atualizar_CLT(contribuintes, posicao):
    nome_CLT = input('\nDigite o Nome do Funcionário: ')
    setor = input('\nQual será o setor de trabalho? ')
    idade = Validacoes.validar_idade_CLT()
    experiencia = input('\nQual a experiência na área: ')
    estuda = input('\nO(a) funcionário(a) estuda? (S/N): ').upper()

    if estuda == "S" or estuda == "SIM":

        local = input('\nOnde Estuda? ')
        ensino = input('\nQual o nível de Ensino? ')
        estudo = input('\nO que Estuda? ')

        dic_novo_CLT = {"nome_CLT": nome_CLT, "setor": setor, "idade": idade, "experiencia": experiencia, "estuda": estuda, "local": local, "ensino": ensino, "estudo": estudo}
        contribuintes[posicao] = dic_novo_CLT
        print(dic_novo_CLT)

        return(dic_novo_CLT)
    
    else:
        dic_novo_CLT = {"nome_CLT": nome_CLT, "setor": setor, "idade": idade, "experiencia": experiencia}
        contribuintes[posicao] = dic_novo_CLT
        print(dic_novo_CLT)

        return(dic_novo_CLT)
    