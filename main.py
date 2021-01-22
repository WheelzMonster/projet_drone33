from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import filedialog

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
    user_label = Label(window, text=text_label, font="none 14 bold", bg='#b40108', fg='#fff', bd=0, width="20",
                       justify=CENTER).place(x=label_posx, y=label_posy)
    user_input = Entry(window, bg='#b40108', fg='#fff', bd=0, width="35", justify=CENTER)
    font_input = font.Font(family="Segoe UI", size=13, weight='bold')
    user_input['font'] = font_input
    user_input.place(x=input_posx, y=input_posy)
    return user_input


# event trigger functions
def save():
    print("sauvegarde")


def open_file(window):
    filename = filedialog.askopenfilename(initialdir="C:/Users/louis/Desktop/dev", title="Selectionnez unlogo",
                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_logo = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(window, text=filename).place(x=260, y=180)


# all widgets in the migration window

def open_migration_window():
    mig_wd = Toplevel()
    mig_wd.geometry("1500x900")
    mig_wd.iconbitmap("img/drone33.ico")
    mig_wd.title("exportation du site")
    mig_wd.resizable(False, False)
    mig_wd.config(background='#000')
    nom = create_input(mig_wd, 'nom du site', 30, 20, 300, 20)
    url = create_input(mig_wd, 'URL', 830, 20, 1100, 20)
    username = create_input(mig_wd, 'nom nouvel admin', 30, 50, 300, 50)
    mdp = create_input(mig_wd, 'mdp nouvel admin', 830, 50, 1100, 50)
    import_logo = create_button(mig_wd, 'importer un logo', 35, 100)
    import_logo["command"] = lambda: open_file(mig_wd)
    global img1
    global img2
    global img3
    global img4
    global img5
    global img6
    global img7
    global img8
    global img9
    global img10
    global img11
    global img12
    img1 = ImageTk.PhotoImage(Image.open("img/slider/accueil.png"))
    img2 = ImageTk.PhotoImage(Image.open("img/slider/accueil2.png"))
    img3 = ImageTk.PhotoImage(Image.open("img/slider/section_agriculture_vignes_zones_corrigées.png"))
    img4 = ImageTk.PhotoImage(Image.open("img/slider/section_architecture_imobilier_zones_corrigées.png"))
    img5 = ImageTk.PhotoImage(Image.open("img/slider/section_cartographie_mesures_zones_corrigées.png"))
    img6 = ImageTk.PhotoImage(Image.open("img/slider/section_contact_zones_corrigées.png"))
    img7 = ImageTk.PhotoImage(Image.open("img/slider/section_footer_zones_corrigées.png"))
    img8 = ImageTk.PhotoImage(Image.open("img/slider/section_marketing_communication_zones_corrigées.png"))
    img9 = ImageTk.PhotoImage(Image.open("img/slider/section_modelisation3D_zones_corrigées.png"))
    img10 = ImageTk.PhotoImage(Image.open("img/slider/section_partenariat_zones_corrigées.png"))
    img11 = ImageTk.PhotoImage(Image.open("img/slider/section_prix_legislation_service_zones_corrigées.png"))
    img12 = ImageTk.PhotoImage(Image.open("img/slider/section_TV_cinema_zones_corrigées.png"))

    img_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]

    global slider_label
    slider_label = Label(mig_wd, image=img1)
    slider_label.place(x=390, y=90)

    def backward(img_number):
        global slider_label

    def forward(img_number, wd):
        global slider_label

        slider_label.place_forget()
        slider_label = Label(wd, image=img_list[img_number-1])
        button_forward = Button(mig_wd, text=">>", command=lambda: forward(img_number+1, mig_wd)).place(x=340, y=380)
        button_back = Button(mig_wd, text="<<", command=lambda: backward(img_number-1)).place(x=340, y=310)
        slider_label.place(x=390, y=90)


    global button_back
    global button_forward
    button_back = Button(mig_wd, text="<<", command=backward).place(x=340, y=310)
    button_forward = Button(mig_wd, text=">>", command=lambda: forward(2, mig_wd)).place(x=340, y=380)


# all widgets in the main window
picture = Image.open("img/logo-drone33.png")
logo = picture.resize((400, 250), Image.ANTIALIAS)
drone_img = ImageTk.PhotoImage(logo)
drone_label = Label(image=drone_img, bd=0).place(x=390, y=260)
sauvegarde = create_button(root, "SAUVEGARDER", 165, 350)
migration = create_button(root, " MIGRATION ", 835, 350)
sauvegarde["command"] = save
migration["command"] = open_migration_window

# program loop
root.mainloop()
