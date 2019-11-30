#!/usr/bin/env python
# coding: utf-8

# In[28]:


#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# РЕКУРСИЯ + СПИСОК

import random,cProfile,timeit,sys
sys.setrecursionlimit(100000000) 



def startx(n):
    listl=[]
    a=0
    #n=int(input('Задайте длину списка: '))
    for i in range(0,n):
        listl.append(random.randint(0,10**12))
    
    return main_f(listl,a)


def main_f(listl,a):
    #определение максимума и минимума
    max_num=maximum(listl)
    min_num=minimum(listl)
    #определение индексов
    imax=listl.index(max_num)
    imin=listl.index(min_num)
    #print (f'\nПри проверке массива:\nпервый раз максимальное число ({max_num}) нашлось на {imax+1} месте, а минимальное ({min_num}) - на {imin+1} месте.\n')
    #print(f'До смены мест значений массив выглядит так:\n{listl}')
    listl[imax],listl[imin]=listl[imin],listl[imax]
    #print(f'После смены мест значений массив выглядит так:\n{listl}')
    return listl



#вызываемые функции
def maximum(listl):
    if len(listl)==2:
        return listl[0] if listl[0]>listl[1] else listl[1]
    maximums=maximum(listl[1:])
    return listl[0] if listl[0]>maximums else maximums

def minimum(listl):
    if len(listl)==2:
        return listl[0] if listl[0]<listl[1] else listl[1]
    minimums=minimum(listl[1:])
    return listl[0] if listl[0]<minimums else minimums
#вызов функций

startx(10)
#cProfile.run('startx(10)')
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

# In[14]:
