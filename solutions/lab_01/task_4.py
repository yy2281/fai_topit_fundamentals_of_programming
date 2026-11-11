student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("Первый символ:", student[0])
print("Последний символ:", student[-1])

print()

print("Имя:", student[:4])
print("Фамилия:", student[5:])

print()

print("Верхний регистр:", student.upper())
print("Нижний регистр:", student.lower())

print()

initials = student[0] + "." + student[5] + "."
print("Инициалы:", initials)

print()

print("Курс наоборот:", course[::-1])

print()

percent = completed / total * 100

print("%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent))

print("{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent))

print(f"{student} — {course}: {completed}/{total} ({percent:.1f}%)")

print()

symbol = "Я"
print("Символ:", symbol)
print("Кодовая позиция (ord):", ord(symbol))
print("Восстановленный символ (chr):", chr(ord(symbol)))
encoded = symbol.encode("utf-8")
print("Байтовое представление (utf-8):", encoded)
print("Длина в байтах:", len(encoded))

print()

print("student[0] = 'О' вызывает TypeError")
