n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite só mais um número: "))

if n1 > n2 and n1 > n3:
maior = n1
elif n2 > n1 and n2 > n3:
maior = n2
elif n3 > n1 and n3 > n2:
maior = n3
else:
    print("Os três são iguais")
print(f"O maior número é {maior.2f}")