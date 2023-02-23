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

# A = 15
# B = 5

# # Находим ближайшее меньшее нечётное число, которое больше B
# if B % 2 == 0:
#     B += 1
# else:
#     B += 2

# # Выводим все нечётные числа от A до B включительно в порядке убывания
# while A >= B:
#     print(A)
#     A -= 2

N = int(input())
sum_all = (N * (N + 1)) // 2
sum_cards = 0

for i in range(1, N):
    sum_cards += int(input())

lost_card = sum_all - sum_cards
print(lost_card)