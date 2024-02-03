import tkinter as tk

# Funktion, um das Fenster in die Mitte des Bildschirms zu zentrieren
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

# Funktion, um die Mausposition beim Klicken auf die Titelleiste zu speichern
def start_move(event):
    global x, y
    x = event.x
    y = event.y

# Funktion, um das Fenster zu verschieben
def move_window(event):
    win_x = root.winfo_x() + (event.x - x)
    win_y = root.winfo_y() + (event.y - y)
    root.geometry(f'+{win_x}+{win_y}')

# Funktion, um die Standard-Titelleiste zu verbergen
def hide_titlebar(event):
    root.overrideredirect(True)

# Hauptfenster erstellen
root = tk.Tk()
root.overrideredirect(True)  # Die Standard-Titelleiste ausblenden
root.geometry("1280x720")  # Größe des Fensters festlegen

# Titelleiste erstellen
titlebar = tk.Frame(root, bg="black")
titlebar.pack(fill=tk.X)

# Titel des Fensters hinzufügen
title = tk.Label(titlebar, text="Wissen ist Macht", bg="black", fg="white")
title.pack(side=tk.LEFT, padx=5, pady=2)

# Schließen-Button hinzufügen
close_button = tk.Button(titlebar, text="X", bg="red", fg="white", command=root.destroy, width=2, height=1)
close_button.pack(side=tk.RIGHT, padx=5, pady=2)

# Funktionen an Ereignisse binden
titlebar.bind('<ButtonPress-1>', start_move)
titlebar.bind('<B1-Motion>', move_window)
root.bind("<Map>", hide_titlebar)
root.bind("<Configure>", hide_titlebar)

# Fenster in die Mitte des Bildschirms zentrieren und Hauptloop starten
center(root)
root.mainloop()