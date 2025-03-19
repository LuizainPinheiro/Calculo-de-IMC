def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso adequado"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    peso = float(input("Digite o seu peso (em kg, exemplo: 50):"))
    altura = float(input("Digite a sua altura (em metros, exemplo: 1.70): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Sua classificação é: {classificacao}")

if __name__ == "__main__":
    main()
