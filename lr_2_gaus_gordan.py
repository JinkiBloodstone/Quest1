#библиотека для работы с матрицами
import numpy

def Metod_Gaussa(arr, brr):
    for k in range(arr.shape[0] - 1):
        #поиск строки с максимальным элементом
        max_elem = 0
        str = 0
        for i in range (k, arr.shape[0]):
            if abs(arr[i,k]) > abs(max_elem):
                max_elem = arr[i,k]
                str = i
        #меняем местами строки квадратной матрицы
        change = numpy.repeat(arr[k], 1)
        arr[k], arr[str] = arr[str], change
        #меняем местами элементы вектора-столбца
        change = numpy.repeat(brr[k], 1)
        brr[k], brr[str] = brr[str], change
        #делим полученную строку на max_elem
        arr[k] = arr[k] / max_elem
        brr[k] = brr[k] / max_elem
        #домножаем строку на коэффициенты и вычитаем ее из остальных строк
        for i in range (k + 1, arr.shape[0]):
            factor = arr[i,k]
            arr[i] = arr[i] - arr[k] * factor
            brr[i] = brr[i] - brr[k] * factor

    #находим аргументы уравнений
    arg = [brr[brr.shape[0] - 1] / (arr[arr.shape[0] - 1, arr.shape[0] - 1])]
    for i in range(arr.shape[0] - 2, -1, -1):
        n = brr[i]
        for j in range(len(arg)):
            n = n - arg[j] * arr[i, arr.shape[0] - 1 - j]
        arg.append(n)

    #переворачиваем значения в списке
    otv = []
    for i in reversed(arg): otv.append(i)
    return otv

#задаем вещественные квадратные матрицы и векторы-столбцы
A = numpy.array([[1.,3,2,-1],[-1,-5,-5,-3],[4,0,0,0],[-1,-4,-4,1]])
a = numpy.array([-11.,9,-12,18])

B = numpy.array([[0.,-3,-2,-2,0],[1,-4,0,-4,-5],[2,2,1,4,-4],[2,-3,-1,-1,1],[4,-5,-3,-3,4]])
b = numpy.array([4.,-14,-13,-1,-1])

#вызов функции и вывод на экран
print(Metod_Gaussa(A,a))
print(" ")
print(Metod_Gaussa(B,b))