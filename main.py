from calcular import logica_calcular 
from janela import *

def main():
  """Principal funcao do sistema que chama os outros módulos."""
  print("==========================================================================")
  print("::BEM VINDO A CALCULADORA AVANÇADA::")  
  usar_interface = str(input("DESEJA REALIZAR SEUS CALCULOS COM A INTERFACE GRÁFICA?(S/N): ")).upper()
  if usar_interface == "S":
    execucao_interface()

  else:
    while True:
      print("==SE DESEJAR SAIR DA CALCULADORA DIGITE 'SAIR'==")
      input_valor = str(input("\nInforme o valor que deseja calcular: ")).upper()
      if input_valor == "SAIR":
        print("Saindo...")
        break

      else:
        resultado = logica_calcular(input_valor)
        print(f"RESULTADO: {resultado}")
      print("\n==========================================================================")
      
main()
