"""
Задание 4. Циклические ссылки и сборщик мусора
Лабораторная работа № 2. Управление объектами и памятью в Python
"""

import gc

# ============================================================
# ЭКСПЕРИМЕНТ 1: Цикл из двух списков
# ============================================================
print("--- Эксперимент с циклом из двух списков ---")

print("Состояние GC (включен?):   ", gc.isenabled())
print("Пороги поколений:           ", gc.get_threshold())
print("Счетчики поколений:         ", gc.get_count())

first = []
second = []
first.append(second)
second.append(first)

print("first ссылается на second: ", first[0] is second)
print("second ссылается на first: ", second[0] is first)
print("id(first):", id(first), "id(second):", id(second))

del first
del second

collected = gc.collect()
print("Ручной вызов gc.collect() собрал объектов:", collected)
assert collected >= 2

# ============================================================
# ЭКСПЕРИМЕНТ 2: Работа при отключенном GC
# ============================================================
print("\n--- Эксперимент при отключенном GC ---")

gc.disable()
print("Сборщик отключен: gc.isenabled() =", gc.isenabled())

# Создаем 5 циклических пар
a, b = None, None
for _ in range(5):
    a = []
    b = []
    a.append(b)
    b.append(a)

del a
del b

print("Счетчики поколений до сбора:", gc.get_count())
collected_disabled = gc.collect()
print("Собрано циклических объектов:", collected_disabled)

gc.enable()
print("Сборщик включен:  gc.isenabled() =", gc.isenabled())

# ============================================================
# ПРАКТИЧЕСКАЯ ЗАДАЧА: Модель графа
# ============================================================
print("\n--- Практическая задача: Модель графа ---")

# Чистим мусор перед экспериментом
gc.collect()
before_count = gc.collect()

# Циклические узлы: A -> B -> C -> A
node_a = {"id": "Node_A", "neighbors": []}
node_b = {"id": "Node_B", "neighbors": []}
node_c = {"id": "Node_C", "neighbors": []}

node_a["neighbors"].append(node_b)
node_b["neighbors"].append(node_c)
node_c["neighbors"].append(node_a)

# Независимый узел D
node_d = {"id": "Node_D", "data": "Independent", "neighbors": []}

print("Связи графа:")
print(f"  {node_a['id']} -> {[n['id'] for n in node_a['neighbors']]}")
print(f"  {node_b['id']} -> {[n['id'] for n in node_b['neighbors']]}")
print(f"  {node_c['id']} -> {[n['id'] for n in node_c['neighbors']]}")
print(f"  {node_d['id']} -> {[n['id'] for n in node_d['neighbors']]} (НЕЗАВИСИМЫЙ)")

# Удаляем только циклические узлы
del node_a
del node_b
del node_c

collected_graph = gc.collect()
print(f"Собрано объектов после разрыва цикла: {collected_graph}")

print("Состояние независимого узла:", node_d)
assert node_d["id"] == "Node_D"
print("-> Независимый узел остался доступен и не пострадал.")
