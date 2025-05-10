# 📌 Задача 8: Дубликаты и копии

# items = ['pen', 'book', 'pen', 'ruler', 'pen']
# Задания:

# Скопируй список в copy_items.

# Удали все вхождения 'pen' из оригинального списка.

# Вставь 'notebook' на вторую позицию.

# Выведи оба списка — сравни их  .





items = ['pen', 'book', 'pen', 'ruler', 'pen']
copy_items=items.copy()
print(copy_items)
while 'pen' in items:
    items.remove('pen')
print(items)
items.insert(1,'notebook')
print(items)