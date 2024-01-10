nombre = input ("introduce tu nombre")
print("Hola, " + nombre + " Cómo estás??")

pregunta = input ("Alguna vez haz hecho arepas??")
print("Que bueno!! pues hoy vamos a hacer Arepas!!")

pregunta2 = int(input("Para cuantas personas quieres hacer arepas?? (indicar solo el número)"))

#lo que quiero conseguir es que la respuesta de pregunta2 se utilice en las operaciones

agua = (1 / 8 * pregunta2)
print("necesitarías " + str(agua) + " tazas de agua")

harina = (1 / 8 * pregunta2)
print("necesitarías " + str(harina) + " tazas de harina")

sal1 = (1 / 3 / 16 / 8 * pregunta2)
print("necesitarías " + str(sal1) + " tazas de sal")

sal2 = (1 / 8 * pregunta2)
print("o  " + str(sal2) + " cucharaditas de sal")

aceite1 = (1 / 16 / 8 * pregunta2)
print("necesitarías " + str(aceite1) + " tazas de aceite")

aceite2 = (1 / 8 * pregunta2)
print("o " + str(aceite2) + " cucharadas de aceite")

bol = agua + harina + sal1

#Lo que toca acá es mucha explicación, no hacen falta más preguntas

print("""En un bol añade el agua, la harina y la sal
    Resultando una masa de aproximadamente """ + str(bol) + " tazas.")

print("Luego empieza a formar unos discos de aproximadamente 10 cm de diámetro (por cada taza de harina se hacen 8 arepas)")

budare = aceite1
print("Esparce el aceite en el budare y coloca los discos que hiciste anteriormente")

print("Dejalas dorar 10 minutos por cada lado y luego retire y coloque en un plato con los rellenos de su elección.")

print("FELICIDADES!!! " + nombre + " has aprendido a hacer AREPAS!!!" )