senha = 141
resp = int(input("Digite a senha: "))

while resp != senha:
    print("Senha incorreta!")
    resp = int(input("Digite a senha: "))

print("Senha correta!")