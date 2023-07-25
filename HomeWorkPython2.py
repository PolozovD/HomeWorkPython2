# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random
# n = int(input("Input number of coins: "))
# arr = [random.randint(0, 1) for _ in range(n)]
# print(arr)

# heads = 0
# tails = 0
# for i in arr:
#     if i == 0:
#         heads += 1
#     else:
#         tails += 1
# print (heads, tails)

# if heads > tails:
#     print(f'Need to flip {tails} coins')
# elif heads == tails:
#     print(f'Need to flip {heads} coins')
# else:
#     print(f'Need to flip {heads} coins')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# s = int(input("Input sum of two numbers X + Y: "))
# p = int(input("Input the product of two numbers X * Y: "))

# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y and x > 0 and x <= 1000 and y > 0 and y <= 1000:
#             print(f'The number X ="{x}", the number Y ="{y}"') 
# # По условиям задачи Петя сначала загадывает числа и подразумевается, что не может ошибаться, поэтому нет проверки на ошибку Пети.


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Input N: "))
# k = 1
# while k <= n:
#     print(k, end = ' ')
#     k = k * 2



# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

# from decimal import *
# n = input("Input N: ")
# numDec = Decimal(str(n))
# print(numDec)

# remains = numDec % 1
# intNum = numDec // 1

# sumIntNum = 0

# while intNum > 0:
#     digit = intNum % 10
#     sumIntNum += digit
#     intNum //= 10

# temp = 0
# sumRemains = 0

# while (remains * 10) % 1 != 0:
#         digit1 = (remains * 10) // 1
#         sumRemains += digit1
#         temp += 1
#         remains = (remains * 10) % 1

# for i in range (temp + 1):
#         digit1 = (remains * 10) // 1
#         sumRemains += digit1
#         remains = (remains * 10) % 1

# print(sumIntNum, sumRemains)
# print(f'Sum of all num of number N is {sumIntNum + sumRemains}')



# задача Де моргана необязательная
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!





# задача 3 необязательная

# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).


# num = int(input("Введите число: "))
# newList = []

# for i in range(1, num+1):
#     if num % i == 0:
#         newList.append(i)

# print (newList)