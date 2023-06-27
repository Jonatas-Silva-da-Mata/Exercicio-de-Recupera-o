def calcular_desconto(idd, valor_p):
    if idd < idade_referencial:
        desconto_maior = valor_p * (15/100)
        return desconto_maior
    else:
        desconto_menor = valor_p * (10/100)
        return desconto_menor 

idade = int(input('Digite a sua idade: '))
valor_produto = int(input('Digite o valor do produto: '))
idade_referencial = 21

print(calcular_desconto(idade, valor_produto)) 
