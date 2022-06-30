from fileinput import close
import json, os.path

accounts = []

print("Obs: Em cursos separe-os por virgulas ao inves de espaços...Ex: matematica aplicada,portugues pra leigos...")
sitename = str(input("Digite o nome do site/empresa: "))
email = str(input("Digite o email registrado:"))
cursos = str(input("Digite o nome dos cursos:"))
scursos = cursos.split(",")
logingoogle = str(input("Login com o google: "))

dictio = {
    "sitename": sitename,
    "email": email,
    "cursos": scursos,
    "logingoogle": logingoogle,
}

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
else:
    accounts.append(dictio)
    jdictio = json.dumps(accounts, indent=4)
    with open("dados.json", "w") as json_file:
        json_file.write(jdictio)
        close


