def f(lista, busca):
    for num, nome in lista:
        if num == busca:
            return nome
    return None

#Usando os exemplos da questão
print(f([(18, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (3, 'Daniela')], 15))  
print(f([(187, 'Isabela'), (13, 'João'), (199, 'Karen'), (201, 'Leonardo')], 199))  
