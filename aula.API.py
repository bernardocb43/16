import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def mostrar_gato():
   url = "https://api.thecatapi.com/v1/images/search"
   resposta = requests.get(url)
   dados = resposta.json()
   print(dados)
   imagem_url = dados[0]["url"]


   imagem_resposta = requests.get(imagem_url)
   imagem = Image.open(BytesIO(imagem_resposta.content))
   imagem = imagem.resize(((300,300)))

   imagem_tk = ImageTk.PhotoImage(imagem)
   imagem_label.config(image=imagem_tk)
   imagem_label.image = imagem_tk




ecra = tk.Tk()
ecra.title("gato aleatorio")

botao = tk.Button(ecra, text="Mostrar Gato",command=mostrar_gato)
botao.pack(pady=10)

imagem_label = tk.Label(ecra)
imagem_label.pack()

ecra.mainloop()
