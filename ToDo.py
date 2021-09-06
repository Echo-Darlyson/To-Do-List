import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from functools import partial
import sys

# Tela
tela = tk.Tk()
tela.geometry("260x500")
tela.title("To Do")
tela.resizable(False, False)

# Cor de fundo
label4 = tk.Label(tela, width = 250, height = 400, bg = "#312eff")
label4.pack()

foto = tk.PhotoImage(file = "todoimage.png").subsample(3, 3)

# Inicializador para somar a qtd de tarefas
qtd = 0

# Lista com as tarefas
lista = []

# Desabilita a caixinha quando é marcado e aumenta a barra de progresso sempre que é chamado
def Realizado(i):
	lista[i]["state"] = "disabled"
	progress["value"] += 100.0 / float(qtd_tarefas.get())
	label5["text"] = f"{int(progress['value'])}% das Tarefas Realizadas!"

	if progress["value"] == 100.0:
		messagebox.showinfo("Parabéns!", "Você cumpriu todas as suas tarefas! Descanse agora!")
		sys.exit()

# Cria novas tarefas uma embaixo da outra de acordo com a quantidade de tarefas digitado
def Criar():
	global qtd
	qtd += 1
	if qtd > int(qtd_tarefas.get()):
		return

	tarefa_box = tk.Checkbutton(scroll, text = tarefas.get()[:29].title(), command = partial(Realizado, qtd - 1), bg = "white", highlightthickness = 0, activebackground = "white", font = ("Comic Sans MS", 8))
	scroll.window_create("end", window = tarefa_box)
	scroll.insert("end", "\n")

	if qtd == int(qtd_tarefas.get()):
		scroll["state"] = "disabled"
		qtd_tarefas["state"] = "disabled"

	tarefas.delete(0, len(tarefas.get()))
	lista.append(tarefa_box)

# ScrollText para as checkbox
scroll = ScrolledText(tela, width = 23, height = 5, highlightthickness = 0, bg = "white")
scroll.place(relx = .5, rely = .7, anchor = "center")

# Estilo da barra de progresso
style = ttk.Style()
style.theme_use('alt')
style.configure("green.Horizontal.TProgressbar", foreground = '#2bad00', background = '#2bad00', thickness = 20)
            
# Barra de Progresso	
progress = ttk.Progressbar(tela, length = 200, style = "green.Horizontal.TProgressbar", orient = "horizontal", mode = "determinate", value = 0.0)
progress.place(relx = .5, rely = .9, anchor = "center")

label = tk.Label(tela, text = "QTD de Tarefas a Cumprir", bg = "#312eff", font = ("Impact", 18))
label.place(relx = .5, y = 90, anchor = "center")

# Spinbox da qtd de tarefas
qtd_tarefas = tk.Spinbox(tela, from_ = 1.0, to = 20.0, width = 4, highlightthickness = 0)
qtd_tarefas.place(relx = .5, y = 125, anchor = "center")

label2 = tk.Label(tela, text="Tarefas a Criar", font = ("Impact", 18), bg = "#312eff")
label2.place(relx = .5, y = 164, anchor = "center")

# Entrada das tarefas a criar
tarefas = tk.Entry(tela, width = 25, highlightthickness = 0)
tarefas.place(relx = .5, rely = .4, anchor = "center")

# Botão que cria a tarefa chamando a função Criar()
criar_tarefa = tk.Button(tela, text="Criar", command = Criar, highlightthickness = 0, relief = "solid")
criar_tarefa.place(relx = .5, rely = .5, anchor = "center")

label3 = tk.Label(tela, image=foto, bg = "#312eff")
label3.place(relx = .5, y = 35, anchor = "center")

label5 = tk.Label(tela, bg = "#312eff", font = ("impact", 12), fg = "#2bad00")
label5.place(relx = .5, y = 485, anchor = "center")

messagebox.showinfo("Aviso", "Digite uma tarefa com apenas 28 caracteres!")

tela.mainloop()