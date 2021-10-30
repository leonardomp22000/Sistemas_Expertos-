# Leonardo Josbad Meza Pantoja

# Sistema Experto "Vida Moderna"

# Variable para seleccionar opciones
opcion = 0

# Variables 'hd' hace referencia a enfermedades heredadas
obesidad_hd = 0
hipertencion_hd = 0
colesterol_hd = 0
accidente_cere_hd = 0
diabetes_hd = 0
cancer_hd = 0
trigliceridos_hd = 0




porcentaje = 0
# Variables de habitos
fumar = 0
sedentario_ejercicio = 0
sedentario_sentado = 0
sueno = 0
no_comer = 0
grasas_azucares = 0
alcohol = 0
no_agua = 0



print("Bienvenido al sistema experto de 'Vida Moderna'")
input()
print("Instrucciones:"
      "Conteste lo mas honestamente a lo expuesto, para que el sistema le diga si es \n"
      "propenso a tener problemas leves, graves o moderados, dependiendo de sus habitos diarios \n "
      "")

edad = int(input("Ingrese su edad: "))

estatura = float(input("Ingrese su estatura en metros: "))

peso = float(input("Ingrese su peso: "))

IMC = peso / estatura**2

print("{0:.2f}".format(IMC))

if IMC < 18.25:
    print("Estas bajo de peso")

elif 18.5 < IMC < 24.9:
    print("Estas en tu peso normal")

elif 25 < IMC < 29.9:
    print("Estas en sobrepeso")

elif IMC > 30:
    print("Estas en sobrepeso")

# Cuestonario inicial para ver probabilidades de heredar una enfermedad

opcion = input("¿Alguno de tus padres o abuelos tienen obesidad? (Responde con 'si' o 'no')")
if opcion == 'Si' or opcion == 'si':

    obesidad_hd = 0
    print(obesidad_hd)

else:
    obesidad_hd = 1
    print(obesidad_hd)

opcion = input("¿Alguno de tus papas o abuelos tiene hipertencion? (Responde con 'si' o 'no')")
if opcion == 'Si' or opcion == 'si':
    hipertencion_hd = 0
    print(hipertencion_hd)


else:
    hipertencion_hd = 1
    print(hipertencion_hd)

opcion = input("¿Alguno de tus papas o abuelos es propenso a tener el colesterol alto? (Responde con 'si' o 'no')")
if opcion == 'Si' or opcion == 'si':
    colesterol_hd = 0
    print(colesterol_hd)
else:
    colesterol_hd = 1
    print(colesterol_hd)


opcion = input("¿Alguno de tus papas o abuelos sufrio algun accidente cerebrobascular? (Responde con 'si' o 'no')")
if opcion == 'Si' or opcion == 'si':
    accidente_cere_hd = 0
    print(accidente_cere_hd)
else:
    accidente_cere_hd = 1
    print(accidente_cere_hd)


opcion = input("¿Alguno de tus papas o abuelos tiene diabetes tipo 2? (Responde con 'si' o 'no')")
if opcion == 'Si' or opcion == 'si':
    diabetes_hd = 0
    print(diabetes_hd)
else:
    diabetes_hd = 1
    print(diabetes_hd)

opcion = input("¿Alguno de tus papas o abuelos parecio cancer? (Responde con 'si' o 'no')")
if opcion == "Si" or opcion == 'si':
    cancer_hd = 0
    print(cancer_hd)

else:
    cancer_hd = 1
    print(cancer_hd)

opcion = input("¿Alguno de sus padres o abuelos padece de trigliceridos altos? (Responde con 'si' o 'no')")
if opcion == "Si" or opcion == 'si':
    trigliceridos_hd = 0
    print(trigliceridos_hd)

else:
    trigliceridos_hd = 1
    print(trigliceridos_hd)






input("Muy bien hecho, ya casi terminamos.\n"
      "Las preguntas de su informacion hereditaria han sido guardadas correctamente\n"
      "A continuacion responda las preguntas segun sus habitos diarios para determinar el porcentaje a desarrollar \n"
      "alguna enfermedad relacionada con estos habitos\n")

opcion = input("¿Usted fuma cigarros, puros, pipas, cigarro electronico etc? (Responda con 'Si' o 'No')")
if opcion == 'Si' or opcion == 'si':
    opcion = input("¿Cuantos cigarros al dia?\n"
                   "A) 5 o menos cigarrillos al dia\n"
                   "B) 5 o mas cigarrilos al dia\n")
    fumar = 0
    print(fumar)
