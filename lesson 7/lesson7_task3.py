#3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Укажиие значение m: '))
list_random = [i * random.randint(1, 1000) for i in range(1,2 * m + 2)]
print(list_random)


def mediana_finder(n):
    while len(n) > 2:
        for i in n:
            def first(n):
                k = 0
                while k < len(n) - 1:
                    if n[k] > n[-1]:
                        n[k], n[-1] = n[-1], n[k]

                    k += 1
                n.pop(-1)
            def second(n):
                k = 1
                while k < len(n):
                    if n[-k] < n[0]:
                        n[-k], n[0] = n[0], n[-k]

                    k += 1
                n.pop(0)

            first(n)
            second(n)

    mediana = n[0]
    return mediana


mediana = mediana_finder(list_random)
print('Медиана списка значений =',mediana)
