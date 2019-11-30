#!/usr/bin/env python
# coding: utf-8

# In[59]:


#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
## ЦИКЛ + СПИСОК
import random,cProfile
def startx(n):
    listl=[]
    a=0
    #n=int(input('Задайте длину списка: '))
    for i in range(0,n):
        listl.append(random.randint(0,10**12))
    
    return main_f(listl,a)

#цикл для формирования списка
def main_f(listl,a):
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
startx(10)
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

# In[ ]:



