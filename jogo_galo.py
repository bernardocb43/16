import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("jogo do galo")

jogador_atual = 'X'
tabuleiro = [''for _ in range(9)]
botoes = []

def verifica_vencedor():
  global tabuleiro
  conbinacoes  = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]
 ]
  for  comb in conbinacoes:
      if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] != '':
          return True
      return False
def reniciar():
    global tabuleiro, botoes, jogador_atual
    tabuleiro = [''for _ in range(9)]

    for botao in botoes:
        botao.config(text='')
        jogador_atual = 'X'
def clica_botao(index):
    global jogador_atual, tabuleiro, botoes

    if tabuleiro[index] == '':
        tabuleiro[index] = 'jogador_atual'
        botoes[index].config(text=jogdor_atual)

        if verifica_vencedor():
            tkinter.messagebox.showinfo(title="fim de jogo", message=f"jogador {jogador_atual} venceu")
            reinniciar()
        elif '' not in tabuleiro:
            tkinter.messagebox.showinfo(title="fim de jogo", message="Empate")
        else:
             jogador_atual = 'O' if jogador_atual == 'X' else 'X'

for i in range(9):
    botao = tk.Button(root, text='', font=('Fixedsys', 40), width=5, height=2, command=lambda i=i: clica_botao(i))
    botao.grid(row=i//3, column=i%3)
    botoes.append(botao)

root.mainloop()
