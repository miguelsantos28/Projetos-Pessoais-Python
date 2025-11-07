co = 0.35
bol = 0.35
riso = 0.35
kibe = 0.38
sal = 0.38
croquete = 0.38
pastel_c = 0.38
pastel_q = 0.38
pq = 0.8
pp = 0.8
ec = 0.75
ef = 0.75
ep = 0.75

v1 = int(input("Qual a quantidade de Coxinhas do Gap da semana ? "))
v2 = int(input("Qual a quantidade de Bolinhas do Gap da semana ? "))
v3 = int(input("Qual a quantidade de Risoles do Gap da semana ? "))
v4 = int(input("Qual a quantidade de Kibes do Gap da semana ? "))
v5 = int(input("Qual a quantidade de Croquetes do Gap da semana ? "))
v6 = int(input("Qual a quantidade de Pastel de carne do Gap da semana ? "))
v7 = int(input("Qual a quantidade de Pastel de queijo do Gap da semana ? "))
v8 = int(input("Qual a quantidade de Pizza de queijo do Gap da semana ? "))
v9 = int(input("Qual a quantidade de Pizza de P/Q do Gap da semana ? "))
v10 = int(input("Qual a quantidade de Esfirra de carne do Gap da semana ? "))
v11 = int(input("Qual a quantidade de Esfirra de frango do Gap da semana ? "))
v12 = int(input("Qual a quantidade de Enroladinho do Gap da semana ? "))

vco = v1 * co
vbo = v2 * bol
vriso = v3 * riso
vkibe = v4 * kibe
vcroq = v5 * croquete
vpcar = v6 * pastel_c
vpquei = v7 * pastel_q
vpq = v8 * pq
vpp = v9 * pp
vec = v10 * ec
vef = v11 * ef
vep = v12 * ep
total = vco + vbo + vriso + vkibe + vcroq + vpcar + vpquei + vpq + vpp + vec + vef + vep

print(f"O valor total do pedido do Gap da semana foi R${total}")

total = vco + vbo + vriso + vkibe + vcroq + vpcar + vpquei + vpq + vpp + vec + vef + vep

vm1 = int(input("Qual a quantidade de Coxinhas do 3 Marias da semana ? "))
vm2 = int(input("Qual a quantidade de Bolinhas do 3 Marias da semana ? "))
vm3 = int(input("Qual a quantidade de Kibe do 3 Marias da semana ? "))
vm4 = int(input("Qual a quantidade de Croquetes do 3 Marias da semana ? "))
vm5 = int(input("Qual a quantidade de Salsichas do 3 Marias da semana ? "))

vmco = vm1 * co
vmbol = vm2 * bol
vmki = vm3 * kibe
vmcroq = vm4 * croquete
vmsal = vm5 * sal

total3m = vmco + vmbol + vmki + vmcroq + vmsal

print(f"O valor total do pedido do 3 Marias da semana foi R${total3m}")

soma_total = total + total3m

print(f"O valor total da semana a receber é {soma_total}")