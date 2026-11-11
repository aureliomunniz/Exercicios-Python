n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
n3 = float(input('Digite a nota 3:'))
media = (n1 + n2 + n3) / 3
print('Sua média é: {}'.format(media))
if media >= 6:
    (print('Aprovado'))
elif media >= 4:
    print('Recuperação')
else:
    (print('Reprovado'))