"""
Problema de Código: Calculadora de Estadísticas de un Archivo de
Datos
Objetivo: Desarrollar una función en Python que lea un archivo de datos, calcule
estadísticas básicas (promedio, mediana, y moda) y las imprima en la consola.
Descripción del Problema: Cada equipo debe implementar una función que cumpla con
los siguientes requisitos:
1. Leer un archivo de texto llamado datos.txt que contiene una lista de números
(uno por línea).
2. Calcular el promedio, la mediana y la moda de los números.
3. Imprimir los resultados en la consola con un formato claro.
Instrucciones Específicas:
1. Lectura del Archivo: La función debe abrir y leer el archivo datos.txt.
2. Cálculo del Promedio: Sumar todos los números y dividir entre la cantidad total de
números.
3. Cálculo de la Mediana: Ordenar los números y encontrar el valor medio (o el
promedio de los dos valores medios si hay un número par de elementos).
4. Cálculo de la Moda: Encontrar el número que más se repite en la lista. Si hay más
de uno, devolver todos los números que tienen la misma máxima frecuencia.
5. Impresión de Resultados: Mostrar en la consola el promedio, la mediana y la moda
con un formato claro.
Formato del Archivo de Entrada:
Copiar código
10
20
20
30
40
50
50
50
60
Ejemplo de Salida:
makefile
Copiar código
Promedio: 37.0
Mediana: 40.0
Moda: 50
Pistas:
● Para leer el archivo, se puede utilizar with open('datos.txt', 'r') as
file:.
● Para calcular la mediana, se puede usar la función median() de la librería
statistics.
● Para calcular la moda, se puede usar la función mode() de la librería statistics.
Si hay más de una moda, deberán implementarlo manualmente.
● Se recomienda manejar las posibles excepciones (e.g., archivo no encontrado).
Tareas:
1. Crear un repositorio con el archivo y los compañeros deberán clonar dicho
repositorio y comenzar a trabajar en la solución.
2. Cada miembro del equipo debe encargarse de una parte específica del problema
(lectura del archivo, cálculo de promedio, mediana, moda, y manejo de
excepciones).
3. Integrar las partes en una función completa.
4. Subir la solución al repositorio y colaborar en la integración final siguiendo el proceso
de pull y merge descrito anteriormente.
5. Resolver cualquier conflicto de fusión que ocurra.
"""

# Importar liberia statistics
import statistics

# Funcion para leer el archivo
def leer_archivo():
    try:
        with open('datos.txt', 'r') as file:
            datos = file.readlines()
            datos = [int(dato) for dato in datos]
            return datos
    except FileNotFoundError:
        print('Archivo no encontrado')
        return None
    
# Funcion para calcular el promedio 
def calcular_promedio(datos):
    promedio = statistics.mean(datos)
    # Redondear a dos decimales
    promedio = round(promedio, 2)
    return promedio

def calcular_mediana(datos):
    mediana = statistics.median(datos)
    return mediana

# Funcion para calcular la moda
def calcular_moda(datos):
    try:
        moda = statistics.mode(datos)
        return moda
    except statistics.StatisticsError:
        # En caso de que haya más de una moda
        frecuencia = statistics.multimode(datos)
        return frecuencia

# Main
datos = leer_archivo()
if datos:
    promedio = calcular_promedio(datos)
    mediana = calcular_mediana(datos)
    moda = calcular_moda(datos)
    
    # Calcular promedio
    print(f'Promedio: {promedio}')
    
    # Calcular mediana
    print(f'Mediana: {mediana}')
    
    # Calcular moda
    if isinstance(moda, list):
        print(f'Moda: {", ".join(map(str, moda))}')
    else:
        print(f'Moda: {moda}')

datos = leer_archivo()
promedio = calcular_promedio(datos)
#calcular promerio
print(f'Promedio: {promedio}')