import tkinter as tk
import random
#from testing import hoch_timer
from questions_folder.questions import *
#from timer_highscore import ScoreTimer, start_quiz
from PIL import Image, ImageTk
import keyboard

#Variabeln
Score = 10
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

#Funktion Timer und ablaufender Score
def hoch_timer(seconds):
    global Score
    timer.config(text=f'Timer: {seconds} s')
    
    if seconds >= 12:
      if (seconds - 12) % 2 == 0:
        Score = max(1, Score -1)
        score.config(text='Score ' + str(Score))
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
    window.bell()#Sorgt für ein ton
    update_score()
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
    window.bell()
    update_score()
    falsche_antworten=["Nein","Falsch","versuchs das nächste mal"]#liste mit verschiedene variationen von antworten
    rand_ant=falsche_antworten[random.randrange(0,3)]#wählt ein element von der falsche_antworten Liste aus
    question.config(text=str(rand_ant))#Aktualisiert die Anzeigt und zeigt falsch an
    window.after(1000,neue_frage)#nach 1 Sekunde wird die neue_frage() funktion aufgerufen
    if index ==9:#Die If funktion prüft ob die zehnte frage angezeigt wurde und stoppt dann die eingabe
        window.after(2000,ende)#Am ende wird Richtig oder falsch angezeigt und erst nach 2 sekunden wird das Ergebnis angezeigt 

#Diese Funktion zeigt am ende der Score an
def ende():
    endergebnis=Score #Score wird in eine unabhängige variabel gespeichert
    question.config(text='Dein Score beträgt:'+str(endergebnis))#Der Score wird angezeigt
    
def start_game():
    global player_name_entry, player_name_label
    player = player_name_entry.get()
    if player:
        global player_name_var
        player_name_var = player
        player_name_label = tk.Label(window, text=player, font=('Arial', 18),fg='white',bg='black')
        player_name_label.grid(row=0, column=2, sticky='NW')
        player_name_entry.grid_forget()
        start_button.grid_forget()
        Buttona.grid(row=3,column=0,padx=80,pady=20)
        Buttonb.grid(row=3,column=4)
        Buttonc.grid(row=4,column=0)
        Buttond.grid(row=4,column=4)
        score.grid(row=0,column=4,sticky='NE')
        question.grid(row=2,column=0,columnspan=6)
        timer.grid(row=0,column=0,sticky='NW')
        erste_frage()

        hoch_timer(0)
#Spielername abfrage

#Grafik einstellungen
window = tk.Tk()
window.title('Wissen ist Macht')
window.geometry('1280x720')
#---------------------------------------------------------------------------------------------
#Das Hintergrundabild importiert und hinzugefügt
importiertes_bild= Image.open("Wissen-ist-Macht/img/background.jpg")
importiertes_bild= importiertes_bild.resize((1280, 720))

hintergrund_bild= ImageTk.PhotoImage(importiertes_bild)

hintergrund_placeholder = tk.Label(window, image=hintergrund_bild)
hintergrund_placeholder.place(x=0, y=0, relwidth=1, relheight=1)
hintergrund_placeholder.lift()

#timer placeholder
timer = tk.Label(window,text='Timer: ',font=('Arial',15),fg='white',bg='black')
#timer.grid(row=0,column=0,sticky='NW')


#Score placeholder
score = tk.Label(window,text='Score: '+str(Score),font=('Arial',15),fg='white',bg='black')
#score.grid(row=0,column=4)
#Fragen placeholder
question = tk.Label(window,text=shown_questions,font=('Arial',20),fg='white',bg='black')
#question.lift(aboveThis=hintergrund_placeholder)
#question.grid(row=2,column=0,columnspan=5)
#---------------------------------------------------------------------------------------------
#Abstände
abstandzw_name_frage= tk.Label(window,text='',width=40,height=5)
abstandzw_name_frage.grid(row=1,column=0,columnspan=2)
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
#Antwort Blöcke

Buttona= tk.Button(window,text='A: ich bin die richtige Antwort vertraue mir',font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[0]))

Buttonb= tk.Button(window,text='B: ich bin leider falsch',font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[1]))

Buttonc= tk.Button(window,text='C: ich bin auch leider falsch',font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[2]))

Buttond= tk.Button(window,text='D: versuch mich nicht',font=('Arial',14),fg='white',bg='black',width=40,height=5,command=lambda:scanner(possible_answer[3]))





player_name_entry = tk.Entry(window, text='Player:', font=('Arial', 15),fg='white',bg='black')
player_name_entry.grid(row=5, column=5)
player_name_entry.lift(aboveThis=hintergrund_placeholder)

start_button = tk.Button(window, text='Start Game', font=('Arial', 15),fg='white',bg='black', command=start_game)
start_button.grid(row=5, column=4)




window.mainloop()



#Frage 80,75,40
