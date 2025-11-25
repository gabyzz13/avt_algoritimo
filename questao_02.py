def f(nums):
    n = len(nums)
    soma_esperada = n * (n + 1) // 2
    soma_real = sum(nums)
    
    vistos = set()
    for num in nums:
        if num in vistos:
            double = num
            break
        vistos.add(num)
    
    missing = soma_esperada - (soma_real - double)
    
    return (double, missing)

#Usando os exemplos da questão
print(f([1, 2, 2, 4]))
print(f([1, 1]))
