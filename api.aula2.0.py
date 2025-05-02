import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def busca_piada():
    url = "https://api.chucknorris.io/jokes/random"
    resposta = requests.get(url)

