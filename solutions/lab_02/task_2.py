import copy


print("--- Исходные структуры ---")
original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print("original:", original, "| id:", id(original), "| id(nested):", id(original[0]), "| id(grade):", id(original[0][1]))
print("alias:   ", alias, "| id:", id(alias), "| id(nested):", id(alias[0]), "| id(grade):", id(alias[0][1]))
print("shallow: ", shallow, "| id:", id(shallow), "| id(nested):", id(shallow[0]), "| id(grade):", id(shallow[0][1]))
print("deep:    ", deep, "| id:", id(deep), "| id(nested):", id(deep[0]), "| id(grade):", id(deep[0][1]))

print("\n--- Модификация 1: original.append(['Databases', 5]) ---")
original.append(["Databases", 5])

print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)

print("\n--- Модификация 2: original[0][1] = 3 ---")
original[0][1] = 3

print("original:", original, "| id(nested):", id(original[0]), "| id(grade):", id(original[0][1]))
print("alias:   ", alias, "| id(nested):", id(alias[0]), "| id(grade):", id(alias[0][1]))
print("shallow: ", shallow, "| id(nested):", id(shallow[0]), "| id(grade):", id(shallow[0][1]))
print("deep:    ", deep, "| id(nested):", id(deep[0]), "| id(grade):", id(deep[0][1]))

print("\n--- Таблица наблюдений ---")
print(f"{'Операция':<22} | {'Новый внешний':<15} | {'Новые вложенные':<16} | {'Изменения независимы'}")
print("-" * 80)
print(f"{'Присваивание':<22} | {'Нет':<15} | {'Нет':<16} | {'Нет (полная зависимость)'}")
print(f"{'Поверхностная копия':<22} | {'Да':<15} | {'Нет':<16} | {'Частично (только добавление в корень)'}")
print(f"{'Глубокая копия':<22} | {'Да':<15} | {'Да':<16} | {'Да (полная изоляция)'}")


print("\n--- Исследование создания матрицы ---")


wrong_matrix = [[0] * 3] * 3
print("Ошибочная матрица до изменения:   ", wrong_matrix)
print("Идентификаторы строк:", id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))

wrong_matrix[0][0] = 1
print("Ошибочная матрица после [0][0]=1: ", wrong_matrix)
print("-> Изменились все строки, так как они ссылаются на один и тот же список!")


correct_matrix = [[0] * 3 for _ in range(3)]
print("\nКорректная матрица до изменения:  ", correct_matrix)
print("Идентификаторы строк:", id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))

correct_matrix[0][0] = 1
print("Корректная матрица после [0][0]=1:", correct_matrix)
print("-> Изменилась только первая строка, так как строки независимы.")

assert wrong_matrix[0] is wrong_matrix[1]
assert correct_matrix[0] is not correct_matrix[1]
assert correct_matrix[0][0] == 1 and correct_matrix[1][0] == 0
