saldo = 1000
user = 617905
senha = 1234
Q = 1
W = 2
E = 3
R = 4
T = 5
A = int(input("qual seu numero de usuario?: "))
if (A == user):
  B = int(input("digite a sua senha: "))
  if(B == senha):
    while True:
      print("=====================")
      print("  CAIXA ELETRONICO")
      print("=====================")
      print("1 - Consultar saldo")
      print("2 - Depositar")
      print("3 - Sacar")
      print("4 - Alterar senha")
      print("5 - Sair")
      Y = int(input("qual a opção desejada?: "))
      if(Y == Q):
        print("seu saldo é de", saldo)
        resp1 = input("quer voltar ao inicio do programa? S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y == W):
        U = float(input("qual o valor você gostaria de depositar?: "))
        if(U < 0):
          print("Não é possivel fazer um deposito de um número negativo!")
        elif(U == 0):
          print("deposite um valor acima de 0!")
        else:
          saldo = saldo + U
          print("seu saldo agora é de {saldo}$")
        resp1 = input("quer voltar ao inicio do programa? S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y == E):
        I = float(input("quanto você deseja sacar?: "))
        if(I < 0):
          print("não é possivel realizar um saque negativo!")
        elif(I == 0):
          print("não é possivel sacar o valor de 0 reais!")
        elif(I > saldo):
          print("não é possivel sacar um valor maior do que o saldo!")
        else:
          saldo = saldo - I
          print("seu saldo agora é de:", saldo)
        resp1 = input("quer voltar ao inicio do programa? S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y == R):
        O = int(input("qual sua senha antiga?: "))
        if(O == senha):
          P = int(input("digite sua nova senha: "))
          senha = P
          print("sua senha agora é:", P)
        else:
          print("a senha informada esta incorreta")
        resp1 = input("quer voltar ao inicio do programa? S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y == T):
        print("até a proxima!")
        break
    else:
      print("senha incorreta")
  else:
      print("usuario incorreto")