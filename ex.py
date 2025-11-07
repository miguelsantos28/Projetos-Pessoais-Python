RADAR_1 = 60
LOCAL_1 = 100
ALCANCE_1 = 1

RADAR_2 = 80
LOCAL_2 = 180
ALCANCE_2 = 1

RADAR_3 = 40
LOCAL_3 = 230
ALCANCE_3 = 1

while True:
    vel_carro = input("Digite a velocidade atual do carro: ")
    local_carro = input("Digite (em km) o local onde o carro se encontra: ")

    try:
        vel_carro_int = int(vel_carro)
        local_carro_int = int(local_carro)
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    multa_1 = vel_carro_int > RADAR_1 and local_carro_int >= (LOCAL_1 - ALCANCE_1) and local_carro_int <= (LOCAL_1 + ALCANCE_1)
    multa_2 = vel_carro_int > RADAR_2 and local_carro_int >= (LOCAL_2 - ALCANCE_2) and local_carro_int <= (LOCAL_2 + ALCANCE_2)
    multa_3 = vel_carro_int > RADAR_3 and local_carro_int >= (LOCAL_3 - ALCANCE_3) and local_carro_int <= (LOCAL_3 + ALCANCE_3)

    if multa_1:
        print("O carro foi multado em radar 1")
    else: 
        print("O carro não foi multado em radar 1")
    if multa_2:
        print("O carro foi multado em radar 2")
    else: 
        print("O carro não foi multado em radar 2")
    if multa_3:
        print("O carro foi multado em radar 3")
    else: 
        print("O carro não foi multado em radar 3")

    decisao = input("Deseja continuar? (sim/não)").lower()
    print("-" * 40)
    if "n" in decisao:
        break