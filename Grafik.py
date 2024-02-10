import tkinter as tk
from questions_folder.questions import *
from PIL import Image, ImageTk
from img import *

# Variabeln
index=0
switcher=True
player_name_var = ''
player_name_label=''
key,imported_questions=get_random_questions()
shown_questions=''
possible_answer=''
Score = 10
total_score = 0
saved_scores=[]

# timer und score 
def hoch_timer(seconds):
    global Score
    timer.config(text=f'Timer: {seconds} s')
    
    if seconds >= 12:
      if (seconds - 12) % 2 == 0:
        Score = max(1, Score -1)
        score.config(text='Score ' + str(Score))
    window.after(1000, hoch_timer, seconds +1)

# Antworten werden auf die Buttons verteilt
def auswahl():
    global possible_answer
    possible_answer=imported_questions[key[index]]['possible_answers']
    Buttona.config(text=possible_answer[0])
    Buttonb.config(text=possible_answer[1])
    Buttonc.config(text=possible_answer[2])
    Buttond.config(text=possible_answer[3])
    
# Nächste Frage wird ausgewählt
def neue_frage():
    global imported_questions
    if index <= 9:
        shown_questions=imported_questions[key[index]]['question'] # aus der imported_questions dict wird ein neues Element ausgewählt
        print(index,key[index],shown_questions) 
        question.config(text=shown_questions)
        auswahl()
    
# Erste Frage, wird einmal aufgerufen
def erste_frage():
    global switcher
    if switcher ==True: # Funktion soll nur einmal aufgerufen werden
        neue_frage()
        switcher=False # if Funktion nicht mehr erfüllt
        
#Score update funktion
def update_score():
    global Score
    Score = 10
    score.config(text='Score: ' + str(Score)) # aktuallisiert den score und zeigt ihn erneut an

# Anzeige richtiges Ergebnis
def richtige_antwort():
    global Score,total_score
    window.bell() # Ton
    update_score()
    total_score += Score
    saved_scores.append(Score)
    question.config(text="Richtig") # Anzeige "Richtig" wenn Antwort richig
    window.after(1000,neue_frage)# Aufruf nächste Frage 
    if index ==9:
        window.after(2000, ende)

# Prüft die Eigbe des Spielers  
def scanner(antwort):
    global index
    if index<=9:
        if antwort==imported_questions[key[index]]['question_answer']:# Prüft ob die Antwort richtig ist
            richtige_antwort()
        else:falsche_antwort()
    else:
        ende()
    index = index +1
    
#Wird ausgeführt, wenn ein Ergbnis falsch ist
def falsche_antwort():
    global index,Score
    window.bell()
    update_score()
    Score = 10
    question.config(text="Falsch")# Aktualisiert die Anzeigt und zeigt "Falsch"
    window.after(1000,neue_frage)
    if index ==9:
        window.after(2000,ende)

# Am Ende wird der Score angezeigt
def ende():
    global saved_scores, total_score
    spiel_bild = Image.open("img/score.jpg")
    spiel_bild = spiel_bild.resize((1280, 720))
    hintergrund_bild_spiel = ImageTk.PhotoImage(spiel_bild)
    hintergrund_placeholder.configure(image=hintergrund_bild_spiel)
    hintergrund_placeholder.image = hintergrund_bild_spiel
    
    Buttona.lower()
    Buttonb.lower()
    Buttonc.lower()
    Buttond.lower()
    score.lower()
    timer.lower()

    if total_score==0:
        saved_scores=[]
    else:
        saved_scores.append(total_score)
    endergebnis=sum(saved_scores) # Score wird in eine unabhängige variabel gespeichert
    question.config(text='Dein Score beträgt:'+str(endergebnis)) # Der Score wird angezeigt
    
# Anhand von der Bildschirmgröße wird der Seitenabstand berechnet (link,rechts,oben,unten) und das Fenster auf dem Bildschirm zentriert
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
    win_x = window.winfo_x() + (event.x - x)
    win_y = window.winfo_y() + (event.y - y)
    window.geometry(f'+{win_x}+{win_y}')

