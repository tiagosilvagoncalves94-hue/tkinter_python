import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("formulário")

#entrada de texto
label_entrada = ttk.Label(janela, text= "Nome")
label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()

#checkbox
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text= "Aceito os termos", variable= checkbox) 
check.pack()

#opcões
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text="masculino" , variable= opcao, value=1)
opc2 = tk.Radiobutton(janela, text="feminino" , variable= opcao, value=2)
opc3 = tk.Radiobutton(janela, text="outro" , variable= opcao, value=3)
opc1.pack()
opc2.pack()
opc3.pack()

#listbox
lista=  tk.Listbox(janela)
lista.insert(1 , "phython")
lista.insert(2 , "java")
lista.insert(3 , "php")
lista.insert(4 , "javaescript")
lista.pack()

#combobox
combo = ttk.Combobox(janela, values= ["MG" , "RJ" , "RS" , "RN"])
combo.set("selecione um Estado")
combo.pack() 

#botão
def clicar():
    messagebox.showinfo("aviso" ,"botão acionado!")

btn = tk.Button(janela , text= "Mostrar mensagem" , command=clicar)
btn.pack()


janela.mainloop()
