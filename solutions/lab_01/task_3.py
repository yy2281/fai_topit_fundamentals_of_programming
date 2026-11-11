import math

print("=" * 50)
print("Эксперимент A. int и арифметические операторы")
print("=" * 50)

x = 17
y = 5

print(f"x + y  = {x + y}, тип: {type(x + y)}")
print(f"x - y  = {x - y}, тип: {type(x - y)}")
print(f"x * y  = {x * y}, тип: {type(x * y)}")
print(f"x / y  = {x / y}, тип: {type(x / y)}")
print(f"x // y = {x // y}, тип: {type(x // y)}")
print(f"x % y  = {x % y}, тип: {type(x % y)}")
print(f"x ** y = {x ** y}, тип: {type(x ** y)}")



print()

print("=" * 50)
print("Эксперимент B. Большие целые числа")
print("=" * 50)

big = 2 ** 1000
print(f"2 ** 1000 = {big}")
print(f"Тип: {type(big)}")

print()

print("=" * 50)
print("Эксперимент C. float")
print("=" * 50)

result = 0.1 + 0.2

print(f"0.1 + 0.2 = {result}")
print(f"result == 0.3: {result == 0.3}")
print(f"result - 0.3 = {result - 0.3}")
print(f"math.isclose(result, 0.3): {math.isclose(result, 0.3)}")

print()

print("=" * 50)
print("Эксперимент D. bool, complex и преобразование типов")
print("=" * 50)

print(f'int("42")       = {int("42")}, тип: {type(int("42"))}')
print(f'float("3.14")   = {float("3.14")}, тип: {type(float("3.14"))}')
print(f'str(2026)       = {str(2026)!r}, тип: {type(str(2026))}')
print(f'bool(0)         = {bool(0)}, тип: {type(bool(0))}')
print(f'bool(-1)        = {bool(-1)}, тип: {type(bool(-1))}')
print(f'bool("")        = {bool("")}, тип: {type(bool(""))}')
print(f'bool("False")   = {bool("False")}, тип: {type(bool("False"))}')


z = complex(2, -3)
print(f'complex(2, -3)  = {z}, тип: {type(z)}')
print(f'  Действительная часть: {z.real}')
print(f'  Мнимая часть:         {z.imag}')
