from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import filedialog
from pathlib import Path
import shutil
from ftplib import FTP
import os

root = Tk()
root.geometry("1200x800-160-0")
root.iconbitmap("img/drone33.ico")
root.title("sauvegarde / export de site")
root.resizable(False, False)
root.config(background='#000')
slider_index = 1
img1 = ImageTk.PhotoImage(Image.open("img/slider/1.png"))
img2 = ImageTk.PhotoImage(Image.open("img/slider/2.png"))
img3 = ImageTk.PhotoImage(Image.open("img/slider/3.png"))
img4 = ImageTk.PhotoImage(Image.open("img/slider/4.png"))
img5 = ImageTk.PhotoImage(Image.open("img/slider/5.png"))
img6 = ImageTk.PhotoImage(Image.open("img/slider/6.png"))
img7 = ImageTk.PhotoImage(Image.open("img/slider/7.png"))
img8 = ImageTk.PhotoImage(Image.open("img/slider/8.png"))
img9 = ImageTk.PhotoImage(Image.open("img/slider/9.png"))
img10 = ImageTk.PhotoImage(Image.open("img/slider/10.png"))
img11 = ImageTk.PhotoImage(Image.open("img/slider/11.png"))
img12 = ImageTk.PhotoImage(Image.open("img/slider/12.png"))
img13 = ImageTk.PhotoImage(Image.open("img/slider/13.png"))
img14 = ImageTk.PhotoImage(Image.open("img/slider/14.png"))
img15 = ImageTk.PhotoImage(Image.open("img/slider/15.png"))
img16 = ImageTk.PhotoImage(Image.open("img/slider/16.png"))
img17 = ImageTk.PhotoImage(Image.open("img/slider/17.png"))
img18 = ImageTk.PhotoImage(Image.open("img/slider/18.png"))
img19 = ImageTk.PhotoImage(Image.open("img/slider/19.png"))
img20 = ImageTk.PhotoImage(Image.open("img/slider/20.png"))
img21 = ImageTk.PhotoImage(Image.open("img/slider/21.png"))
img22 = ImageTk.PhotoImage(Image.open("img/slider/22.png"))
img23 = ImageTk.PhotoImage(Image.open("img/slider/23.png"))
img24 = ImageTk.PhotoImage(Image.open("img/slider/24.png"))
img25 = ImageTk.PhotoImage(Image.open("img/slider/25.png"))
img26 = ImageTk.PhotoImage(Image.open("img/slider/26.png"))
img27 = ImageTk.PhotoImage(Image.open("img/slider/27.png"))
img28 = ImageTk.PhotoImage(Image.open("img/slider/28.png"))
img29 = ImageTk.PhotoImage(Image.open("img/slider/29.png"))
img30 = ImageTk.PhotoImage(Image.open("img/slider/30.png"))
img31 = ImageTk.PhotoImage(Image.open("img/slider/31.png"))
img32 = ImageTk.PhotoImage(Image.open("img/slider/32.png"))
img33 = ImageTk.PhotoImage(Image.open("img/slider/33.png"))
img34 = ImageTk.PhotoImage(Image.open("img/slider/34.png"))
img35 = ImageTk.PhotoImage(Image.open("img/slider/35.png"))
img36 = ImageTk.PhotoImage(Image.open("img/slider/36.png"))
img37 = ImageTk.PhotoImage(Image.open("img/slider/37.png"))
img38 = ImageTk.PhotoImage(Image.open("img/slider/38.png"))
img39 = ImageTk.PhotoImage(Image.open("img/slider/39.png"))
img40 = ImageTk.PhotoImage(Image.open("img/slider/40.png"))
img41 = ImageTk.PhotoImage(Image.open("img/slider/41.png"))
img42 = ImageTk.PhotoImage(Image.open("img/slider/42.png"))
img43 = ImageTk.PhotoImage(Image.open("img/slider/43.png"))
img44 = ImageTk.PhotoImage(Image.open("img/slider/44.png"))
img45 = ImageTk.PhotoImage(Image.open("img/slider/45.png"))
img46 = ImageTk.PhotoImage(Image.open("img/slider/46.png"))
img47 = ImageTk.PhotoImage(Image.open("img/slider/47.png"))
img48 = ImageTk.PhotoImage(Image.open("img/slider/48.png"))


