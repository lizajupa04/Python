# ----------------------------------
# -- Variables -- #
# ----------------------------------



# ----------------------------------
# -- Strings-- #
# ----------------------------------

variable_10 = "Hola" # Strings comillas dobles
variable_11 = 'Hola mundo' # Strings comillas simples
print(variable_10)
print(variable_11)

# -- Indexacion -- #
variable_12 = "Alejandro"
print(variable_12[2]) # Toma la letra en la posicion 2. Y empieza desde 0

variable_13 = "Alejandro"
print(variable_13[-2]) # Toma la letra en la posicion al reves. No empieza en 0

# -- Slicing -- #
# Extrae una cadena de caracteres del string. Toma un rango [m:n]

variable_14 = "Santiago Hernandez" 
print(variable_14[0:3]) # Caracteres positivos
print(variable_14[-9:-3]) # Caracteres negativos. El numero inicial es de atras para adelante
print(variable_14[5:]) # Se deja en blanco para que tome el caracter inicial
print (variable_14[-9:]) # Se deja en blanco para que tome todo

# -- Stride -- #
# Forma de indexar un String. Usamos : y agregamos un tercer indice para tomar los saltos

print(variable_14[0:8:2]) # Esto resulta como Snig. Porque toma los primeros 8 y salta cada 2
print(variable_14[:8:1]) # Indicamos que lea desde el principio con salto de 1

# Tambien se puede con indices negativos


# -- Strings de multiples lineas -- #
# Son aquellos que tienen varios saltos de linea usando \n o usando """

variable_15 = "Liza\nPalomino\nMarciales"
print(variable_15)

variable_16 = """Liza
Palomino
Chouinard"""
print(variable_16)

# --------------------------------------------------------------------------
# -- EJERCICIO -- #
parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."
parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."
parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

print("Mensajes Secreto Decodificados:")
print("Mesaje secreto 1:")
print(parrafo1[1: :18])
print("Mesaje secreto 2:")
print(parrafo2[138:147])
print("Mesaje secreto 3:")
print(parrafo3[125] + parrafo3[94] + parrafo3[35] + parrafo3[107] + parrafo3[20] + parrafo3[1])

# --------------------------------------------------------------------------

# ----------------------------------
# -- Numeros -- #
# ----------------------------------
