lista = []
for i in  range(5):
    n = float(input("Digite um número: "))
    lista.append(n)
print("\nOs números digitados foram: ", lista)
print("\nO maior número da lista é: ", max(lista))
print("\nO menor número da lista é: ", min(lista))
print("\nA soma dos números da lista é: ", sum(lista))
print("\nA média da lista é: ", sum(lista)/len(lista))