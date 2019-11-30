#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Пользователь вводит данные о количестве предприятий,
#их наименования и прибыль за четыре квартала для каждого предприятия.
#Программа должна определить среднюю прибыль (за год для всех предприятий)
#и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict,OrderedDict

a=int(input('Задайте количество компаний: '))

comp_dict=OrderedDict()
com_income=0
for i in range(a):
    k=str(input('Введите название компаний (по-одной): '))
    comp_dict[k]=1

for k in comp_dict:
    comp_dict[k]=(float(input(f'Введите прибыль за первый квартал для "{k}": ')),
                     float(input(f'Введите прибыль за второй квартал для "{k}": ')),
                         float(input(f'Введите прибыль за третий квартал для "{k}": ')),
                             float(input(f'Введите прибыль за четвертый квартал для "{k}": ')))


summa=0
for i in comp_dict:
    summa+=sum(comp_dict[i])
print('Средний доход за год: ', summa/a)
less=[]
more=[]
for i in comp_dict:
    s = sum(comp_dict[i])
    if s<summa/a:
        less.append(i)
    if s>summa/a:
        more.append(i)
print(f'Компания/ии {", ".join(more)} заработала/и больше среднего')
print(f'Компания/ии {", ".join(less)} заработала/и меньше среднего')


# In[ ]:




