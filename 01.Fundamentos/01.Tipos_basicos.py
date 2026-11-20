# ==========================================
# TEMA: NÚMEROS Y OPERADORES ARITMÉTICOS
# ==========================================

# --- 1. Tipos numéricos ---
entero = 10          # int
decimal = 3.14       # float
complejo = 2 + 3j    # complex (poco común al inicio)
print("1. Tipos:", type(entero), type(decimal))

# --- 2. Operadores clave (los que más se confunden) ---
print("2. División normal (/):", 10 / 3)     # 3.3333... (siempre da float)
print("2. División entera (//):", 10 // 3)   # 3 (descarta decimales)
print("2. Módulo / residuo (%):", 10 % 3)    # 1 (útil para saber si es par/impar)
print("2. Potencia (**):", 2 ** 3)           # 8

# --- 3. Conversión de tipos (Casting) ---
texto_num = "25"
suma = int(texto_num) + 5
print("3. Conversión str a int:", suma)      # 30