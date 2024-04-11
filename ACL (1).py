# Definir un diccionario que mapee los rangos de números de ACL a sus tipos
tipos_acl = {
    range(1, 100): "Estándar",
    range(100, 200): "Extendida"
}

while True:
    # Solicitar al usuario que ingrese el número de ACL IPv4
    numero_acl = input("Ingrese el número de ACL IPv4 (o 'salir' para terminar): ")

    if numero_acl.lower() == "salir":
        print("¡Adiós!")
        break

    # Verificar si el número corresponde a una ACL Estándar, Extendida, o está fuera del rango
    if numero_acl.isdigit():
        numero_acl = int(numero_acl)
        tipo_acl = None
        for rango, tipo in tipos_acl.items():
            if numero_acl in rango:
                tipo_acl = tipo
                break
        if tipo_acl:
            print("La ACL", numero_acl, "es una ACL", tipo_acl + ".")
        else:
            print("El número de ACL está fuera del rango de ACL.")
    else:
        print("El número de ACL no es válido.")

