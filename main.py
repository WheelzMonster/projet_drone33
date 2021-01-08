from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.geometry("1200x800-160-0")
root.iconbitmap("img/drone33.ico")
root.title("sauvegarde / export de site")
root.resizable(False, False)
root.config(background='#000')


# creation functions
def create_button(window, button_text, posx, posy):
    button = Button(window, text=button_text, bg='#b40108', fg='#fff', bd=0, padx=18.45, pady=15.45)
    font_button = font.Font(family="Segoe UI", size=14, weight='bold')
    button['font'] = font_button
    button.place(x=posx, y=posy)
    return button


def create_input(window, text_label, label_posx, label_posy, input_posx, input_posy):
    user_label = Label(window, text=text_label, font="none 14 bold", bg='#b40108', fg='#fff', bd=0, width="20", justify=CENTER, padx=10, pady=10)\
        .grid(sticky=W, row=label_row, column=label_col)
    user_input = Entry(window, bg='#b40108', fg='#fff', bd=0, width="60", justify=CENTER)
    font_input = font.Font(family="Segoe UI", size=14, weight='bold')
    user_input['font'] = font_input
    user_input.grid(row=input_row, column=input_col, pady=10)
    return user_input


# event trigger functions
def save():
    print("sauvegarde")


def open_migration_window():
    mig_wd = Toplevel()
    mig_wd.geometry("1500x900")
    mig_wd.iconbitmap("img/drone33.ico")
    mig_wd.title("exportation du site")
    mig_wd.resizable(False, False)
    mig_wd.config(background='#000')
    nom = create_input(mig_wd, 'nom', 1, 0, 1, 1)
    url = create_input(mig_wd, 'url', 2, 0, 2, 1)
    username = create_input(mig_wd, 'nom nouvel admin', 3, 0, 3, 1 )
    user_logo = create_button(mig_wd, "logo", 100, 200)
    accueil = create_button(mig_wd, "accueil", 100, 300)
    services = create_button(mig_wd, "services", 300, 300)
    pilotes = create_button(mig_wd, "tele_pilotes", 500, 300)
    realisations = create_button(mig_wd, "realisations", 700, 300)
    contact = create_button(mig_wd, "contact", 900, 300)


# all widgets in the main window
picture = Image.open("img/logo-drone33.png")
logo = picture.resize((400, 250), Image.ANTIALIAS)
drone_img = ImageTk.PhotoImage(logo)
drone_label = Label(image=drone_img, bd=0).place(x=390, y=260)
sauvegarde = create_button(root, "SAUVEGARDER", 165, 350)
migration = create_button(root, " MIGRATION ", 835, 350)
sauvegarde["command"] = save
migration["command"] = open_migration_window

# all widgets in the migration window


# program loop
root.mainloop()
