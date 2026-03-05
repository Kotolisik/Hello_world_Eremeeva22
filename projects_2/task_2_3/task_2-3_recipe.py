name_of_the_nutrient_medium = input("введите питательную среду:")
agar_concentration = input("введите концентрацию(%):") 
sterilization_temperature = input("введите температуру стерилизации(с):")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{name_of_the_nutrient_medium}\n{agar_concentration}\n{sterilization_temperature}")
print("Файл 'recipe.txt' успешно сформирован!")
