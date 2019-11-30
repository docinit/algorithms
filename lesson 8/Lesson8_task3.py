#!/usr/bin/env python
# coding: utf-8

# In[48]:


#3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
#в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#Примечания:
#a. граф должен храниться в виде списка смежности;
#b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


### Формирование случайного графа. Согласно разъяснениям преподавателя: можно сделать связи не с каждой вершиной.

import random

## Ввод начальных данных: количество вершин (1) и номер вершины (2), для которой ищутся связи
size=int(input('Введите количество вершин: '))
start=int(input('Введите вершину, для которой искать связи: '))
## Генерация графа - функция
def graph(size):
    #range_verticies=[i for i in range(size)]
    graph=[]
    #print(graph)
    for i in range(size):
        k=[random.randint(0,size-1) for k in list(set(range(random.randint(1,size-1))))]
        k.sort
        graph.append(k)
    for k,i in enumerate(graph):
        for f,x in enumerate(i):
            if k==f:
                graph[k][f]=0
            while len(i)>0 and i[-1]==0:
                i.pop(-1)
                
    for i in graph:
        print(i)
    return graph
## Генерация графа - запуск функции        
graph=graph(size)


## Поиск вглубину
def dfs(graph, start, is_visited=0):
    if is_visited==0:
        is_visited = []
    is_visited.append(start)
    for next in graph[start]:
        if next not in is_visited:
            dfs(graph, next, is_visited)
    
    return is_visited



## Проверка: вдруг пользователь указал номер вершины, которой не может быть...?
if start > size-1:
    start=size-1
    print('Вы указали недопустимое значение; будет анализироваться последняя вершина',size-1)
    
## Запуск поиска вглубину
visited=dfs(graph, start)

# Первое добавленное значение - стартовая вершина; ее можно удалить, т.к. идти до нее не нужно.
visited.pop(0)
print('С указанной вершины можно дойти до следующих вершин:',sorted(visited))

