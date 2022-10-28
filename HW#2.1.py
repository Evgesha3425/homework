"""
Вводятся три целых числа. Определить,
какое из них наибольшее.
"""

# Вариант 1 (Если вводить каждое число на отдельной строке)

a, b, c = int(input()), int(input()), int(input())

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)

# Вариант 2 (Если вводить числа в одну строку)

my_list = [i for i in input().split()]
print(max(my_list))
