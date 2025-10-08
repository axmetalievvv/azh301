price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for weight in range(1, 11):
    kg = weight / 10
    cost = kg * price_per_kg
    print(f"{kg:.1f} кг конфет стоит {cost:.2f}")