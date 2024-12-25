# "Стиль кода часть II. Цикл While"

# Begin
list_of_numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # Исходные данные
positive_numbers = []                                           # Итоговый список

for my_list in list_of_numbers:
    if my_list < 0:
        break
    if my_list > 0:
        positive_numbers.append(my_list)

print ('Список положительных чисел:', positive_numbers)         # Полученный результат
# End

# Второй вариант решения задачи
# Begin
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # Исходные данные
positive_numbers = []                                   # Итоговый список
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        break
    if numbers[i] > 0:
        positive_numbers.append(numbers[i])
    i += 1
# Полученный результат
print('Список положительных чисел (второй вариант):',positive_numbers)