# creation functions
def create_button(window, button_text, posx, posy):
    button = Button(window, text=button_text, bg='#b40108', fg='#fff', bd=0, padx=18.45, pady=15.45)
    font_button = font.Font(family="Segoe UI", size=14, weight='bold')
    button['font'] = font_button
    button.place(x=posx, y=posy)
    return button


def create_input(window, text_label, label_posx, label_posy, input_posx, input_posy):
    user_label = Label(window, text=text_label, font="none 14 bold", bg='#b40108', fg='#fff', bd=0, width="20", justify=CENTER).place(x=label_posx, y=label_posy)
    user_input = Entry(window, bg='#b40108', fg='#fff', bd=0, width="35", justify=CENTER)
    font_input = font.Font(family="Segoe UI", size=13, weight='bold')
    user_input['font'] = font_input
    user_input.place(x=input_posx, y=input_posy)
    return user_input


# event trigger functions
def save():
    print("sauvegarde")
    open_ftp_window()


def open_ftp_window():
    ftp_wd = Toplevel()
    ftp_wd.geometry("800x400-400-200")
    ftp_wd.iconbitmap("img/drone33.ico")
    ftp_wd.title("exportation du site")
    ftp_wd.resizable(False, False)
    ftp_wd.config(background='#000')
    host_input = create_input(ftp_wd, "nom d'hôte", 50, 50, 325, 50)
    user_input = create_input(ftp_wd, "nom d'utilisateur", 50, 100, 325, 100)
    user_password = create_input(ftp_wd, "mot de passe", 50, 150, 325, 150)
    site_name = create_input(ftp_wd, "nom du site", 50, 200, 325, 200)

    host = "depot-drone33.go.yj.fr"
    username = "gverepzz"
    password = "CGRj2Mfyr1HdQx"

    def retrieve_file():
        with FTP(host) as ftp:
            ftp.login(user=username, passwd=password)
            print(ftp.getwelcome())

            with open('database.txt', 'wb') as f:
                ftp.retrbinary("RETR " + "hello.txt", f.write, 1024)

            ftp.quit()

    validation_button = create_button(ftp_wd, "Valider", 325, 275)
    validation_button['command'] = retrieve_file


# all widgets in the migration window

