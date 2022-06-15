# Задача 1: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print('The result of adding the first and second is', first + second)

print('The result of subtracting the second from the first is', first - second)

print('The result of multiplying the first and second is', first * second)

print('The result of dividing the first by the second is', first / second)

print('The division remainder is', first % second)

print('The exponentiation result for the first and second is', first ** second)

print('The floor division result for the first and second is', first // second)


# Задача 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

comparison_result = first < second
print('first < second ==>', comparison_result)

comparison_result = first > second
print('first > second ==>', comparison_result)

comparison_result = first == second
print('first == second ==>', comparison_result)

comparison_result = first != second
print('first != second ==>', comparison_result)


# Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран.

str1 = "Hello "
str2 = "world"
concatenation_result = str1 + str2
print(concatenation_result)
