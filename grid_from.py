import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("formulário")
janela.geometry("300x300")

tk.Label(janela , text= "nome: ").grid(row=0, column=0)
entrada_nome = tk.Entry(janela ,font=("Arial"))
entrada_nome.grid(row=0, column=1)
opc= tk.IntVar()


tk.Label(janela, text="sexo:").grid(row=2, column=0)
frame_sx = tk.Frame(janela)
frame_sx.grid(row=3 , column=1 , padx=10 , pady= 5 , sticky="w")
tk.Radiobutton(frame_sx, text= "masculino",font= ("Arial") ,value =1,variable=opc)\
    .pack(anchor="w")
tk.Radiobutton(frame_sx, text= "feminino",font= ("Arial") , value =2,variable=opc)\
    .pack(anchor="w")





janela.mainloop()