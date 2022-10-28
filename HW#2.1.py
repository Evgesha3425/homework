"""
Вводятся три целых числа. Определить,
какое из них наибольшее.
"""

a, b, c = int(input()), int(input()), int(input())

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)
