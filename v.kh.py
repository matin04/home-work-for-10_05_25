# 📌 Задача 4: Индексы и вставки
# Дан список:

# letters = ['a', 'b', 'd', 'e']
# Задания:

# Найди индекс элемента 'd'.

# Вставь 'c' перед 'd', используя метод insert() и найденный индекс.

# Переверни список.

# Удали 'b'.

# Выведи результат.




letters = ['a', 'b', 'd', 'e']
index=letters.index('d')
letters.insert(2,'c')
print(letters)
print(index)
letters.remove('b')
print(letters)

