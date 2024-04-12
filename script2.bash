# Numero de ACL IPv4
aclNum = int(input("Ingrese N° de ACL :"))

# Tipo de ACL IPv4
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL IPv4 estandar.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL IPv4 extendida.")
else:
    print("Esto no es una ACL IPv4 estandar o extendida.")