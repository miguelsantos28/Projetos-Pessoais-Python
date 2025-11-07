juros = float(input("Digite a taxa de juros ao mês: \n"))
capital = float(input("Digite o capital: \n"))
periodo = int(input("Digite o período em meses: \n"))
contador = 0

for i in range (0, periodo):
    capital = capital + (capital * (juros/100))
    contador = contador + 1
    print(f"{contador}° mês = R${capital},00!")