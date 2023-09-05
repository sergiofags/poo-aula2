def calcularMedia(a, b):
  return (a + b)/2

num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))

media = calcularMedia(num1, num2)

def comparacao(a, b):
  if a > b:
    maior = a
  elif a < b:
    maior = b
  return maior
  
maior = comparacao(num1, num2)

if media < 6:
  num3 = float(input('Digite a terceira nota: '))
  media = calcularMedia(maior, num3)
  
if media > 6:
  print('Aprovado')
else: 
  print('Reprovado')
