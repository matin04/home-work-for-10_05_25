# 📌 Задача 5: Очистка списка
# Дан список:

# data = [10, 20, 30]
# Задания:

# Добавь в него 40 и 50.

# Выведи длину списка.

# Очисти список.

# Выведи список и его длину после очистки.




data = [10, 20, 30]
data.extend([40,50])
print(data)
print(len(data))
data.clear()
print(data)
print(data)
print(len(data))
