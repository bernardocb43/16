import tkinter as tk
import random as r
from time import sleep
from tkinter import messagebox

pontuacao = 0
tempo_restante = 30
nome_jogador = ""

def clicar_quadrado(evento):
    global pontuacao
    if tempo_restante > 0:
        pontuacao += 1
        etiqueta_pontuacao.config(text=f"Pontuação: {pontuacao}")

def mover_quadrado():
    if tempo_restante > 0:
        novo_x = r.randint(0, 400)
        novo_y = r.randint(0, 400)
        canvas.coords(quadrado, novo_x, novo_y, novo_x + 50, novo_y + 50)


        janela.after(1000, mover_quadrado)

def atualizar_tempo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        etiqueta_tempo.config(text=f"Tempo: {tempo_restante}s")
        janela.after(1000, atualizar_tempo)
    else:
        etiqueta_tempo.config(text="Tempo esgotado!")
        messagebox.showinfo(title="Fim de jogo", message=f"Tempo esgotado! Sua pontuação foi: {pontuacao}")
        salvar_resultado()

def salvar_resultado():
    global nome_jogador, pontuacao
    with open("resultados_caca.txt", "a") as ficheiro:
        ficheiro.write(f"{nome_jogador}, {pontuacao}\n")

def iniciar_jogo():
    global nome_jogador
    nome_jogador = entrada_nome.get()
    if not nome_jogador:
        messagebox.showwarning(title="Aviso", message="Digite um nome antes de começar")
        return

    mover_quadrado()
    atualizar_tempo()

def novo_jogo():
    global pontuacao, tempo_restante
    pontuacao = 0
    tempo_restante = 30
    etiqueta_pontuacao.config(text=f"Pontuação: {pontuacao}")
    etiqueta_tempo.config(text=f"Tempo: {tempo_restante}s")

    mover_quadrado()
    atualizar_tempo()


janela = tk.Tk()
janela.title("Caça ao Quadrado")
janela.geometry("500x500")


tk.Label(janela, text="Nome do jogador: ", font=("Fixedsys", 12)).pack()
entrada_nome = tk.Entry(janela, font=("Fixedsys", 12))
entrada_nome.pack()


botao_iniciar_jogo = tk.Button(janela, text="Iniciar Jogo", font=("Fixedsys", 12), command=iniciar_jogo)
botao_iniciar_jogo.pack()

botao_novo_jogo = tk.Button(janela, text="Novo Jogo", font=("Fixedsys", 12), command=novo_jogo)
botao_novo_jogo.pack()


canvas = tk.Canvas(janela, width=500, height=500, bg="white")
canvas.pack()


quadrado = canvas.create_rectangle(50, 50, 100, 100, fill="red")


etiqueta_pontuacao = tk.Label(janela, text=f"Pontuação: {pontuacao}", font="Fixedsys 18 bold")
etiqueta_pontuacao.pack()

etiqueta_tempo = tk.Label(janela, text=f"Tempo: {tempo_restante}s", font="Fixedsys 18 bold")
etiqueta_tempo.pack()


canvas.tag_bind(quadrado, "<Button-1>", clicar_quadrado)

janela.mainloop()
