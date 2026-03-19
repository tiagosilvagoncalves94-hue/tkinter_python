import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário de cadastro")
janela.geometry("400x400")

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    escola = escolaridade.get()
    atuacao_valor = opc.get()
    
    if atuacao_valor == 1:
        atuacao = "Gêrencia"
    if atuacao_valor == 2:
        atuacao = "Administrativo"
    if atuacao_valor == 3:
        atuacao = "Profissional téc."
    if atuacao_valor == 4:
        atuacao = "Analista sistema"
    if atuacao_valor == 5:
        atuacao = "Estágiario t.i"
    
    
    msg= f"Nome: {nome}\n Idade: {idade}\n Escolaridae: {escola} \n Area de atuação: {atuacao}"
    messagebox.showinfo("dados enviados", msg)

#dados
tk.Label(janela, text="Dados pessoais" ,font=("Arial" ,14)).grid(column=1,pady= 20)
tk.Label(janela , text= "nome: ").grid(row=1, column=0)
entrada_nome = tk.Entry(janela ,font=("Arial"))
entrada_nome.grid(row=1, column=1)

#idade
tk.Label(janela , text= "idade: ").grid(row=2, column=0)
entrada_idade = tk.Entry(janela ,font=("Arial"))
entrada_idade.grid(row=2, column=1)

#dados
tk.Label(janela, text="Dados profissionais " ,font=("Arial" ,14)).grid(column=1,pady= 20)

#escolaridade
tk.Label(janela, text="Escolaridade: ",font=("Arial")).grid(row=4, column=0)
escolaridade = ttk.Combobox(janela, values= ["ensino fundamental completo" , "ensino fundamental incompleto" , "ensino médio completo" , "ensino médio incompleto" , "ensino superior"])
escolaridade.grid(row=4, column=1)

#atuação
opc= tk.IntVar()
tk.Label(janela, text="área de atuação:").grid(row=6, column=0)
tk.Radiobutton(janela, text= "Gêrencia",font= ("Arial") ,value =1,variable=opc)\
    .grid(row=6,column=1)
tk.Radiobutton(janela, text= "Administrativo",font= ("Arial") , value =2,variable=opc)\
    .grid(row=7,column=1)
tk.Radiobutton(janela, text= "Profissional téc.",font= ("Arial") , value =3,variable=opc)\
    .grid(row=8,column=1)
tk.Radiobutton(janela, text= "Analista sistema",font= ("Arial") , value =4,variable=opc)\
    .grid(row=9,column=1)
tk.Radiobutton(janela, text= "Estágiario t.i",font= ("Arial") , value =5,variable=opc)\
    .grid(row=10,column=1)


tk.Button(janela, text= "enviar", command= enviar).grid(row=11, column=1, pady=20)






janela.mainloop()