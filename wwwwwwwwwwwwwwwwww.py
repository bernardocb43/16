from tkinter import  *

azul=("#0000FF")
vermelho=("#FF0000")
amarelo=("#FFFF00")
verde=("#00FF00")
root = Tk()
root.title("color changer")
root.geometry("500x400+400+100")
root.wm_resizable(width=False, height=False)

def bg_azul():
    root.configure(background=azul)

def bg_vermelho():
    root.configure(background=vermelho)

def bg_amarelo():
    root.configure(background=amarelo)

def bg_verde():
    root.configure(background=verde)

button1 = Button(root, text="Azul",command=bg_azul, font="Impact 30 bold")
button1.place(width=200, height=160, x=40, y=20)

button2 = Button(root, text="Vermelho",command=bg_vermelho, font="Impact 30 bold")
button2.place(width=200, height=160, x=40, y=200)

button3 = Button(root, text="Amarelo",command=bg_amarelo, font="Impact 30 bold")
button3.place(width=200, height=160, x=270, y=20)

button4 = Button(root, text="Verde",command=bg_verde, font="impact 30 bold")
button4.place(width=200, height=160, x=270, y=200)


root.mainloop()
