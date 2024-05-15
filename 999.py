import csv

total_cost = 0
shopping_list = []

with open('pokupki.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 3:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            total_cost += quantity * price
            shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")

print("Нужно купить:")
for item in shopping_list:
    print(item)

print(f"Итоговая сумма: {total_cost} руб.")
