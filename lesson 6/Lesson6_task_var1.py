#!/usr/bin/env python
# coding: utf-8

# In[3]:


#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

## Рекурсия; для создания первичного массива используется список.

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
sys.setrecursionlimit(100000000) 



def startx(n,x_rec_size):
    global listl, a
    listl=[]
    a=0
    #n=int(input('Задайте длину списка: '))
    for i in range(0,n):
        listl.append(random.randint(256,10**12))
    
    return main_f(listl,a,x_rec_size)


def main_f(listl,a,x_rec_size):
    global max_num, min_num, imax, imin
    #определение максимума и минимума
    max_num=maximum(listl,x_rec_size)
    #print(bx_rec_size)
    min_num=minimum(listl,x_rec_size)
    #print(ax_rec_size)
    #определение индексов
    imax=listl.index(max_num)
    imin=listl.index(min_num)
    #print (f'\nПри проверке массива:\nпервый раз максимальное число ({max_num}) нашлось на {imax+1} месте, а минимальное ({min_num}) - на {imin+1} месте.\n')
    #print(f'До смены мест значений массив выглядит так:\n{listl}')
    listl[imax],listl[imin]=listl[imin],listl[imax]
    #print(f'После смены мест значений массив выглядит так:\n{listl}')
    return listl



#вызываемые функции
def maximum(listl,x_rec_size):
    global maximums
    global bx_rec_size
    if len(listl)==2:
        return listl[0] if listl[0]>listl[1] else listl[1]
    x_rec_size+=sys.getsizeof(listl[1:])
    bx_rec_size=x_rec_size
    maximums=maximum(listl[1:],x_rec_size)
    
    return listl[0] if listl[0]>maximums else maximums

def minimum(listl,x_rec_size):
    global ax_rec_size
    global minimums
    if len(listl)==2:
        return listl[0] if listl[0]<listl[1] else listl[1]
    x_rec_size+=sys.getsizeof(listl[1:])
    minimums=minimum(listl[1:],x_rec_size)
    ax_rec_size=x_rec_size
    return listl[0] if listl[0]<minimums else minimums
#вызов функций
n=10000
global x_rec_size
x_rec_size=0
startx(n,x_rec_size)
x_rec_size=ax_rec_size+bx_rec_size
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

mem_used=show_size(listl,x_size)+show_size(maximums,x_size)+show_size(minimums,x_size)+show_size(max_num,x_size)+show_size(min_num,x_size)+show_size(imax,x_size)+show_size(imin,x_size)+show_size(a,x_size)+show_size(n,x_size)+x_rec_size
print('Затрачено памяти:', mem_used, 'байт.\n(Исходный и результирующий списки скрыты; количество чисел менять значением )')


# In[ ]:




