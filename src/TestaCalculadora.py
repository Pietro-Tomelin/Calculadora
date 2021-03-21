from src.Calculadora import Calculadora

def main():

    numero = str(input('Informe o primeiro número: '))
    numero2 = str(input('Informe o segundo número: '))

    calc = Calculadora(numero, numero2)

    base = 0  # 1-Decimal/Binario | 2=Decimal/Hexadecimal | 3-Decimal/Octal | 4-Binario/Decimal | 5-Hexadecimal/Decimal
    while base != 5:
        try:
            base = int(input('\nSelecione uma das opções abaixo: '
                              '\n1 - Converter DECIMAL para BINÁRIO'
                              '\n2 - Converter DECIMAL para HEXADECIMAL'
                              '\n3 - Converter DECIMAL para OCTAL'
                              '\n4 - Converter BINÁRIO para DECIMAL'
                              '\n5 - Converter HEXADECIMAL para DECIMAL '
                              '\n'))

            if (base == 1):
                calc.converteBinario(numero)
                calc.converteBinario(numero2)
                break

            elif (base == 2):
                calc.converteHexa(numero)
                calc.converteHexa(numero2)
                break

            elif (base == 3):
                calc.converteOctal(numero)
                calc.converteOctal(numero2)
                break

            elif (base == 4):
                calc.converteBinDec(numero)
                calc.converteBinDec(numero2)
                break

            elif (base == 5):
                calc.converteHexDec(numero)
                calc.converteHexDec(numero2)
                break

            elif (base > 5):
                print('\nOpção inválida!')

        except:
            print('\nFavor informar uma opção válida (1, 2, 3, 4 ou 5).')
            main()

    expressao = 0  # 1-Decimal/Binario | 2=Decimal/Hexadecimal | 3-Decimal/Octal | 4-Binario/Decimal | 5-Hexadecimal/Decimal
    while expressao != 5:
        try:
            expressao = int(input('\nSelecione uma das opções abaixo'
                              '\n1 - Somar'
                              '\n2 - Subtrair'
                              '\n3 - Multiplcar'
                              '\n4 - Retornar ao Início'
                              '\n5 - Encerrar'
                              '\n'))

            if (expressao == 1):
                if (base == 1):
                    calc.somaBinario(numero, numero2)
                elif (base == 2 or base == 5):
                    calc.somaHexa(numero, numero2)
                elif (base == 3):
                    calc.somaOctal(numero, numero2)
                elif (base == 4):
                    calc.somaDecimalBin(numero, numero2)

            elif (expressao == 2):
                if (base == 1 or base == 4):
                    calc.subtrairBinario(numero, numero2)
                elif (base == 2 or base == 5):
                    calc.subtrairHexa(numero, numero2)
                elif (base == 3):
                    calc.subtrairOctal(numero, numero2)

            elif (expressao == 3):
                if (base == 1 or base == 4):
                    calc.multiplicarBinario(numero, numero2)
                elif (base == 2 or base == 5):
                    calc.multiplicarHexa(numero, numero2)
                elif (base == 3):
                    calc.multiplicarOctal(numero, numero2)

            elif (expressao == 4):
                main()

            elif (base > 5):
                print('\nOpção inválida!')

        except:
            print('\nFavor informar uma opção válida (1, 2, 3, 4 ou 5).')
            main()

if __name__ == '__main__':
    main()