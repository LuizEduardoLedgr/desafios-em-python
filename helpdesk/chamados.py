import time
class Chamado:
  def __init__(self, id, user, desc, cat, prior, resp):
    self.id = id
    self.user = user
    self.desc = desc
    self.cat = cat
    self.prior = prior
    self.resp = resp
    self.status = "Aberto"
cha1 = Chamado(1, "João", "Computador Não Liga", "Hardware", "Urgente", "Luiz")
cha2 = Chamado(2, "Pedro", "Erro de Conexão", "Rede", "Urgente", "Yago")
cha3 = Chamado(3, "Henrique", "Monitor com falhas", "Hardware", "Medio", "Luiz")
Chamados = []
Chamados.extend([cha1, cha2, cha3])
while True:
  print("====================================")
  print("        CENTRAL DE CHAMADOS")
  print("====================================")
  print("1 - Registrar um novo chamado")
  print("2 - Procurar chamados em abertos")
  print("3 - Ver chamados concluidos")
  print("4 - Resolver chamados")
  print("5 - Consultar chamado por responsavel")
  print("6 - Consulta de chamados por prioridades")
  print("7 - Consultar chamado pelo ID")
  print("8 - Total de chamados")
  print("9 - Sair")
  print("====================================")
  opcao = int(input("Escolha uma opção: "))
  if(opcao == 1):
    nome = input("Digite o seu nome: ")
    desp = input("Descreva seu problema: ")
    cate = input("Qual a categoria do seu chamado?: ")
    while True:
      print("============================")
      print("   ESCOLHA A PRIORIDADE")
      print("============================")
      print("1 - Urgente")
      print("2 - Medio")
      print("3 - Leve")
      opcao2 = int(input("Escolha uma opção: "))
      if(opcao2 == 1):
        prioridade = "Urgente"
        break
      elif(opcao2 == 2):
        prioridade = "Medio"
        break
      elif(opcao2 == 3):
        prioridade = "Leve"
        break
      else:
        print("escolha um correto")
    while True:
      print("=========================")
      print("  ESCOLHA O RESPONSAVEL")
      print("=========================")
      print("1 - Luiz")
      print("2 - Otavio")
      print("3 - Yago")
      opcao3 = int(input("Qual responsavel você escolhe?: "))
      if(opcao3 == 1):
        respo = "Luiz"
        break
      elif(opcao3 == 2):
        respo = "Otavio"
        break
      elif(opcao3 == 3):
        respo = "Yago"
        break
      else:
        print("Escolha uma opção existente!")
    novo_id = Chamados[-1].id + 1
    novo_chamado = Chamado(novo_id, nome, desp, cate, prioridade, respo)
    Chamados.append(novo_chamado)
  elif(opcao == 2):
    encontrou = False
    for c in Chamados:
      print("================================================")
      if(c.status == "Aberto"):
        print(f"| {c.id} | {c.user} | {c.desc} | {c.cat}")
        encontrou = True
    if(encontrou == False):
      print("Nenhum chamados aberto!")
    time.sleep(1.5)      
  elif(opcao == 3):
    encontrou = False
    for c in Chamados:
      if(c.status == "Concluido"):
        print(f"| {c.id} | {c.user} | {c.desc} | {c.cat}")
        encontrou = True
        time.sleep(2)
    if(encontrou ==False):
      print("Nenhum chamado com status de concluido!")
      time.sleep(2)
    print("retornando ao menu.....")
    time.sleep(2)
  elif(opcao == 4):
    encontrou = False
    for c in Chamados:
        if(c.status == "Aberto"):
            print("=========================================")
            print(f"| {c.id} | {c.user} | {c.desc} | {c.cat}")
            encontrou = True
    if(encontrou == True):
        resp1 = int(input("\nDigite o id do chamado desejado: "))
        resolvido = False
        id_encontrado = False
        for c in Chamados:
            if(resp1 == c.id):
                id_encontrado = True
                if(c.status == "Aberto"):
                    conf = input("Para concluir, digite CONCLUIDO: ")
                    if(conf == "CONCLUIDO"):
                        c.status = "Concluido"
                        print("Chamado concluído!")
                        resolvido = True
                    else:
                        print("O chamado não foi fechado!")
                else:
                    print("Esse chamado já foi concluído!")
        if(id_encontrado == False):
            print("Nenhum ID foi encontrado!")
    else:
        print("Nenhum chamado em aberto!")
  elif(opcao == 9):
    print("Até a proxima!")
    break
  elif(opcao == 5):
    escolha = (input("Digite o nome do responsavel: "))
    encontrou = False
    for c in Chamados:
      if(escolha == c.resp):
        encontrou = True
        if(encontrou == True):
          time.sleep(2)
          print(f" | {c.id} | {c.user} | {c.desc} | {c.cat} | {c.resp} | {c.status}")
          time.sleep(2)
    if(encontrou == False):
      print("Nenhum usuario com esse rensponsavel foi encontrado")
      time.sleep(2)
  elif(opcao == 6):
      print("============================")
      print("   ESCOLHA A PRIORIDADE")
      print("============================")
      print("1 - Urgente")
      print("2 - Medio")
      print("3 - Leve")
      opcao0 = int(input("Qual a prioridade escolhida?: "))
      if(opcao0 == 1):
        escolha = "Urgente"
      elif(opcao0 == 2):
        escolha = "Medio"
      elif(opcao0 == 3):
        escolha = "Leve"
      else:
        print("Opção inválida!")
        continue
      encontrou = False
      for c in Chamados:
        if(escolha == c.prior and c.status == "Aberto"):
          encontrou = True
          print(f" | {c.id} | {c.user} | {c.desc} | {c.cat} | {c.resp} | {c.status}")
      if(encontrou == False):
        time.sleep(2)
        print("Nenhum chamado com essa prioridade foi encontrado em aberto!")
        time.sleep(2)
  elif(opcao == 7):
    encontrou = False
    resp = int(input("Digite o ID do chamado: "))
    for c in Chamados:
      if(resp == c.id):
        encontrou = True
        print(f" | {c.id} | {c.user} | {c.desc} | {c.cat} | {c.resp} | {c.status}")
        time.sleep(2)
    if(encontrou == False):
      print("Nenhum chamado com esse ID foi encontrado!")
      time.sleep(2)
  elif(opcao == 8):
    print("==========================================")
    print("       ESCOLHA UMA OPÇÃO")
    print("1 - Quantidade total de chamados")
    print("2 - Quantidade de chamados abertos")
    print("3 - Quantidade de chamados concluido")
    print("==========================================")
    opcao01 = int(input("Escolha uma opção: "))
    if(opcao01 == 1):
      time.sleep(2)
      print(f"O total de chamados é de: {len(Chamados)}")
      time.sleep(2)
    elif(opcao01 == 2):
      quantidade = 0
      for c in Chamados:
        if(c.status == "Aberto"):
          quantidade += 1
          time.sleep(2)
      print(f"Total de chamados abertos: {quantidade}")
      time.sleep(2)
    elif(opcao01 == 3):
      quantidade = 0
      for c in Chamados:
        if(c.status == "Concluido"):
          quantidade += 1
          time.sleep(2)
      print(f"Total de chamados concluidos: {quantidade}")
      time.sleep(2)
    else:
      print("Opção invalida!")
      time.sleep(2)
  else:
    print("escolha uma opção existente!")
    time.sleep(1.5)