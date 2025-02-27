#!/usr/bin/env python
# coding: utf-8

# In[2]:


#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.


# Алгоритм:
# Начало
# Создать пустой список
# Ввод значений
# Проверка правильности ввода значений
# Вывод сообщений об ошибках в случае наличия ошибок
# min_num=b+1, max_num = a-1
# Заполнение списка
# Определение максимального и минимального чисел, а также их индексов.
# Создание списка для суммирования необходимых значений (между min_num и max_num)
# Суммирование
# Вывод результатов
# Конец

import random
listl=[]
mult1,mult2=0,0
while True:
    try:
        a=int(input('Введите минимальное целое число списка: '))
        b=int(input('Введите максимальное целое число списка: '))
        n=int(input('Введите количество элементов списка: '))
        if a>b:
            a,b=b,a
        if a<b:
            min_num=b+1
            max_num = a-1            
            for i in range(0,n):
                listl.append(random.randint(a,b))
            for k,i in enumerate(listl):
                if k<=len(listl)-1:
                    if listl[k]>max_num:
                        max_num=listl[k]
                        imax=k
                    elif listl[k]<min_num:
                        min_num=listl[k]
                        imin=k
            if imin<imax:
                listl2=listl[imin+1:imax]
            else:
                listl2=listl[imax+1:imin]
            print (f'\nМаксимальное значение = {max_num}, а минимальное = {min_num}.')
            print (f'Их индексы (первые вхождения): {imax}, {imin}, соответственно.')            
            print(f'Сумма значений между позициями этих элементов = {sum(listl2)}')
            print('\nПросуммированные значения: ',listl2, '\nЗначения списка: ',listl)
            break
        else:
            print ('Вы ввели одинаковые значения в качестве минимума и максимума. Попробуйте ввести правильные значения еще раз.') 
    except ValueError:
        print ('Вы ввели неверные значения. Попробуйте ввести правильные значения еще раз.')


# In[ ]:




