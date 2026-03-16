import tkinter as tk 
#criação de janela
janela_main = tk.Tk()

janela_main.title("jogador")
janela_main.configure(background= "blue")
janela_main.minsize(300,300)
janela_main.maxsize(600,600)
janela_main.geometry("400x400")

#obejetos na janela
tk.Label(janela_main, 
         text= "CRISTIANO RONALDO",
         bg = "gold",
         font= ("arial" ,20 ,"bold")
        ).pack()

imagem=tk.PhotoImage(file="cr77.png")
imagem=imagem.subsample(3,3)
tk.Label(janela_main,image=imagem).pack()

tk.Label(janela_main, 
         text= "\nJogador de futebol com 41 anos " \
         "\nem atividade no esporte"\
         "\ncom alto rendimento em campo" \
         "\npelo time do al-nassar",
         bg = "gold",
         font= ("arial" ,18)
        ).pack()


#imagens



janela_main.mainloop()