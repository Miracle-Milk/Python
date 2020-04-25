from tkinter import *
from tkinter.filedialog import *

filename = ""

## function ##
def func_open() :
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF file", "*.gif"), ("All file", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

def func_zoomIn() :
    photo = PhotoImage(file = filename)
    photo = photo.zoom(2,2)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_zoomOut() :
    photo = PhotoImage(file = filename)
    photo = photo.subsample(2,2)
    pLabel.configure(image = photo)
    pLabel.image = photo

## main code ##
window = Tk()
window.geometry("400x400")
window.title("Art appreciation")
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
zoomMunu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
mainMenu.add_cascade(label = "picture effect",menu = zoomMunu)
fileMenu.add_command(label = "open file", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = func_exit)
zoomMunu.add_command(label = "zoom in", command = func_zoomIn)
zoomMunu.add_command(label = "zoom out",command = func_zoomOut)

window.mainloop()