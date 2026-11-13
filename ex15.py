aluguel = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos quilometros você rodou?'))
valor = (km * 7) + (aluguel * 15)
print('O total a pagar é {:.2f}'.format(valor))
