import tkinter as tk
from tkinter import messagebox

#Infos
def afficher_details():
    messagebox.showinfo("Informations", "Email copié dans le presse-papier!")
    root.clipboard_clear()
    root.clipboard_append("olivier.valentini@outlook.fr")
    root.update()

#Fenêtre Tkinter
root = tk.Tk()
root.title("Carte de Visite")
root.geometry("300x150")
root.configure(bg='lightgray')

#Contenu
titre = tk.Label(root, text="Olivier VALENTINI", font=("Arial", 14, "bold"), bg='lightgray')
titre.pack(pady=5)

poste = tk.Label(root, text="Développeur Python amateur", font=("Arial", 10), bg='lightgray')
poste.pack()

email = tk.Label(root, text="olivier.valentini@outlook.fr", font=("Arial", 10, "underline"), fg="blue", cursor="hand2", bg='lightgray')
email.pack(pady=5)
email.bind("<Button-1>", lambda e: afficher_details())

poste = tk.Label(root, text="07.85.16.23.20", font=("Arial", 10), bg='lightgray')
poste.pack()

#Launch
root.mainloop()
