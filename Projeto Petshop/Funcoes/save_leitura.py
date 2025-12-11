from Funcoes import Cadastro_login





def save_usuarios(usuario):
    rota = "C:\\Users\\drama\OneDrive\\Documents\\Pasta VScode - Daniel\\Projeto PetShop\\Arquivos Salvos\\usuarios.txt"
    with open (rota, "r") as arquivos:
         linhas = arquivos.readline

    with open (rota, "w") as arquivos:
        for linha in linhas:
            arquivos.write(linha)

    with open (rota, "a") as arquivos:
        lin_user = f'{usuario["nome"]};{usuario["numero"]};{usuario["endereco"]};{usuario["user"]};{usuario["login"]};{usuario["senha"]}'
        lin_user = lin_user.replace("\n", "")
        arquivos.write(lin_user + '\n')

def leitura_usuarios():
    rota = "C:\\Users\\drama\OneDrive\\Documents\\Pasta VScode - Daniel\\Arquivos Salvos\\Usuarios.txt"
    with open (rota, "r") as arquivo:
         trazer = arquivo.readline()
         
def save_compras(usuario):
    rota2 = "C:\\Users\\drama\OneDrive\\Documents\\Pasta VScode - Daniel\\Projeto PetShop\\Arquivos Salvos\\historico_cmp.txt"
    with open (rota2, "r") as arquivos:
         linhas = arquivos.readline

    with open (rota2, "w") as arquivos:
        for linha in linhas:
            arquivos.write(linha)

    with open (rota2, "a") as arquivos:
        lin_user = f'{usuario["nome"]};{usuario["numero"]};{usuario["endereco"]};{usuario["user"]};{usuario["login"]};{usuario["senha"]}'
        lin_user = lin_user.replace("\n", "")
        arquivos.write(lin_user + '\n')

def save_produtos():
    rota3 = "C:\\Users\\drama\OneDrive\\Documents\\Pasta VScode - Daniel\\Projeto PetShop\\Arquivos Salvos\\produtos.txt"
    with open (rota3, "r") as arquivos:
         linhas = arquivos.readline

    with open (rota3, "w") as arquivos:
        for linha in linhas:
            arquivos.write(linha)

    with open (rota3, "a") as arquivos:
        lin_user = f'{usuario["nome"]};{usuario["numero"]};{usuario["endereco"]};{usuario["user"]};{usuario["login"]};{usuario["senha"]}'
        lin_user = lin_user.replace("\n", "")
        arquivos.write(lin_user + '\n')