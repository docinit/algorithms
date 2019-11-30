#!/usr/bin/env python
# coding: utf-8

# In[30]:


#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#При этом каждое число представляется как массив, элементы которого — цифры числа.
#Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import ChainMap, defaultdict
a1=str.upper(input('Введите шестнадцатеричное число: '))
a2=str.upper(input('Введите шестнадцатеричное число: '))
list_num1=[*a1]
list_num2=[*a2]

num_dict={}
for i in range(10):
    num_dict[str(i)]=i
letter_dict=defaultdict(int)
for k,i in enumerate(['A','B','C','D','E','F']):
    letter_dict[i]=k+10

hex_map=ChainMap(num_dict,letter_dict)

list_num1.reverse()
k=0
hex_result1=0
for i in list_num1:
    hex_result1+=hex_map[i]*16**k
    k+=1
    
list_num2.reverse()
k=0
hex_result2=0
for i in list_num2:
    hex_result2+=hex_map[i]*16**k
    k+=1

summa=hex_result1+hex_result2
mult=hex_result1*hex_result2

#а теперь в 16-виде
def d(n,b=16):
    d.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'           
    r=''
    while n:
        n, y = divmod(n, b) 
        r=d.t[y]+r
    return r
print('произведение = ', list(d(mult)))
print('сумма = ', list(d(summa)))


# In[ ]:




