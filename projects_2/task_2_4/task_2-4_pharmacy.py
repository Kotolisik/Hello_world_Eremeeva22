at_all = int(input("Введите общее количество произведенных капсул:"))
in_package = int(input("Введите количество капсул в одной упаковке:"))

num_pac = at_all // in_package
remainder = at_all % in_package

print("--- Отчет фасовочного цеха ---")
print(f"полных упаковок:\t{num_pac}\nостаток капсул: \t{remainder}")
