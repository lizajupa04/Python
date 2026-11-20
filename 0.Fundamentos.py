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