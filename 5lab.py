# 1esep


students = []

while True:
    name = input(" имя студента (или 'q' для выхода): ")
    if name == 'q':
        break
    grade = int(input(" класс студента: "))
    subject = input(" предмет студента: ")
    students.append((name, grade, subject))

students_sorted = sorted(students, key=lambda student: student[1])

for student in students_sorted:

    print(f"{student[0]} - {student[1]} класс, изучает {student[2]}")


# 2esep


# grades = {
#     'Zakarin': [4, 5, 5, 4],
#     'Baizhanov': [3, 4, 4, 5],
#     'Kosherbaev': [5, 4, 5, 4],
#     'Tursynbaev': [4, 5, 4, 3]
# }

# # Функция, возвращающая оценки ученика
# def get_grades(name):
#     if name in grades:
#         return grades[name]
#     else:
#         return []

# # Запрашиваем имя ученика и выводим его оценки
# name = input(' имя ученика: ')
# student_grades = get_grades(name)

# if student_grades:
#     print(f'Оценки ученика {name}: {student_grades}')
# else:
#     print(f'Ученик {name} не найден')


# 3esep


# numbers = []

# while True:
#     num = int(input("Введите целое число (для завершения введите 0): "))
#     if num == 0:
#         break
#     numbers.append(num)

# sorted_nums = sorted(numbers)

# for num in sorted_nums:
#     print(num)


# 4esep

# numbers = []
# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     numbers.append(num)

# numbers.sort(reverse=True)

# print("Числа в порядке убывания:")
# for num in numbers:
#     print(num)


# 5esep


# import random

# # Выбираем 6 случайных чисел из диапазона от 1 до 49
# numbers = random.sample(range(1, 50), 6)

# # Выводим номера билета в порядке возрастания
# print(sorted(numbers))


# 6esep


# def is_sorted(lst):
#     if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
#         return True
#     elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
#         return True
#     else:
#         return False

# # Запросить у пользователя последовательность чисел для списка
# lst = input("Введите последовательность чисел через пробел: ").split()
# lst = [int(x) for x in lst]

# # Проверить, отсортирован ли список
# if is_sorted(lst):
#     print("Список отсортирован")
# else:
#     print("Список не отсортирован")
