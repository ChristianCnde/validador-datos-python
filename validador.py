import pandas as pd 
import re

# Cargar el archivos CSV
df = pd.read_csv(r'C:\Users\chris\OneDrive\Escritorio\validacion_datos\usuarios.csv')

# Funcion para validar el mail 
def es_email_valido(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

# Funcion para validar edad
def es_edad_valida(edad):
    return isinstance(edad, int) and edad >=18

# Revisar cada fila y detectar errores
errores = []

for index, fila in df.iterrows():
    email_valido = es_email_valido(fila['email'])
    edad_valida = es_edad_valida(fila['edad'])

    if not email_valido or not edad_valida:
        errores.append({
            'fila': index + 1,
            'email': fila['email'],
            'edad': fila['edad'],
            'email_valido': email_valido,
            'edad_valida': edad_valida
        })

# Mostrar resultados
if errores:
    print("Se encontraron errores en los siguientes registros: ")
    for error in errores:
        print(error)
else:
    print("Todos los datos son validos.") 