# Funktion, um die Standard-Titelleiste zu verbergen XXX
def hide_titlebar(event):
    window.overrideredirect(True)

# GUI erstellen
window = tk.Tk()
window.geometry('1280x740')

# Background
spiel_bild= Image.open("img/start.PNG")
spiel_bild= spiel_bild.resize((1280, 720))
hintergrund_bild_spiel= ImageTk.PhotoImage(spiel_bild)
hintergrund_placeholder = tk.Label(window, image=hintergrund_bild_spiel)
hintergrund_placeholder.place(x=0, y=10, relwidth=1, relheight=1)
hintergrund_placeholder.lift()

# Score,question,timer placeholder
score = tk.Label(window,text='Score: '+str(Score),font=('Arial',15),fg='white',bg='black')
question = tk.Label(window,text=shown_questions,font=('Arial',20),fg='white',bg='black')
timer = tk.Label(window,text='Timer: ',font=('Arial',15),fg='white',bg='black')

# Abstände als Labels deklariert
abstandzw_name_frage= tk.Label(window,text='',width=40,height=5)
abstandzw_frage_antwort= tk.Label(window,text='',width=40,height=15)
abstandmitte= tk.Label(window,text='',width=20,height=5)
abstand_score_rand=tk.Label(window,text='',width=10,height=5)
abstandzw_regeln_spielername=tk.Label(window,text='',width=15,height=6)
#Abstände positionen festgelegt
abstandzw_name_frage.grid(row=2,column=0,columnspan=2)
abstandzw_frage_antwort.grid(row=3,column=0,columnspan=2)
abstandmitte.grid(row=4,column=2)
abstand_score_rand.grid(row=0,column=5)
abstandzw_regeln_spielername.grid(row=7,column=4)
#Abstände hinter dem Hintergrund festgesetzt
abstandzw_name_frage.lower(belowThis=hintergrund_placeholder)
abstandzw_frage_antwort.lower(belowThis=hintergrund_placeholder)
abstandmitte.lower(belowThis=hintergrund_placeholder)
abstand_score_rand.lower(belowThis=hintergrund_placeholder)
abstandzw_regeln_spielername.lower()

# Antwort Blöcke
Buttona= tk.Button(window,font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[0]))
Buttonb= tk.Button(window,font=('Arial',14),fg='black',bg='darkred',width=40,height=5,command=lambda:scanner(possible_answer[1]))
Buttonc= tk.Button(window,font=('Arial',14),fg='black',bg='darkred',width=40,height=5,command=lambda:scanner(possible_answer[2]))
Buttond= tk.Button(window,font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[3]))

# Funktion, um das Quiz über den Discord Bot zu starten
def f(name =""):
    print("Übergeberner Name " + name)
    def start_game():
        global player_name_label, player, player_name_var
        player = name
        player_name_var = name
        player_name_label = tk.Label(window, text=player, font=('Arial', 18),fg='white',bg='black')
        player_name_label.grid(row=0, column=0, columnspan=10, padx=0, pady=30, sticky='n')
        start_button.grid_forget()
        Buttona.grid(row=3,column=0,padx=80,pady=40)
        Buttonb.grid(row=3,column=4)
        Buttonc.grid(row=4,column=0)
        Buttond.grid(row=4,column=4)
        score.grid(row=0,column=4, padx=0, pady=30, sticky='ne')
        question.grid(row=2,column=0, columnspan=6, pady=80, sticky='n')
        timer.grid(row=0,column=0, padx=70, pady=30, sticky='nw')
        spiel_bild = Image.open("img/background.jpg")
        spiel_bild = spiel_bild.resize((1280, 720))
        hintergrund_bild_spiel = ImageTk.PhotoImage(spiel_bild)
        hintergrund_placeholder.configure(image=hintergrund_bild_spiel)
        hintergrund_placeholder.image = hintergrund_bild_spiel
        erste_frage()
        hoch_timer(0)

    # player-name
    player_name_entry = tk.Label(window, text=name, font=('Arial', 15),fg='white',bg='black')
    player_name_entry.grid(row=8, column=0, columnspan=12, padx=0, pady=30)
    player_name_entry.lift(aboveThis=hintergrund_placeholder)

    # start-button
    start_button = tk.Button(window, text='Start Game', font=('Arial', 15),fg='white',bg='black', command=start_game)
    start_button.grid(row=9, column=0,columnspan=12, padx=0, pady=0)

    # black-bar
    black_bar = tk.Label(window, text="Wissen ist Macht", bg="black", fg="white", width=184, height=1)
    black_bar.grid(row=0, column=0, columnspan=6, padx=0, pady=0, sticky='n')

    # close-button
    close_button = tk.Button(window, text="X", bg="red", fg="white", command=window.destroy, width=2, height=1,  borderwidth=0, highlightthickness=0)
    close_button.place(relx=1, rely=0, anchor='ne')

    # Funktionen an Ereignisse binden
    black_bar.bind('<ButtonPress-1>', start_move)
    black_bar.bind('<B1-Motion>', move_window)
    window.bind("<Map>", hide_titlebar)
    window.bind("<Configure>", hide_titlebar)

    # Quiz ausführen
    center(window)
    window.mainloop()
    
