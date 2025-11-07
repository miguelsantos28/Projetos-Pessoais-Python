login = "admin"
senha = "1234"
entrada = input("Digite o nome de usuário: ")
entrada2 = input("Digite a senha: ")
if login == entrada and senha == entrada2:
    print("Acesso permitido!")
else:
    print("Acesso negado!")