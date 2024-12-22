# А.Мудрицкий. "Условная конструкция. Операторы if, elif, else"

# Begin
first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
print ('Отлично, проверяем результат: ')

if first == second and first == third:
    print ('Третье число: ', third)

elif first == second or second == third or first == third:
    print ('Второе число: ', second)

elif first != second and second != third and first != third:
    print ('Среди введенных чисел равных нет: ', 0)
# End
