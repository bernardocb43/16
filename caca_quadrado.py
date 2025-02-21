import tkinter as tk
import random as r
from time import sleep

pontuacao = 0
tempo_restante = 30

def clicar_quadrado(evento):
    global pontuacao
    if tempo_restante > 0:
        pontuacao += 1
        etiqueta_pontuacao.config(text=f"Pontução: {pontuacao}")

def mover_quadrado():
    global tempo_restante
    if tempo_restante > 0:
        x = random.randint(a= 10, b= 400)
        y = random.randint(a= 10, b= 400)
        janela.after(ms=1000, mover_quadrado)




janela = tk.Tk()
janela.title("Caça ao Quadrado")
janela.geometry("500x500")

canvas = tk.Canvas(janela, width=500, height=500, bg="white")
canvas.pack()

quadrado = canvas.create_rectangle(50,50,100,100, fill="red")

etiqueta_pontuacao = tk.Label(janela, text=f" Pontuação: {pontuacao}", font="Fixedsys 18 bold")
etiqueta_pontuacao.pack()

etiqueta_tempo = tk.Label(janela, text=f"tempo: {tempo_restante}", font="Fixedsys 18 bold")
etiqueta_tempo.pack()

canvas.tag_bind(quadrado, "<Button-1>", clicar_quadrado)





janela.mainloop()
