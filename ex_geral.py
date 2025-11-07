nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome ao contrário é {nome [-1::-1]}")
    if " " in nome:
        print("Seu nome possui espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {(len(nome))} caracteres")
    print(f"A primeira letra do seu nome é {nome [0]}")
    print(f"A ultima letra do seu nome é {nome [-1]}")
else:
    print("Desculpe, mas vc deixou campos vazios.")
    
