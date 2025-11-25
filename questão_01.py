def f(nums, goal):
    vistos = {}
    
    for i, num in enumerate(nums):
        comp = goal - num
        if comp in vistos:
            return (vistos[comp], i)
        vistos[num] = i

#Usando os exemplos da questão
print(f([2, 7, 11, 15], 9))
print(f([3, 2, 4], 6))
print(f([3, 3], 6))
