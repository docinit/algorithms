#!/usr/bin/env python
# coding: utf-8

# In[20]:


#В программе генерируется случайное целое число от 0 до 100.
#Пользователь должен его отгадать не более чем за 10 попыток.
#После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
#чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random
x=random.randint(0,100)
i=0
def conj (x,i):
    try:
        y=int(input('Попытайтесь угадать загаданное число от 0 до 100. Введите целое число. Введите \'-1\' для завершения. '))
    except ValueError:
        print('Внимание! Вводить можно только целые числа!\nПопробуйте еще раз.')
        y=-2
        i+=1
    if y==x:
        print('Вам удалось угадать загаданное число!')
    elif y<x:
        print('Вы не угадали. Ваше число меньше загаданного.')
    else:
        print('Вы не угадали. Ваше число больше загаданного.')
    if i<10 and y!=x and y!=-1:
        i+=1        
        conj(x,i)
    elif i==10:
        print('Вы так и не угадали загаданное число:(')

conj(x,i) 


# In[62]:


import random, timeit
x=random.randint(0,100)
listx=[i for i in range(0,101)]

def conj (x,listx):
    y=0
    print(f'y={y}')    
    print(f'x={x}')
    if x!=y:
        try:
            y=int(input('Попытайтесь угадать загаданное число от 0 до 100. Введите целое число. Введите \'-1\' для завершения. '))
        except ValueError:
            print('Внимание! Вводить можно только целые числа!\nПопробуйте еще раз.')
            y=-2
        if x!=y:
            if x in listx[:y]:
                # отбрасываем все справа - и считаем заново, сохраняя полученный ранее base_x,
                # но не беря в расчет base_i с индексом base_k-1
                listx=listx[:y]
                print('Загаданное число меньше!')
            # если же число находится справа, то надо подсчитать все, что было слева
            # base_k в конце индекса не уменьшаем, т.к. значение индекса = base_k не включится в список,
            # если base_k указан последним
            elif x in listx[y:]:
                # считаем, включая base_k-1 (содержит base_i) - его мы отбросим;
                # число с индексом, соответствующим base_k (=следующее за base_i) не включается в подсчет,
                # и будет использовано для дальнейшего поиска
                y=y-len(listx[:y])
                listx=listx[y:]
                print('Загаданное число больше!')
            conj(x,listx)
        else:
            print('Вам удалось угадать загаданное число!')
            print(f'y={y}')
    return

conj(x,listx)


# In[ ]:




