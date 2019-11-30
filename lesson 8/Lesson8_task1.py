#1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# Количество друзей в задании не указано - берем случайное значени, например, от 10 до 400 (можно менять)

import random

num_of_friends = random.randint(10, 400)
friend_list = [i for i in range(num_of_friends)]
event = []
for k, i in enumerate(friend_list):
    event.append(k)
for k, i in enumerate(event):
    event[k] = [1] * (num_of_friends)
    event[k][k] = 0


def count(event):
    counter = 0
    start = 0
    is_counted = [False] * num_of_friends
    while start < len(event) - 1:
        is_counted[start] = True
        print('подсчитаны', is_counted)
        for k, i in enumerate(event[start]):

            if i == 1 and not is_counted[k]:
                counter += 1
        start += 1

    return counter


print(f'{num_of_friends} друзей совершили {count(event)} рукопожатий')
