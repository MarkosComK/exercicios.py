print('===========LOJAS SOARES===========')
preco = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTOS')
print('''[ 1 ] À vista dinheiro / cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção: '))
if opcao == 3:
    print(f'O valor será de {preco} em duas parcelas de {preco/2:.2f}R$')
if opcao == 1:
    desconto = preco / 100 * 10
    print(f'O valor das compras com desconto de 10% será de {preco - desconto:.2f}R$')
if opcao == 2:
    desconto = preco / 100 * 5
    print(f'O valor das compras com desconto de 5% será de {preco - desconto:.2f}R$')
if opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = preco / 100 * 20
    print(f'O valor será de {preco + valor}R$ em {parcelas}x parcelas de {(preco + valor) / parcelas}R$ cada')
else:
    print('Opção inválida de pagamento, tente novamente.')