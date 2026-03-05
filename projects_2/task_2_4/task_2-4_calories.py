proteins = input("Масса белков в продукте (г):")
num_p = int(proteins)

fats = input("Масса жиров в продукте (г):")
num_f = int(fats)

carbohydrates = input("Масса углеводов в продукте (г):")
num_c = int(carbohydrates)

#Кал=(Белки×4)+(Жиры×9)+(Углеводы×4)
call = (num_p * 4) + (num_f * 9) + (num_c * 4) 
print(f"каллорийность: {call}")
