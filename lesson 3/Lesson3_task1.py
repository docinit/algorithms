#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. В диапазоне натуральных чисел от 2 до 99 определить,
#сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
list1=[i for i in range(2,100)]
list2=[i for i in range(2,10)]
#для индекса
i=0
#(дополнительно, краткий вид) для формирования таблицы
counter=[0]*len(list2)
#проверяем каждое число из list2 (от 2 до 9)
for num2 in list2:
    #простой счетчик
    count = 0
    #проверяем каждое число из list1 (от 2 до 99)
    for num1 in list1:
        #если вторые делятся на первое без остатка, то
        if num1%num2==0:
            # увеличиваем счетчик на 1
            count+=1
    counter[i]=count
    i+=1
    print(f'Количество чисел в диапазоне от 2 до 99, которые делятся без остатка на {num2}, равно {count}.')

print('\n','Или вкратце: ','\n')    
for numerus,values in enumerate(list2):
        print(list2[numerus],':',counter[numerus])


# In[ ]:




