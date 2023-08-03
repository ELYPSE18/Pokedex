import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.geometry("1000x800")
fenetre.title("Pokédex")

class DB:
    def __init__(self, nom, type, capacités, image):
            self.nom = nom
            self.type = type
            self.capacités = capacités
            self.image = image
            

sangoku = DB("san goku", "saiyan", "téléportation", "img/sangoku.png" )
sangohan = DB("san gohan", "saiyan", "malin comme un singe", "img/sangohan.png" )
krilin = DB("krilin", "humain", "a un cyborg comme femme", "img/krilin.png" )

persos = [sangoku, sangohan, krilin]

def affiche_detail():
    indexDuPerso = int(listbox.curselection()[0])
    nom_label.config(text=f"nom {persos[indexDuPerso].nom}")
    type_label.config(text=f"type {persos[indexDuPerso].type}")
    capacités_label.config(text=f"capacités {persos[indexDuPerso].capacités}")
    img = Image.open(persos[indexDuPerso].image)
    img = img.resize((100,100))
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo
   
def ajouter_combattant():
     nom = nom_input_label.get()
     type = type_input_label.get()
     capacités = capacités_input_label.get()
     persos.append(DB(nom, type, capacités))
     listbox.insert(tk.END, nom)
     nom_input_label.delete(0, tk.END)
     type_input_label.delete(0, tk.END)
     capacités_input_label.delete(0, tk.END)

     messagebox.showinfo("Ajout réussi", "Combattant ajouté")

 #création d'un logo sur fenetre tkinter

logo = Image.open("Dragon-Ball-Logo.png")
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
label = tk.Label(fenetre, image=logo)
label.place(x=10, y=10)

image = Image.open("img/ball.png")
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(fenetre, image=image)


nom_label = tk.Label(fenetre, text=" ")
type_label = tk.Label(fenetre, text=" ")
capacités_label = tk.Label(fenetre, text=" ")
nom_label.place(x=300, y=500)
type_label.place(x=300, y=520)
capacités_label.place(x=300, y=540)
image_label.place(x=300, y=250)

 #creation d'une liste déroulante
listbox = tk.Listbox(fenetre)
listbox.place(x=800, y=200)

 #ajout de pokemon à la liste déroulante
listbox.insert(tk.END, "sangoku")
listbox.insert(tk.END, "sangohan")
listbox.insert(tk.END, "krilin")



 #création d'un bouton por récupurer la valeur saisie
button = tk.Button(fenetre, text="Afficher les détails", command=affiche_detail)
button.place(x=810, y=367)


 #création d'un bouton "ajout de personnage"
button = tk.Button(fenetre, text="Ajouter un personnage", command=ajouter_combattant)
button.place(x=810, y=700)


 #creation des champs de saisie "Nouveau combattant"
nouveau_combattant = tk.Frame(fenetre)
nouveau_combattant.place(x=780, y=500)

nom_input_label = tk.Label(nouveau_combattant, text="Nom du combattant")
nom_input_label.grid(row=0, column=0, padx=10, pady=1)
nom_input_label = tk.Entry(nouveau_combattant)
nom_input_label.grid(row=1, column=0, padx=10, pady=1)

type_input_label = tk.Label(nouveau_combattant, text="Type du combattant")
type_input_label.grid(row=2, column=0, padx=10, pady=1)
type_input_label = tk.Entry(nouveau_combattant)
type_input_label.grid(row=3, column=0, padx=10, pady=1)

capacités_input_label = tk.Label(nouveau_combattant, text="Capacités du combattant")
capacités_input_label.grid(row=4, column=0, padx=10, pady=1)
capacités_input_label = tk.Entry(nouveau_combattant)
capacités_input_label.grid(row=5, column=0, padx=10, pady=1)










fenetre.mainloop()