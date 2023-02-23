# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)
# count = 0
# while count < 5:
#   print(count)
#   count += 1
# for i in range(5):
#   print(i)
# for i in range(2, 8, 2):
#   print(i)
# numbers = list(range(5))
# print(numbers)

# import random
# random_number = random.randint(1, 10)
# print("Random number between 1 and 10:", random_number)
# import random
# random_number = random.randrange(1, 11, 2)
# print("Random odd number between 1 and 10:", random_number)
# import random
# random_float = random.random()
# print("Random float between 0 and 1:", random_float)

# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#   print(index, fruit)
# A = int(input("first number: "))
# B = int(input("second number: "))
# for i in range(A, B + 1):
#   print(i)

# A = int(input(" first number: "))
# B = int(input(" second number: "))
# if A < B:
#   for i in range(A, B + 1):
#     print(i)
# else:
#   for i in range(A, B - 1, -1):
#     print(i)

# A = int(input(" first number: "))
# B = int(input(" second number: "))
# for i in range(A - (A + 1) % 2, B - 1, -2):
#   print(i)
# n = int(input())
# sum_n = n * (n + 1) // 2
# sum_lost = 0
# for i in range(n - 1):
#     x = int(input())
#     sum_lost += x
# print(sum_n - sum_lost)