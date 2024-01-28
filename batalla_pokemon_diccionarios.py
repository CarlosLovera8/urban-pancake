import random

ps_jugador = 100
ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

lista_ataque = ['malicioso', 'placaje', 'ascuas'] 
fuerza_ataque = ['-10 en defensa', '-35 en vida del oponente', '-20 en vida del oponente']
diccionario_ataque = {'malicioso': '-10 en defensa', 'placaje': '-35 en vida del oponente', 'ascuas': '-20 en vida del oponente'}

while ps_jugador > 0 and ps_oponente > 0:
    
    for lista_ataque, fuerza_ataque in diccionario_ataque.items():
        print('El ataque {} tiene un efecto de {}.'.format(lista_ataque, fuerza_ataque))
        
    ataque_jugador = input('que ataque quieres ejecutar:')
    ataque_jugador == ataque_jugador.lower()
    
    if ataque_jugador == 'malicioso':
        defensa_oponente -= 10
        print("has bajado la defensa del oponente a " + str(defensa_oponente))
        if defensa_oponente <= 10:
            defensa_oponente = 1
            
    elif ataque_jugador == 'placaje':
        ps_oponente -= 35 / (defensa_oponente/100) #Tambien se puede poner como: 35 * (100/defensa_oponente)
        print("has bajado la vida de tu oponente a " + str(ps_oponente))
        
    elif ataque_jugador == 'ascuas':
        ps_oponente -= 20
        print("has bajado la vida de tu oponente a " + str(ps_oponente))
        
    else:
        print('Que estas haciendo?! Tus ataques son malicioso, placaje y ascuas!')
        continue
    
    #Turno del oponente
    ataque_oponente = random.randrange(1,3+1)
    
    if ataque_oponente == 1: #latigo
        defensa_jugador == defensa_jugador - 10
        print("Tu enemigo ha usado latigo, tu defensa es ahora:" + str(defensa_jugador))
        
        if defensa_jugador <= 0:
            defensa_jugador = 1
            
    elif ataque_oponente == 2: #placaje
        ps_jugador -= 35 * (100/defensa_jugador)
        print("Tu enemigo ha usado placaje, tu vida es ahora:" + str(ps_jugador))
        
    elif ataque_oponente == 3: #pistola de agua
        ps_jugador -= 40
        print("Tu enemigo ha usado pistola de agua, tu vida es ahora:" + str(ps_jugador))
    #randrange esta garantizado entr 1 y 3
    
#Si termina el ciclo, alguien ha ganado
if ps_oponente <= 0 and ps_jugador <=0:
    print('Empate')
elif ps_oponente <= 0: #ya sabemos que el jugador es > 0
    print('Felicidades, has ganado')
else:
    print('Lo siento, has perdido')