import osimport os
from tkinter import *
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk  # Make sure to import Image and ImageTk from PIL

root = Tk()
root.title('teste aula')
root.geometry('900x700')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = TkinterMapView(my_label, width=800, height=600, corner_radius=0)
map_widget.set_position(39.81222, -7.99138)  # Set the map center coordinates

# Get the current directory and set the image path
current_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_path, "images", "braganca.png")  # Make sure to specify the file name here

# Verify that the image exists
if os.path.exists(image_path):
    # Load the image
    braganca_image = Image.open(image_path)
    braganca_image = ImageTk.PhotoImage(braganca_image)

    # Add the image as a map marker
    map_widget.set_marker(39.81222, -7.99138, image=braganca_image)  # Example coordinates for the marker
else:
    print("Image file not found at:", image_path)

map_widget.set_zoom(7)
map_widget.pack()

root.mainloop()
from tkinter import *
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

root = Tk()
root.title('teste aula')
root.geometry('900x700')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = TkinterMapView(my_label, width=800, height=600, corner_radius=0)
map_widget.set_position(39.81222, -7.99138)
current_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_path, "images", "braganca.png")

# Verify that the image exists
if os.path.exists(image_path):
    # Load the image
    braganca_image = Image.open(image_path)
    braganca_image = ImageTk.PhotoImage(braganca_image)


    map_widget.set_marker(39.81222, -7.99138, image=braganca_image)
else:
    print("Image file not found at:", image_path)

map_widget.set_zoom(7)
map_widget.pack()

root.mainloop()