else:
    fumar = 1
    print(fumar)

opcion = input("Haces ejercicio? (Respone con 'Si' o 'No')")
if opcion == 'Si' or opcion == 'si':
    opcion = input("¿Cuanto tiempo al dia?\n"
                   "A) 10-15 minutos\n"
                   "B) 15-30 minutos\n"
                   "C) 30-60 minutos\n")
    if opcion == 'A' or opcion == 'a':
        sedentario_ejercicio = 0
        print(sedentario_ejercicio)
    elif opcion == 'B' or opcion == 'b':
        sedentario_ejercicio = 1
        print(sedentario_ejercicio)
    elif opcion == 'C' or opcion == 'c':
        sedentario_ejercicio = 1
        print(sedentario_ejercicio)

else:
    sedentario_ejercicio = 0
    print(sedentario_ejercicio)

opcion = input("¿Cuantas horas pasas sentado al dia? Ya sea por trabajo o por entretenimiento\n"
               "A) 1-2 horas\n"
               "B) 3-5 horas\n"
               "C) 5-8 horas\n"
               "D) 8 o mas\n")
if opcion == 'A' or opcion == 'a':
    sedentario_sentado = 1
    print(sedentario_sentado)
elif opcion == 'B' or opcion == 'b':
    sedentario_sentado = 1
    print(sedentario_sentado)
elif opcion == 'C' or opcion == 'c':
    sedentario_sentado = 0
    print(sedentario_sentado)
elif opcion == 'D' or opcion == 'd':
    sedentario_sentado = 0
    print(sedentario_sentado)


opcion = input("¿Cuantas duerme en promedio todos los dias?\n"
               "A) 8-10 horas\n"
               "B) 7-8 horas\n"
               "C) 6-7 horas\n"
               "D) 6 o menos\n")
if opcion == 'A' or opcion == 'a':
    sueno = 1
    print(sueno)
elif opcion == 'B' or opcion == 'b':
    sueno = 1
    print(sueno)
elif opcion == 'C' or opcion == 'c':
    sueno = 1
    print(sueno)
elif opcion == 'D' or opcion == 'd':
    sueno = 0
    print(sueno)


opcion = input("¿Que tan frecuente es que omita comidas en una semana?\n"
               "A) 4 dias o mas\n"
               "B) 3 dias\n"
               "C) 2 dias\n"
               "D) 1 o ninguno\n")

if opcion == 'A' or opcion == 'a':
    no_comer = 0
    print(no_comer)
elif opcion == 'B' or opcion == 'b':
    no_comer = 0
    print(no_comer)
elif opcion == 'C' or opcion == 'c':
    no_comer = 1
    print(no_comer)
elif opcion == 'D' or opcion == 'd':
    no_comer = 1
    print(no_comer)

opcion = input("¿Que tan frecuente es su consumo de grasas y azucares por semana en alimentos como: carnitas,\n"
               "chicharronesFrappes, Hamburguesas, Hot-dogs, y comida chatarra en general?\n"
               "A) 3 Dias o mas\n"
               "B) 2 Dias\n"
               "C) 1 o ninguno\n")
if opcion == 'A' or opcion == 'a':
    grasas_azucares = 0
    print(grasas_azucares)
elif opcion == 'B' or opcion == 'b':
    grasas_azucares = 0
    print(grasas_azucares)
elif opcion == 'C' or opcion == 'C':
    grasas_azucares = 1
    print(grasas_azucares)

opcion = input("¿Consume bebidas alcoholicas?(Responda con 'Si' o 'No')")
if opcion == 'Si' or opcion == 'No':
    opcion = input(" Que tan frecuente es su consumo de bebidas alcoholicas a la semana?\n"
                   "A) Ocasionalmente (Solo situaciones muy selectas, pocas veces al año)\n"
                   "B) 1-2 veces por semana\n"
                   "C) 4 o mas veces por semana\n")
    if opcion == 'A' or opcion == 'a':
        alcohol = 1
        print(alcohol)
    elif opcion == 'B' or opcion == 'b':
        alcohol = 0
        print(alcohol)
        print(alcohol)
    elif opcion == 'C' or opcion == 'c':
        alcohol = 0

