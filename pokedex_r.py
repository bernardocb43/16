import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io
import difflib
from playsound import playsound
import threading

class PokedexApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokédex Clássica")
        self.geometry("700x800")
        self.configure(bg="#B22222")
        self.fullscreen = False
        self.pokemon_list = self.carregar_lista_pokemon()
        self.criar_interface()

    def criar_interface(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6,
                        background="#8B0000", foreground="white")
        style.map("TButton", background=[("active", "#A52A2A")])

        style.configure("TLabel", background="#B22222", foreground="white", font=("Segoe UI", 11))
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="white", background="#B22222")
        style.configure("Card.TFrame", background="#FAFAFA", relief="ridge", padding=10)

        container = ttk.Frame(self, style="Card.TFrame")
        container.pack(expand=True, fill="both", padx=30, pady=20)

        title = ttk.Label(container, text="🧭 💩Pokédex🐸", font=("Segoe UI", 22, "bold"))
        title.pack(pady=(0, 10))

        title = ttk.Label(self, text="🍷🗿", style="Title.TLabel")
        title.pack(pady=(100, 10))

        search_frame = ttk.Frame(container, style="Card.TFrame")
        search_frame.pack(pady=5)

        self.pesquisa_var = tk.StringVar()
        self.pesquisa_var.trace_add("write", self.atualizar_sugestoes)

        self.entry = ttk.Entry(search_frame, textvariable=self.pesquisa_var, width=30, font=("Segoe UI", 11))
        self.entry.pack(side="left", padx=5)
        self.entry.focus()

        buscar_btn = ttk.Button(search_frame, text="🔍 Buscar", command=self.buscar)
        buscar_btn.pack(side="left", padx=5)

        fullscreen_btn = ttk.Button(search_frame, text="🖵 Tela cheia", command=self.toggle_fullscreen)
        fullscreen_btn.pack(side='left', padx=5)

        self.sugestoes_listbox = tk.Listbox(container, height=4, font=("Segoe UI", 10))
        self.sugestoes_listbox.pack(fill='x', pady=5)
        self.sugestoes_listbox.bind("<<ListboxSelect>>", self.selecionar_sugestao)

        self.imagem_label = ttk.Label(container, background="#FAFAFA")
        self.imagem_label.pack(pady=10)

        self.info_label = ttk.Label(container, text="", justify="center", font=("Segoe UI", 11), wraplength=600, foreground="black", background="#FAFAFA")
        self.info_label.pack(pady=10)

        self.extra_info = ttk.Label(container, text="", justify="center", font=("Segoe UI", 10, "italic"), wraplength=600, foreground="black", background="#FAFAFA")
        self.extra_info.pack(pady=5)

        self.evo_label = ttk.Label(container, text="", justify="center", font=("Segoe UI", 10), wraplength=600, foreground="#555", background="#FAFAFA")
        self.evo_label.pack(pady=10)

        self.footer_label = ttk.Label(self, text="Desenvolvido com (GPT)✅ e Tkinter❌", font=("Segoe UI", 9, "italic"), background="#B22222", foreground="white")
        self.footer_label.pack(pady=(10, 10))

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)

    def carregar_lista_pokemon(self):
        try:
            resposta = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
            dados = resposta.json()
            return [p['name'] for p in dados['results']]
        except:
            return []

    def atualizar_sugestoes(self, *_):
        termo = self.pesquisa_var.get().lower()
        self.sugestoes_listbox.delete(0, tk.END)

        if termo:
            matches = difflib.get_close_matches(termo, self.pokemon_list, n=5, cutoff=0.3)
            for m in matches:
                self.sugestoes_listbox.insert(tk.END, m)

    def selecionar_sugestao(self, event):
        selecionado = self.sugestoes_listbox.get(tk.ACTIVE)
        self.pesquisa_var.set(selecionado)
        self.sugestoes_listbox.delete(0, tk.END)
        self.buscar()

    def tocar_som(self, arquivo):
        threading.Thread(target=playsound, args=(arquivo,), daemon=True).start()

    def buscar(self):
        nome = self.pesquisa_var.get().lower().strip()
        if not nome:
            messagebox.showinfo("Aviso", "Digite o nome de um 💩Pokémonus mythologica🐸.")
            return


        match = difflib.get_close_matches(nome, self.pokemon_list, n=1, cutoff=0.6)
        if match:
            nome = match[0]

        try:
            resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")
            if resposta.status_code != 200:
                raise Exception("Não encontrado.")
            dados = resposta.json()

            nome_formatado = dados['name'].capitalize()
            tipos = ", ".join([t['type']['name'].capitalize() for t in dados['types']])
            habilidades = ", ".join([a['ability']['name'].capitalize() for a in dados['abilities']])
            altura = dados['height'] / 10
            peso = dados['weight'] / 10
            id_pokemon = dados['id']

            info = f"📛 {nome_formatado}  |  ID: #{id_pokemon}\n👾 Tipo: {tipos}\n📏 Altura: {altura:.1f} m\n⚖️ Peso: {peso:.1f} kg"
            self.info_label.config(text=info)
            self.extra_info.config(text=f"✨ Habilidades: {habilidades}")


            sprite_url = dados['sprites']['other']['official-artwork']['front_default']
            img_data = requests.get(sprite_url).content
            image = Image.open(io.BytesIO(img_data)).resize((250, 250))
            self.tk_image = ImageTk.PhotoImage(image)
            self.imagem_label.config(image=self.tk_image)


            self.tocar_som("sucesso.mp3")

            self.buscar_evolucoes(dados['species']['url'])

        except:
            self.info_label.config(text="Esse 💩Pokémon💩 não existe seu troxa.")
            self.imagem_label.config(image="")
            self.extra_info.config(text="")
            self.evo_label.config(text="")
            self.tocar_som("erro.mp3")

    def buscar_evolucoes(self, species_url):
        try:
            species_data = requests.get(species_url).json()
            evo_chain_url = species_data['evolution_chain']['url']
            chain_data = requests.get(evo_chain_url).json()

            evolucoes = []
            atual = chain_data['chain']
            while atual:
                nome = atual['species']['name'].capitalize()
                evolucoes.append(nome)
                if atual['evolves_to']:
                    atual = atual['evolves_to'][0]
                else:
                    break

            if len(evolucoes) > 1:
                texto = "🔁🧬✅ Evoluções: " + " → ".join(evolucoes)
            else:
                texto = "🔁🧬❌ Este Pokémon não evolui."

            self.evo_label.config(text=texto)

        except:
            self.evo_label.config(text="❓ Evoluções indisponíveis.")

if __name__ == "__main__":
    app = PokedexApp()
    app.mainloop()
