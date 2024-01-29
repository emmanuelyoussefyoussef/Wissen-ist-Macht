import tkinter as tk
from PIL import Image, ImageTk

def zeige_bild():
    fenster = tk.Tk() #erstellt tk Fenster
    bild = Image.open("questions_folder\img\history.jpg") # öffnet das Bild
    bild_tk = ImageTk.PhotoImage(bild) # konvertiert das Bild

    bild_label = tk.Label(fenster, image=bild_tk) # erstellt ein Label um das Bild anzuzeigen
    bild_label.pack() # lädt das Bild in ein tk-Fenster hoch

    bild_label.image = bild_tk # Refernz auf den Speicherort des Bildes (speichert das Bild)

    fenster.mainloop() # zeigt das tk Fenster an

zeige_bild()