opcion = input("¿Cuantos litros de agua en promedio tomas al dia?\n"
               "A) Entre 0.5 y 1 litro\n"
               "B) Entre 1 y 1.5 litros\n"
               "C) Entre 1.5 y 2 litros\n"
               "D) Entre 2 y 3 litros\n")

if opcion == 'A' or opcion == 'a':
    no_agua = 0
    print(no_agua)
elif opcion == 'B' or opcion == 'b':
    no_agua = 0
    print(no_agua)
elif opcion == 'C' or opcion == 'c':
    no_agua = 1
    print(no_agua)
elif opcion == 'D' or opcion == 'd':
    no_agua = 1
    print(no_agua)







# Motor de explicacion


total = 1
explicacion_obesidad_hd ="Eres propenso a tener sobrepeso por tu predisposición genética. De acuerdo con un reciente\n" \
                         "estudio realizado por la Universidad de Sussex, en Reino Unido, alrededor del 40% del Índice\n" \
                         "de Masa Corporal (IMC) se hereda de los padres. Si a ello se le suma el ambiente familiar que\n" \
                         "se forma por los hábitos de los padres, la influencia puede llegar a 60%.\n"

explicacion_hipertension_hd = "Eres propenso a sufir hipertensión de manera hereditaria. Múltiples estudios\n" \
                              "epidemiológicos sugieren que el aporte de los genes (en la variabilidad de la\n" \
                              "presión arterial) es aproximadamente un 30%. Un paciente con antecedentes familiares\n" \
                              "de hipertensión tiene más riesgo de presentar la enfermedad.\n "

explicacion_colesterol_hd = "Eres propenso a tener el colesterol alto debido a factores hereditarios. Es una enfermedad\n" \
                            "que se hereda de generación en generación, con un 50% de probabilidad de que los familiares\n" \
                            "de un individuo afectado nazcan con hipercolesterolemia familiar.\n"

explicacion_acc_cere = "Eres propenso a tener un accidente cerebrovascular debido a factores hereditarios. Al igual que\n" \
                       "muchas enfermedades, el riesgo de accidente cerebrovascular puede resultar afectado por factores\n" \
                       "tanto hereditarios como ambientales. Un ejemplo de un riesgo heredado son los antecedentes\n" \
                       "familiares de accidente cerebrovascular.\n"

explicacion_diabetes = "Tienes predisposición a presentar en un futuro diabetes tipo 2, pero solo es una predisposición,\n" \
                       "no quiere decir que necesariamente la presentes. Dicha enfermedad es causada por malos hábitos,\n" \
                       "por lo cual la mejor opción sera comer saludable y mantener una vida activa.\n"

explicacion_cancer_hd = "Tienes riesgo de presentar en un futuro algún tipo de cáncer. Entre un 5 y un 10% de los cánceres\n" \
                        "tienen un carácter familiar o hereditario. En realidad, lo que ocurre es que se transmite de padres\n" \
                        "a hijos una mutación genética concreta que confiere la susceptibilidad de padecer un tipo concreto\n" \
                        "de cáncer, lo que no implica la seguridad de que este hecho se vaya a producir.\n"

explicacion_trigliceridos_hd = "Tienes riesgo de presentar triglicéridos, o ya puedes haber tenido un indicio de que\n" \
                               "eres propenso a tener esta afección. Es una enfermedad que se hereda de generación en\n" \
                               "generación, con un 50% de probabilidad de que los familiares de un individuo afectado\n" \
                               "nazcan con hipercolesterolemia\n"


explicacion_alcohol = "El alcohol tiene  consecuencias directas que contribuyen a la disfuncion erectil en el hombre o \n" \
                      "a la infertilidad en la mujer\n"
explicacion_fumar = "Fumer tiene consecuencias directas en la disfuncion erectil\n"

explicacion_sedentarismo = "El sedentarismo es un estilo de vida que se caracteriza por la inactividad física o la falta\n " \
                           "de ejercicio. Cuando una persona pasa la mayor parte del día sentado sin realizar actividad \n" \
                           "física, es considerada sedentaria. Esta condición puede generar problemas significativos para \n" \
                           "la salud, ya que es un factor de riesgo para padecer enfermedades al corazón. Las probabilidades\n " \
                           "de sufrir un infarto cardiaco, tener enfermedades coronarias o sufrir de hipertensión aumentan\n" \
                           "cuando las personas son sedentarias. Además, la inactividad o la falta de ejercicio, provoca\n" \
                           "que los niveles de colesterol malo aumenten, pudiendo provocar obesidad, sobrepeso\n" \
                           "y enfermedades metabólicas.\n"



