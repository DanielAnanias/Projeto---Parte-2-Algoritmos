usuarios = [['Daniel', '8340028922', 'Gato Preto', 'Admin', 'DanielAdemir', 'Admin100107']] + [['Adrian', '55521213', 'Cat Black', 'Cliente', 'AdinCli', 'Cliente001']]
pet = []
produtos = [['Ração', 'Alimentício', 15.99, 400]] + [['Alpiste', 'Alimentício', 9.90, 748]] + [['Shampoo', 'Estético', 30.00, 55]] + [['Condicionador', 'Estético', 12.00, 100]]
servicos = [['Banho', 'Estético', 35.99, ['13:00', '14:00', '15:00', '16:00', '17:00', '18:00']]] + [['Vacinação', 'Clínico', 15.99, ['7:00', '7:30', '8:00', '8:30', '9:00', '9:30', '10:00']]] + [['Tosa', 'Estético', 35.00, ['11:00', '11:30', '12:00']]] +[['Castração','clinico',90.00,['7:00', '7:30', '8:00', '8:30', '9:00', '9:30', '10:00']]]
historico_servicos = []
horarios_agendados = []
historico_compra = []
agendamentos = []
contribuintes = [['Fabiano', 'Limpeza', 18, 'Nenhuma', 'Não', '1.518.66' ]] + [['Yarley', 'Veterinário', 22, '2 Anos prestando Serviço Público', '25556698', '2.578.73' ]]
avaliacao = []
validacao = 'PetPetSerttão352'
logado = False

# def addcontato():
#     nome = input('\n\nDigite o nome para cadastro: ')
#     numero = input('\nDigite o DDD e o número de telefone: ')
#     while len(numero) < 11 or len(numero) > 11:
#         numero = input('Digite o DDD e o número de telefone: ')
#     endereco = input('\nDigite o endereço: ').capitalize()
#     user = input('\nDigite qual o tipo de usuário está sendo cadastrado: (Cliente/Admin) ').capitalize()
#     if user == 'Admin':
#         codigo = input('\nDigite o Código de validação do ADM: ')
#         if codigo != validacao:
#             print('\nVocê não tem acesso ao perfil de ADM!!')
#             break
#     login = input('\nCrie um login bom e seguro: ')
#     senha = input('\nCrie uma senha segura: ')
#     usuarios.append([nome, numero, endereco, user, login, senha])



while True:
    print('Bem vindo ao Petshop - PetSertão onde até os animais saem contentes!!')
    print('1 - login de Usuário; ')
    print('2 - Cadastrar novo Usuário;')
    print('0 - Sair')
    escolha = int(input('\nDigite quais das opções deseja: '))
    while escolha < 0 or escolha > 2:
        escolha = int(input('Digite quais das opções deseja: '))
    if escolha == 0:
        print('\nObrigado pela preferência e volte sempre!!')
        break

    elif escolha == 2:
        nome = input('\n\nDigite o nome para cadastro: ')
        numero = input('\nDigite o DDD e o número de telefone: ')
        while len(numero) < 11 or len(numero) > 11:
            numero = input('Digite o DDD e o número de telefone: ')
        endereco = input('\nDigite o endereço: ').capitalize()
        user = input('\nDigite qual o tipo de usuário está sendo cadastrado: (Cliente/Admin) ').capitalize()
        if user == 'Admin':
            codigo = input('\nDigite o Código de validação do ADM: ')
            if codigo != validacao:
                print('\nVocê não tem acesso ao perfil de ADM!!')
                break
        login = input('\nCrie um login bom e seguro: ')
        senha = input('\nCrie uma senha segura: ')
        usuarios.append([nome, numero, endereco, user, login, senha])
        

    elif escolha == 1:
        print("\n\nEfetue o login para acessar nossos serviços")
        nome = input('Digite seu nome de cadastro: ')
        login = input('Digite seu Usuário Login: ')
        senha = input('Digite sua senha: ')
        for log in usuarios:
            if log[4] == login and log[5] == senha:
                print(f'\n\nBem vindo {log[0]}, o que podemos fazer pelo senhor hoje? ')
                logado = True
                tipo = log[3]
                break

        if logado == False:
            print('\nUsuário não encontrado, login inválido')
    


    while logado:
        if tipo == 'Cliente':
            print(f'\n\nOlá {nome}, o que o(a) senhor(a) deseja?')

            print('\n1 - Compra de Produtos;')
            print('2 - Agendamento de Serviços;')
            print('3 - Adicionar Pet;')
            print('4 - FeedBack;')
            print('0 - Voltar')

            escolha = int(input('\nDigite quais das opções deseja: '))
            while escolha < 0 or escolha > 4:
                escolha = int(input('Digite quais das opções deseja: '))
            if escolha == 0:
                print('\nObrigado pela preferência e volte sempre!!')
                break

            elif escolha == 1:
                print(f'\nBem vindo à ala de compras, qual produto o senhor deseja comprar?')
                for pro in range(len(produtos)):
                    print('\n -------------------------')
                    print(f'Número do Produto: {pro} - Produto: {produtos[pro][0]} - Preço: {produtos[pro][2]:.2f} - Quantidade/KG: {produtos[pro][3]}')
                    print(' -------------------------')
                indice = int(input('\nDigite o número do produto que deseja comprar: '))
                quantidade = int(input(f'\nQual a quantia deseja comprar do produto? '))
                while quantidade <= 0 or quantidade > produtos[indice][3] or indice < 0:
                    indice = int(input('Digite o número do produto que deseja comprar: '))
                    quantidade = int(input(f'Qual a quantia deseja comprar do produto? '))
                compra = input(f'\nO produto: {produtos[indice][0]} custa {produtos[indice][2]} qual a forma de pagamento? (A vista/Cartão): ').capitalize()
                if compra == 'A vista' and quantidade >= 10:
                    print('\n\nParabéns, graças a esse método de pagamento, vc recebe um desconto de 10%')
                    valor_real = produtos[indice][2] * quantidade
                    valor_c_desconto = valor_real - ((produtos[indice][2] * quantidade) * 0.10)
                    print(f'\nO valor total do produto foi de {valor_real:.2f}, já com o desconto ficou por {valor_c_desconto:.2f}')
                if compra == 'Cartão':
                    credito = input('\n\nÉ cartão de crédito ou débito? ').lower()
                    if credito == 'débito':
                        print('\n\nParabéns, graças a esse método de pagamento, vc recebe um desconto de 5%')
                        valor_real = produtos[indice][2] * quantidade
                        valor_c_desconto = valor_real - ((produtos[indice][2] * quantidade) * 0.05)
                        print(f'\nO valor total do produto foi de {valor_real:.2f}, já com o desconto ficou por {valor_c_desconto:.2f}')
                    else:
                        valor_real = produtos[indice][2] * quantidade
                        print(f'\n\nO valor da Compra ficou de {valor_real:.2f}')
                        parcelar = input('\nO senhor deseja parcelar? ').capitalize()
                        if parcelar == 'S' or parcelar == 'Sim':
                            valor_parcelado = int(input('\nConseguimos parcelar em até 6 vezes, deseja parcelar em quantas? '))
                            valor_real /= valor_parcelado
                            print(f'\nFicará no valor de: {valor_real:.2f}R$')  
                
                historico_compra.append([nome, produtos[indice][0], quantidade, valor_real])
                produtos[indice][3] -= quantidade
                print(f'\n\nAgora tem-se {produtos[indice][3]} do {produtos[indice][0]} Compra Realizada com sucesso!!')


            elif escolha == 2:
                print('\n\nBem vindo a área de agendamento!!')
                print('\n1 - Agendar serviço;')
                print('2 - Listar Horários Disponíveis;')
                print('3 - Cancelar Agendamento;')
                print('0 - Voltar;')
                alternativa = int(input('\nDigite qual ação deseja executar: '))
                while alternativa > 3 or alternativa < 0:
                    alternativa = int(input('Digite qual ação dejeja exacutar: '))

                if alternativa == 0:
                    print('\nServiço encerrado!')
                    break


                elif alternativa == 1:
                    for s in servicos:
                        print('\n\n -------------------------')
                        print(f'\nNome do Serviço: {s[0]}')
                        print(f'Horários Disponíveis: {s[3]}')
                        print('\n -------------------------')
                    nome_servico = input('\nDigite qual serviço deseja buscar: ').capitalize()
                    for s in servicos:
                        while nome_servico not in s[0]:
                            nome_servico = input('Digite qual serviço deseja buscar: ').capitalize()
                        for s in servicos:
                            if nome_servico in s:
                                print(f'\nNome do serviço: {s[0]} - Valor: {s[2]} - Horários Disponíveis: {s[3]} ')
                        
                        
                            while True:
                                valido = True
                                horario_especifico = input('\nDigite qual horário deseja: ')
                                for agendamento in agendamentos:
                                    if horario_especifico == agendamento[4] and s[0] == agendamento[1]:
                                        print('\nHorário já agendado!!')
                                        valido = False
                                if not valido:
                                    continue
                                while horario_especifico not in s[3]:
                                    print('\nHorário Inválido!!')
                                    horario_especifico = input('\nDigite qual horário deseja: ')


                                    
                                historico_servicos.append([nome, s[0], s[1], s[2], horario_especifico])
                                agendamentos.append([nome, s[0], s[1], s[2], horario_especifico])
                                print('\nAgendamento, marcado com sucesso!!')
                                break
                            break
                        break
                        

                elif alternativa == 2:

                        for agenda in servicos:
                            print('\n\n -------------------------')
                            print(f'Serviço: {agenda[0]} - Tipo: {agenda[1]} - Preço: {agenda[2]} - Horários disponíveis: {agenda[3]}')
                            print('-------------------------\n\n')       
    

                elif alternativa == 3:

                    for agenda in range(len(agendamentos)):
                        print(f'\n\nNúmero do serviço agendado: {agenda} - Serviço: {agendamentos[agenda][1]} - Horário(s) agendado(s): {agendamentos[agenda][4]}')
                        
                    numero_servico = int(input('\nDigite qual o número do serviço deseja desmarcar: '))
                    if nome == agendamentos[numero_servico][0]:
                        while numero_servico < 0 or numero_servico >= len(agendamentos):
                            print('\nInválido')
                            numero_servico = int(input('\nDigite qual o indice você deseja remover: '))
                        agendamentos.remove(agendamentos[numero_servico])
                        print(f'\nSeu horário foi desmarcardo e voltado à antiga lista!!')



            elif escolha == 3:
                print('\n\nBem vindo ao Adição de Pet!!')

                print('\n1 - Cadastrar Pet;')
                print('0 - Voltar para o MENU.')
                print('OBS: Para funções mais avançadas é necessário o auxílio do Administrador')

                funcao = int(input('\nDigite qual função deseja executar? '))
                while funcao < 0 or funcao > 1:
                    funcao = int(input('Digite qual função deseja executar? '))

                if funcao == 0:
                    print('\nObrigado pela preferência, Volte sempre!!')
                    break

                if funcao == 1:

                    print(f'\n\nBem Vindo ao Cadastro Pet!!')
                    dono = input('Nome do Dono: ').capitalize()
                    nome_pet = input('Digite qual o nome do Seu Pet: ').capitalize()
                    animal = input('Qual o animal seu Pet é? ').capitalize()
                    raca = input('Qual a raça é seu Pet? ').capitalize()
                    idade = int(input('Qual a idade do seu Pet? '))
                    peso = input('Qual o peso do Pet? ')

                    for bixo in pet:
                        if dono == bixo[0] and nome_pet == bixo[1] and animal == bixo[2] and raca == bixo[3] and idade == bixo[4] and peso == bixo[5]:
                            print('\nPet já cadastrado!!')

                    pet.append ([dono, nome_pet, animal, raca, idade, peso])


        elif escolha == 5:
            print(f'\n\nBem vindo(a) {nome}, ao Setor de FeedBack, onde sua opinião é válida!!')

            print('\nAqui é onde o(a) senhor(a) pode colocar críticas ou avaliações construtivas para que possamos melhorar nossos serviços de atendimento ao cliente!!')

            escala = float(input('\nNuma escala de 0 à 10, qual a nota do nosso atendimento? '))
            escala_atend = float(input('\nNuma escala de 0 à 10, qual a nota do nosso sistema? '))

            opiniao = input('\nGostaria de dar uma opinião sincera sobre nosso sistema? (S/N): ').upper()
            if opiniao == 'S' or opiniao == 'SIM':
                opinar = input('\nDigite sua avaliação sincera sobre nosso serviço ou atendimento, ou até mesmo sobre nosso próprio sistema: ')

                avaliacao.append([nome, escala, escala_atend, opinar])

            elif opiniao == 'N' or opiniao == 'NÃO':
                print('\nOk, obrigado pela contribuição!!')
                break


                    




                
            
        if tipo == 'Admin':
            print(f'\n\nOlá {nome}!!')
            gerenciamento = input('\nO que deseja Gerenciar? (Serviços/Produtos): ').capitalize().strip()
            while gerenciamento != 'Serviços' and gerenciamento != 'Produtos' and gerenciamento != '0' and gerenciamento != 'Servicos':
                gerenciamento = input('\nO que deseja Gerenciar? (Serviços/Produtos): ').capitalize().strip()
            print('\nEscolha - 0 - Se quiser voltar ao Menu Principal')
            if gerenciamento == '0':
                break
            while gerenciamento == 'Produtos':
                print('\n 1 - Cadastrar Produto;')
                print('2 - Busca de Produtos;')
                print('3 - Remover Produto;')
                print('4 - Atualizar Produto;')
                print('5 - Histórico de vendas de produtos;')
                print('6 - Controle Pet;')
                print('0 - Voltar.')
                escolha = int(input('\nDigite quais das opções deseja: '))
                while escolha > 6 or escolha < 0 or escolha == '':
                    escolha = int(input('\nDigite quais das opções deseja: '))

                
                if escolha == 0:
                    print('\nObrigado pela preferência e volte sempre!!')
                    break

                elif escolha == 1:
                    produto = input('\nDigite o nome do produto: ')
                    while produto in produtos:
                        print('Produto já cadastrado com este Nome')
                        produto = input('\nDigite o nome do produto: ')

                    classificacao = input('\nQual será o tipo de produto oferecido? ').capitalize()
                    valor = float(input('\nDigite qual será o valor do Produto: '))
                    while valor <= 0:
                        valor = float(input('\nDigite qual será o valor do Produto: '))

                    if classificacao == 'Alimenticio':
                        kg = int(input(f'\nQuantas quilogramas foram compradas de {produto} do fornecedor? '))
                        while kg <= 0:
                            kg = int(input(f'\nQuantas quilogramas foram compradas de {produto}? '))
                        produtos.append ([produto, classificacao, valor, kg])
                    else:
                        quantidade = int(input('\nQual a quantidade deste produto? '))
                        while quantidade <= 0:
                            quantidade = int(input('\nQual a quantidade deste produto? '))
                        produtos.append ([produto, classificacao, valor, quantidade])

                elif escolha == 2:
                    for p in produtos:
                        print(p[0])
                    busca = input('\nDigite qual produto deseja buscar: ').capitalize()
                    print('\n -------------------------')
                    for p in produtos:
                        if busca in p: 
                            print(f'\nNome: {p[0]} - Tipo: {p[1]} - Valor: {p[2]} - Quantidade/KG: {p[3]}')
                    print('\n -------------------------')

                elif escolha == 3:
                    for posicao in range(len(produtos)):
                        print(f'Indice: {posicao} - Nome do Produto: {produtos[posicao][0]}')

                    posicao = int(input('\nDigite qual o indice você deseja remover: '))
                    while posicao < 0 or posicao >= len(produtos):
                        print('Inválido')
                        posicao = int(input('\nDigite qual o indice você deseja remover: '))
                    produtos.remove(produtos[posicao])

                elif escolha == 4:
                    for posicao in range(len(produtos)):
                        print(f'Código {posicao} - Nome {produtos[posicao][0]}')

                    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
                    while posicao < 0 or posicao >= len(produtos):
                        print('Inválido')
                        posicao = int(input('\nDigite o índice que você deseja atualizar: '))
                    
                    produto = input('\nDigite o nome do Serviço: ').capitalize()
                    classificacao = input('\nDigite o tipo de Serviço: ').capitalize()
                    valor = input('\nDigite qual o valor Reajustado: ')
                    if classificacao == 'Alimentícia':
                        kg = int(input(f'\nQuantas quilogramas foram compradas de {produto}? '))
                        while kg <= 0:
                            kg = int(input(f'Quantas quilogramas foram compradas de {produto}? '))

                        sublistaNova = [produto, classificacao, valor, kg]
                        produtos[posicao] = sublistaNova
                        print(sublistaNova)
                    else:
                        quantidade = int(input('\nQual a quantidade deste produto? '))
                        while quantidade <= 0:
                            quantidade = int(input('Qual a quantidade deste produto? '))
                        sublistaNova = [produto, classificacao, valor, quantidade]
                        produtos[posicao] = sublistaNova
                        print(sublistaNova)
                    

                elif escolha == 5:
                    print("\n----HIstórico de Compras----")
                    if len(historico_compra) == 0:
                        print('\n Nenhuma compra foi realizada até o momento!')

                    else :
                        for compra in historico_compra:
                                print(f"\nCliente: {compra[0]} - Produto:{compra[1]} - Quanrtidade:{compra[2]} - Total : R${compra[3]:.2f}  ")
                              
                            

                elif escolha == 6:
                    print('\n\n1 - Listar Pets;')
                    print('2 - Atualizar Pets;')
                    print('3 - Remover Pet;')  
                    print('0 - Voltar ao MENU;')
                    opcao = int(input('\nQual das opções deseja? '))
                    while opcao < 0 or opcao > 3:
                        opcao = int(input('Qual das opções deseja? '))

                    if opcao == 0:
                        print('\nFim da Execução!!')
                        break


                    elif opcao == 1:
                        print('\n\n -------------------------')
                        for pets in pet:
                            print(f'\n\nDono: {pets[0]} Nome: {pets[1]} - Animal: {pets[2]} - Raça: {pets[3]} - Idade: {pets[4]} - Peso: {pets[5]}')
                        print('-------------------------\n\n')


                    elif opcao == 2:
                        for colocação in range(len(pet)):
                            print(f'\n\nÍndice: {colocação} - Nome {pet[colocação][0]}')

                        indice = int(input('\nDigite o índice que você deseja atualizar: '))
                        while colocação < 0 or colocação >= len(pet):
                            print('\nNão encontrado!!')
                            indice = int(input('Digite o índice que você deseja atualizar: '))
                        
                        dono = input('\nNome do Dono: ')
                        nome_pet = input('\nDigite qual o nome do Seu Pet: ')
                        animal = input('\nQual o animal seu Pet é? ')
                        raca = int(input('\nQual a raça é seu Pet? '))
                        idade = int(input('\nQual a idade do seu Pet? '))
                        peso = input('\nQual o peso do Pet? ')
                        sublistaPet = [dono, nome_pet, animal, raca, idade, peso]
                        pet[indice] = sublistaPet
                        print(sublistaPet)


                    elif opcao == 3:
                        for lugar in range(len(pets)):
                            print(f"\n\nIndice: {lugar} - Nome do Pet : {pets[lugar][1]} - Dono: {pets[lugar][0]}")
                        lugar = int(input("\nDigite qual o indice do Pet você deseja remover:"))
                        while lugar < 0 or lugar >= (len(pets)):
                            print("\nInválido!")
                            lugar=int(input("Digite qual o índice do Pet você deseja remover:"))
                        pets.remove(pets[lugar])


            while gerenciamento == 'Serviços' or gerenciamento == 'Servicos':
                print('\n\n1 - Cadastrar Serviço;')
                print('2 - Busca de Serviços;')
                print('3 - Remover Serviço;')
                print('4 - Atualizar dados de Serviço;')
                print('5 - Histórico de Agendamentos de Seviços;')
                print('6 - Cadastro de Funcionários e Veterinários;')
                print('0 - Voltar.')
                escolha = int(input('\nDigite quais das opções deseja: '))
                while escolha < 0 or escolha > 6:
                    escolha = int(input('Digite quais das opções deseja: '))
                if escolha == 0:
                    print('\nObrigado pela preferência e volte sempre!!')
                    break
                

                elif escolha == 1:
                    servico = input('\n\nDigite o nome do serviço: ')
                    classificacao = input('\nQual será o tipo de serviço oferecido? ')
                    valor = float(input('\nDigite qual será o valor do Serviço: '))
                    while valor <= 0:
                        valor = float(input('\nDigite qual será o valor do Serviço: '))
                    horarios = input('\nDigite quais serão os horário disponíveis: ').split()
                    while len(horarios) <= 0 or len(horarios) > 18:
                        horarios = input('Digite quais serão os horário disponíveis: ').split()
                    servicos.append ([servico, classificacao, valor, horarios])

                elif escolha == 2:
                    for s in servicos:
                        print(s[0])
                    busca = input('\n\nDigite qual Serviço deseja buscar: ').capitalize()
                    print('\n -------------------------')
                    for s in servicos:
                        if busca in s:  
                            print(f'Nome: {s[0]} - Tipo: {s[1]} - Valor: {s[2]} - Horarios Disponíveis: {s[3]} ')

                elif escolha == 3:
                    for posicao in range(len(servicos)):
                        print(f'\n\nIndice: {posicao} - Nome do Serviço: {servicos[posicao][0]}')

                    posicao = int(input('\nDigite qual o indice você deseja remover: '))
                    while posicao < 0 or posicao >= len(servicos):
                        print('\nInválido')
                        posicao = int(input('Digite qual o indice você deseja remover: '))
                    servicos.remove(servicos[posicao])

                elif escolha == 4:
                    for posicao in range(len(servicos)):
                        print(f'\n\nCódigo {posicao} - Nome {servicos[posicao][0]}')

                    posicao = int(input('\nDigite o índice que você deseja atualizar: '))
                    while posicao < 0 or posicao >= len(servicos):
                        print('Inválido')
                        posicao = int(input('Digite o índice que você deseja atualizar: '))
                    
                    servico = input('\nDigite o nome do Serviço: ')
                    classificacao = input('\nDigite o tipo de Serviço: ')
                    descricao = input('\nDê uma breve Descrição do serviço')
                    valor = int(input('\nDigite qual o valor Reajustado: '))
                    while valor <= 0:
                        valor = int(input('Digite qual o valor Reajustado: '))
                    sublistaNova = ([servico, classificacao, descricao, valor])
                    servicos[posicao] = sublistaNova
                    print(sublistaNova)

                elif escolha == 5:
                    print("\n---- Histórico de Agendamentos de Seviços ----")
                    if len(historico_servicos) == 0:
                        print('\n Nenhum agendamneto foi realizado até o momento!')

                    else :
                        for serv in historico_servicos:
                                print(f"\nCliente: {serv[0]} - Produto:{serv[1]} - Quanrtidade:{serv[2]} - Total : R${serv[3]:.2f}  ")


                elif escolha == 6:
                    print('\n\nBem vindo à ala de Cadastro de Funcionários!!')
                    print('\n1 - Cadastrar Funcionário;')
                    print('2 - Lista de Funcionários;')
                    print('3 - Remover Funcionário;')
                    print('4 - Atualizar dados do Funcionário;')
                    print('0 - Voltar.')
                    
                    acao = int(input('\nDigite qual das opções deseja: '))
                    while acao < 0 and acao > 4:
                        acao = int(input('Digite qual das opções deseja: '))

                    if acao == 0:
                        print('\nFim desta Aba!!')
                        break
                    elif acao == 1:
                        atuacao = input('\nQual será a área de atuação do Funcionário(a): ')
                        if atuacao == 'Veterinária':
                            confirm = input('\nÉ Médico(a) Veterinário(a)? (S/N): ').upper()
                            if confirm == 'S':
                                nome_vet = input('\nDigite qual o Nome do(a) Veterinário(a): ')
                                idade = int(input('\nDigite a idade: '))
                                if idade < 24:
                                    print('\nIdade Insuficiente!!')
                                    break
                                experiente = input('\nQual a experiência na área? ').capitalize()
                                crmv = input('\nQual CRMV do Veterinário(a)? ').upper()
                                salario = input('\nDigite qual será o Salário: ')
                                contribuintes.append([nome_vet, idade, experiente, crmv, salario])

                        else:
                            nome_CLT = input('\nDigite o Nome do Funcionário: ')
                            setor = input('\nQual será o setor de trabalho? ')
                            idade = int(input('\nDigite qual a idade do funcionário: '))
                            if idade < 18:
                                print('\nNão pode contratar!!')
                                break
                            experiencia = input('\nQual a experiência na área: ')
                            estuda = input('\nO(a) funcionário(a) estuda? (S/N): ').upper()
                            if estuda == 'N' or estuda == 'NÃO':
                                contribuintes.append([nome_CLT, setor, idade, experiencia, estuda])
                            if estuda == 'S' or estuda == 'SIM':
                                local = input('\nOnde Estuda? ')
                                ensino = input('\nQual o nível de Ensino? ')
                                estudo = input('\nO que Estuda? ')
                                contribuintes.append([nome_CLT, setor, idade, experiencia, estuda, local, ensino, estudo])


                    elif acao == 2:
                        print('\n\n -------------------------')
                        for clt in contribuintes:
                            print(f'Funcionário: {clt[0]} setor: {clt[1]} - Idade: {clt[2]} - Experiência: {clt[3]}')
                        print('-------------------------\n\n')

                    elif acao == 3:
                        for posicao in range(len(contribuintes)):
                            print(f'\n\nIndice: {posicao} - Nome do Contribuinte: {contribuintes[posicao][0]}')

                        posicao = int(input('\nDigite qual o indice você deseja remover: '))
                        while posicao < 0 or posicao >= len(contribuintes):
                            print('\nInválido')
                            posicao = int(input('Digite qual o indice você deseja remover: '))
                        contribuintes.remove(contribuintes[posicao])

                    elif acao == 4:
                        for posicao in range(len(contribuintes)):
                            print(f'\n\nCódigo {posicao} - Nome {contribuintes[posicao][0]}')

                        posicao = int(input('\nDigite o índice que você deseja atualizar: '))
                        while posicao < 0 or posicao >= len(contribuintes):
                            print('\nInválido')
                            posicao = int(input('Digite o índice que você deseja atualizar: '))
                        atuacao = input('\nQual a atuação do(a) Funcionário(a)? ')
                        
                        if atuacao == 'Veterinário':
                            confirm = input('\nÉ Médico(a) Veterinário(a)? (S/N): ').upper()
                            if confirm == 'S':
                                nome_vet = input('\nDigite qual o Nome do(a) Veterinário(a): ')
                                idade = int(input('\nDigite a idade: '))
                                if idade < 24:
                                    print('\nIdade Insuficiente!!')
                                    break
                                experiente = input('\nQual a experiência na área? ').capitalize()
                                crmv = input('\nQual CRO do Veterinário(a)? ').upper()
                                salario = input('\nDigite qual será o Salário: ')
                                sublistaNova_CLT = ([nome_vet, idade, experiente, crmv, salario])
                                contribuintes[posicao] = sublistaNova_CLT
                                print(sublistaNova_CLT)

                            else:
                                nome_CLT = input('\nDigite o Nome do Funcionário: ')
                                setor = input('\nQual será o setor de trabalho? ')
                                idade = int(input('\nDigite qual a idade do funcionário: '))
                                if idade < 18:
                                    print('\nNão pode contratar!!')
                                    break
                                experiencia = input('\nQual a experiência na área: ')
                                estuda = input('\nO(a) funcionário(a) estuda? (S/N): ').upper()

                                if estuda == 'S' or estuda == 'SIM':
                                    local = input('\nOnde Estuda? ')
                                    ensino = input('\nQual o nível de Ensino? ')
                                    estudo = input('\nO que Estuda? ')
                                sublistaNova_CLT = ([nome_CLT, setor, idade, experiencia, estuda, local, ensino, estudo])
                                contribuintes[posicao] = sublistaNova_CLT
                                print(sublistaNova_CLT)
                                
                                if estuda == 'N' or estuda == 'NÃO':
                                    sublistaNova_CLT = ([nome_CLT, setor, idade, experiencia, estuda])
                                contribuintes[posicao] = sublistaNova_CLT
                                print(sublistaNova_CLT)
                                        

