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
            
sangoku = DB("San Goku", "Saiyan", "Téléportation", "img/sangoku.png" )
sangohan = DB("San Gohan", "Saiyan", "Malin comme un singe", "img/sangohan.png" )
krilin = DB("Krilin", "Humain", "A un cyborg comme femme", "img/krilin.png" )
Piccolo = DB("Piccolo", "Namec", "je sais pas, il est cool", "img/piccolo.png" )

persos = [sangoku, sangohan, krilin, Piccolo]

def affiche_detail():
    indexDuPerso = int(listbox.curselection()[0])
    nom_label.config(text=f"Nom : {persos[indexDuPerso].nom}")
    type_label.config(text=f"Type : {persos[indexDuPerso].type}")
    capacités_label.config(text=f"Capacités : {persos[indexDuPerso].capacités}")
    img = Image.open(persos[indexDuPerso].image)
    img = img.resize((300,300))
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo
   
def ajouter_combattant():
     nom = nom_input_label.get()
     type = type_input_label.get()
     capacités = capacités_input_label.get()
     image_combattant = "img/"+nom+".png"
     persos.append(DB(nom, type, capacités, image_combattant ))
     listbox.insert(tk.END, nom)
     nom_input_label.delete(0, tk.END)
     type_input_label.delete(0, tk.END)
     capacités_input_label.delete(0, tk.END)

     messagebox.showinfo("Ajout réussi", "Combattant ajouté")

def supprimer_combattant():
     indexDuPerso = int(listbox.curselection()[0])
     persos.pop(indexDuPerso)
     listbox.delete(indexDuPerso)

     messagebox.showinfo("Suppression réussi", "Combattant supprimé")

top_frame = tk.Frame(fenetre, bg="DarkOrange2", bd=10, width=1000, height=800).pack()

 #création d'un logo sur fenetre tkinter
logo = Image.open("img/Dragon-Ball-Logo.png")
logo = logo.resize((200, 200))
logo = ImageTk.PhotoImage(logo)
label = tk.Label(fenetre, image=logo, bg="DarkOrange2")
label.place(x=10, y=10)

#création d'un logo sur fenetre tkinter
logo2 = Image.open("img/nuage.png")
logo2 = logo2.resize((150, 100))
logo2 = ImageTk.PhotoImage(logo2)
label = tk.Label(fenetre, image=logo2, bg="DarkOrange2")
label.place(x=750, y=0)

#création d'un logo sur fenetre tkinter
logo3 = Image.open("img/nuage.png")
logo3 = logo3.resize((150, 100))
logo3 = ImageTk.PhotoImage(logo3)
label = tk.Label(fenetre, image=logo3, bg="DarkOrange2")
label.place(x=500, y=0)

#création d'un logo sur fenetre tkinter
logo4 = Image.open("img/nuage.png")
logo4 = logo4.resize((150, 100))
logo4 = ImageTk.PhotoImage(logo4)
label = tk.Label(fenetre, image=logo4, bg="DarkOrange2")
label.place(x=250, y=0)

image = Image.open("img/central.png")
image = image.resize((300, 400))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(fenetre, image=image, bg="DarkOrange2")

nom_label = tk.Label(fenetre, text=" ", bg="DarkOrange2", font="font")
type_label = tk.Label(fenetre, text=" ", bg="DarkOrange2",font="font")
capacités_label = tk.Label(fenetre, text=" ", bg="DarkOrange2", font="font")
nom_label.place(x=50, y=550)
type_label.place(x=50, y=590)
capacités_label.place(x=50, y=630)
image_label.place(x=300, y=250)

 #creation d'une liste déroulante
listbox = tk.Listbox(fenetre, width="20", height="10", bg="DarkOrange2", font="font", bd=5, relief="ridge", highlightcolor="yellow")
listbox.place(x=740, y=100)

 #ajout de pokemon à la liste déroulante
listbox.insert(tk.END, "Sangoku")
listbox.insert(tk.END, "Sangohan")
listbox.insert(tk.END, "Krilin")
listbox.insert(tk.END, "Piccolo")

 #enlever le hover sur la liste déroulante
listbox.bind("<Enter>", lambda e: listbox.config(bg="yellow"))
listbox.bind("<Leave>", lambda e: listbox.config(bg="DarkOrange2"))

 #création d'un bouton por récupurer la valeur saisie
button = tk.Button(fenetre, text="Afficher les détails", command=affiche_detail, bg="yellow", font="font")
button.place(x=770, y=367)

 #création d'un bouton "ajout de personnage"
button = tk.Button(fenetre, text="Ajouter un combattant", command=ajouter_combattant, bg="yellow", font="font")
button.place(x=750, y=650)

 #creation des champs de saisie "Nouveau combattant"
nouveau_combattant = tk.Frame(fenetre, bg="DarkOrange2")
nouveau_combattant.place(x=730, y=440)

 #création d'un bouton "Supprimer le combattant"
button = tk.Button(fenetre, text="Supprimer le combattant", command=supprimer_combattant, bg="yellow", font="font")
button.place(x=739, y=700)

nom_input_label = tk.Label(nouveau_combattant, text="Nom du combattant", bg="DarkOrange2", font="font")
nom_input_label.grid(row=0, column=0, padx=10, pady=1)
nom_input_label = tk.Entry(nouveau_combattant, width=30)
nom_input_label.grid(row=1, column=0, padx=10, pady=1)

type_input_label = tk.Label(nouveau_combattant, text="Type du combattant", bg="DarkOrange2", font="font")
type_input_label.grid(row=2, column=0, padx=10, pady=1)
type_input_label = tk.Entry(nouveau_combattant, width=30)
type_input_label.grid(row=3, column=0, padx=10, pady=1)

capacités_input_label = tk.Label(nouveau_combattant, text="Capacités du combattant", bg="DarkOrange2", font="font")
capacités_input_label.grid(row=4, column=0, padx=10, pady=1)
capacités_input_label = tk.Entry(nouveau_combattant, width=30)
capacités_input_label.grid(row=5, column=0, padx=10, pady=1)










fenetre.mainloop()