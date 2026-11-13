from asyncio import all_tasks

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede tem a dmensão de {}x{} e sua área é de {}m2'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))