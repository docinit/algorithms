#1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
#заданный случайными числами на промежутке [-100; 100).
#Выведите на экран исходный и отсортированный массивы.

import random, cProfile

size = int(input('укажите количество значений для сортировки: '))
array = [i for i in range(-size, size)]
random.shuffle(array)

print('Дано:', array)
def bubble_sort (array,z=1):
    global ex
    ex = 0
    a=len(array)
    while z < a:
        x=z
        while z>=1 and array[z-1] < array[z]:
            array[z-1], array[z] = array[z], array[z-1]
            ex+=1
            z-=1
        z=x+1

cProfile.run('bubble_sort(array)')
#При замерах cProfile результат для данного метода чуть лучше, чем кода,
# представленном на уроке (время на выполнение меньше, примерно на 10%)
print('Результат:', array,'\n',ex,'замен')
