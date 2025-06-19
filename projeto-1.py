artistas_cadas = {}
def cadastro_artista():
    nome= input("digite seu nome completo:")
    prof = input("digite seu ramo na arte:")
    est= input("digite seu estilo artistico:")
    cid= input("digite sua cidade:")
    cpf = int(input("digite seu cpf:"))
    while cpf < 10000000000:
        print("cpf invalido")
        cpf=int(input("digite outro cpf:"))
    while cpf in artistas_cadas:
        print("ja possui cadastro na plataforma")
        cpf=int(input("digite outro cpf:"))
    nome = str(nome).lower()
    prof = str(prof).lower()
    est = str(est).lower()
    cid = str(cid).lower()
    dados_artista = {"nome": nome, "profissão":prof, "estilo":est,"cidade":cid}
    artistas_cadas[cpf] = dados_artista
def pesquisa()
    Print(///////////////////////////////////)
    Print(//  Digite como quer pesquisar   //)
    Print(//             nome              //)
    Print(//           profissão           //)
    Print(//            estilo             //)
    Print(///////////////////////////////////)
    pesquisa = input()
    if 
