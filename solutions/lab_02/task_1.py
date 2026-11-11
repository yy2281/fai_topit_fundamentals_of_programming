import copy


print("--- Эксперимент A. Неизменяемый объект ---")
a = 10
b = a

print("До изменения:")
print("a =", a, "b =", b)
print("id(a) =", id(a), "id(b) =", id(b))
print("a is b:", a is b)

a += 1

print("\nПосле a += 1:")
print("a =", a, "b =", b)
print("id(a) =", id(a), "id(b) =", id(b))
print("a is b:", a is b)
print("Значение b не изменилось, так как int неизменяем и создан новый объект.")


print("\n--- Эксперимент B. Изменяемый объект ---")
first = [10, 20]
second = first

print("До изменения:")
print("first =", first, "second =", second)
print("id(first) =", id(first), "id(second) =", id(second))

second.append(30)

print("\nПосле second.append(30):")
print("first =", first, "second =", second)
print("id(first) =", id(first), "id(second) =", id(second))


second = [10, 20, 30]
print("\nПосле переназначения second = [10, 20, 30]:")
print("first =", first, "second =", second)
print("id(first) =", id(first), "id(second) =", id(second))


print("first == second:", first == second)
print("first is second:", first is second)


second.append(40)
print("\nПосле second.append(40):")
print("first =", first)
print("second =", second)
print("Не повлияло")


print("\n--- Практическая задача: Конфигурации проекта ---")


config_orig = {
    "name": "Проект Alpha",
    "participants": ["Алиса", "Боб"],
    "launch_params": [["mode", "debug"], ["threads", 4]],
}


config_alias = config_orig
config_alias["participants"].append("Чарли")
print("После изменения через псевдоним:")
print("  config_orig participants :", config_orig["participants"])
print("  config_alias participants:", config_alias["participants"])
print("Из-за общего объекта изменился и оригинал")


config_orig["participants"] = ["Алиса", "Боб"]


config_independent = copy.deepcopy(config_orig)
config_independent["name"] = "Проект Beta"
config_independent["participants"].append("Дмитрий")
config_independent["launch_params"][0][1] = "release"

print("\nСостояние конфигураций после независимого изменения:")
print("Оригинал:   ", config_orig)
print("Новая копия:", config_independent)


assert config_orig["name"] == "Проект Alpha"
assert config_orig["participants"] == ["Алиса", "Боб"]
assert config_independent["participants"] == ["Алиса", "Боб", "Дмитрий"]
assert config_orig["launch_params"][0][1] == "debug"
assert config_independent["launch_params"][0][1] == "release"
assert config_orig is not config_independent
assert config_orig["participants"] is not config_independent["participants"]
assert config_orig["launch_params"][0] is not config_independent["launch_params"][0]

print("\nИтог связей объектов:")
print("  Словарь конфигурации:  ", "ОБЩИЙ" if config_orig is config_independent else "НЕЗАВИСИМЫЙ")
print("  Список участников:     ", "ОБЩИЙ" if config_orig["participants"] is config_independent["participants"] else "НЕЗАВИСИМЫЙ")
print("  Вложенные параметры:   ", "ОБЩИЙ" if config_orig["launch_params"][0] is config_independent["launch_params"][0] else "НЕЗАВИСИМЫЙ")
