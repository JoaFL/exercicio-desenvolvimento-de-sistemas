SENHA = "1234"

tentativa: str = input("Digite a senha: ")

if tentativa == SENHA:
    print("Acesso permitido")
else:
    print("Senha incorreta")