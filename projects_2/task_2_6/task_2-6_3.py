phenotype_d = input("Введите фенотип группы крови донора(I, II, III, IV): ").strip().upper()
phenotype_p = input("Введите фенотип группы крови пациента(I, II, III, IV): ").strip().upper()

if phenotype_d == phenotype_p:
    print("Группа крови совпадает, переливать можно")
elif phenotype_d == "I":
    print("Группа крови донора 0, переливать можно")
elif phenotype_d not in ["I", "II", "III", "IV"] or phenotype_p not in ["I", "II", "III", "IV"]:
    print("Некорректный ввод")
else:
    print("Донор не подходит")
