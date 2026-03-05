weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (см): "))

bmi = weight / ((height / 100) ** 2)

print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height} см\nВес:\t{weight} кг\nИндекс массы тела:  {bmi:.3f}") 
