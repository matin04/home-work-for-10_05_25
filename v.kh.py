# 📌 Задача 7: Работа со строками и числами

# mixed = [3, 'hi', 5, 'hello', 2, 'hi']
# Задания:

# Посчитай, сколько раз встречается 'hi'.

# Удали все вхождения 'hi' (в цикле, с remove()).

# Добавь в конец 'bye' и число 0.

# Найди индекс 'hello' и вставь 'welcome' перед ним.

# Выведи итоговый список.



mixed = [3, 'hi', 5, 'hello', 2, 'hi']
print(mixed)
k=mixed.count('hi')
print(k)
for i in mixed[:]:
    if i=='hi':
        mixed.remove(i)
print(mixed)
mixed.extend(['bye',0])
print(mixed)
i=mixed.index('hello')
print(i)
mixed.insert(2,'welcome')
print(mixed)