explicacion_desvelos = "Más allá de la somnolencia, la falta de sueño causa estragos en el cerebro, que afectan el estado\n" \
                       "de ánimo y empeoran la depresión, exacerban el dolor y socavan las funciones ejecutivas que afectan\n" \
                       "el juicio, la planificación, la organización, la concentración, la memoria y el rendimiento.\n" \
                       "Las hormonas que influyen en el peso y el crecimiento se desequilibran.Se afecta el sistema\n" \
                       "inmunológico, y esto nos hace más susceptibles a las enfermedades y se desarrolla una tendencia\n" \
                       "a las inflamaciones.\n"



explicacion_no_comer = "Hay una cosa que es simple: si te saltas las comidas, junto con la restricción de calorías\n" \
                       "tendrás antojos, y cuando caes ante esas tentaciones se produce un alza de azúcar en la sangre,\n" \
                       " ¿sus consecuencias? Tu cuerpo crea una elevada cantidad de triglicéridos, que a su vez, se\n" \
                       " convierten en acumulación de grasa, a su vez el glucógeno pobre provoca bajos niveles de\n" \
                       " energía porque el azúcar en la sangre no está siendo reemplazada. El resultado de esto es\n" \
                       " que el peso que se pierde es principalmente agua y músculo\n"

explicacion_azucar_grasa = "El exceso de sal, azúcar y grasas puede desatar enfermedades como la diabetes, el sobrepeso\n" \
                           "y la hipertensión.\n"

explicacion_no_agua = "No beber agua puede causar fatiga, una disminución de la función cognitiva, alteraciones en el \n" \
                      "estado de ánimo, una caída en la presión arterial y en la humedad de la piel... Un cerebro \n" \
                      "deshidratado se contrae -literalmente- ante la falta de agua, ya que requiere de un esfuerzo \n " \
                      "extremo para funcionar. Si la deshidratación se prolonga durante varios días, el organismo\n" \
                      " experimenta secuelas más graves y eventualmente la muerte.\n "


# Bronquitis y enfisema pulmonar y degeneracion de la retina

if fumar == 0:
    print("*********************************************************************************************************\n")
    print("BRONQUITIS, ENFISEMA PULMONAR Y DEGENERACION DE LA RETINA\n")

    print("Tienes un 100% de probabilidad de desarrollar Bronquitis y enfisema pulmonar, ademas de degeneracion de la retina \n"
          "ya que dichas enfermedades es una consecuencia directa de fumar. Segun estudios fumar 1 cigarrillo al dia \n"
          "o muchos no hace ninguna diferencia, por lo que se recomienda dejar de fumar para evitar estas enfermedades \n"
          "a largo plazo ")
    print(explicacion_fumar)
    print("*********************************************************************************************************\n")



# Disfuncion erectil y algunos tipos de cancer

variables_disf_cancer = [fumar, alcohol]
print("*************************************************************************************************************\n")
print("DISFUNCION ERECTIL Y ALGUNOS TIPOS DE CANCER\n")

for elemento in variables_disf_cancer:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 2
    if elemento == fumar and elemento == 0:
        print(explicacion_fumar)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
if porcentaje == 0:
    porcentaje = 1
porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar  disfuncion erectil y de presentar algun tipo de cancer es de {porcentaje_final} ")

print("**************************************************************************************************************\n")



# Obesidad

variables_obesidad = [sedentario_sentado, no_agua, grasas_azucares, no_comer ]
print("*************************************************************************************************************\n")
print("OBESIDAD\n")

for elemento in variables_obesidad:
    if elemento == 0:

        porcentaje = porcentaje + 1
        total = 4
    if elemento == sedentario_sentado and elemento == 0:
        print(explicacion_sedentarismo)
    if elemento == no_agua and elemento == 0:
        print(explicacion_no_agua)
    if elemento == grasas_azucares and elemento == 0:
        print(grasas_azucares)
    if elemento == no_comer and elemento == 0:
        print(explicacion_no_comer)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar  obesidad es de {porcentaje_final} ")

print("*************************************************************************************************************\n")


# Colesterol alto

