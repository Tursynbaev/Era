tup = (11, 2, 3, 4, 15, 6, 17, 8, 9, 10)
set_ = set([3, 8, 7, 19, 11])

# Функция len()
print("Количество кортежa:", len(tup))
print("Количество множеств:", len(set_))

# Функция sorted()
print("Отсортированный кортеж:", sorted(tup))
print("Отсортированное множество:", sorted(set_))

# Функция sum()
print("Сумма кортежа:", sum(tup))
print("Сумма множества:", sum(set_))

# Функция any() 
print("Множество содержит элемент 7?", any(x == 7 for x in set_))

# Функция all() 
print("Все элементы кортежа положительные?", all(x > 0 for x in tup))

# 1esep

# import random

# def fill_tuple(n, a, b):
#     return tuple(random.randint(a, b) for _ in range(n))


# tup1 = fill_tuple(10, 0, 5)
# tup2 = fill_tuple(5, -5, 0)

# tup3 = tup1 + tup2

# count_zero = tup3.count(0)


# print("1 кортеж:", tup1)
# print("2 кортеж:", tup2)
# print("3 кортеж:", tup3)
# print("Количество нулей B 3:", count_zero)


# 2esep

# t = (12, (2.14, (1 + 3j, ('qazaqstan', ()))) )

# print(t[1][1][1][0])


# 3esep

# days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

# # Создаем пустой словарь
# rashod = {'Transport': [], 'Obed': [], 'Uzhin': [], 'Drugoe': []}

# # Заполняем словарь 
# for day in days:
#     print('Rashod ', day)
#     rashod['Transport'].append(float(input('Transport: ')))
#     rashod['Obed'].append(float(input('Obed: ')))
#     rashod['Uzhin'].append(float(input('Uzhin: ')))
#     rashod['Drugoe'].append(float(input('Drugoe: ')))

# for category, category_rashod in rashod.items():
#     print('Obwii', category, 'rashod:', sum(category_rashod))


# 4esep

# names = tuple(input("Имена студентов : ").split())

# result = ""

# for name in names:
#     if "ва" in name:
#         result += name + " "

# print("Имена, содержащие 'ва':", result)

# 5esep

# def kazakh_to_latin(text):
   
#     cyrillic = 'АӘБВГҒДЕЁЖ ЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШ ЩЪ ЫІЬЭЮ Я'
#     latin = 'AÁBVGĞDEYoJZIYKQLMNNŊOÖPRSTUÚÜFXHCÇŞShS’YI’’EYúYa'
#     # заменяем кириллические символы на латиницу    
#     for i in range(len(cyrillic)):
#         text = text.replace(cyrillic[i], latin[i])
#     return text

# text = input('Введите текст на казахском языке: ')

# latin_text = kazakh_to_latin(text)

# print('Текст на латинице: ', latin_text)