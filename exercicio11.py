total = []

for i in range(5):
    numero: float = float(input(f"Digite o {i + 1}º número: "))
    total.append(numero)
    
soma = 0   
for num in total:
    soma += num
    
print(soma)