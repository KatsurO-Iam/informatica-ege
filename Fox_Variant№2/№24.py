# 1. Читаем файл
with open('24') as f:
    s = f.read().strip()

# 2. Разбиваем строку на список подстрок, где разделитель — буква F
parts = s.split('F')

max_len = 0

# Если частей меньше 4, значит букв F меньше 3, и условие невыполнимо
if len(parts) >= 4:
    # Итерируемся по списку фрагментов
    # Нам нужно объединить 4 соседних фрагмента (между ними как раз 3 буквы F)
    for i in range(len(parts) - 3):
        # Собираем кусок из 4 фрагментов: parts[i], parts[i+1], parts[i+2], parts[i+3]
        # Длина этого куска будет:
        # сумма длин самих фрагментов + 3 символа 'F', которые мы "выкинули" при split
        current_len = len(parts[i]) + len(parts[i + 1]) + len(parts[i + 2]) + len(parts[i + 3]) + 3

        if current_len > max_len:
            max_len = current_len

print(max_len)
