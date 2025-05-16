import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io

class PokedexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex")
        self.root.geometry("480x620")
        self.root.configure(bg="#F0F0F0")
        self.root.resizable(False, False)

        self.historico = []
        self.configurar_estilo()
        self.criar_widgets()

    def configurar_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("TLabel", background="#F0F0F0", foreground="#333333", font=("Segoe UI", 11))
        estilo.configure("Titulo.TLabel", font=("Segoe UI", 24, "bold"), foreground="#E33535", background="#F0F0F0")
        estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 14, "bold"), foreground="#555555", background="#F0F0F0")
        estilo.configure("TButton", background="#E33535", foreground="#FFFFFF", font=("Segoe UI", 13, "bold"), padding=8)
        estilo.map("TButton", background=[("active", "#C12B2B")], foreground=[("active", "#FFFFFF")])
        estilo.configure("TEntry", fieldbackground="#FFFFFF", font=("Segoe UI", 13), padding=5)

    def criar_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=15, pady=15)

        self.aba_principal = ttk.Frame(self.notebook)
        self.aba_principal.configure(style="TFrame")
        self.notebook.add(self.aba_principal, text="Pokédex")

        self.aba_historico = ttk.Frame(self.notebook)
        self.aba_historico.configure(style="TFrame")
        self.notebook.add(self.aba_historico, text="Histórico")

        self.criar_widgets_aba_principal()
        self.criar_widgets_aba_historico()

    def criar_widgets_aba_principal(self):
        titulo = ttk.Label(self.aba_principal, text="Pokédex", style="Titulo.TLabel")
        titulo.pack(pady=(10, 20))

        self.entrada = ttk.Entry(self.aba_principal, font=("Segoe UI", 13), justify="center")
        self.entrada.pack(pady=5, ipadx=8, ipady=6)

        self.botao_buscar = ttk.Button(self.aba_principal, text="Buscar", command=self.buscar_pokemon)
        self.botao_buscar.pack(pady=10, ipadx=15)

        self.canvas_imagem = tk.Canvas(self.aba_principal, width=200, height=200, bg="#FFFFFF", highlightthickness=0)
        self.canvas_imagem.pack(pady=15)
        self.canvas_imagem.create_text(100, 100, text="Imagem\nPokémon", font=("Segoe UI", 14), fill="#999999")

        self.resultado = ttk.Label(self.aba_principal, text="Nome: \nTipo: \nAltura: \nPeso:", justify="left")
        self.resultado.pack(anchor='w', padx=30, pady=5)

        ttk.Separator(self.aba_principal, orient="horizontal").pack(fill='x', padx=20, pady=10)

        self.habilidades_label = ttk.Label(self.aba_principal, text="Habilidades:", style="Subtitulo.TLabel")
        self.habilidades_label.pack(anchor='w', padx=30)

        self.habilidades_text = ttk.Label(self.aba_principal, text="", wraplength=400, justify="left")
        self.habilidades_text.pack(anchor='w', padx=40, pady=(0, 10))

        ttk.Separator(self.aba_principal, orient="horizontal").pack(fill='x', padx=20, pady=10)

        self.stats_label = ttk.Label(self.aba_principal, text="Base Stats:", style="Subtitulo.TLabel")
        self.stats_label.pack(anchor='w', padx=30)

        self.stats_text = ttk.Label(self.aba_principal, text="", justify="left")
        self.stats_text.pack(anchor='w', padx=40)

    def criar_widgets_aba_historico(self):
        self.lista_historico = tk.Listbox(self.aba_historico, font=("Segoe UI", 12), bg="#FFFFFF", fg="#333333",
                                          selectbackground="#E33535", selectforeground="#FFFFFF")
        self.lista_historico.pack(fill='both', expand=True, padx=15, pady=15)
        self.lista_historico.bind('<<ListboxSelect>>', self.selecionar_historico)

    def buscar_pokemon(self):
        nome = self.entrada.get().strip().lower()

        if not nome:
            messagebox.showwarning("Entrada inválida", "Digite o nome ou número de um Pokémon!")
            return

        url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

        try:
            resposta = requests.get(url)

            if resposta.status_code == 200:
                dados = resposta.json()

                nome = dados["name"].capitalize()
                tipos = ", ".join([t["type"]["name"].capitalize() for t in dados["types"]])
                altura = dados["height"] / 10
                peso = dados["weight"] / 10

                texto = f"Nome: {nome}\nTipo: {tipos}\nAltura: {altura} m\nPeso: {peso} kg"
                self.resultado.config(text=texto)

                habilidades = ", ".join([h['ability']['name'].replace('-', ' ').capitalize() for h in dados['abilities']])
                self.habilidades_text.config(text=habilidades)

                stats = "\n".join([f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in dados['stats']])
                self.stats_text.config(text=stats)

                sprite_url = dados['sprites']['front_default']
                if sprite_url:
                    self.mostrar_imagem(sprite_url)
                else:
                    self.canvas_imagem.delete("all")
                    self.canvas_imagem.create_text(100, 100, text="Sem imagem", font=("Segoe UI", 14), fill="#999999")

                if nome not in self.historico:
                    self.historico.append(nome)
                    self.lista_historico.insert(tk.END, nome)

                self.notebook.select(self.aba_principal)

            else:
                messagebox.showerror("Erro", f"Pokémon '{nome}' não encontrado.")
                self.limpar_dados()
        except requests.exceptions.RequestException:
            messagebox.showerror("Erro", "Erro de conexão com a PokéAPI.")
            self.limpar_dados()

    def mostrar_imagem(self, url):
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            imagem_bytes = resposta.content
            imagem = Image.open(io.BytesIO(imagem_bytes)).resize((150, 150), Image.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.canvas_imagem.delete("all")
            self.canvas_imagem.create_image(100, 100, image=self.imagem_tk)
        except Exception as e:
            print("Erro ao carregar imagem:", e)
            self.canvas_imagem.delete("all")
            self.canvas_imagem.create_text(100, 100, text="Erro ao carregar imagem", font=("Segoe UI", 14), fill="#999999")

    def limpar_dados(self):
        self.resultado.config(text="Nome: \nTipo: \nAltura: \nPeso:")
        self.habilidades_text.config(text="")
        self.stats_text.config(text="")
        self.canvas_imagem.delete("all")
        self.canvas_imagem.create_text(100, 100, text="Imagem\nPokémon", font=("Segoe UI", 14), fill="#999999")

    def selecionar_historico(self, event):
        if not self.lista_historico.curselection():
            return
        indice = self.lista_historico.curselection()[0]
        nome = self.lista_historico.get(indice)
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, nome)
        self.buscar_pokemon()

if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()
