km = float(input('Quanto Km seu carro percorreu enquanto você utilizava?'))
dia = float(input('Por quantos dias você alugou o carro?'))

print(f'Você alugou o carro com um total de {int(dia)} diarias e você rodou {km}KM. O valor total '
      f'que você deve pagar é de R${(km * 0.15) + (60 * dia):.5}.'
      f'Obrigado pela escolha!')
