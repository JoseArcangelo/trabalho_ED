from tkinter import *
from calcular import *

valor_input = ""
def execucao_interface():
  """Funcão que executa a interface."""
  janela = Tk()
  janela.title("CountCraft")
  ##tamanho da janela
  janela.geometry("320x390")

  ##dividindo a janela em duas
  frame_input = Frame(janela, width=320, height=50, bg="white")
  frame_input.grid(column=0, row=0)

  frame_botoes = Frame(janela, width=320, height=340)
  frame_botoes.grid(column=0, row=1)

  def entrada_do_valor(v):
    """Função que acrescenta um valor ao input da calculadora."""
    global valor_input
    valor_input += v
    input_usuario.config(text=valor_input)

  def calcular_resultado(valor_input):
    """Funação que ao clicar o botao = chama a funcao logica_calcular,
    passando o valor do input."""
    valor_input = logica_calcular(valor_input)
    if valor_input == "[ERROR]":
      input_usuario.config(fg="red")
    input_usuario.config(text=valor_input)
    
  def remover_valor():
    """Funcao responsavel de remover o primeiro valor do input."""
    global valor_input
    valor_input = valor_input[:-1]  # Remove o último caractere
    input_usuario.config(text=valor_input)

  input_usuario = Label(frame_input, textvariable=valor_input,width=19, height=2, anchor="e", justify=RIGHT, font=("Ivy 20"))
  input_usuario.place(x=0, y=0)

  botao1 = Button(frame_botoes, text="<-", width=8, height=3, font="20",background="black", fg="white", command=lambda: remover_valor())
  botao1.place(x=0, y=0)

  botao2 = Button(frame_botoes, text="(", width=8, height=3, background="orange", font="20", command=lambda: entrada_do_valor("("))
  botao2.place(x=80, y=0)

  botao3 = Button(frame_botoes, text=")", width=8, height=3, bg="orange", font="20", command=lambda: entrada_do_valor(")"))
  botao3.place(x=160, y=0)

  botao4 = Button(frame_botoes, text="/", width=8, height=3, bg="orange", font="20", command=lambda: entrada_do_valor("/"))
  botao4.place(x=240, y=0)

  botao5 = Button(frame_botoes, text="7", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("7"))
  botao5.place(x=0, y=68)

  botao6 = Button(frame_botoes, text="8", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("8"))
  botao6.place(x=80, y=68)

  botao7 = Button(frame_botoes, text="9", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("9"))
  botao7.place(x=160, y=68)

  botao7 = Button(frame_botoes, text="X", width=8, height=3, bg="orange", font="20", command=lambda: entrada_do_valor("*"))
  botao7.place(x=240, y=68)

  botao8 = Button(frame_botoes, text="4", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("4"))
  botao8.place(x=0, y=136)

  botao9 = Button(frame_botoes, text="5", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("5"))
  botao9.place(x=80, y=136)

  botao10 = Button(frame_botoes, text="6", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("6"))
  botao10.place(x=160, y=136)

  botao11 = Button(frame_botoes, text="+", width=8, height=3, bg="orange", font="20", command=lambda: entrada_do_valor("+"))
  botao11.place(x=240, y=136)

  botao12 = Button(frame_botoes, text="1", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("1"))
  botao12.place(x=0, y=204) 

  botao13 = Button(frame_botoes, text="2", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("2"))
  botao13.place(x=80, y=204)

  botao14 = Button(frame_botoes, text="3", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("3"))
  botao14.place(x=160, y=204) 

  botao15 = Button(frame_botoes, text="-", width=8, height=3, bg="orange", font="20", command=lambda: entrada_do_valor("-"))
  botao15.place(x=240, y=204)

  botao16 = Button(frame_botoes, text="0", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("0"))
  botao16.place(x=0, y=272)

  botao17 = Button(frame_botoes, text=".", width=8, height=3, bg="black", font="20", fg="white", command=lambda: entrada_do_valor("."))
  botao17.place(x=80, y=272) 

  botao17 = Button(frame_botoes, text="=", width=18, height=3, bg="green", font="20", fg="white", command=lambda: calcular_resultado(valor_input))
  botao17.place(x=160, y=272)

  janela.mainloop()
