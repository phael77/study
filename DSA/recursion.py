def countdown(x):
    if x > 0:
        print(x)
        return countdown(x - 1)
    print(0)

x = int(input("Digite o seu numero aqui: "))
countdown(x)