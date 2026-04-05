#8- Crie um programa que receba a nota de um aluno e mostre:
#•	Aprovado se a nota for maior ou igual a 7
#•	Reprovado caso contrário.
nota: int = int(input("Digite sua nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado!")
elif nota >= 0 and nota <= 7:
    print("Reprovado!")
else:
    print("Nota inválida")
