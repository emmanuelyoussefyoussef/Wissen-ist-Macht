import tkinter as tk
import random
import time
from questions_folder.questions import *
import os
#Variabeln
Score = 0 
richtige_antwort=''
#frage=questions_dict[random_num()]

def random_num():
    num=random.random()*99 +1
    return int(num)

frage=questions_dict[random_num()]['question']

def neue_frage():
    #global frage
    frage=questions_dict[random_num()]['question']
    question.config(text=frage)

#Score update funktion
def update_score(key):
    #global Score
    if key == 'A':
        Score = int(random.random()*100)
        score.config(text='Score: ' + str(Score))
    #window.after(1000,update_score)


#Diese Funktion zeigt das Ergebnis Richtig an
def antwort():
    question.config(text="Richtig")
    window.after(1000,neue_frage)

#diese funktion prüft ab ob die eingabe des spielers richtig ist    
def scanner(key):
    if key==richtige_antwort:
        antwort()
    else:falsche_antwort()

#Diese Funktion zeigt das Ergebnis Falsch an
def falsche_antwort():
    #global frage
    question.config(text="Falsch HAHAHAHAHA")
    Score = 0
    score.config(text='Score: ' + str(Score))
    window.after(1000,neue_frage)

#Diese Funktion zeigt wieder die Nächste frage an
def reset_frage():
    #global frage
    frage="placeholder for the question"
    question.config(text=frage)
    window.after(1500,reset_frage)

#Spielername wird damit abgefragt
current_player=input('Player name:')


#Grafik einstellungen
window = tk.Tk()

window.title('Wissen ist Macht')
window.geometry('1280x720')
#---------------------------------------------------------------------------------------------
#Spieler code
player_name = tk.Label(window,text='Player:'+' '+current_player,font=('Arial',15))
player_name.grid(row=0,column=0,sticky='NW')

#Score code
score = tk.Label(window,text='Score:'+str(Score),font=('Arial',15))
score.grid(row=0,column=4,sticky='NE')

#Fragen_funktion
question = tk.Label(window,text=frage,font=('Arial',20),bg="beige")
question.grid(row=2,column=0,columnspan=5)

#---------------------------------------------------------------------------------------------

#Abstände
abstandzw_name_frage= tk.Label(window,text='',width=40,height=5)
abstandzw_name_frage.grid(row=1,column=0,columnspan=2)

abstandzw_frage_antwort= tk.Label(window,text='',width=40,height=15)
abstandzw_frage_antwort.grid(row=3,column=0,columnspan=2)

abstandmitte= tk.Label(window,text='',width=40,height=5)
abstandmitte.grid(row=4,column=2)

#Antwort Blöcke
Buttona= tk.Button(window,text='A: ich bin die richtige Antwort vertraue mir',font=('Arial',14),bg='#ff6666',width=40,height=5,command=lambda:(update_score('A'),antwort()))
Buttona.grid(row=4,column=0,padx=30)

Buttonb= tk.Button(window,text='B: ich bin leider falsch',font=('Arial',14),bg='#458B74',width=40,height=5,command=lambda:(update_score('B'),falsche_antwort()))
Buttonb.grid(row=4,column=4)

Buttonc= tk.Button(window,text='C: ich bin auch leider falsch',font=('Arial',14),bg='skyblue',width=40,height=5,command=lambda:(update_score('C'),falsche_antwort()))
Buttonc.grid(row=5,column=0)

Buttond= tk.Button(window,text='D: versuch mich nicht',font=('Arial',14),bg='#a37d00',width=40,height=5,command=lambda:(update_score('D'),falsche_antwort()))
Buttond.grid(row=5,column=4)



#diese funktion ruft jede sekunde die update_score funktion auf
#window.after(1500,reset_frage)

window.mainloop()








