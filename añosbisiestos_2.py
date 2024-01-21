entrada = int(input('Ingrese el año:'))
                    
contador = 0

for i in range (1901, entrada+1):
    if(i % 4 == 0):
        contador += 1
    if(i % 100 != 0 and i % 400 == 0):
        contador += 1
    else:
        contador += 0
    
        
print (f'La cantidad de años bisiestos entre 1900 y {entrada} es {contador}')