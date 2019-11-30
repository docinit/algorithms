#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

import hashlib,sys
#sys.setrecursionlimit(1000000) 
def n_substrings(string,var_string,x):

    assert len(string)>0, 'Строка не может быть пустой!'
    string=list(string)
    if len(string) == 1:
        if var_string.get(''.join(string)):
            pass
        else:
            ha=hashlib.sha1(''.join(string).encode('utf-8')).hexdigest()
            var_string[''.join(string)]=''.join(ha)
    elif len(string)>1: 
        for index, item in enumerate(string):
            if index<len(string):
                if var_string.get(''.join(string[index:])):
                    pass
                elif string[index:]!=x:
                    ha=hashlib.sha1(''.join(string[index:]).encode('utf-8')).hexdigest()
                    var_string[''.join(string[index:])]=''.join(ha)
        string=string[:-1]
        n_substrings(string,var_string,x)
    k=len(var_string)
    return k,var_string


var_string={}
string = str(input('Введите Вашу фразу: '))
x=list(string)
n,var_string=n_substrings(string,var_string,x)


print(f'Строка содержит {n} подстрок')

