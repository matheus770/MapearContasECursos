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
accounts.append(dictio)
jdictio = json.dumps(accounts, indent=4)

if(os.path.isfile('dados.json')):
    with open("dados.json", "r") as json_file:
        dados = json.load(json_file)
        print(dados)
        close
        #!Se existir dados pegar eles adicionar o novo json e salvar o arquivo com os dados atualizados
else:
    with open("dados.json", "w") as json_file:
        json_file.write(jdictio)
        close


