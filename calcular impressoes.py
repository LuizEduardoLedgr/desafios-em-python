P = 75
B = 65
C = 74
TF = float(input("quantas gramas de filamento seu pedido pede?: "))
CF = str(input("Qual a cor do filamento? (P - preto, B - branco, C - cinza): "))
if(CF == "P"):
  CF = P
elif(CF == "B"):
  CF = B
else:
  CF = C
fil_grama = 1000
taxa_ene = 0.002
TE = float(input("quanto tempo em minutos sua impressão vai demorar?: "))
CalF = (float(TF * CF) / fil_grama)
CalE = (float(TE * taxa_ene))
CalT = CalF + CalE
if(TF <= 9):
  preco_venda = CalT * 5
elif(TF <= 25):
  preco_venda = CalT * 4
elif(TF <= 50):
  preco_venda = CalT * 3
elif(TF <= 65):
  preco_venda = CalT * 2.5
elif(TF <= 90):
  preco_venda = CalT * 2
elif(TF > 90):
  preco_venda = CalT * 1.5
print("o total de gasto é de: ", CalT)
print("o preço final seria de", preco_venda)