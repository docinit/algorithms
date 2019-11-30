#!/usr/bin/env python
# coding: utf-8

# In[32]:


#2. Закодируйте любую строку по алгоритму Хаффмана.

string = str(input('Введите фразу для кодирования по алгоритму Хаффмана: '))
# table_code нужен для сохранения закодированных символов
table_code={}
# count_dict и count_list нужны для подготовки и сортировки символов
count_dict={}
count_list=[]
# лист haffman нужен для перебора отсортированных символов и их наборов
haffman=[]
for i in string:
    table_code[i]=''
for i in string:
    count=1
    for k in string:
        if i==k:
            count+=1
    count_list.append([count,i])
count_list.sort()
#убираем дубликаты символов добавлением в словарь count_dict
for i in count_list:
    count_dict[i[1]]=[i[0]]
# для дальнейшей обработки нужен список
count_list=[]
for i in count_dict:
    count_list.append([[i],count_dict[i][0]])
# печать - проверка перед началом обработки
print(*count_list,sep='\n')
 
#####
#Создание списков завершено. Переход к сортировке.
#####

### Выполнение цикла, который располагает символы в пары и более длинные списки, согласно
# их частоте их встречаемости во фразе, которую мы обрабатываем.
while len(count_list)>1:
    k=0
    # вычисляем сумму
    pair_sum=count_list[k][-1]+count_list[k+1][-1]
    # на основании суммы и соответствующих символов,
    # создаем строку для дальнейшего использования
    x=[[''.join([count_list[k][0][0],count_list[k+1][0][0]])],pair_sum]
    # для каждой строки в списке count_list
    for i in count_list[k+1:]:
        # проверяем, что вычисленная сумма меньше или равна частоте, которая указана в
        # конце каждой строки
        if pair_sum <= i[-1]:
            # если это так, то вставляем значение x на ее место, сдвигая ячейки вправо
            count_list.insert(count_list.index(i),x)
            # сразу заканчиваем цикл, чтобы не испортить другие ячейки
            break
        # если же это не так, то, если сумма больше частоты, указанной в последней строке
        elif pair_sum > count_list[-1][-1]:
            # добавляем x в списко count_list
            count_list.append(x)
    # удаляем 2 строки с наименьшими частотами, которые мы использовали для создания x
    count_list.pop(k)
    count_list.pop(k)
    # и не забудем добавить x в список haffman для дальнейшей обработки
    haffman.append(x)
# печать результата преобразованной фразы в отсортированный список (точнее - строку) символов
print(count_list[0][0][0])

set_sign=list(set(string))
set_sign.sort()
for k,i in enumerate(haffman):
    #№№№№№№№ Берем первый (и др.) символ - и проверяем на условия
    for item in set_sign:
        # обработкой символов занимаемся, если символа еще нет в таблице кодов
        if table_code[item]=='':
            # ноль
            null_code='0'
            # один
            one_code='1'
            # начало кода каждого символа: пустой код
            letter_code=''
            # НАЧАЛО: для каждого символа в наборе символов (set_sign)
            #№№№№№№№ Если символ есть в i-строке (см. начало цикла for) от haffman
            if item in i[0][0]:
                #print('Формируем код для ', item)
                # если символ находится в строке списка huffman
                #№№№№№№№ и находится в конце этой строки, то пишем "0"
                if item==i[0][0][-1]:
                    # сохраняем значение в новую переменную
                    item_revealed=i[0][0]
                    # пишем первый символ кода для символа
                    letter_code=letter_code+one_code
                #№№№№№№№# и находится в начале строки, то пишем "1"
                if item==i[0][0][0]:
                    item_revealed=i[0][0]
                    letter_code=letter_code+null_code
            #№№№№№№№# на этом этапе все буквы, которые встали в пары сзади, получили 0, а если спереди - 1.
            # в обоих случаях сохраняем строку huffman с этим символом как новый "символ"
            # и теперь надо проверить, есть ли этот новый символ внизу huffman-списка
            # huffman-список изменять не можем, кроме того, там вложенные списки, да еще и указание частоты,
            # но вот сохранить его остаток (ниже проверяемой строки) - можно
            #№№№№№№№# СЛЕДУЮЩИЙ ЭТАП
                if k<len(haffman)-1:
                    haffman_next_step=haffman[k+1:]
                    for k_index,next_i in enumerate(haffman_next_step):
                        # делаем из этого второго списка простой список набора символов
                        # из переменной x - теперь мы можем сравнивать наш item_revealed с x
                        haffman_next_step[k_index]=next_i[0][0]
                # проходясь по этому списку, ищем item_revealed,
                # приравнивая всю строку к item_revealed, если будет найдена, и повторяя поиск
                for i_check in haffman_next_step:
                    if item_revealed in i_check:
                        if item_revealed==i_check[len(i_check)-len(item_revealed):]:
                            item_revealed=i_check
                            letter_code=one_code+letter_code
                        else:
                            item_revealed=i_check
                            letter_code=null_code+letter_code
                table_code[item]=letter_code

                
table_code_list=[]
for i in table_code:
      table_code_list.append([i,table_code[i]])  
table_code_list.sort()
print('Результат работы прогрммы:')
print('Таблица кодов',*table_code_list,sep='\n')
new_string=[]
for i in string:
    for k in table_code_list:
        if i==k[0]:
            new_string.append(k[1])
print('Строка в закодированном виде:\n',' '.join(new_string))