def open_migration_window():
    mig_wd = Toplevel()
    mig_wd.geometry("1500x900")
    mig_wd.iconbitmap("img/drone33.ico")
    mig_wd.title("exportation du site")
    mig_wd.resizable(False, False)
    mig_wd.config(background='#000')
    email = create_input(mig_wd, 'email nouvel admin', 30, 20, 300, 20)
    username = create_input(mig_wd, 'nom nouvel admin', 30, 50, 300, 50)
    mdp = create_input(mig_wd, 'mdp nouvel admin', 830, 20, 1100, 20)
    import_logo = create_button(mig_wd, 'importer un logo', 35, 100)
    import_logo["command"] = lambda: import_img("logo")
    import_pilote1 = create_button(mig_wd, 'importer photo pilote 1', 35, 200)
    import_pilote1["command"] = lambda: import_img("pilote1")
    import_pilote2 = create_button(mig_wd, 'importer photo pilote 2', 35, 300)
    import_pilote2["command"] = lambda: import_img("pilote2")
    import_cgv = create_button(mig_wd, 'importer CGV', 35, 400)
    import_cgv["command"] = lambda: import_img("cgv")
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
    global img13
    global img14
    global img15
    global img16
    global img17
    global img18
    global img19
    global img20
    global img21
    global img22
    global img23
    global img24
    global img25
    global img26
    global img27
    global img28
    global img29
    global img30
    global img31
    global img32
    global img33
    global img34
    global img35
    global img36
    global img37
    global img38
    global img39
    global img40
    global img41
    global img42
    global img43
    global img44
    global img45
    global img46
    global img47
    global img48

    variable_list = []

    img_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24, img25, img26, img27, img28, img29, img30, img31, img32, img33, img34, img35, img36, img37, img38, img39, img40, img41, img42, img43, img44, img45, img46, img47, img48]

    global slider_label
    slider_label = Label(mig_wd, image=img1)
    slider_label.place(x=390, y=90)

    def string_parser(textstr):
        return textstr.replace('â', '\\\\u00e2').replace('à', '\\\\u00e0').replace('ä', '\\\\u00e4') \
            .replace('ç', '\\\\u00e7').replace('é', '\\\\u00e9').replace('è', '\\\\u00e8') \
            .replace('ê', '\\\\u00ea').replace('ë', '\\\\u00eb').replace('î', '\\\\u00ee').replace('ï', '\\\\u00ef') \
            .replace('ô', '\\\\u00f4').replace('ö', '\\\\u00f6').replace('ù', '\\\\u00f9') \
            .replace('û', '\\\\u00fb').replace('ü', '\\\\u00fc').replace('À', '\\\\u00c0') \
            .replace('É', '\\\\u00c9').replace('È', '\\\\u00c8').replace('Ç', '\\\\u00c7') \
            .replace('Ê', '\\\\u00ca').replace('&', '&amp;')

    def backward(img_number, wd):
        global slider_index
        global slider_label
        global button_forward
        global button_backward

        slider_index -= 1

        slider_label.place_forget()
        slider_label = Label(wd, image=img_list[img_number - 1])
        button_forward = Button(mig_wd, text=">>", command=lambda: forward(img_number + 1, mig_wd)).place(x=340, y=380)
        button_backward = Button(mig_wd, text="<<", command=lambda: backward(img_number - 1, mig_wd)).place(x=340, y=310)
        slider_label.place(x=390, y=90)
        print("backward ", slider_index)

        if img_number == 1:
            button_backward = Button(mig_wd, text="<<", state=DISABLED).place(x=340, y=310)

    def forward(img_number, wd):
        global slider_index
        global slider_label
        global button_forward
        global button_backward

        slider_index += 1

        slider_label.place_forget()
        slider_label = Label(wd, image=img_list[img_number - 1])
        button_forward = Button(mig_wd, text=">>", command=lambda: forward(img_number + 1, mig_wd)).place(x=340, y=380)
        button_backward = Button(mig_wd, text="<<", command=lambda: backward(img_number - 1, mig_wd)).place(x=340, y=310)
        slider_label.place(x=390, y=90)

        if img_number == 48:
            button_forward = Button(mig_wd, text=">>", state=DISABLED).place(x=340, y=380)

    def validation(text):
        global slider_index
        my_user_text = text.get()
        if ((slider_index - 1) >= len(variable_list)):
            variable_list.append(my_user_text)
        else:
            variable_list[slider_index - 1] = my_user_text

        text.delete(0, 'end')

    def import_img(dest):
        filename = filedialog.askopenfilename(initialdir=Path.cwd(), title="Selectionnez un logo", filetypes=(("png files", "*.png"), ("all files", "*.*")))
        image_to_import = ImageTk.PhotoImage(Image.open(filename))
        img_path = Path(filename)
        actual_dir = str(Path.cwd())
        if dest == "logo":
            dest_dir = Path("{0}/site/wp-content/uploads/2018/01".format(actual_dir))
            shutil.copy(img_path.absolute(), dest_dir)
            Path.rename(Path("{0}/site/wp-content/uploads/2018/01/{1}".format(actual_dir, img_path.name)), Path("{0}/site/wp-content/uploads/2018/01/logo-{1}.png".format(actual_dir, variable_list[4])))
        elif dest == "pilote1":
            dest_dir = Path("{0}/site/wp-content/uploads/2019/09".format(actual_dir))
            shutil.copy(img_path.absolute(), dest_dir)
            Path.rename(Path("{0}/site/wp-content/uploads/2019/09/{1}".format(actual_dir, img_path.name)), Path("{0}/site/wp-content/uploads/2019/09/Team-Adrien-768x768.png".format(actual_dir)))
        elif dest == "pilote2":
            dest_dir = Path("{0}/site/wp-content/uploads/2019/09".format(actual_dir))
            shutil.copy(img_path.absolute(), dest_dir)
            Path.rename(Path("{0}/site/wp-content/uploads/2019/09/{1}".format(actual_dir, img_path.name)), Path("{0}/site/wp-content/uploads/2019/09/Team-Charles-768x768.png".format(actual_dir)))
        elif dest == "cgv":
            dest_dir = Path("{0}/site/wp-content/uploads/2020/04".format(actual_dir))
            shutil.copy(img_path.absolute(), dest_dir)
            Path.rename(Path("{0}/site/wp-content/uploads/2020/04/{1}".format(actual_dir, img_path.name)), Path("{0}/site/wp-content/uploads/2020/04/CGV-{1}.pdf".format(actual_dir, variable_list[3])))

    def unzip():
        for dir in os.listdir('.'):
            if (dir.endswith('.zip')):
                shutil.unpack_archive(dir, 'site', 'zip')

    def zip():
        new_name = ""

        for dir in os.listdir('.'):
            if dir.endswith('.zip'):
                org_name = dir

                for i in range(len(org_name) - 4):
                    new_name = new_name + org_name[i]
        shutil.make_archive(new_name, 'zip', 'site')
        shutil.rmtree('site', ignore_errors=True)

    def file_operations(var_list, name, pw, email):
        Label(mig_wd, text="Les changements sont en cours, veuillez patienter...", font="none 14 bold", bg='#000000', fg='#fff', bd=0, justify=CENTER).place(x=50, y=700)
        unzip()
        sql_file = ''
        admin_name = name.get()
        admin_pw = pw.get()
        admin_email = email.get()
        actual_dir = str(Path.cwd())

        for dir in os.listdir('{0}/site/dup-installer'.format(actual_dir)):
            if dir.endswith('.sql'):
                sql_file = dir

        titre_min_espace1 = "drone 33"
        titre_min_espace2 = var_list[0]

        titre_maj_espace1 = "Drone 33"
        titre_maj_espace2 = var_list[1]

        titre_fullmaj_espace1 = "DRONE 33"
        titre_fullmaj_espace2 = var_list[2]

        titre_fullmaj1 = "DRONE33"
        titre_fullmaj2 = var_list[3]

        titre_min1 = "drone33"
        titre_min2 = var_list[4]

        titre_maj1 = "Drone33"
        titre_maj2 = var_list[5]

        rougeenbleu1 = "#c80108"
        rougeenbleu2 = var_list[6]

        ED1 = "ED5378"
        ED2 = var_list[7]

        numero_sans_points1 = "06 66 52 33 64"
        numero_sans_points2 = var_list[8]

        numero_avec_points1 = "06.66.52.33.64"
        numero_avec_points2 = var_list[9]

        youtube1 = "https://www.youtube.com/c/{0}".format(titre_min2)
        youtube2 = var_list[10]

        facebook1 = "www.facebook.com/{0}fr".format(titre_min2)
        facebook2 = var_list[11]

        twitter1 = "twitter.com/adriensifre"
        twitter2 = var_list[12]

        insta1 = "instagram.com/fotografik33"
        insta2 = var_list[13]

        linkedin1 = "linkedin.com/company/15870000"
        linkedin2 = var_list[14]

        contact1 = "contact@{0}.fr".format(titre_min2)
        contact2 = var_list[15]

        hundred_metters1 = "150 m"
        hundred_metters2 = var_list[16]

        thousand_metters1 = "1000 m"
        thousand_metters2 = var_list[17]

        small_scrolling_nbr1 = "150"
        small_scrolling_nbr2 = var_list[18]

        big_scrolling_nbr1 = "1000"
        big_scrolling_nbr2 = var_list[19]

        first_pilote_name_caps1 = "Adrien SIFRE"
        first_pilote_name_caps2 = var_list[20]

        first_pilote_name1 = "Adrien Sifre"
        first_pilote_name2 = var_list[21]

        tribunaux1 = "aux tribunaux compétents de Bordeaux"
        tribunaux2 = var_list[22]

        siren1 = " SIREN 820 758 019 00013"
        siren2 = var_list[23]

        second_pilote_name1 = "Charles Debitus"
        second_pilote_name2 = var_list[24]

        second_pilote_name_caps1 = "Charles DEBITUS"
        second_pilote_name_caps2 = var_list[25]

        sieca1 = "SIECA -"
        sieca2 = var_list[26]

        contrat1 = "de contrat : 6539"
        contrat2 = var_list[27]

        premier_pilote1 = "Adrien est le fondateur de {0} mais également de fotografik33 et visite-virtuelle33. Il fait également partie du collectif Creative4. Avec plus de 100 heures de vol sur des drones DJI, il est spécialisé dans la photographie et la vidéo pour les domaines industriel et commercial (3D, Cartographie, Mesures, Immobilier, Marketing ..).".format(titre_min2)
        premier_pilote2 = var_list[28]

        second_pilote1 = "Riche d'une expérience de plus de 15 ans dans différents postes de l'audiovisuel (chef de plateau, assistant mise en scène ou encore cadreur et compositeur), Charles est un télé-pilote spécialisé sur notre offre TV & Cinéma (Broadcasting) mais également sur notre offre Agriculture."
        second_pilote2 = var_list[29]

        title_text_premier_pilote1 = "Adrien"
        title_text_premier_pilote2 = var_list[30]

        title_text_second_pilote1 = "Charles"
        title_text_second_pilote2 = var_list[31]

        roseenbleu1 = "#c1230b"
        roseenbleu2 = var_list[32]

        roseenjaune1 = "#f92763"
        roseenjaune2 = var_list[33]

        adresse1 = "84 Avenue Pasteur,<br \\\\/>33185 le Haillan<br \\\\/>Gironde<br \\\\/>Nouvelle Aquitaine"

        rue = var_list[34]
        code_postale = var_list[35]
        departement = var_list[36]
        region = var_list[37]

        bgna1 = "Bordeaux - Gironde - Nouvelle Aquitaine"
        bgna2 = var_list[38]

        small_adress1 = "33185 LE HAILLAN"
        small_adress2 = var_list[39]

        vdr1 = "Bordeaux, en gironde et en Nouvelle Aquitaine"
        vdr2 = var_list[40]

        tpvdr1 = "télé-pilotes de drone à bordeaux, gironde et en nouvelle aquitaine"
        tpvdr2 = var_list[41]

        ctpvdr1 = "Télé-Pilotes de drone à Bordeaux, Gironde et Nouvelle Aquitaine"
        ctpvdr2 = var_list[42]

        tiret_ville1 = "- Bordeaux"
        tiret_ville2 = var_list[43]

        adresse_contactez_nous1 = "{0} - GIRONDE".format(small_adress2)
        adresse_contactez_nous2 = var_list[44]

        reportage_video1 = "Des reportages vidéos complets à Bordeaux et en Gironde"
        reportage_video2 = var_list[45]

        ville_et_region1 = "Bordeaux et sa région"
        ville_et_region2 = var_list[46]

        ville_entre_par1 = "(Gironde, Nouvelle-Aquitaine)"
        ville_entre_par2 = var_list[47]

        parse_tribunaux1 = string_parser(tribunaux1)
        parse_tribunaux2 = string_parser(tribunaux2)
        parse_premier_pilote1 = string_parser(premier_pilote1)
        parse_premier_pilote2 = string_parser(premier_pilote2)
        parse_second_pilote1 = string_parser(second_pilote1)
        parse_second_pilote2 = string_parser(second_pilote2)
        parse_adresse1 = string_parser(adresse1)
        parse_bgna1 = string_parser(bgna1)
        parse_bgna2 = string_parser(bgna2)
        parse_small_adress1 = string_parser(small_adress1)
        parse_small_adress2 = string_parser(small_adress2)
        parse_vdr1 = string_parser(vdr1)
        parse_vdr2 = string_parser(vdr2)
        parse_tpvdr1 = string_parser(tpvdr1)
        parse_tpvdr2 = string_parser(tpvdr2)
        parse_ctpvdr1 = string_parser(ctpvdr1)
        parse_ctpvdr2 = string_parser(ctpvdr2)
        parse_tiret_ville1 = string_parser(tiret_ville1)
        parse_tiret_ville2 = string_parser(tiret_ville2)
        parse_titre_min_espace1 = string_parser(titre_min_espace1)
        parse_titre_min_espace2 = string_parser(titre_min_espace2)
        parse_titre_maj_espace1 = string_parser(titre_maj_espace1)
        parse_titre_maj_espace2 = string_parser(titre_maj_espace2)
        parse_titre_fullmaj_espace1 = string_parser(titre_fullmaj_espace1)
        parse_titre_fullmaj_espace2 = string_parser(titre_fullmaj_espace2)
        parse_titre_fullmaj1 = string_parser(titre_fullmaj1)
        parse_titre_fullmaj2 = string_parser(titre_fullmaj2)
        parse_titre_min1 = string_parser(titre_min1)
        parse_titre_min2 = string_parser(titre_min2)
        parse_titre_maj1 = string_parser(titre_maj1)
        parse_titre_maj2 = string_parser(titre_maj2)
        parse_first_pilote_name_caps1 = string_parser(first_pilote_name_caps1)
        parse_first_pilote_name_caps2 = string_parser(first_pilote_name_caps2)
        parse_first_pilote_name1 = string_parser(first_pilote_name1)
        parse_first_pilote_name2 = string_parser(first_pilote_name2)
        parse_second_pilote_name1 = string_parser(second_pilote_name1)
        parse_second_pilote_name2 = string_parser(second_pilote_name2)
        parse_second_pilote_name_caps1 = string_parser(second_pilote_name_caps1)
        parse_second_pilote_name_caps2 = string_parser(second_pilote_name_caps2)
        parse_rue = string_parser(rue)
        parse_code_postal = string_parser(code_postale)
        parse_departement = string_parser(departement)
        parse_region = string_parser(region)
        parse_title_text_premier_pilote1 = string_parser(title_text_premier_pilote1)
        parse_title_text_premier_pilote2 = string_parser(title_text_premier_pilote2)
        parse_title_text_second_pilote1 = string_parser(title_text_second_pilote1)
        parse_title_text_second_pilote2 = string_parser(title_text_second_pilote2)
        parse_adresse_contactez_nous1 = string_parser(adresse_contactez_nous1)
        parse_adresse_contactez_nous2 = string_parser(adresse_contactez_nous2)
        parse_reportage_video1 = string_parser(reportage_video1)
        parse_reportage_video2 = string_parser(reportage_video2)
        parse_ville_et_region1 = string_parser(ville_et_region1)
        parse_ville_et_region2 = string_parser(ville_et_region2)
        parse_ville_entre_par1 = string_parser(ville_entre_par1)
        parse_ville_entre_par2 = string_parser(ville_entre_par2)

        sql_path = Path("{0}/site/dup-installer/{1}".format(actual_dir, sql_file))

        # read input file
        fin = open(sql_path, "r", encoding='utf-8')
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        data = data.replace("\\\\u2019", "'").replace("\\\\u2013", "-").replace("\\'", "'") \
            .replace(parse_titre_min_espace1, parse_titre_min_espace2) \
            .replace(parse_titre_maj_espace1, parse_titre_maj_espace2) \
            .replace(parse_titre_fullmaj_espace1, parse_titre_fullmaj_espace2) \
            .replace(parse_titre_fullmaj1, parse_titre_fullmaj2).replace(parse_titre_min1, parse_titre_min2) \
            .replace(parse_titre_maj1, parse_titre_maj2) \
            .replace(rougeenbleu1, rougeenbleu2).replace(ED1, ED2).replace(numero_sans_points1, numero_sans_points2) \
            .replace(numero_avec_points1, numero_avec_points2).replace(youtube1, youtube2) \
            .replace(facebook1, facebook2).replace(twitter1, twitter2).replace(insta1, insta2) \
            .replace(linkedin1, linkedin2).replace(contact1, contact2).replace(hundred_metters1, hundred_metters2) \
            .replace(thousand_metters1, thousand_metters2) \
            .replace('ending_number\\\":{0}'.format(small_scrolling_nbr1), 'ending_number\\\":{0}'.format(small_scrolling_nbr2)) \
            .replace('ending_number\\\":{0}'.format(big_scrolling_nbr1), 'ending_number\\\":{0}'.format(big_scrolling_nbr2)) \
            .replace(parse_first_pilote_name_caps1, parse_first_pilote_name_caps2) \
            .replace(parse_first_pilote_name1, parse_first_pilote_name2) \
            .replace(parse_tribunaux1, parse_tribunaux2).replace(siren1, siren2) \
            .replace(parse_second_pilote_name1, parse_second_pilote_name2).replace(parse_second_pilote_name_caps1, parse_second_pilote_name_caps2) \
            .replace(sieca1, sieca2).replace(contrat1, contrat2).replace(parse_premier_pilote1, parse_premier_pilote2) \
            .replace(parse_second_pilote1, parse_second_pilote2) \
            .replace("title_text\\\":\\\"{0}".format(parse_title_text_premier_pilote1), "title_text\\\":\\\"{0}".format(parse_title_text_premier_pilote2)) \
            .replace("title_text\\\":\\\"{0}".format(parse_title_text_second_pilote1), "title_text\\\":\\\"{0}".format(parse_title_text_second_pilote2)) \
            .replace(roseenbleu1, roseenbleu2).replace(roseenjaune1, roseenjaune2) \
            .replace(parse_adresse1, "{0},<br \\\\/>{1}<br \\\\/>{2}<br \\\\/>{3}".format(parse_rue, parse_code_postal, parse_departement, parse_region)) \
            .replace(parse_bgna1, parse_bgna2).replace(parse_small_adress1, parse_small_adress2).replace(parse_vdr1, parse_vdr2).replace(parse_tpvdr1, parse_tpvdr2) \
            .replace(parse_ctpvdr1, parse_ctpvdr2).replace(parse_tiret_ville1, parse_tiret_ville2) \
            .replace(parse_adresse_contactez_nous1, parse_adresse_contactez_nous2) \
            .replace(parse_reportage_video1, parse_reportage_video2).replace(parse_ville_et_region1, parse_ville_et_region2) \
            .replace(parse_ville_entre_par1, parse_ville_entre_par2)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(sql_path, "w", encoding='utf-8')
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()

        # read CSS file

        css_path = Path("{0}/site/wp-content/uploads/apollo13_framework_files/css/user.css".format(actual_dir))
        fin = open(css_path, "r", encoding='utf-8')
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        data = data.replace(rougeenbleu1, rougeenbleu2)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(css_path, "w", encoding='utf-8')
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()

        # add the sql admmin user and password at the end of the file

        with open(sql_path, encoding='utf-8') as file:
            lines = file.readlines()
            lines.insert(59845, 'TRUNCATE mod238_users;\n')
            lines.insert(59846, 'TRUNCATE mod238_usermeta;\n')
            lines.insert(59847, "INSERT INTO mod238_users (ID, user_login, user_pass, user_nicename, user_email, user_url, user_registered, user_activation_key, user_status, display_name) VALUES ('1', '{0}', MD5('{1}'), '{0}', '{2}', '', '2021-01-02 00:00:00', '', '0', '{0}');\n".format(name, pw, email))
            lines.insert(59848, '''INSERT INTO mod238_usermeta (umeta_id, user_id, meta_key, meta_value) VALUES (NULL, '1', 'mod238_capabilities', 'a:1:{s:13:"administrator";s:1:"1";}');\n''')
            lines.insert(59849, '''INSERT INTO mod238_usermeta (umeta_id, user_id, meta_key, meta_value) VALUES (NULL, '1', 'mod238_user_level', '10');\n''')
            with open(sql_path, 'w', encoding='utf-8') as _file:
                for line in lines:
                    _file.write(line)
        zip()

        Label(mig_wd, text="Changements terminés, vous pouvez fermer l'application en toute sécurité !", font="none 14 bold", bg='#000000', fg='#fff', bd=0, justify=CENTER).place(x=50, y=700)

    global button_backward
    global button_forward
    button_backward = Button(mig_wd, text="<<", state=DISABLED).place(x=340, y=310)
    button_forward = Button(mig_wd, text=">>", command=lambda: forward(2, mig_wd)).place(x=340, y=380)
    user_text = create_input(mig_wd, 'entrez le texte', 50, 600, 400, 600)
    user_text["width"] = 70
    validate_btn = create_button(mig_wd, 'valider', 1150, 575)
    validate_btn['command'] = lambda: validation(user_text)
    end_button = create_button(mig_wd, 'terminer', 1300, 575)
    end_button['command'] = lambda: file_operations(variable_list, username, mdp, email)


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
