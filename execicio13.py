numeros = []

for i in range(3):
    num: int = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)
    
print(f"O maior é: {max(numeros)}")