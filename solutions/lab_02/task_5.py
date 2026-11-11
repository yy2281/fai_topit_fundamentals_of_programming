"""
Задание 5. Исследование потребления памяти
Лабораторная работа № 2. Управление объектами и памятью в Python
"""

import sys
import tracemalloc

# ============================================================
# ЧАСТЬ 1: Размер отдельных объектов через sys.getsizeof()
# ============================================================
print("--- Часть 1. Размеры объектов (sys.getsizeof) ---")

print("Пустой список []:          ", sys.getsizeof([]), "байт")
print("Список из 10 чисел:        ", sys.getsizeof(list(range(10))), "байт")
print("Кортеж из 10 чисел:        ", sys.getsizeof(tuple(range(10))), "байт")
print("Строка из 10 символов:     ", sys.getsizeof("0123456789"), "байт")
print("Целое число 10:            ", sys.getsizeof(10), "байт")
print("Объект None:               ", sys.getsizeof(None), "байт")

# ============================================================
# ЧАСТЬ 2: Рост списка (100 append)
# ============================================================
print("\n--- Часть 2. Изменение размера списка при append() ---")

lst = []
prev_size = sys.getsizeof(lst)
print(f"Длина: {len(lst):<3} | Размер: {prev_size:<4} байт (начальный)")

for i in range(1, 101):
    lst.append(i)
    cur_size = sys.getsizeof(lst)
    if cur_size != prev_size:
        print(f"Длина: {len(lst):<3} | Размер: {cur_size:<4} байт (+{cur_size - prev_size} байт)")
        prev_size = cur_size

# ============================================================
# ЧАСТЬ 3: Измерение через tracemalloc
# ============================================================
print("\n--- Часть 3. Измерение через tracemalloc ---")

# Вариант 1: list(range(100_000))
tracemalloc.start()
numbers_list = list(range(100_000))
cur_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Вариант 2: range(100_000)
tracemalloc.start()
numbers_range = range(100_000)
cur_range, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"list(range(100_000)): пик = {peak_list / 1024:.2f} КБ")
print(f"range(100_000):       пик = {peak_range / 1024:.2f} КБ")
ratio = peak_list / max(peak_range, 1)
print(f"Список требует в {ratio:.1f} раз больше памяти, чем range!")