# Funktion, um das Quiz über die IDE zu starten
if __name__ == "__main__":
    def start_game():
        global player_name_entry, player_name_label, player, player_name_var
        player = player_name_entry.get()
        if player:
            player_name_var = player
            player_name_label = tk.Label(window, text=player, font=('Arial', 18),fg='white',bg='black')
            player_name_label.grid(row=0, column=0, columnspan=6, padx=0, pady=30, sticky='n')
            player_name_entry.grid_forget()
            start_button.grid_forget()
            Buttona.grid(row=3,column=0,padx=80,pady=40)
            Buttonb.grid(row=3,column=4)
            Buttonc.grid(row=4,column=0)
            Buttond.grid(row=4,column=4)
            score.grid(row=0,column=4, padx=0, pady=30, sticky='ne')
            question.grid(row=2,column=0, columnspan=6, pady=80, sticky='n')
            timer.grid(row=0,column=0, padx=70, pady=30, sticky='nw')
            #das hintergrundsbild wird aktualisiert
            spiel_bild = Image.open("img/background.jpg")
            spiel_bild = spiel_bild.resize((1280, 720))
            hintergrund_bild_spiel = ImageTk.PhotoImage(spiel_bild)
            hintergrund_placeholder.configure(image=hintergrund_bild_spiel)
            hintergrund_placeholder.image = hintergrund_bild_spiel
            erste_frage()
            hoch_timer(0)

    # player-name
    player_name_entry = tk.Entry(window, text="player", font=('Arial', 15),fg='white',bg='black')
    player_name_entry.grid(row=8, column=0,columnspan=12, padx=0, pady=30)
    player_name_entry.lift(aboveThis=hintergrund_placeholder)

    # start-button
    start_button = tk.Button(window, text='Start Game', font=('Arial', 15),fg='white',bg='black', command=start_game)
    start_button.grid(row=9, column=0, columnspan=12, padx=0, pady=0)

    # black-bar
    black_bar = tk.Label(window, text="Wissen ist Macht", bg="black", fg="white", width=184, height=1)
    black_bar.grid(row=0, column=0, columnspan=6, padx=0, pady=0, sticky='n')

    # close-button
    close_button = tk.Button(window, text="X", bg="red", fg="white", command=window.destroy, width=2, height=1,  borderwidth=0, highlightthickness=0)
    close_button.place(relx=1, rely=0, anchor='ne')

    # Funktionen an Ereignisse binden
    black_bar.bind('<ButtonPress-1>', start_move)
    black_bar.bind('<B1-Motion>', move_window)
    window.bind("<Map>", hide_titlebar)
    window.bind("<Configure>", hide_titlebar)

    # Quiz ausführen
    center(window)
    window.mainloop()
