dna = input("Введите последовательность ДНК: ").upper()

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

length = len(dna)

print(f"=== Анализ последовательности ДНК ===\nПоследовательность в верхнем регистре:{dna}\nПодсчёт нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}\nОбщая длина: {length} нуклеотидов")
