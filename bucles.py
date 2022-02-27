# import string
# resultado=0
# c=0
# for i in range (0,1000000,1):
#     potencia=2**c
#     if i==potencia:
#         print("2**"+str(c)+"= "+str(i))
#         c=c+1
    
#     #print(i)
#     #print(potencia)
#ciclo while

def run():
    #LAS CONTANTES SE DEFINEN COMO MAYUSCULAS
    LIMITE =1000000
    contador=0
    potencia_2=2**contador
    while potencia_2<LIMITE:
        print('2 elevado a '+ str(contador)+ ' es igual a: '+ str(potencia_2))
        contador=contador+1
        potencia_2=2**contador

if __name__ == '__main__':
    run()
    


