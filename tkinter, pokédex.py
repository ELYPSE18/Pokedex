import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.geometry("1024x768")
fenetre.title("Pokédex")

class DB:
    def __init__(self, nom, type, capacités):
            self.nom = nom
            self.type = type
            self.capacités = capacités
            # self.image = ImageTk.PhotoImage(Image.open("images/" + self.nom + ".png"))



sangoku = DB("san goku", "saiyan", "téléportation")
sangohan = DB("san gohan", "saiyan", "malin comme un singe")
krilin = DB("krilin", "humain", "a un cyborg comme femme")

persos = [sangoku, sangohan, krilin]
    

         


# def change_label_text(text):
#     label.config(text=text)

def affiche_detail(indexDuPerso):
     nom_label.config(text="nom" + persos[indexDuPerso].nom)
     type_label.config(text="type" + DB.type)
     capacités_label.config(text="capacités"+ DB.capacités)
   

 #création d'un logo sur fenetre tkinter
image = Image.open("Dragon-Ball-Logo.png")
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)
label = tk.Label(fenetre, image=image)
label.place(x=10, y=10)



 #creation d'une liste déroulante
listbox = tk.Listbox(fenetre)
listbox.place(x=800, y=300)

#ajout de pokemon à la liste déroulante
listbox.insert(tk.END, "sangoku")
listbox.insert(tk.END, "sangohan")
listbox.insert(tk.END, "krilin")



#création d'un bouton por récupurer la valeur saisie
button = tk.Button(fenetre, text="Afficher les détails", command=affiche_detail)
button.place(x=810, y=464)

DB_frame = tk.Frame(fenetre)
DB_frame.place()

nom_label = tk.Label(DB_frame, text="")
nom_label.pack()

type_label = tk.Label(DB_frame, text="")
type_label.pack

capacités_label = tk.Label(DB_frame, text="")
capacités_label.pack()


# création d'un champ de saisie
champ_saisie = tk.Entry(fenetre)
champ_saisie.place(x=800, y=491)








fenetre.mainloop()