"""
Итоговая утилита memory_report.py
Лабораторная работа № 2. Задание 5 (Практическая часть)
Запускает все измерения задания 5 и выводит сводный отчет.
"""

import sys
import tracemalloc

# ============================================================
# 1. Сбор измерений и сохранение в структуру данных
# ============================================================
scenarios = [
    ("Пустой список []", 0, lambda: []),
    ("Список из 10 чисел", 10, lambda: list(range(10))),
    ("Кортеж из 10 чисел", 10, lambda: tuple(range(10))),
    ("Строка из 10 символов", 10, lambda: "0123456789"),
    ("Целое число 10", 1, lambda: 10),
    ("Объект None", 0, lambda: None),
    ("list(range(100k))", 100_000, lambda: list(range(100_000))),
    ("range(100k)", 100_000, lambda: range(100_000)),
]

results = []

for name, count, creator in scenarios:
    tracemalloc.start()
    obj = creator()
    cur_bytes, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results.append({
        "name": name,
        "count": count,
        "sizeof": sys.getsizeof(obj),
        "cur_kb": cur_bytes / 1024,
        "peak_kb": peak_bytes / 1024,
    })

# ============================================================
# 2. Форматированный вывод сводного отчета
# ============================================================
print("=" * 80)
print(f"{'Сценарий':<25} | {'Элементов':<10} | {'sys.getsizeof':<14} | {'Пик (КБ)':<12}")
print("-" * 80)

for r in results:
    size_str = f"{r['sizeof']} Б"
    print(f"{r['name']:<25} | {r['count']:<10} | {size_str:<14} | {r['peak_kb']:<12.2f}")

print("-" * 80)

# Отношение пикового объема list vs range
list_peak = next(r["peak_kb"] for r in results if "list(range" in r["name"])
range_peak = next(r["peak_kb"] for r in results if r["name"] == "range(100k)")
ratio = list_peak / max(range_peak, 0.001)

print(f"Отношение пикового объема (list vs range): {ratio:.1f}x экономии в пользу range()!")
print("=" * 80)
