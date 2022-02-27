def conversor(tipo_peso,valor_dolar):
    pesosMxn = input("¿Cuantos pesos "+tipo_peso+ " tienes ?")
    pesosMxn = float(pesosMxn)
    # Declaracion de valores
    dolares = pesosMxn/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+dolares + " Dolares")
# Input del usuario
menu = """
Bienvenido al Conversor de monedas😛
1- Pesos Colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

Elige una Opcion:"""

opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos",3875)
elif opcion == 2:
    conversor("Mexicanos",20)

elif opcion == 3:
    conversor("Argentinos",65)
else:
    print('Ingrese Una opcion correcta')