import sys
import weakref


class Record:
    pass



print("--- Эксперимент со счетчиком ссылок ---")

data = [1, 2, 3]
c1 = sys.getrefcount(data)
print("После создания:              ", c1)

alias = data
c2 = sys.getrefcount(data)
print("После создания alias:        ", c2)

container = [data]
c3 = sys.getrefcount(data)
print("После помещения в контейнер: ", c3)

del alias
c4 = sys.getrefcount(data)
print("После del alias:             ", c4)

container.clear()
c5 = sys.getrefcount(data)
print("После очистки контейнера:    ", c5)

assert c2 == c1 + 1
assert c3 == c2 + 1
assert c4 == c3 - 1
assert c5 == c4 - 1


print("\n--- Эксперимент со слабой ссылкой ---")

record = Record()
weak_record = weakref.ref(record)

print("Слабая ссылка создана:    ", weak_record())
del record
print("После del record:         ", weak_record())
print("-> Объект уничтожен, так как слабые ссылки не удерживают его в памяти.")



print("\n--- Практическая задача: Реестр WeakValueDictionary ---")

registry = weakref.WeakValueDictionary()

r1 = Record()
r2 = Record()
temp_r3 = Record()

registry["user1"] = r1
registry["user2"] = r2
registry["user3"] = temp_r3

print("1. Исходный состав реестра:      ", list(registry.keys()))
assert len(registry) == 3

del temp_r3
print("2. После удаления del temp_r3:   ", list(registry.keys()))
assert "user3" not in registry
assert len(registry) == 2

del r1
print("3. После удаления del r1:        ", list(registry.keys()))
assert "user1" not in registry
assert len(registry) == 1

print("-> Слабый словарь автоматически очистился от удаленных объектов.")
