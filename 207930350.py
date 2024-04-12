vlansw1 = [10, 20, 30]
navsw1 = [99]
vlansw2 = [40, 50, 60]
navsw2 = [200]

resp1 = int(input("Ingresar Vlan Nativa SW1:"))
if resp1 == 99:
    print("Las vlans son iguales y cumplen con el requerimiento")
else:
    print("Las vlans son diferentes y no cumplen con el requerimiento")

resp2 = input("Ingresar Vlans del SW1:")
resp2_list = list(map(int, resp2.split(',')))
if resp2_list == vlansw1:
    print("Las vlans son iguales y cumplen con el requerimiento")
else:
    print("Las vlans son diferentes y no cumplen con el requerimiento")

resp3 = int(input("Ingresar Vlan Nativa SW2:"))
if resp3 == 200:
    print("Las vlans son iguales y cumplen con el requerimiento")
else:
    print("Las vlans son diferentes y no cumplen con el requerimiento")

resp4 = input("Ingresar Vlans del SW2:")
resp4_list = list(map(int, resp4.split(',')))
if resp4_list == vlansw2:
    print("Las vlans son iguales y cumplen con el requerimiento")
else:
    print("Las vlans son diferentes y no cumplen con el requerimiento")
