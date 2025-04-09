import os.path
from tkinter import *
from PIL import Image, ImageTk
import tkintermapview


root = Tk()
root.title('teste aula')
root.geometry('900x700')


my_label = LabelFrame(root)
my_label.pack(pady=20)


map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
braganca_image = ImageTk.PhotoImage(Image.open(os.path.join((current_path, "images", "img.png")).resize(80, 80)))

marker_1 = map_widget.set_marker(41.8060, -6.7567, text="braganca", icon=braganca_image)

map_widget.set_position(39.81222, -7.99138)

map_widget.set_zoom(7)
map_widget.pack()
root.mainloop()
