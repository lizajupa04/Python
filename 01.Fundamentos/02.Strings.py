# ==========================================
# TEMA: STRINGS (CADENAS DE TEXTO)
# ==========================================

# --- 1. Declaración ---
saludo_doble = "Hola"
saludo_simple = "Hola mundo"
print("1. Saludos:", saludo_doble, "|", saludo_simple)

# --- 2. Indexación (acceso a un carácter) ---
# Positiva: empieza en 0 desde la izquierda
# Negativa: empieza en -1 desde la derecha
nombre = "Alejandro"
print("2. Índice 2:", nombre[2])  # 'e'
print("2. Índice -2:", nombre[-2])  # 'd'

# --- 3. Slicing [inicio:fin] ---
# Toma desde 'inicio' (incluido) hasta 'fin' (excluido)
frase = "Santiago Hernandez"
print("3. [0:3]:", frase[0:3])      # 'San'
print("3. [-9:-3]:", frase[-9:-3])  # 'Hernan'
print("3. [5:]:", frase[5:])        # Desde índice 5 hasta el final
print("3. [-9:]:", frase[-9:])      # Últimos 9 caracteres

# --- 4. Stride [inicio:fin:paso] ---
# El tercer valor define cada cuántos caracteres avanza
print("4. [0:8:2]:", frase[0:8:2])  # 'Snig'
print("4. Reversa:", frase[::-1])   # Truco clásico para invertir un string

# --- 5. Strings multilínea ---
# Útiles para textos largos, menús o plantillas
lista_n1 = "Liza\nPalomino\nMarciales"
lista_n2 = """Liza
Palomino
Chouinard"""
print("5. Multilínea con \\n:\n" + lista_n1)
print("5. Multilínea con comillas triples:\n" + lista_n2)

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

