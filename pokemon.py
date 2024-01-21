x = input("Eres chico o chica?").lower() 
w="Bienvenid"
if x == "chico":
    w += 'o'
else: 
    w += 'a'
print(w, "al mundo de los pokemon!")
y = input("Que edad tienes?")
if int(y)<10:
    if x == "chico":
        print("No tienes edad",
              "para ser entrenador")
    else:
        print("No tienes edad",
              "para ser entrenadora")
        quit()
else:
    print("Vamos!!")
