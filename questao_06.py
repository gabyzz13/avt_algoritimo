def f(x=100):
    from itertools import product
    numbrs = "123456789"
    operadores = ["", "+", "-"]
    result = []
    
    for ops in product(operadores, repeat=len(numbrs)-1):
        expr = "".join(num + op for num, op in zip(numbrs, ops + ("",)))
        if eval(expr) == x:
            result.append(expr + "==" + str(x))
    return result

#Usando os exemplos da questão
for eq in f(100):
    print(eq)
