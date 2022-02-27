from pickletools import OpcodeInfo


def run():
    print("""
    Bienvenido al juego del ahorcado 
    Trata de adivinar la palabra Que el Deev ingreso en el Programa""")
    palbra_secreta='HOLA MUNDO'
    menu = """Solo tienes tres oportunidades para divininar la palabra
    1.- Ingresa una letra
    2.- Ingrea la palabra
    3.- Exit
    """
    drawingX="""
                                     STRIKES

                                  ____ ____ ____

                                ADIVINA LA PALBRA
                  
                  1:___ 2:___ 3:___ 4:___   5:___ 6:___ 7:___ 8:___ 9:___
    """
    strikes='____'
    strikes2='X'
    op=int(input(menu))
    letraInput=''
    while True:
        if op==3:
            break
        elif op==1:
            letraInput=int(input('Ingrese una Palabra: '))
            if letraInput in palbra_secreta:
                pass


        op=int(input(menu))




    # print(len(drawingX))
    # drawingX=drawingX.replace(strikes+' '+strikes+' '+strikes, 'X  '+strikes+' '+strikes)
    # print(drawingX)


if __name__ == '__main__':
    run()