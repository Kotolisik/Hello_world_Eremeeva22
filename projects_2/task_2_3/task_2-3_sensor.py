operator_name = input("ввдете имя оператора:")
current_pressure_value = input("введите текущее значение давления(Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as table:
    table.write(f"оператор: {operator_name}\tзначение: {current_pressure_value}")
print("Данные успешно сохранены в sensor_log.txt")
