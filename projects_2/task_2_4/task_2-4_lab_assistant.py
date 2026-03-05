volume = float(input("введите объем:"))
salt_mass = volume * 0.009
salt_mass_r = round(salt_mass, 2)

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\nОбщий объем: \t{volume} мл\nМасса соли: \t{salt_mass_r} г\nОбъем воды: \t{volume} мл")
