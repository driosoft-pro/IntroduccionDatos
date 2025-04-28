# Búsqueda Lineal
def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en una lista para encontrar el índice del elemento objetivo.
    
    Args:
        lista (list): Lista en la que se busca el elemento.
        objetivo: Elemento que se desea encontrar.
    
    Returns:
        int: Índice del elemento objetivo si se encuentra, -1 si no está en la lista.
    """
    for i in range(len(lista)):  # Itera sobre los índices de la lista.
        if lista[i] == objetivo:  # Compara cada elemento con el objetivo.
            return i  # Retorna el índice si encuentra el objetivo.
    return -1  # Retorna -1 si no encuentra el objetivo.

# Ejemplo de uso de búsqueda lineal
datos = [10, 20, 30, 40, 50]
print(busqueda_lineal(datos, 30))  # Resultado: 2 (el índice del número 30 en la lista)



# Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar el índice del elemento objetivo.
    
    Args:
        lista (list): Lista ordenada en la que se busca el elemento.
        objetivo: Elemento que se desea encontrar.
    
    Returns:
        int: Índice del elemento objetivo si se encuentra, -1 si no está en la lista.
    """
    inicio, fin = 0, len(lista) - 1  # Define los límites iniciales de la búsqueda.
    while inicio <= fin:  # Continúa mientras el rango de búsqueda sea válido.
        medio = (inicio + fin) // 2  # Calcula el índice del elemento medio.
        if lista[medio] == objetivo:  # Si el elemento medio es el objetivo:
            return medio  # Retorna el índice del elemento medio.
        elif lista[medio] < objetivo:  # Si el objetivo es mayor que el elemento medio:
            inicio = medio + 1  # Ajusta el límite inferior.
        else:  # Si el objetivo es menor que el elemento medio:
            fin = medio - 1  # Ajusta el límite superior.
    return -1  # Retorna -1 si no encuentra el objetivo.

# Ejemplo de uso de búsqueda binaria
datos = [10, 20, 30, 40, 50]
print(busqueda_binaria(datos, 40))  # Resultado: 3 (el índice del número 40 en la lista)


# Ordenamiento Quick Sort
def quick_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento rápido (Quick Sort).
    
    Args:
        lista (list): Lista que se desea ordenar.
    
    Returns:
        list: Lista ordenada.
    """
    if len(lista) <= 1:  # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada.
        return lista
    pivote = lista[len(lista) // 2]  # Selecciona el elemento pivote (el del medio).
    menores = [x for x in lista if x < pivote]  # Elementos menores que el pivote.
    iguales = [x for x in lista if x == pivote]  # Elementos iguales al pivote.
    mayores = [x for x in lista if x > pivote]  # Elementos mayores que el pivote.
    # Llama recursivamente a quick_sort para ordenar las sublistas y las combina.
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo de uso de Quick Sort
datos = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(datos))  # Resultado: [1, 1, 2, 3, 6, 8, 10] (lista ordenada)


# Algoritmo de Euclides
def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
    
    Returns:
        int: Máximo común divisor de a y b.
    """
    while b:  # Continúa mientras b no sea 0.
        a, b = b, a % b  # Actualiza a con el valor de b y b con el residuo de a dividido por b.
    return a  # Cuando b es 0, a contiene el MCD.

# Ejemplo de uso del cálculo del MCD
print(mcd(48, 18))  # Resultado: 6 (el MCD de 48 y 18)
