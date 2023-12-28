def sisagold(a, b):
    return a - b

def kurang(a, b):
    return a - b

def apply_function_with_params(func, param_func, a, b):
    return func(param_func(a, b))

# Contoh penggunaan:
hasil = apply_function_with_params(sisagold, kurang, 431, 10)
print(hasil)
