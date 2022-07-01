from fileinput import close
import json, os.path
from model import ContaCurso


while True:
    accounts = []

    print("Obs: Em cursos separe-os por virgulas ao inves de espaços...Ex: matematica aplicada,portugues pra leigos...")
    sitename = str(input("Digite o nome do site/empresa: "))
    email = str(input("Digite o email registrado:"))
    cursos = str(input("Digite o nome dos cursos:"))
    scursos = cursos.split(",")
    logingoogle = str(input("Login com o google: "))

    dadosuser = ContaCurso(sitename,email,scursos,logingoogle)
    dadosdic = dadosuser.to_Json()
    accounts.append(dadosdic)
    dictio = accounts
    
    if(os.path.isfile('dados.json')):              
        jdictio = json.dumps(dictio, indent=4)
        with open("dados.json", "r") as json_file:
            dados = json.load(json_file)
            dados.append(dictio)
            close
        with open("dados.json", "w") as json_file:
            jdictio = json.dumps(dados, indent=4)
            json_file.write(jdictio)
            close
        with open('dados.txt','a',newline='') as arquivo:
            arquivo.write(dadosuser.show())
            arquivo.write('\n')
            close
        print("O que deseja fazer 1 == Registrar outra conta || 2 == Sair ")
        op = int(input("Qual a opção desejada: "))
        if op == 1:
            continue
        elif op == 2:
            break
    else:
        jdictio = json.dumps(accounts, indent=4)
        with open("dados.json", "w") as json_file:
            json_file.write(jdictio)
            close
        with open('dados.txt','a',newline='') as arquivo:
            arquivo.write(dadosuser.show())
            arquivo.write('\n')
            close
        break


