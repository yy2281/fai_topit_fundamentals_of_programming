"""
Задание 5. Информационная карточка вычислительного эксперимента
Программа запрашивает у пользователя данные об эксперименте,
выполняет вычисления и выводит карточку.
"""
researcher = input("Введите имя исследователя: ")
experiment = input("Введите название эксперимента: ")
runs = int(input("Количество выполненных запусков: "))
duration = float(input("Длительность одного запуска (сек): "))
real_part = float(input("Действительная часть комплексного коэффициента: "))
imag_part = float(input("Мнимая часть комплексного коэффициента: "))

total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(real_part, imag_part)
mod_squared = real_part ** 2 + imag_part ** 2
has_runs = bool(runs)

print()

print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {mod_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")

print()

print("    Диагностика типов")
print(f"researcher:  {type(researcher)}")
print(f"experiment:  {type(experiment)}")
print(f"runs:        {type(runs)}")
print(f"duration:    {type(duration)}")
print(f"real_part:   {type(real_part)}")
print(f"imag_part:   {type(imag_part)}")
