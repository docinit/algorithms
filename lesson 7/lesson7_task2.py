#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.


import random, cProfile

size = int(input('укажите количество значений для сортировки: '))
array = [random.uniform(0, 50) for i in range(-size, size)]
random.shuffle(array)
print('Дано:', array)


def merge_sort(array):
    # если входной массив состоит из одного элемента, возращаем его обратно в качестве результата
    if len(array) == 1:
        return array
    # в остальных случаях
    else:
        # делим массив на 2 без остатка
        middle = len(array) // 2
        # получаем левый и правый массив
        left_array = array[:middle]
        right_array = array[middle:]
        merge_sort(left_array)
        merge_sort(right_array)
        # используются разные массивы для каждой половины и результирующего списка
        # поэтому используем разные счетчики: k,i,j
        k = 0
        i = 0
        j = 0
        # т.к. один массив может быть больше другого, нужно 3 цикла
        # 1: если массивы одинаковые, смотрим все числа в каждом из них
        # 1 число - не надо сортировать, просто сравним
        # 2 числа и больше - не надо сортировать, т.к. были отсортированы после сранения в предыдущем шаге рекурсии
        # в array[k] каждый раз попадает наименьшее число
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            array[k] = left_array[-1]
            k += 1
            i += 1
        while j < len(right_array):
            array[k] = right_array[j]
            k += 1
            j += 1
    #print(array)
    return array


print(merge_sort(array))
