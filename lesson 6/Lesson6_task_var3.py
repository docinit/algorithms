#!/usr/bin/env python
# coding: utf-8

# In[9]:


#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

## ЦИКЛ + СПИСОК; для создания первичного массива используется список.

#Python 3.7.4
#OS: Linux, Fedora 30, 64-bit
#В коде решений создается массив (список) случайных чисел.
#Разработаны варианты решений: с использованием списка, словаря и рекурсии.
#В предложенных решениях создается рандомный список случайных чисел. Поиск выполняется по словарю, другому списку из двух элементов (сравниваются 2 значения, каждое из которых сохраняется как минимальное или максимальное, в зависимости от выполняемой в коде функции) или рекурсией, в которой по-одному отбрасываются значения, пока не останется всего 2, из которых сохраняется минимальное/максимальное – и функция возвращается к предыдущей итерации, чтобы закончить ее.
#Итак, имеется:
#    • один изначальный список, содержащий один набор значений;
#    • переменные, которые ссылаются на значения из того же списка;
#    • переменные, содержащие индексы, которые необходимы для обмена значений.
#    • копии списков, уменьшаемые на 1 элемент при каждом “заходе” рекурсивной функции с теми же самыми значениями (т.е. память на эти значения уже затрачена и повторно их подсчитывать не нужно).
#Я исключил первые числа от 0 до 255, которые статически хранятся в памяти компьютера.

#Результаты: рекурсия требует больше всего памяти. Варианты с использованием списка или словаря не имеют большой разницы по затратам памяти компьютера.


import random,cProfile,timeit,sys
def startx(n):
    global listl, a
    listl=[]
    a=0
    #n=int(input('Задайте длину списка: '))
    for i in range(0,n):
        listl.append(random.randint(256,10**12))
    
    return main_f(listl,a)

#цикл для формирования списка
def main_f(listl,a):
    global maximum, minimum, mink, maxk
    maximum=minimum=listl[0]
    mink=maxk=-1
    while a<len(listl)-1:
        if listl[a]>maximum:
            maximum=listl[a]
            maxk=a
        if listl[a]<minimum:
            minimum=listl[a]
            mink=a
        a+=1
    #print (f'\nПри проверке массива:\nпервый раз максимальное число ({maximum}) нашлось на {maxk+1} месте, а минимальное ({minimum}) - на {mink+1} месте.\n')
    #print(f'До смены мест значений массив выглядит так:\n{listl}')
    listl[maxk],listl[mink]=listl[mink],listl[maxk]
    #print(f'После смены мест значений массив выглядит так:\n{listl}')
    return listl
n=1000000
startx(n)
#cProfile.run('startx(10000)')
#В коде решений создается массив (список) случайных чисел.
#Разработаны варианты решений: с использованием списка, словаря и рекурсии.
#Из результатов видно, что работа рекурсии занимает значительно больше времени, функции
#выполняются n-1 раз, а время работы можно выразить в виде О(n 2 ): время выполнения кода
#растет на 1 порядок при увеличении числа элементов в 10 раз, а затем резко возрастает (10000
#элементов) и достигает неразумных пределов уже на попытке выполнить операцию со 100
#тысячами значений.
#Цикл с использованием словаря или списка показали себя почти одинаково хорошо (словарь –
#чуть лучше, но имеющейся разницей можно пренебречь, пока не доказана ее статистическая
#достоверность). О-большое этих алгоритмов составляет О(n) – имеется почти линейная
#зависимость от количества элементов: при росте количества чисел в массиве в 10 раз, скорость
#работы снижается на 1 порядок.
print(n, 'чисел')

#lst=[i for i in range(10)]
#print(sys.getsizeof(lst))
global x_size
x_size=0
def show_size(x,x_size, level=0):
    #print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)},object={x}')
    x_size+=sys.getsizeof(x)
    if hasattr(x,'__iter__'):
        if hasattr(x,'items'):
            for xx in x.items():
                show_size(xx,x_size, level+1)
                x_size+=sys.getsizeof(xx)
                
        elif not isinstance(x,str):
            for xx in x:
                show_size(xx,x_size, level+1)
                x_size+=sys.getsizeof(xx)
    return x_size
mem_used=show_size(listl,x_size)+show_size(maximum,x_size)+show_size(minimum,x_size)+show_size(mink,x_size)+show_size(maxk,x_size)+show_size(a,x_size)+show_size(n,x_size)
print('Затрачено памяти:', mem_used, 'байт.\n(Исходный и результирующий списки скрыты; количество чисел менять значением n.)')


# In[ ]:



