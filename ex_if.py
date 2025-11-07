n1 = float(input("Digite  um  número: "))
n2 = float (input("Digite  outro  número: "))

if  n1  > n2:
    print(f"{n1:.2f} é > que {n2:.2f}!")
elif n1 == n2:
    print(f"{n1:.2f} é = a {n2:.2f}!")
else:
    print(f"{n2:.2f} é > que {n1:.2f}!")
