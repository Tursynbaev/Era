# 1esep


# text = "This is a sample string for testing."

# # функция len() - выводит длину строки
# print("Длина строки:", len(text))

# # метод str.upper() - преобразует строку к верхнему регистру
# print("Верхний регистр:", text.upper())

# # метод str.lower() - преобразует строку к нижнему регистру
# print("Нижний регистр:", text.lower())

# # метод str.capitalize() - преобразует первую букву строки к верхнему регистру
# print("Первая буква заглавная:", text.capitalize())

# # метод str.title() - преобразует каждое слово в строке к начальному заглавному регистру
# print("Каждое слово с заглавной буквы:", text.title())

# # метод str.startswith() - возвращает True, если строка начинается с указанной подстроки
# print("Начинается ли строка с 'This'?", text.startswith("This"))

# # метод str.endswith() - возвращает True, если строка заканчивается на указанную подстроку
# print("Заканчивается ли строка на 'testing.'?", text.endswith("testing."))

# # метод str.count() - возвращает количество вхождений указанной подстроки в строке
# print("Сколько раз встречается подстрока 'is'?", text.count("is"))

# # метод str.replace() - заменяет указанную подстроку на другую строку
# new_text = text.replace("sample", "new")
# print("Заменяем 'sample' на 'new':", new_text)

# # метод str.split() - разбивает строку на подстроки по указанному разделителю
# words = text.split(" ")
# print("Слова в строке:", words)


# 2esep


# students = []
# while True:
#     name = input("Введите фамилию ученика (или Enter для завершения): ")
#     if not name:
#         break
#     grade = int(input("Введите класс ученика: "))
#     students.append((name, grade))

# students.sort(key=lambda x: x[1])

# print("Список учеников по возрастанию классов:")
# for student in students:
#     print(f"{student[0]} - {student[1]} класс")


# 3esep


# s = input("Введите строку: ")
# upper_count = 0
# lower_count = 0
# for c in s:
#     if c.isupper():
#         upper_count += 1
#     elif c.islower():
#         lower_count += 1
# if upper_count > lower_count:
#     s = s.upper()
# else:
#     s = s.lower()
# print(s)


# 4esep


# while True:
#     num1 = input("Введите первое число: ")
#     num2 = input("Введите второе число: ")

#     if num1.isdigit() and num2.isdigit():
#         num1 = int(num1)
#         num2 = int(num2)
#         print(f"Сумма чисел: {num1 + num2}")
#         break
#     else:
#         print("Ошибка: необходимо ввести целые числа!")
