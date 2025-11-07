nota = float(input("Digite a nota do aluno: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota inválida, digite novamente: "))
if nota >= 6:
    print("Aluno aprovado!")
elif nota >= 4:
    print("Aluno de recuperação!")
else:
    print("Aluno reprovado!")