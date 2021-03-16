materia = input('Digite a materia ')
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))

media = (nota1 + nota2 + nota3)/ 3


# o ponto depois da media e para eu escolher quantos digitos fiquem no numero

print(f'na materia {materia} a media final ficou {media:.2}')