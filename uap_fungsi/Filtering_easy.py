ganjil_generator = (x for x in range(51) if x % 2 != 0)

kelipatan_3 = list(filter(lambda x: x % 3 == 0, ganjil_generator))

print(kelipatan_3)
