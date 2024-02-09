import tkinter as tk
import random
from questions_folder.questions import *
from PIL import Image, ImageTk
import keyboard
from img import *

#Variabeln

richtige_antwort=''
index=0
switcher=True
player_name_var = ""  # Die Variable für den Spielername initialisieren
player_name_label=''
#diese variabel speichert 10 importierte fragen 
key,imported_questions=get_random_questions()
#Variabeln
shown_questions=''
correct_questions=''
answer=''
possible_answer=''
#timer_running=False
Score = 10
total_score = 0
saved_scores=[]

#Funktion Timer und ablaufender Score
def hoch_timer(seconds):
    global Score
    #global timer_running
    timer.config(text=f'Timer: {seconds} s')
    
    if seconds >= 12:
      if (seconds - 12) % 2 == 0:
        Score = max(1, Score -1)
        score.config(text='Score ' + str(Score))
    #if timer_running:
    window.after(1000, hoch_timer, seconds +1)


#Diese Funktionen verteilt die Antworten auf den Buttons
def auswahl():
    global possible_answer
    possible_answer=imported_questions[key[index]]['possible_answers']#Die variable possible_answer erhält asu der dict die 4 antwortmöglichkeiten
    Buttona.config(text=possible_answer[0])#Aus der possible_answer liste das erste Element
    Buttonb.config(text=possible_answer[1])#Aus der possible_answer liste das zweite Element
    Buttonc.config(text=possible_answer[2])#Aus der possible_answer liste das dritte Element
    Buttond.config(text=possible_answer[3])#Aus der possible_answer liste das vierte Element
#Diese funktion sorgt dafür dass neue fragen ausgewählt werden
def neue_frage():
    global imported_questions
    global correct_questions
    global answer
    if index <= 9:
        shown_questions=imported_questions[key[index]]['question'] #aus der imported_questions dict wird ein element ausgesucht und eingespeichert
        print(index,key[index],shown_questions)#Dient zur kontrolle
        question.config(text=shown_questions)#Das bearbeitet den Text und aktualisiert die anzeige
        auswahl()
    
#Diese FRage wird ein mal aufgerufen um die erste frage zu bekommen am anfang dann ist die Funktion nutzlos
def erste_frage():
    global switcher
    global possible_answer
    if switcher ==True:#If funktion damit die Funktion erste_frage() nicht ständig läuft sondern einmalig
        neue_frage()
        switcher=False#Setzt switcher auf false damit die If funktion nicht mehr erfüllbar wird
#Score update funktion
def update_score():
    global Score
    Score = 10
    score.config(text='Score: ' + str(Score))#Hier wird die Score Anzeige aktualisiert und erneut angezeigt

#Diese Funktion zeigt das Ergebnis Richtig an
def richtige_antwort():
    global Score
    global total_score
    window.bell()#Sorgt für ein ton
    update_score()
    total_score += Score
    saved_scores.append(Score)
    question.config(text="Richtig")#Ändert die Frage und falls die antwort richtig war dann wird Richtig angezeigt
    window.after(1000,neue_frage)#Nach 1Sekunde wird die neue_frage() funktion aufgerufen
    if index ==9:#Die If funktion prüft ob die zehnte frage angezeigt wurde und stoppt dann die eingabe
        window.after(2000, ende)#Am ende wird Richtig oder falsch angezeigt und erst nach 2 sekunden wird das Ergebnis angezeigt


#diese funktion prüft ab ob die eingabe des spielers richtig ist    
def scanner(antwort):
    global index
    if index<=9:#Solange wir nicht die 10te frage errreicht haben wird die kontrolle fortlaufen
        if antwort==imported_questions[key[index]]['question_answer']:#prüft ob die ausgewählte antwort die richtige ist
            richtige_antwort()
        else:falsche_antwort()
    else:
        ende()
    index = index +1#erhöht die index variable um 1 nach dem beantworten einer Frage
#Diese Funktion zeigt das Ergebnis Falsch an
def falsche_antwort():
    global index
    global Score
    window.bell()
    update_score()
    Score = 10
    question.config(text="Falsch")#Aktualisiert die Anzeigt und zeigt falsch an
    window.after(1000,neue_frage)#nach 1 Sekunde wird die neue_frage() funktion aufgerufen
    if index ==9:#Die If funktion prüft ob die zehnte frage angezeigt wurde und stoppt dann die eingabe
        window.after(2000,ende)#Am ende wird Richtig oder falsch angezeigt und erst nach 2 sekunden wird das Ergebnis angezeigt 

#Diese Funktion zeigt am ende der Score an
def ende():
    global saved_scores
    global total_score
    global Score
    spiel_bild = Image.open("img/score.jpg")
    spiel_bild = spiel_bild.resize((1280, 720))
    hintergrund_bild_spiel = ImageTk.PhotoImage(spiel_bild)
    hintergrund_placeholder.configure(image=hintergrund_bild_spiel)
    hintergrund_placeholder.image = hintergrund_bild_spiel
    
    Buttona.lower()
    Buttonb.lower()
    Buttonc.lower()
    Buttond.lower()

    if total_score==0:
        saved_scores=[]
    else:
        saved_scores.append(total_score)
    endergebnis=sum(saved_scores) #Score wird in eine unabhängige variabel gespeichert
    question.config(text='Dein Score beträgt:'+str(endergebnis))#Der Score wird angezeigt

