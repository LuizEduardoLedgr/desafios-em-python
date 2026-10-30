import time
class CaixaEletronico:
    def __init__(self, saldo, user, senha, extrato, total_dep, total_sac):
        self.saldo = saldo
        self.user = user
        self.senha = senha
        self.extrato = extrato
        self.total_dep = total_dep
        self.total_sac = total_sac
caixa = CaixaEletronico(1000, 617905, 1234, [], 0, 0)
Q = 1
W = 2
E = 3
R = 4
T = 6
W2 = 5
Q2 = caixa.saldo
A = int(input("qual seu numero de usuario?: "))
if (A == caixa.user):
  B = int(input("digite a sua senha: "))
  if(B == caixa.senha):
    print("verificando user.....")
    time.sleep(3)
    print("usuario validado")
    time.sleep(1.5)
    while True:
      print("=====================")
      print("  CAIXA ELETRONICO")
      print("=====================")
      print("1 - Consultar Saldo")
      print("2 - Depositar")
      print("3 - Sacar")
      print("4 - Alterar Senha")
      print("5 - Verificar Extrato")
      print("6 - Sair")
      Y = int(input("qual a opção desejada?: "))
      if(Y == Q):
        print("procurando seu saldo.....")
        time.sleep(1.5)
        print("seu saldo é de", caixa.saldo)
        time.sleep(1.5)
        resp1 = input("quer voltar ao inicio pressione ENTER, para sair digite N: ")
        if(resp1 == "N"):
          break
      elif(Y == W):
        U = float(input("qual o valor você gostaria de depositar?: "))
        print("depositando.....")
        time.sleep(2)
        if(U < 0):
          print("Não é possivel fazer um deposito de um número negativo!")
        elif(U == 0):
          print("deposite um valor acima de 0!")
        else:
          caixa.saldo = caixa.saldo + U
          caixa.total_dep = caixa.total_dep + U
          time.sleep(1.5)
          print("\n valor depositado com sucesso!")
          time.sleep(1.5)
        #resp2 = input()
          time.sleep(1)
        resp1 = input("quer voltar ao inicio pressione ENTER, para sair digite N: ")
        if(resp1 == "N"):
          break
      elif(Y == E):
        I = float(input("quanto você deseja sacar?: "))
        if(I < 0):
          print("não é possivel realizar um saque negativo!")
        elif(I == 0):
          print("não é possivel sacar o valor de 0 reais!")
        elif(I > caixa.saldo):
          print("não é possivel sacar um valor maior do que o saldo!")
        else:
          caixa.saldo = caixa.saldo - I
          caixa.total_sac = caixa.total_sac + I
          print("sacando.....")
          time.sleep(1.5)
          print("seu saldo agora é de:", caixa.saldo)
          time.sleep(1)
        resp1 = input("quer voltar ao inicio pressione ENTER, para sair digite N: ")
        if(resp1 == "N"):
          break
      elif(Y == R):
        O = int(input("qual sua senha antiga?: "))
        if(O == caixa.senha):
          print("verificando senha.....")
          time.sleep(1.5)
          P = int(input("digite sua nova senha: "))
          caixa.senha = P
          print("atualizando senha.....")
          time.sleep(1.5)
          print("sua senha agora é:", P)
        else:
          print("a senha informada esta incorreta")
        resp1 = input("quer voltar ao inicio do programa S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y < 1 or Y > 6):
        print("opção não existe, por favor escolher uma opção existente!")
        time.sleep(2)
      elif(Y == W2):
        print("carregando extrato bancario.....")
        time.sleep(1.5)
        print("=====================")
        print("  EXTRATO BANCARIO")
        print("=====================")
        print(f"o total depositado foi de: {caixa.total_dep} R$")
        print(f"o total sacado foi de: {caixa.total_sac} R$")
        print(f"seu saldo inicial era de: {Q2} R$")
        print(f"seu saldo atual é de: {caixa.saldo} R$")
        print("=====================")
        time.sleep(3)
        resp1 = input("quer voltar ao inicio do programa S ou N?: ")
        if(resp1 == "N"):
          break
      elif(Y == T):
        print("saindo.....")
        time.sleep(2)
        print("até a proxima!")
        break
  else:
    print("senha incorreta")
else:
  print("usuario incorreto")
