from random import random


class Calculadora:

    def __init__(self, numero, numero2):
        self._Numero = numero
        self._Numero2 = numero2

    @property
    def numero(self):
        return self._Numero
    @numero.setter
    def numero(self, numero):
        self._Numero = numero

    @property
    def numero2(self):
        return self._Numero2
    @numero2.setter
    def numero2(self, numero2):
        self._Numero2 = numero2

    #conversões

    #converte de decimal para binário
    def converteBinario(self, numero):
        num = int(numero)
        binario = ""
        while num != 0:
            binario = binario + str(num % 2)
            num = int(num / 2)
        print('\nResultado em BINÁRIO: {}'.format(binario[::-1]))

    # converte de decimal para Octal
    def converteOctal(self, numero):
        num = int(numero)
        octal = ""
        while num != 0:
            octal = octal + str(num % 8)
            num = int(num / 8)
        print('\nResultado em OCTAL: {}'.format(octal[::-1]))

    # converte de decimal para hexadecimal
    def converteHexa(self, numero):
        num = int(numero)
        hexadecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
        resultado = []
        while num > 0:
            resultado.append(hexadecimal[(num % 16)])
            num = num // 16
        print('\nResultado em HEXADECIMAL: ', end='')
        print(''.join(map(str, resultado[::-1])))

    # converte de binário para decimal
    def converteBinDec(self, numero):
        soma = 0
        exp = len(numero) - 1

        for i in range(len(numero)):
            soma = soma + (int(numero[i]) * (2 ** exp))
            exp = exp - 1
        print('\nO valor convertido para decimal é: ' + str(soma))

    # converte de hexadecimal para decimal
    def converteHexDec(self, numero):
        def _getDecDigit(digit):
            digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'A', 'B', 'C', 'D', 'E', 'F']
            for x in range(len(digits)):
                if digit == digits[x]:
                    return x

        def hexToDec(hexNum):
            decNum = 0
            power = 0
            for digit in range(len(hexNum), 0, -1):
                decNum = decNum + 16 ** power * _getDecDigit(hexNum[digit - 1])
                power += 1
            print(str(decNum))

        print('\nO valor convertido para decimal é: ')
        hexToDec(numero)

    #operações
    def somaDecimalBin(self, numero, numero2):
        self.converteBinDec(numero)
        resultadoSoma = int(numero) + int(numero2)
        self.converteBinario(resultadoSoma)

    def somaBinario(self, numero, numero2):
        resultadoSoma = int(numero) + int(numero2)
        self.converteBinario(resultadoSoma)

    def somaHexa(self, numero, numero2):
        resultadoSoma = numero + numero2
        self.converteHexa(resultadoSoma)

    def somaOctal(self, numero, numero2):
        resultadoSoma = numero + numero2
        self.converteOctal(resultadoSoma)

    def subtrairBinario(self, numero, numero2):
        resultadoSubtracao = int(numero) - int(numero2)
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteBinario(resultadoSubtracao)

    def subtrairHexa(self, numero, numero2):
        num = float(numero)
        num2 = float(numero2)
        resultadoSubtracao = numero - numero2
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteHexa(resultadoSubtracao)

    def subtrairOctal(self, numero, numero2):
        resultadoSubtracao = numero - numero2
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteOctal(resultadoSubtracao)

    def multiplicarBinario(self, numero, numero2):
        num = float(numero)
        num2 = float(numero2)
        resultadoMultipliacao = num * num2
        self.converteBinario(resultadoMultipliacao)

    def multiplicarHexa(self, numero, numero2):
        resultadoMultipliacao = numero * numero2
        self.converteHexa(resultadoMultipliacao)

    def multiplicarOctal(self, numero, numero2):
        resultadoMultipliacao = numero * numero2
        self.converteOctal(resultadoMultipliacao)
