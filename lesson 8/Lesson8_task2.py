#!/usr/bin/env python
# coding: utf-8

# In[70]:


#2. Доработать алгоритм Дейкстры (рассматривался на уроке),
#чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

###############РЕШЕНИЕ####################
#### I. Метод разбора пар вершина-родитель
#### Вывод результатов встроенными функциями (1) и через dataframe (2)

import pandas as pd, numpy as np
g=[
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]

def dextra(graph,start):
#### I. Код из лекции
    length=len(graph)
    is_visited=[False]*length
    cost=[float('inf')]*length
    parent=['Нет родителей']*length
    cost[start]=0
    min_cost=0
    path=[]
    while min_cost<float('inf'):
        is_visited[start]=True

        for i, vertex in enumerate(graph[start]):
            if vertex!=0 and not is_visited[i]:
                if cost[i]>vertex+cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i]=start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost=cost[i]
                start=i
                # для того, чтобы сохранить информцию о родителях и текущей вершине, стоимость до которой подсчитана,
                # т.е. до которой можно дойти, сохраним обоих в списке
                #(получится всего 2 элемента для каждой вершины, до которой можно дойти)
                path.append([parent[i],i,f'за {min_cost} у.e.'])

### II. Разбор получившихся вложенных списков в массиве path
####а. объединение списков в полноценные пути
    x_iter=1
    path2=path.copy()
    # два одинаковых массива для объединения связанных полей
    def gathering(path,path2):
    # если в массиве path один из вложенных циклов имеет такой последний элемент, на который начинается другой
    # вложенный список, то добавим к этому другому первый элемент в начало списка 
        for z,i in enumerate(path):#
            x=path[z]
            for m,k in enumerate(path2):
                y=path2[m]
                if x[-2]==y[0]:
                    start_y=y[0]
                    y.insert(0,x[0])
                    path2[m]=y

        return path2
    # этот цикл запускает функцию gathering len(path)-1 раз
    while x_iter<len(path):
        path2=gathering(path,path2)
        x_iter+=1
        
####б. удаление получившихся дубликатов
    #удаляем лишние результаты (дубликаты)
    #для этого создаем пустой список
    result_remove=[]
    for k,i in enumerate(path2):
        for l,e in enumerate(path2):
            if e==i and k!=l:
                result_remove.append(l)
    k=0
    for i in list(set(result_remove))[1:]:
        del path2[i-k]
        k+=1
    return parent,path2

s=int(input('От какой вершины идти: '))
if s<len(g):
    parent,path2=dextra(g,s)

    ### III. Вывод результатов
    for k,p in enumerate(parent):
        if p=='Нет родителей' and k!=s:
            print(f'До вершины {k} не дойти.')
    for k,p in enumerate(parent):
        if k==s:
            print(f'Вершина {k} - отправная точка, до нее не надо идти.')


    #### Вывод без использования dataframe        
    for i in path2:
        print(f'Путь до {i[-2]} вершины {i[-1]}: ',*i[:-1],sep='\t')
    print('*'*50)
#################################################
#################################################
    #### Вывод с использованием dataframe
    path_dataframe = pd.DataFrame(path2)
    path_dataframe
    index=0
    path_dataframe['Стоимость']=''
    path_dataframe['Цель']=''
    while index<len(path_dataframe):
        column=0
        while column<path_dataframe.shape[1]-2:
            if path_dataframe.iloc[index,column]==None:
                path_dataframe.iloc[index,column]=''
            if isinstance(path_dataframe.iloc[index,column],str):
                path_dataframe.iloc[index,-1]=str(path_dataframe.iloc[index,-1])+str(path_dataframe.iloc[index,column-1])
                path_dataframe.iloc[index,column+1]=path_dataframe.iloc[index,column]
                path_dataframe.iloc[index,column]=''

            i=1
            while path_dataframe.iloc[i-1,column]=='':
                i+=1
                if i==len(path_dataframe):
                    column_del=column
                    break
            column+=1

        index+=1
    path_dataframe.drop(path_dataframe.iloc[:,column_del:column_del+1], axis=1,inplace=True)
    path_dataframe=path_dataframe.sort_values('Цель',ascending=1)
    path_dataframe.set_index('Цель',inplace=True)
else:
    path_dataframe=pd.DataFrame([])
    print('Такой вершины нет.')
    
for k,p in enumerate(parent):
    if p=='Нет родителей' and k!=s:
        print(f'До вершины {k} не дойти.')
for k,p in enumerate(parent):
    if k==s:
        print(f'Вершина {k} - отправная точка, до нее не надо идти.')
path_dataframe


# In[ ]:


#2. Доработать алгоритм Дейкстры (рассматривался на уроке),
#чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

###############РЕШЕНИЕ####################
####II. Метод просмотра родителей каждой вершины до получения исходной (стартовой) вершины, введенной пользователем.
g=[
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]

def dextra(graph,start):
#### I. Код из лекции
    length=len(graph)
    is_visited=[False]*length
    cost=[float('inf')]*length
    parent=['Нет родителей']*length
    cost[start]=0
    min_cost=0
    path=[start]
    s=start
    while min_cost<float('inf'):
        is_visited[start]=True

        for i, vertex in enumerate(graph[start]):
            path.insert(i,start)
            if vertex!=0 and not is_visited[i]:
                if cost[i]>vertex+cost[start]:
                    parent[i]=start
                    #path.append(parent[i])
                    cost[i] = vertex + cost[start]
                    

        min_cost = float('inf')
        for i in range(length):
            path[len(path)-1]=parent[i]
            if min_cost > cost[i] and not is_visited[i]:
                min_cost=cost[i]
                start=i
                
#####
# Лучший родитель (по цене) уже выбран и сохранен в первой части
# заносим каждого родителя в full_path - и печатаем
    full_path=[]
    for i in range(len(g)):
        start_point=i
        full_path.append(str(i))
        while i!=s and isinstance(parent[i],int):
            i=parent[i]
            full_path.append(str(i))
            #print('parent = ',i)
        if i==s:
            
            full_path.reverse()
            
            #print("\t".join(full_path)) 
            print(f'{start_point}: {"   ".join(full_path)}')
            full_path=[]
        else:
                  print(f'{i}: нет пути')
    return

s=int(input('От какой вершины идти: '))
dextra(g,s)

