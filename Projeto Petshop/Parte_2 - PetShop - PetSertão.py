from Funcoes import Cadastro_login
# from Funcoes import Validacoes
# from Funcoes import MENU_ADM_Prod
# from Funcoes import MENU_Cli
from Funcoes import save_leitura
logado = False

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

    elif escolha == 1:
        
        loga = Cadastro_login.Login_user()
        save_leitura.leitura_usuarios(usuario)

    elif escolha == 2:

        usuario = Cadastro_login.Cadastrar_User()
        save_leitura.save_usuarios(usuario)

    while logado:
        
