# ==========================================
# TEMA: NÚMEROS Y OPERADORES ARITMÉTICOS
# ==========================================

# --- 1. Números enteros (int) ---
entero = 10
print("1. Entero:", entero, "| Tipo:", type(entero))

# Podemos escribir números grandes más legibles usando guion bajo (_)
# En Python no se usan puntos para miles (1.000.000 sería un error o float)
sin_separador = 1000000
un_millon = 1_000_000
print("1. Un millón:", un_millon, "| Iguales:", sin_separador == un_millon)

# --- 2. Números decimales (float) ---
# Siempre con punto (.). La coma (,) separa elementos en otras estructuras (como tuplas)
decimal = 10.5
print("2. Decimal:", decimal, "| Tipo:", type(decimal))

# --- 3. Conversión de texto a número (Casting) ---
texto_entero = "10"
entero_convertido = int(texto_entero)
print("3. str a int:", entero_convertido, "| Tipo:", type(entero_convertido))

texto_decimal = "10.5"
decimal_convertido = float(texto_decimal)
print("3. str a float:", decimal_convertido, "| Tipo:", type(decimal_convertido))

# --- 4. Números complejos (complex) ---
# Tienen parte real y parte imaginaria (se usa 'j' en Python)
complejo = 1 + 2j
print("4. Complejo:", complejo)
print("4. Parte real:", complejo.real)       # 1.0
print("4. Parte imaginaria:", complejo.imag) # 2.0

# --- 5. Operadores aritméticos clave ---
print("5. División normal (/):", 10 / 3)     # 3.3333... (siempre devuelve float)
print("5. División entera (//):", 10 // 3)   # 3 (descarta decimales)
print("5. Módulo / residuo (%):", 10 % 3)    # 1 (útil para pares/impares)
print("5. Potencia (**):", 2 ** 3)           # 8