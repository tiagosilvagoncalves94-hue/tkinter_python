import tkinter as tk 
#ceiação de janela
janela_main = tk.Tk()

janela_main.title("times de futebol")
janela_main.configure(background= "red")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#obejetos na janela
tk.Label(janela_main, 
         text= "hello world!",
         bg = "red",
         font= ("arial" ,20 ,"bold")
        ).pack()
tk.Label(janela_main, 
         text= "thiago gonçalves silva",
         bg = "red",
         font= ("arial" ,20)
        ).pack()

#imagens
imagem=tk.PhotoImage(file="cr77.png")
imagem=imagem.subsample(3,3)
tk.Label(janela_main,image=imagem).pack()


janela_main.mainloop()