def center(win):
    win.update_idletasks() #Anhand von der Bildschirmgröße wird der Seitenabstand berechnet (link,rechts,oben,unten) XXX
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

# Funktionen an Ereignisse binden
window.bind("<Map>", hide_titlebar)
window.bind("<Configure>", hide_titlebar)

# Background
spiel_bild= Image.open("img/start.PNG")
spiel_bild= spiel_bild.resize((1280, 720))
hintergrund_bild_spiel= ImageTk.PhotoImage(spiel_bild)
hintergrund_placeholder = tk.Label(window, image=hintergrund_bild_spiel)
hintergrund_placeholder.place(x=0, y=10, relwidth=1, relheight=1)
hintergrund_placeholder.lift()
timer = tk.Label(window,text='Timer: ',font=('Arial',15),fg='white',bg='black')

# Score placeholder
score = tk.Label(window,text='Score: '+str(Score),font=('Arial',15),fg='white',bg='black')
question = tk.Label(window,text=shown_questions,font=('Arial',20),fg='white',bg='black')

# Abstände
abstandzw_name_frage= tk.Label(window,text='',width=40,height=5)
abstandzw_name_frage.grid(row=2,column=0,columnspan=2)
abstandzw_name_frage.lower(belowThis=hintergrund_placeholder)
abstandzw_frage_antwort= tk.Label(window,text='',width=40,height=15)
abstandzw_frage_antwort.grid(row=3,column=0,columnspan=2)
abstandzw_frage_antwort.lower(belowThis=hintergrund_placeholder)
abstandmitte= tk.Label(window,text='',width=20,height=5)
abstandmitte.grid(row=4,column=2)
abstandmitte.lower(belowThis=hintergrund_placeholder)
abstand_score_rand=tk.Label(window,text='',width=10,height=5)
abstand_score_rand.grid(row=0,column=5)
abstand_score_rand.lower(belowThis=hintergrund_placeholder)
abstandzw_regeln_spielername=tk.Label(window,text='',width=15,height=6)
abstandzw_regeln_spielername.grid(row=7,column=4)
abstandzw_regeln_spielername.lower()

# Antwort Blöcke
Buttona= tk.Button(window,font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[0]))
Buttonb= tk.Button(window,font=('Arial',14),fg='black',bg='darkred',width=40,height=5,command=lambda:scanner(possible_answer[1]))
Buttonc= tk.Button(window,font=('Arial',14),fg='black',bg='darkred',width=40,height=5,command=lambda:scanner(possible_answer[2]))
Buttond= tk.Button(window,font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[3]))

def f(name =""):
    print("Übergeberner Name " + name)
    def start_game():
        global player_name_entry, player_name_label, player, player_name_var
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
        #das hintergrundsbild wird aktualisiert
        spiel_bild = Image.open("img/background.jpg")
        spiel_bild = spiel_bild.resize((1280, 720))
        hintergrund_bild_spiel = ImageTk.PhotoImage(spiel_bild)
        hintergrund_placeholder.configure(image=hintergrund_bild_spiel)
        hintergrund_placeholder.image = hintergrund_bild_spiel
        erste_frage()
        hoch_timer(0)

    player_name_entry = tk.Label(window, text=name, font=('Arial', 15),fg='white',bg='black')
    player_name_entry.grid(row=8, column=0, columnspan=12, padx=0, pady=30)
    player_name_entry.lift(aboveThis=hintergrund_placeholder)
    start_button = tk.Button(window, text='Start Game', font=('Arial', 15),fg='white',bg='black', command=start_game)
    start_button.grid(row=9, column=0,columnspan=12, padx=0, pady=0)

    # Schwarzen Balken erstellen XXX
    black_bar = tk.Label(window, text="Wissen ist Macht", bg="black", fg="white", width=184, height=1)
    black_bar.grid(row=0, column=0, columnspan=6, padx=0, pady=0, sticky='n')

    # Close-Button erstellen und in den Vordergrund bringen
    close_button = tk.Button(window, text="X", bg="red", fg="white", command=window.destroy, width=2, height=1,  borderwidth=0, highlightthickness=0)
    close_button.place(relx=1, rely=0, anchor='ne')

    center(window)
    window.mainloop()

if __name__ == "__main__":#wenn über ID gestartet wird
    def start_game():
        global player_name_entry, player_name_label, player
        player = player_name_entry.get()
        if player:
            global player_name_var
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

    player_name_entry = tk.Entry(window, text="player", font=('Arial', 15),fg='white',bg='black')
    player_name_entry.grid(row=8, column=0,columnspan=12, padx=0, pady=30)
    player_name_entry.lift(aboveThis=hintergrund_placeholder)
    start_button = tk.Button(window, text='Start Game', font=('Arial', 15),fg='white',bg='black', command=start_game)
    start_button.grid(row=9, column=0, columnspan=12, padx=0, pady=0)

    # Schwarzen Balken erstellen
    black_bar = tk.Label(window, text="Wissen ist Macht", bg="black", fg="white", width=184, height=1)
    black_bar.grid(row=0, column=0, columnspan=6, padx=0, pady=0, sticky='n')

    # Close-Button erstellen und in den Vordergrund bringen
    close_button = tk.Button(window, text="X", bg="red", fg="white", command=window.destroy, width=2, height=1,  borderwidth=0, highlightthickness=0)
    close_button.place(relx=1, rely=0, anchor='ne')

    center(window)
    window.mainloop()
