#como en todos los lenguajes es recomendable crear una funcion principal en python la cual 
#va a correr primero  puede llamarse main o run
def palindromo(texto):
    #strip quita los espacios de una palabra inecesarios por eso en este caso se usa replace
    texto= texto.replace(' ','')
    print(texto)
    texto =texto.lower()
    textoInver=texto[::-1]
    if texto==textoInver:
        return True
    else:
        return False

def run():
    palabra= input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo== True:
        print('Es palindromo')
    else:
        print('No es palindromo')

#punto de entrada del programa entrypoint osea va a ser lo primero que va a corre como la clase pincipal
#en java con su respectivo main
if __name__ == '__main__':
    run()
