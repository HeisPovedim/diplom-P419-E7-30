import csv
import random

# Создаем список данных
data = []
for i in range(10):
    x = i
    y = random.randint(0, 100)
    data.append([x, y])

# Записываем данные в файл CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    for row in data:
        writer.writerow(row)