def main():

    hexadecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    numero = int(input("Digite um número inteiro: "))
    resultado = []
    while numero > 0:
        resultado.append(hexadecimal[(numero % 16)])
        numero = numero // 16
    for r in range(len(resultado) - 1, -1, -1):
        print(resultado[r], end="")

if __name__ == "__main__":
    main()