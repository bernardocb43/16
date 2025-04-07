import os.path
from tkinter import *
import tkintermapview

root = Tk()
root.title('teste aula')
root.geometry('900x700')


my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
map_widget.set_position(39.81222, -7.99138)

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

braganca_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images"))


map_widget.set_zoom(7)
map_widget.pack()
root.mainloop()

