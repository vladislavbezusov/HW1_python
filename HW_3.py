# Найти НОК двух чисел
# import math

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))

# def lcm(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# def mcd(n,m):
#     return (n/lcm(n,m))*m  
# print(int(mcd(a,b)))    

# ************************************************************************************************

# Составить список простых множителей натурального числа N

# n = int(input('Введите число: '))

# def primfacs(n):
#     i = 2
#     arr = []
#     while i*i<=n:
#         while n%i == 0:
#             arr.append(i)
#             n = n/i
#         i += 1
#     if n > 1:
#         arr.append(n)
#     return arr 

# print(primfacs(n))     

# ************************************************************************************************

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [1, 2, 2, 3, 3, 3, 6, 10]

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(numbers)
print(get_unique_numbers(numbers))

