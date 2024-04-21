from pilhas import *

def pilha_pop(p):
  """Funçaõ que da um pop no topo de uma pilha."""
  p.n = p.n - 1
  v = p.vet[p.n - 1]
  return v

def calcular_pilha(pilha_operandos, pilha_operadores):
  """Função que pega os 2 primeiros elementos da pilha operandos e calcula-os usando o primeiro
    elemento da pilha operador: Exempo 2 + 2."""
  operando1 = ""
  operador = ""
  operando2 = ""
  resultado = 0

  ##Primeiro valor
  operando1 = float(pilha_operandos.vet[pilha_operandos.n-1])
  pilha_pop(pilha_operandos)

  ##Segundo valor
  operador = pilha_operadores.vet[pilha_operadores.n-1]
  pilha_pop(pilha_operadores)
  
  ##Terceiro valor
  operando2 = float(pilha_operandos.vet[pilha_operandos.n-1])
  pilha_pop(pilha_operandos)

  # print(operando1, operador, operando2)

  if operador == "+":
    resultado += operando1 + operando2
  
  elif operador == "-":
    resultado += operando1 - operando2

  elif operador == "*":
    resultado += operando1 * operando2

  elif operador == "/":
    try:
      r = operando1 / operando2
    
    except ZeroDivisionError:
      return False
    
    else:
      resultado += r
      return resultado
  return resultado
    
def pilha_cria(n):
  """Função que cria uma pilha."""
  p = Pilha(n) 
  p.n = 0
  return p

def pilha_push(p, v):
  """Função que da um push em um elemento para o topo da pilha."""
  p.vet.insert(p.n, v)
  p.n = p.n + 1

def inserir_valor_lista_encadeada(lst, valor):
  """Função que insere um elemento em uma lista encadeada."""
  aux = Lista(valor)
  aux.prox = lst
  return aux

def separar_input(valor, operadores_preferencia):
  """Função responsável por sprar o valor do input colocando cada elemento separadamente 
    em uma lista encadeada."""
  l_aux = None
  variavel_aux = ""
  operador_anterior = ""

  for i in range(len(valor)):
    #Se for um numero
    if valor[i] != " " and valor[i] not in operadores_preferencia:
      variavel_aux += valor[i]
      operador_anterior = ""

    elif valor[i] == "-" and i == 0:
      variavel_aux += valor[i]

    elif valor[i] in operadores_preferencia and operador_anterior != "" and valor[i] == "-" and operador_anterior != ")":
      variavel_aux += valor[i]
      operador_anterior = ""
    
    ##Se for um operador
    elif i != " " and valor[i] in operadores_preferencia:
      l_aux = inserir_valor_lista_encadeada(l_aux, variavel_aux)
      l_aux = inserir_valor_lista_encadeada(l_aux, valor[i])
      variavel_aux = ""
      operador_anterior = valor[i]

  l_aux = inserir_valor_lista_encadeada(l_aux, variavel_aux)
  return l_aux

def logica_calcular(valor):
  """Função responsável pela lógica do sistema, onde a lista encadeada é percorrida e em 
  cada valor é dado um push para sua respectiva pilha(pilha_operandos, pilha_operadores). Ao 
  colocar cada valor, também é verificado a preferência de operadores. No final o resultado é retornado."""
  resultado = 0
  operadores_preferencia = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 0, ")":0}
  
  ##Caso tenha um parenteses e falte outro, retorna ERRO
  if "(" in valor and ")" not in valor or ")" in valor and "(" not in valor:
    return "[ERROR]"
  ##Separando os valores
  lst_valor = separar_input(valor, operadores_preferencia)
  
  ##Criando as pilhas
  pilha_operandos = pilha_cria(200)
  pilha_operadores = pilha_cria(200)

  ##adicionando os elementos nas pilhas
  atual = lst_valor
  while atual is not None:
    ##Se nao for um operador, adiciono na pilha de operandos

    if atual.info not in operadores_preferencia and atual.info != "":
      pilha_push(pilha_operandos, atual.info)

    else:
      ##Se for o ( realizara as operaçoes ate encontrar o )
      if atual.info == "(":
        while True:
          if pilha_operadores.vet[pilha_operadores.n-1] == ")":
            pilha_pop(pilha_operadores)
            break

          else:
            resultado = calcular_pilha(pilha_operandos, pilha_operadores)
            pilha_push(pilha_operandos, resultado)

      elif atual.info != "":        
        ##Se o tamanho da pilha for > 0, e o operador atual tiver preferencia sobre os demais
        while pilha_operadores.n > 0 and operadores_preferencia[atual.info] < operadores_preferencia[pilha_operadores.vet[pilha_operadores.n-1]] and pilha_operadores.vet[pilha_operadores.n-1]!= ")" and atual.info != ")": 
          resultado = calcular_pilha(pilha_operandos, pilha_operadores)
          pilha_push(pilha_operandos, resultado)
          if resultado == False:
            return "[ERROR]"

        pilha_push(pilha_operadores, atual.info)

    atual = atual.prox

  while pilha_operadores.n != 0:
    resultado = calcular_pilha(pilha_operandos, pilha_operadores)
    if resultado == False:
      return "[ERROR]"
    pilha_push(pilha_operandos, resultado)

  return resultado
