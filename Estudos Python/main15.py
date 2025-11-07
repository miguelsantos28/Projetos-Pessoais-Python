n = int(input("Digite um número: "))
contador = 0
for i in range(1, 11):
    contador = contador + 1
    multiplicação = n * contador
    print(f"{n} X {contador} = {multiplicação}")