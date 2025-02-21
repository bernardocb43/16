import tkinter as tk
from tkinter.messagebox import showinfo as msg

root = tk.Tk()
root.title("Jogo do galo")
root.wm_resizable(width=False, height=False)

player = "✘"
table = ["" for _ in range(9)]
btns = []


def verify():
    combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for ir in combinations:
        if table[ir[0]] == table[ir[1]] == table[ir[2]] != "":
            return True
    return False


def reset():
    global table, btns, player
    table = ["" for _ in range(9)]
    for b in btns:
        b.config(text="")
    player = "✘"


def clicked(index):
    global player, table, btns
    if table[index] == "":
        table[index] = player
        btns[index].config(text=player)
        if verify():
            msg("Fim de Jogo", f"O jogador {player} 🇻🇪🇳🇨🇪🇺! (🇻 🇪 🇳 🇨 🇪 🇺)")
            reset()
        elif "" not in table:
            msg("Fim de Jogo", "Empate")
            reset()
        else:
            player = "◯" if player == "✘" else "✘"


for i in range(9):
    btn = tk.Button(root, text="", font="Arial 20 bold", width=10, height=4, command=(lambda i1=i: clicked(i1)))
    btn.grid(row=i//3, column=i % 3)
    btns.append(btn)
root.mainloop()
