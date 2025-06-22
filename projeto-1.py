import os
artistas_cadas = {}
p_ativo = True

def limp_term():
    if os.name == "nt":
        _= os.system("cls")
    else:
        _= os.system("clear")

def cadastro_artista():
    nome= input("digite seu nome : ")
    limp_term()
    snome= input("digite seu sobrenome : ")
    limp_term()
    prof = input("digite seu ramo na arte: ")
    limp_term()
    est= input("digite seu estilo artistico: ")
    limp_term()
    cid= input("digite sua cidade: ")
    limp_term()
    cpf = int(input("digite seu cpf: "))
    limp_term()
    while cpf < 10000000000:
        print("cpf invalido")
        cpf=int(input("digite outro cpf: "))
        limp_term()
    while cpf in artistas_cadas:
        print("ja possui cadastro na plataforma")
        cpf=int(input("digite outro cpf: "))
        limp_term()
    nome = str(nome).lower()
    prof = str(prof).lower()
    est = str(est).lower()
    cid = str(cid).lower()
    dados_artista = {"nome": nome, "sobrenome": snome, "profissão":prof, "estilo":est,"cidade":cid}
    artistas_cadas[cpf] = dados_artista

def pesquisa():
    t_pesquisas = ["nome", "profissão", "estilo", "cidade"]
    print("///////////////////////////////////")
    print("//     Digite como pesquisar     //")
    print("//             nome              //")
    print("//           profissão           //")
    print("//            estilo             //")
    print("//            cidade             //")
    print("///////////////////////////////////")
    pesquisa = input()
    limp_term()
    encontrados = {}
    
    while pesquisa not in t_pesquisas:
        pesquisa = input("digite um tipo de pesquisa valido: ")
        limp_term()

    if pesquisa == "nome":
        nome_busca = input("digite o primeiro nome: ")
        nome_busca = nome_busca.lower()
        limp_term()
        for cpf, dados_artista in artistas_cadas.items():
            if dados_artista["nome"] == nome_busca:
                print(f"cpf:{cpf}")
                encontrados[cpf] = dados_artista
                for chave, valor in dados_artista.items():
                    print(f"{chave.capitalize()}: {valor}")

    elif pesquisa == "profissão":
        nome_busca = input("digite a modalidade: ")
        nome_busca = nome_busca.lower()
        limp_term()
        for cpf, dados_artista in artistas_cadas.items():
            if dados_artista["profissão"] == nome_busca:
                print(f"cpf:{cpf}")
                encontrados[cpf] = dados_artista
                for chave, valor in dados_artista.items():
                    print(f"{chave.capitalize()}: {valor}")
    
    elif pesquisa == "estilo":
        nome_busca = input("digite o estilo de arte: ")
        nome_busca = nome_busca.lower()
        limp_term()
        for cpf, dados_artista in artistas_cadas.items():
            if dados_artista["estilo"] == nome_busca:
                print(f"cpf:{cpf}")
                encontrados[cpf] = dados_artista
                for chave, valor in dados_artista.items():
                    print(f"{chave.capitalize()}: {valor}")
    
    elif pesquisa == "cidade":
        nome_busca = input("digite a cidade: ")
        nome_busca = nome_busca.lower()
        limp_term()
        for cpf, dados_artista in artistas_cadas.items():
            if dados_artista["cidade"] == nome_busca:
                print(f"cpf:{cpf}")
                encontrados[cpf] = dados_artista
                for chave, valor in dados_artista.items():
                    print(f"{chave.capitalize()}: {valor}")
while p_ativo == True:
    options = ["cadastro", "pesquisa"]
    print("///////////////////////////////////")
    print("//            Menu:              //")
    print("//           cadastro            //")
    print("//           pesquisa            //")
    print("///////////////////////////////////")
    opt = input("")
    limp_term()
    while opt not in options:
        print("Digite uma opção valida")
        print("///////////////////////////////////")
        print("//            Menu:              //")
        print("//           cadastro            //")
        print("//           pesquisa            //")
        print("///////////////////////////////////")
        opt = input("")
        limp_term()
    if opt == "cadastro":
        cadastro_artista()
    elif opt == "pesquisa":
        pesquisa()
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')
