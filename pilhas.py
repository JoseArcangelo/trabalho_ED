class Lista:
  def __init__(self, info = None):
    self.info = info
    prox = None

class Pilha:
    def __init__(self, max):
      self.n = 0 #contador de elementos na pilha
      self.max = max
      self.vet = []
