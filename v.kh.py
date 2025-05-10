# 📌 Задача 10: Расширенная работа с .pop()

# values = [10, 20, 30, 40, 50]
# Задания:

# Удали третий элемент и сохрани его в переменную removed.

# Вставь removed в начало списка.

# Добавь в конец значение removed * 2.

# Переверни список.

# Выведи итоговый список.





values = [10, 20, 30, 40, 50]
print(values)
removed=values.pop(2)
print(removed)
print(values)
values.insert(0,removed)
print(values)
values.append(removed*2)
print(values)
values.reverse()
print(values)