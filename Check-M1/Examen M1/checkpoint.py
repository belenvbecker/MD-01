# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np
from Lista import Lista

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    #Tu código aca:

    """
    En el contexto de la biblioteca de Python llamada pandas, el atributo shape se utiliza para obtener la forma o dimensiones de un DataFrame o un objeto de tipo Series.
    En concreto, el atributo shape devuelve una tupla que indica el número de filas y columnas presentes en el DataFrame o la Serie. La forma de la tupla es (n_filas, n_columnas), donde n_filas representa el número de filas y n_columnas el número de columnas en el DataFrame o la Serie.
    """

    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv('datasets/Fuentes_Consumo_Energia.csv')
    colombia_registros= df[df['Entity']=='Colombia'].shape[0]
    mexico_registros = df[df['Entity'] == 'Mexico'].shape[0]
    return (mexico_registros,colombia_registros)

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:

    df = pd.read_csv('datasets/fuentes_consumo_energia.csv')
    df=df.drop(columns=['Code', 'Entity'])
    df
    cantidad_columnas=df.shape[1]
    print(cantidad_columnas)
    return cantidad_columnas

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:

    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv("datasets/fuentes_consumo_energia.csv")

    # Obtener la cantidad de registros no nulos en la columna 'Year'
    cantidad_registros = df['Year'].count()

    return cantidad_registros

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:

    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv("datasets/fuentes_consumo_energia.csv")

    # Realizar la conversión de unidades de Exajulios a Teravatios/Hora
    campos_EJ = [col for col in df.columns if col.endswith('_EJ')]
    for campo in campos_EJ:
        campo_TWh = campo.replace('_EJ', '_TWh')
        df[campo_TWh] = df[campo] * 277.778

    # Crear el campo "Consumo_Total" con la sumatoria de los consumos en Teravatios/Hora
    campos_TWh = [col for col in df.columns if col.endswith('_TWh')]
    df['Consumo_Total'] = df[campos_TWh].sum(axis=1)

    # Filtrar los registros para la entidad 'World' y el año '2019'
    consumo_total = df[(df['Entity'] == 'World') & (df['Year'] == 2019)]['Consumo_Total'].sum()

    return round(consumo_total, 2)

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:

    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv("datasets/fuentes_consumo_energia.csv")

    # Filtrar los registros para la entidad 'Europe'
    df_europe = df[df['Entity'] == 'Europe']

    # Encontrar el año de mayor generación de energía hídrica
    max_generation_year = df_europe['Hydro_Generation_TWh'].idxmax()
    max_generation_year = df_europe.loc[max_generation_year, 'Year']

    return int(max_generation_year)

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:

    try:
        result = np.matmul(np.matmul(m1, m2), m3)
        return True
    except ValueError:
        return False

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    #Tu código aca:

    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv("datasets/GGAL - Cotizaciones historicas.csv")
    
    # Calcular la suma de los valores de la columna "máximo"
    suma_maximo = round(df['maximo'].sum(), 4)
    
    return suma_maximo

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:

    # Ingestar el contenido del archivo en un DataFrame
    df = pd.read_csv('datasets/Fuentes_Consumo_Energia.csv')

    # Obtener la cantidad de entidades diferentes
    cantidad_entidades = df['Entity'].nunique()

    # Retornar el resultado como un entero
    return int(cantidad_entidades)

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:

    # Ingestar el contenido de las tablas en DataFrames
    df1 = pd.read_csv("datasets/Tabla1_ejercicio.csv", sep=";")
    df2 = pd.read_csv("datasets/Tabla2_ejercicio.csv", sep=";")

    # Calcular el promedio de puntuación para cada persona en la tabla 2
    df2_avg = df2.groupby('pers_id')['score'].mean().reset_index()

    # Unir los dataframes utilizando la columna 'pers_id' como clave
    df_merged = pd.merge(df1, df2_avg, on='pers_id')

    # Calcular el promedio de puntuación para cada género sin tener valores repetidos
    df_unique = df_merged.drop_duplicates(subset='pers_id')

    # Calcular el promedio de puntuación para cada género
    score_promedio_femenino = df_unique[df_unique['sexo'] == 'F']['score'].mean()
    score_promedio_masculino = df_unique[df_unique['sexo'] == 'M']['score'].mean()

    # Redondear los resultados a 2 decimales
    score_promedio_femenino = round(score_promedio_femenino, 2)
    score_promedio_masculino = round(score_promedio_masculino, 2)

    # Retornar los resultados en formato tupla
    return score_promedio_femenino, score_promedio_masculino

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:

    # Obtener la cabecera de la lista
    cabecera = lista.getCabecera()

    # Contar la cantidad de nodos
    contador = 0
    puntero = cabecera
    while puntero is not None:
        contador += 1
        puntero = puntero.getSiguiente()

    return contador
