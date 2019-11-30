#!/usr/bin/env python
# coding: utf-8

# In[77]:


import timeit,cProfile
def simple_num(n):
    list_num = [i for i in range(n)]
    list_num[1]=0
    for i in range(2,n):
        if list_num[i]!=0:
            j=i*2
            while j<n:
                list_num[j]=0
                j+=i
    #print(list_num)
    result=[i for i in list_num if i!=0]
    return result

def main(n):
    m=n
    list_num=simple_num(n)
    while len(list_num)<m:
        n+=n
        list_num=simple_num(n)
        #print(len(list_num))
    x=list_num[m-1]
    return x

main(1000)
#print(x)
#cProfile.run('main(1000000)')
#В задачах с поиском простого числа по номеру этого числа алгоритм, разработанный на уроке
#проявил себя лучше, чем второй, который выполняется методом перебора. Время выполнения
#задачи первого кода растет примерно на 1 порядок при увеличении номера искомого числа в 10
#раз. А второй код растет примерно в 100 раз при увеличении номера элемента в 10 раз. Таким
#образом, время работы первого алгоритма выражается О(n), а второго – О(n 2 ). При этом,
#количество вызовов функций в первом случае растет незначительно , а во втором – не растет
#вообще.

# In[ ]:




