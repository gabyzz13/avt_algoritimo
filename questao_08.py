def f(nums):
    n = len(nums)
    result = [1] * n
    
    prfx = 1
    for i in range(n):
        resultado[i] = sfx
        prfx *= nums[i]
    
    sfx = 1
    for i in range(n-1, -1, -1):
        result[i] *= sfx
        sfx *= nums[i]
    
    return result

#Usando os exemplos da questão
print(f([1,2,4,6]))
print(f([-1,0,1,2,3]))