variables_colesterol = [fumar, no_agua, alcohol, sedentario_sentado]
print("*************************************************************************************************************\n")
print("COLESTEROL ELEVADO\n")
for elemento in variables_colesterol:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 4
    if elemento == fumar and elemento == 0:
        print(explicacion_fumar)
    if elemento == no_agua and elemento == 0:
        print(explicacion_no_agua)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
    if elemento == sedentario_sentado and elemento == 0:
        print(explicacion_sedentarismo)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar colesterol alto es de {porcentaje_final} ")
print("*************************************************************************************************************\n")




# Problemas de la piel

variables_problemas_piel = [sueno,no_agua,fumar]
print("**************************************************************************************************************\n")
print("PROBLEMAS DE LA PIEL\n")
for elemento in variables_problemas_piel:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 3
    if elemento == sueno and elemento == 0:
        print(explicacion_desvelos)
    if elemento == no_agua and elemento == 0:
        print(explicacion_no_agua)
    if elemento == fumar and elemento == 0:
        print(explicacion_fumar)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar problemas en la piel es de {porcentaje_final} ")

print("*************************************************************************************************************\n")


# Propenso a infarto

variables_infarto = [sedentario_sentado, alcohol, grasas_azucares]
print("**************************************************************************************************************\n")
print("PROPENSO A INFARTO\n")

for elemento in variables_infarto:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 3
    if elemento == sedentario_sentado and elemento == 0:
        print(explicacion_sedentarismo)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
    if elemento == grasas_azucares and elemento == 0:
        print(explicacion_azucar_grasa)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar un infarto es de {porcentaje_final} ")

print("**************************************************************************************************************\n")

# Problemas de aprendizaje

variables_problemas_aprendizaje = [sueno,no_agua, alcohol ]
print("**************************************************************************************************************\n")
print("PROBLEMAS DE APRENDIZAJE Y MEMORIA\n")

for elemento in variables_problemas_aprendizaje:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 3
    if elemento == sueno and elemento == 0:
        print(explicacion_desvelos)
    if elemento == no_agua and elemento == 0:
        print(explicacion_no_agua)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar problemas de aprendizaje es de: {porcentaje_final} ")

print("**************************************************************************************************************\n")

#Enfermedades neurodegenerativas

variables_neurodegenerativa = [sueno, no_comer]
print("**************************************************************************************************************\n")
print("ENFERMEDADES NEURODEGENERATIVAS\n")
for elemento in variables_neurodegenerativa:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 2
    if elemento == sueno and elemento == 0:
        print(explicacion_desvelos)
    if elemento == no_comer and elemento == 0:
        print(explicacion_no_comer)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de ser propenso a enfermedades neurodegenerativas es de: {porcentaje_final} ")

print("**************************************************************************************************************\n")


# Osteoporosis
print("**************************************************************************************************************\n")
print("OSTEOPOROSIS\n")
if sedentario_sentado == 0:
    print(sedentario_sentado)
    print("La probabilidad de presentar Osteoporosis es muy alta")
print("**************************************************************************************************************\n")


# Depresion o ansiedad
variables_depresion = [sedentario_sentado, alcohol, sueno]
print("**************************************************************************************************************\n")
print("DEPRESION O ANSIEDAD\n")
for elemento in variables_depresion:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 3
    if elemento == sedentario_sentado and elemento == 0:
        print(explicacion_sedentarismo)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
    if elemento == sueno and elemento == 0:
        print(explicacion_desvelos)

porcentaje_final = (porcentaje * 100) / total
print(
    f"El porcentaje que se tiene de presenar Sentimiento de ansiedad es de: {porcentaje_final} ")
print("**************************************************************************************************************\n")

# Hipertension

print("HIPERTENSION\n")

variables_hipertension = [sedentario_sentado, alcohol, sueno]
print("**************************************************************************************************************\n")

for elemento in variables_hipertension:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 3
    if elemento == sedentario_sentado and elemento == 0:
        print(explicacion_sedentarismo)
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
    if elemento == sueno and elemento == 0:
        print(explicacion_desvelos)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar hipertension es de {porcentaje_final} ")
print("**************************************************************************************************************\n")


