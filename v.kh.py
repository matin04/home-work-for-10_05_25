# 📌 Задача 6: Сортировка с условиями

# nums = [7, 2, 9, 3, 5, 1, 8]
# Задания:

# Удали из списка все нечётные числа (используй remove() и цикл).

# Отсортируй список по убыванию.

# Добавь 10 и 12 в список.

# Переверни список.

# Выведи итоговый список.




nums = [7, 2, 9, 3, 5, 1, 8]
print("Аввал:", nums)
for num in nums[:]:
    if num % 2 != 0:
        nums.remove(num)
print(nums)
nums.sort(reverse=True)
print(nums)
nums.extend([10,12])
print(nums)
nums.reverse()
print(nums)