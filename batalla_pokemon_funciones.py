import random

def ataque_malicioso(items_oponentes, diccionario_ataque):
    items_oponentes = items_oponentes[0], items_oponentes[1] - diccionario_ataque['malicioso'][1]
    return items_oponentes

def ataque_placaje(items_oponentes, diccionario_ataque):
    items_oponentes = items_oponentes[0] - diccionario_ataque['placaje'][1] * (100/items_oponentes[1]), items_oponentes[1]
    return items_oponentes

def ataque_ascuas(items_oponentes, diccionario_ataque):
    items_oponentes = items_oponentes[0] - diccionario_ataque['ascuas'][1], items_oponentes[1]
    return items_oponentes

def ataque_oponente(ataque_oponente, items_jugador, diccionario_ataque):
    if ataque_oponente == 1: #latigo
        items_jugador = items_jugador[0] - 10, items_jugador[1] - 10
        print("Tu enemigo ha usado latigo, tu vida y tu defensa han cambiado, ahora son:" + str(items_jugador))
        if items_jugador[1] <= 0:
            items_jugador = 1, 1
    elif ataque_oponente == 2: #placaje
        items_jugador = placaje(items_jugador, diccionario_ataque)
        print("Tu enemigo ha usado placaje, tu vida es ahora:" + str(items_jugador[0]))
    elif ataque_oponente == 3: #pistola de agua
        items_jugador = items_jugador[0] - 40, items_jugador[1]
        print("Tu enemigo ha usado pistola de agua, tu vida es ahora:" + str(items_jugador[0]))
    return items_jugador

items_jugador = 100, 100
items_oponentes = 100, 100

lista_ataque = ['malicioso', 'placaje', 'ascuas']
malicioso = (0, 10, 'malicioso')
placaje = (35, 0, 'placaje')
ascuas = (20, 0, 'ascuas')

diccionario_ataque = {
    'malicioso': ('baja defensa', 10),
    'placaje': ('baja vida oponente', 35),
    'ascuas': ('baja vida oponente', 20)
}

while items_jugador[0] > 0 and items_oponentes[0] > 0:
    print(diccionario_ataque)

    ataque_jugador = input('que ataque quieres ejecutar:')
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == 'malicioso':
        items_oponentes = ataque_malicioso(items_oponentes, diccionario_ataque)
        print("has bajado la defensa del oponente a " + str(items_oponentes[1]))
        if items_oponentes[1] <= 10:
            items_oponentes = 1, 1

    elif ataque_jugador == 'placaje':
        items_oponentes = ataque_placaje(items_oponentes, diccionario_ataque)
        print("has bajado la vida de tu oponente a " + str(items_oponentes[0]))

    elif ataque_jugador == 'ascuas':
        items_oponentes = ataque_ascuas(items_oponentes, diccionario_ataque)
        print("has bajado la vida de tu oponente a " + str(items_oponentes[0]))
        
    else:
        print('Que estas haciendo?! Tus ataques son malicioso, placaje y ascuas!')
        continue
    
    #Turno del oponente
    ataque_oponente = random.randrange(1,3+1)
    
    if ataque_oponente == 1: #latigo
        items_jugador == items_jugador[0] - 10, items_jugador[1] - 10
        print("Tu enemigo ha usado latigo, tu vida y tu defensa han cambiado, ahora son:" + str(items_jugador))
        if items_jugador[1] <= 0:
            items_jugador[1] = 1
            
    elif ataque_oponente == 2: #placaje
        items_jugador = items_jugador[0] - 35 * (100/items_jugador[1]), items_jugador[1]
        print("Tu enemigo ha usado placaje, tu vida es ahora:" + str(items_jugador[0]))
        
    elif ataque_oponente == 3: #pistola de agua
        items_jugador = items_jugador[0] - 40, items_jugador[1]
        print("Tu enemigo ha usado pistola de agua, tu vida es ahora:" + str(items_jugador[0]))
    #randrange esta garantizado entr 1 y 3
    
#Si termina el ciclo, alguien ha ganado
if items_oponentes[0] <= 0 and items_jugador[0] <=0:
    print('Empate')
elif items_oponentes[0] <= 0: #ya sabemos que el jugador es > 0
    print('Felicidades, has ganado')
else:
    print('Lo siento, has perdido')
