# 📌 Задача 2: Работа с копиями
# Дан список:

# nums = [1, 2, 3, 2, 4, 2]
# Задания:

# Создай копию этого списка в переменную nums_copy.

# Посчитай, сколько раз встречается число 2.

# Удали первое вхождение 2 из оригинального списка.

# Выведи оба списка  .

# sharti 1

# nums = [1, 2, 3, 2, 4, 2]
# nums1=nums.copy()
# print(nums)
# print(nums1)


# sharti 2

# nums = [1, 2, 3, 2, 4, 2]
# k=nums.count(2)
# print(k)



# sharti umumi

nums = [1, 2, 3, 2, 4, 2]
print(nums)
nums1=nums.copy()
print(nums1)
k=nums.count(2)
print(k)
nums.remove(2)
print(nums)