# Diabetes
porcentaje = 0
variables_diabetes = [fumar, alcohol, no_agua, grasas_azucares, no_comer, sueno, sedentario_sentado]
print("**************************************************************************************************************\n")
print("DIABETES\n")
for elemento in range(len(variables_diabetes)):
    if elemento in variables_diabetes:

        if elemento == 0:
            porcentaje = porcentaje + 1
            total = 7
            print(elemento+1)
        if elemento == fumar and elemento == 0:
            print(explicacion_fumar)
        if elemento == alcohol and elemento == 0:
            print(explicacion_alcohol)
        if elemento == no_agua and elemento == 0:
            print(explicacion_no_agua)
        if elemento == grasas_azucares and elemento == 0:
            print(explicacion_azucar_grasa)
        if elemento == no_comer and elemento == 0:
            print(explicacion_no_comer)
        if elemento == sueno and elemento == 0:
            print(explicacion_desvelos)
        if elemento == sedentario_sentado and elemento == 0:
            print(explicacion_sedentarismo)


print(porcentaje)
porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar diabetes es de {porcentaje_final} ")
print("**************************************************************************************************************\n")


# Aumento de trigliceridos y caries

print("**************************************************************************************************************\n")
print("AUMENTO DE TRIGLICERIDOS Y CARIES\n")
if grasas_azucares == 0:
    print(explicacion_azucar_grasa)
    print("El porcentaje que usted tiene de presentar trigliceridos altos es muy elevado, al igual que presentar caries\n"
          " Estos efectos se pueden contrarrestar bajando el consumo de grasas y azucares y haciendo ejercicio  diariamente\n")

print("**************************************************************************************************************\n")


# Accidente cerebrovascular
print("**************************************************************************************************************\n")
print("ACCIDENTE CEREBROVASCULAR\n")

if sedentario_sentado == 0:
    print(explicacion_sedentarismo)
    print("El porcentaje que usted tiene de presentar un accidente cerebrovascular es muy alto, esto solo se puede\n"
          "siendo una persona mas activa, haciendo ejercicio")

print("**************************************************************************************************************\n")

# Cirrosis, Pelagra, gota
print("**************************************************************************************************************\n")
print("CIRROSIS, PELAGRA Y GOTA\n")

if alcohol == 0:
    print(explicacion_alcohol)
    print("La probabilidad de que usted desarrolle Cirrosis, pelagra o gota, es muy elevada, yaque el consumo excesivo\n"
          " de alcohol tiene consecuencias directas con estas enfermedades")

print("**************************************************************************************************************\n")

#Gastritis
variables_gastritis = [alcohol, no_comer]
print("**************************************************************************************************************\n")
print("GASTRITIS\n")

for elemento in variables_disf_cancer:
    if elemento == 0:
        porcentaje = porcentaje + 1
        total = 2
    if elemento == alcohol and elemento == 0:
        print(explicacion_alcohol)
    if elemento == no_comer and elemento == 0:
        print(explicacion_no_comer)

porcentaje_final = (porcentaje * 100)/total
print(f"El porcentaje que se tiene de presenar  gastritis es de {porcentaje_final} ")

print("**************************************************************************************************************\n")

'''

# Entre mas puntos acumulen las variables quiere decir que son mas sanos

ejercicio = input("¿Haces ejercicio? (Conteste con un 'si' o un 'no'): ")
if ejercicio == 'si':
    print("Sumar 1 punto")

    puntos_ejercicio = puntos_ejercicio +1
    print(puntos_ejercicio)

    print(ejercicio)

    bandera_ejercicio = True

else:
    print("No se añaden puntos ")


Horas_sentado = input("Seleccione de los siguientes rangos las horas que pasa sentado al dia en diversas actividadaes,"
                      "Como por ejemplo: Ver TV, trabajar, o cualquier actividad recreativa : \n"
                      "A) 0-6 \n"
                      "B) 6-10\n"
                      "C) 10 o mas\n"
                      "A continuacion escriba su respuesta (Solo la letra): ")

if (Horas_sentado == 'A' or Horas_sentado == 'a'):
    print("Las horas sentadas son aceptables")
    puntos_ejercicio = puntos_ejercicio + 2
    print(puntos_ejercicio)

elif(Horas_sentado == 'B' or Horas_sentado == 'b'):
    print("Las horas sentado son moderadas")
    puntos_ejercicio = puntos_ejercicio + 1
    print(puntos_ejercicio)

elif(Horas_sentado == 'C' or Horas_sentado == 'c'):
    print("Posible problema cardiovascular")
    puntos_ejercicio = puntos_ejercicio + 0
    print(puntos_ejercicio)


if (Horas_sentado == 'A' or Horas_sentado == 'a'):
    print("No hacer nada")

'''
















