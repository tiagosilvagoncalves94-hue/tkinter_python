import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário de cadastro")
janela.geometry("400x400")
janela.configure(background= "beige")

def enviar():
    nome = entrada_nome.get()
    sobrenome = entrada_sobre.get()
    data = entrada_nasc.get()
    cpf = entrada_cpf.get()
    cep = entrada_cep.get()
    sexo = opc.get()
    estado = combo_estado.get()
    cidade = entrada_cdd.get()

    sexo_texto ="masculino" if sexo == 1 else "feminino"


    msg= f"Nome: {nome}\n Sobrenome: {sobrenome}\n data nascimento: {data} \n CPF: {cpf} \n CEP: {cep} \n sexo: {sexo}\n estado: {estado}\n cidade: {cidade}"
    messagebox.showinfo("dados enviados", msg)



#nome
tk.Label(janela, text="Formulário de cadastro" ,font=("Arial" ,14)).grid(column=1,pady= 20)
tk.Label(janela , text= "nome: ").grid(row=1, column=0)
entrada_nome = tk.Entry(janela ,font=("Arial"))
entrada_nome.grid(row=1, column=1)

#sobrenome
tk.Label(janela , text= "sobrenome: ").grid(row=2, column=0)
entrada_sobre = tk.Entry(janela ,font=("Arial"))
entrada_sobre.grid(row=2, column=1)

#data
tk.Label(janela , text= "data de nascimento: ").grid(row=3, column=0)
entrada_nasc = tk.Entry(janela ,font=("Arial"))
entrada_nasc.grid(row=3, column=1)

#cpf
tk.Label(janela , text= "CPF: ").grid(row=4, column=0)
entrada_cpf = tk.Entry(janela ,font=("Arial"))
entrada_cpf.grid(row=4, column=1)

#cep
tk.Label(janela , text= "CEP: ").grid(row=5, column=0)
entrada_cep = tk.Entry(janela ,font=("Arial"))
entrada_cep.grid(row=5, column=1)

#sexo
opc = IntVar()
tk.Label(janela, text="sexo:").grid(row=6, column=0)
tk.Radiobutton(janela, text= "masculino",font= ("Arial") ,value =1,variable=opc)\
    .grid(row=6,column=1)
tk.Radiobutton(janela, text= "feminino",font= ("Arial") , value =2,variable=opc)\
    .grid(row=7,column=1)

#estado
tk.Label(janela, text="Estado: ",font=("Arial")).grid(row=8, column=0)
combo_estado = ttk.Combobox(janela, values= ["MG" , "SP" , "RJ" , "RN" , "BA" ,"PE" , "DF" , "AM" , "AC" , "PA" ,"MT" , "PR" , "TO" , "RO" , "ES"])
combo_estado.grid(row=8, column=1)

#CDD
tk.Label(janela , text= "Cidade: ").grid(row=9, column=0)
entrada_cdd = tk.Entry(janela ,font=("Arial"))
entrada_cdd.grid(row=9, column=1)   

tk.Button(janela, text= "cadastrar", command= enviar).grid(row=10, column=1, pady=20)





janela.mainloop()