# from Arquivos_Salvos import usuarios.txt
from Funcoes import Validacoes

# def comprar_produto(produtos):
#     print(f'\nBem vindo à ala de compras, qual produto o senhor deseja comprar?')
#     for pro in range(len(produtos)):
#         print('\n -------------------------')
#         print(f'Número do Produto: {pro} - Produto: {produtos[pro]["nome"]} - Preço: {produtos[pro]["valor"]:.2f} - Quantidade/KG: {produtos[pro]["quantia/KG"]}')
#         print(' -------------------------\n')
#     nome_prod = input('\nDigite o nome do produto que deseja comprar: ')
#     Validacoes.validar_quantia_prod()
#     compra = input(f'\nO produto: {produtos[nome_prod]["nome"]} custa {produtos[nome_prod]["valor"]} qual a forma de pagamento? (A vista/Cartão): ').capitalize()


# def pagamento(compra, quantidade, produtos, nome_prod, historico_compra):
#     if compra == 'A vista' and quantidade >= 10:
#         print('\n\nParabéns, graças a esse método de pagamento, vc recebe um desconto de 10%')
#         valor_real = produtos[nome_prod]["valor"] * quantidade
#         valor_c_desconto = valor_real - ((produtos[nome_prod]["quantia"] * quantidade) * 0.10)
#         print(f'\nO valor total do produto foi de {valor_real:.2f}, já com o desconto ficou por {valor_c_desconto:.2f}')
#     if compra == 'Cartão':
#         credito = input('\n\nÉ cartão de crédito ou débito? ').lower()
#         if credito == 'débito':
#             print('\n\nParabéns, graças a esse método de pagamento, vc recebe um desconto de 5%')
#             valor_real = produtos[nome_prod]["valor"] * quantidade
#             valor_c_desconto = valor_real - ((produtos[nome_prod]["valor"] * quantidade) * 0.05)
#             print(f'\nO valor total do produto foi de {valor_real:.2f}, já com o desconto ficou por {valor_c_desconto:.2f}')
#         else:
#             valor_real = produtos[nome_prod]["valor"] * quantidade
#             print(f'\n\nO valor da Compra ficou de {valor_real:.2f}')
#             parcelar = input('\nO senhor deseja parcelar? ').capitalize()
#             if parcelar == 'S' or parcelar == 'Sim':
#                 valor_parcelado = int(input('\nConseguimos parcelar em até 6 vezes, deseja parcelar em quantas? '))
#                 valor_real /= valor_parcelado
#                 print(f'\nFicará no valor de: {valor_real:.2f}R$')  
    


def agendar_serv(servicos, agendamentos):
    for s in servicos:
        print('\n\n -------------------------')
        print(f'\nNome do Serviço: {s["nome"]}')
        print(f'Horários Disponíveis: {s["horarios"]}')
        print('\n -------------------------')
        nome_servico = input('\nDigite qual serviço deseja buscar: ').capitalize()
        for s in servicos:
            while nome_servico not in s["nome"]:
                nome_servico = input('Digite qual serviço deseja buscar: ').capitalize()
            for s in servicos:
                if nome_servico in s:
                    print(f'\nNome do serviço: {s["nome_S"]} - Valor: {s["valor"]} - Horários Disponíveis: {s["horarios"]} ')
        
        
            while True:
                valido = True
                horario_especifico = input('\nDigite qual horário deseja: ')
                for agendamento in agendamentos:
                    if horario_especifico == agendamento["horarios"] and s["nome"] == agendamento["nome_S"]:
                        print('\nHorário já agendado!!')
                        valido = False
                if not valido:
                    continue
                while horario_especifico not in s["horarios"]:
                    print('\nHorário Inválido!!')
                    horario_especifico = input('\nDigite qual horário deseja: ')


# def compra_P(produtos):
#     print(f'\nBem vindo à ala de compras, qual produto o senhor deseja comprar?')
#     for pro in range(len(produtos)):
#         print('\n -------------------------')
#         print(f'Número do Produto: {pro} - Produto: {produtos[pro]["nome"]} - Preço: {produtos[pro]["valor"]:.2f} - Quantidade/KG: {produtos[pro]["quantia/KG"]}')
#         print(' -------------------------\n')

     
#     Validacoes.validar_quantia_prod_comp()

#     compra = input(f'\nO produto: {produtos[nome_prod]["nome"]} custa {produtos[nome_prod]["valor"]} qual a forma de pagamento? (A vista/Cartão): ').capitalize()

def listar_agenda(servicos):

    for agenda in servicos:
        print('\n\n -------------------------')
        print(f'Serviço: {agenda[0]} - Tipo: {agenda[1]} - Preço: {agenda[2]} - Horários disponíveis: {agenda[3]}')
        print('-------------------------\n\n')


def cancel_agenda(agendamentos):
    for agenda in range(len(agendamentos)):
        print(f'\n\nNúmero do serviço agendado: {agenda} - Serviço: {agendamentos[agenda]["nome_S"]} - Horário(s) agendado(s): {agendamentos[agenda]["horarios_agendados"]}')

        numero_servico = Validacoes.validar_cancel_S()
        agendamentos.pop(numero_servico)
        print(f'\nSeu horário foi desmarcardo e voltado à antiga lista!!')


def cadastrar_PET(pet):
    print(f'\n\nBem Vindo ao Cadastro Pet!!')
    dono = input('Nome do Dono: ').capitalize()
    nome_pet = input('Digite qual o nome do Seu Pet: ').capitalize()
    animal = input('Qual o animal seu Pet é? ').capitalize()
    raca = input('Qual a raça é seu Pet? ').capitalize()
    idade = int(input('Qual a idade do seu Pet? '))
    peso = input('Qual o peso do Pet? ')

    for bixo in pet:
        if dono == bixo["dono"] and nome_pet == bixo["nome_PET"] and animal == bixo["animal"] and raca == bixo["raca"] and idade == bixo["idade"] and peso == bixo["peso"]:
            print('\nPet já cadastrado!!')
            return cadastrar_PET()
        
    pet = {
        "dono": dono,
        "nome_PET": nome_pet,
        "animal": animal,
        "raca": raca,
        "idade": idade,
        "peso": peso
    }

    return(pet)


def feedback_AV(nome, avaliacao):
    print(f'\n\nBem vindo(a) {nome}, ao Setor de FeedBack, onde sua opinião é válida!!')

    print('\nAqui é onde o(a) senhor(a) pode colocar críticas ou avaliações construtivas para que possamos melhorar nossos serviços de atendimento ao cliente!!')

    escala = Validacoes.validar_AV1()
    escala_atend = Validacoes.validar_AV2()

    opiniao = input('\nGostaria de dar uma opinião sincera sobre nosso sistema? (S/N): ').upper()
    if opiniao == 'S' or opiniao == 'SIM':
        opinar = input('\nDigite sua avaliação sincera sobre nosso serviço ou atendimento, ou até mesmo sobre nosso próprio sistema: ')

        avaliacao = {
            "nome_cliente": nome,
            "avaliacao-1": escala,
            "avaliacao-2": escala_atend,
            "opiniao": opinar
            }
        
        return(avaliacao)

    elif opiniao == 'N' or opiniao == 'NÃO':
        print('\nOk, obrigado pela contribuição!!')

        avaliacao = {
            "nome_cliente": nome,
            "avaliacao-1": escala,
            "avaliacao-2": escala_atend
            }
        