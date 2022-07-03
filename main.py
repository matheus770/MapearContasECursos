from fileinput import close
import json, os.path
from model import ContaCurso

while(True):
    
    print("O que deseja fazer 1 == Registrar Dados || 2 == Sair: ")
    opcao = input("Qual a opção desejada: ")
    if opcao == str(1):
        accounts = []

        print("Obs: Em cursos separe-os por virgulas ao inves de espaços...Ex: matematica aplicada,portugues pra leigos...")
        sitename = str(input("Digite o nome do site/empresa: "))
        email = str(input("Digite o email registrado:"))
        cursos = str(input("Digite o nome dos cursos:"))
        splitcursos = cursos.split(",") #! É gerado um split separando os cursos pelo caractere "," e armazenado em um array com os nome dos cursos separados.
        logingoogle = str(input("Login com o google: "))

        dadoscontacurso = ContaCurso(sitename,email,splitcursos,logingoogle)
        dadosdict = dadoscontacurso.to_Json()
        
        if(os.path.isfile('dados.json')):              
            dadosjson = json.dumps(dadosdict, indent=4)
            with open("dados.json", "r") as json_file:
                dados = json.load(json_file)
                dados.append(dadosdict)
                close
            with open("dados.json", "w") as json_file:
                dadosjson = json.dumps(dados, indent=4)
                json_file.write(dadosjson)
                close
            with open('dados.txt','a',newline='') as arquivo:
                arquivo.write(dadoscontacurso.show())
                arquivo.write('\n')
                close
        else:
            accounts.append(dadosdict)
            dadosjson = json.dumps(accounts, indent=4)
            with open("dados.json", "w") as json_file:
                json_file.write(dadosjson)
                close
            with open('dados.txt','a',newline='') as arquivo:
                arquivo.write(dadoscontacurso.show())
                arquivo.write('\n')
                close
    elif opcao == str(2):
        break
    elif (opcao != 1) or (opcao != 2) or (type(opcao) == str):
        print("Digite uma opção valida!!!")
        continue
    


