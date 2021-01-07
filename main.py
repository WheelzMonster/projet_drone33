from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.geometry("1200x800")
root.iconbitmap("img/drone33.ico")
root.title("sauvegarde / export drone33")
root.resizable(False, False)
root.config(background='#000')


# creation functions
def create_button(button_text, posx, posy):
    button = Button(root, text=button_text, bg='#b40108', fg='#fff', bd=0, padx=18.45, pady=15.45)
    font_button = font.Font(family="Segoe UI", size=14, weight='bold')
    button['font'] = font_button
    button.place(x=posx, y=posy)
    return button


# event trigger functions
def save():
    print("sauvegarde")


def migrate():
    print("migration")

# creating a label widget and implementing elements on the grid
picture = Image.open("img/logo-drone33.png")
logo = picture.resize((400, 250), Image.ANTIALIAS)
drone_img = ImageTk.PhotoImage(logo)
drone_label = Label(image=drone_img, bd=0).place(x=390, y=260)
sauvegarde = create_button("SAUVEGARDER", 165, 350)
migration = create_button(" MIGRATION ", 835, 350)
sauvegarde["command"] = save
migration["command"] = migrate


# program loop
root.mainloop()
