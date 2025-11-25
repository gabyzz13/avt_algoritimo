def f(x, y):
    result = []
    for a, b in zip(x, y):
        result.extend([a, b])
    return result

#Usando os exemplos da questão
print(f(["a", "b", "c"], [1, 2, 3]))
