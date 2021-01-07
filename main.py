from tkinter import *

root = Tk()
root.geometry("1200x800")
root.title("sauvegarde / export drone33")
root.resizable(False, False)
root.config(background='black')


# trigger functions
def clicked_button(buttonNumber):
    if buttonNumber == 1:
        message = Label(root, text="J'effectue une restauration du site drone 33")
    elif buttonNumber == 2:
        message = Label(root, text="Je déploie un nouveau site")
    message.grid(row=3, column=0)


# creating a label widget and implementing elements on the grid
button1 = Button(root, text="restauration", command=lambda: clicked_button(1)).grid(row=0, column=0)
button2 = Button(root, text="déployer un nouveau site", command=lambda: clicked_button(2)).grid(row=1, column=0)

# program loop
root.mainloop()
