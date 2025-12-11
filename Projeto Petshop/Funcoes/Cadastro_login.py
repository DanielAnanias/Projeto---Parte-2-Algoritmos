validacao = 'PetPetSerttão352'
from Funcoes import Validacoes
from Funcoes import save_leitura

def Cadastrar_User():
    nome = input('\n\nDigite o nome para cadastro: ')
    numero = Validacoes.validar_numero()
    endereco = input('\nDigite o endereço: ').capitalize()
    user = Validacoes.validar_adm(validacao)
    login = input('\nCrie um login bom e seguro: ')
    senha = Validacoes.validar_senha()

    usuario = {
        "nome": nome,
        "numero": numero,
        "endereco": endereco,
        "user": user,
        "login": login,
        "senha": senha
    }
    return(usuario)

def Login_user():
    ler = save_leitura.Leitura_usuarios()
    print("\n\nEfetue o login para acessar nossos serviços")
    nome = input('Digite seu nome de cadastro: ') 
    log = Validacoes.validar_login()
    save_leitura.Leitura_usuarios()
