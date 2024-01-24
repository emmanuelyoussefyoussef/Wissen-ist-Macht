import tkinter as tk
import random
import time

Score = 0 
frage="placeholder for the question"
#Score update funktion
def update_score(key):
    global Score
    if key == 'A':
        Score = int(random.random()*100)
        score.config(text='Score: ' + str(Score))
    #window.after(1000,update_score)
def antwort():
    global frage
    frage = "Richtig"
    question.config(text=frage)

def falsche_antwort():
    global frage
    frage="Falsch HAHAHAHAHA"
    question.config(text=frage)

def reset_frage():
    global frage
    frage="placeholder for the question"
    question.config(text=frage)
    window.after(1500,reset_frage)


current_player=input('Player name:')

window = tk.Tk()

window.title('Wissen ist Macht')

#---------------------------------------------------------------------------------------------
#Spieler code
player_name = tk.Label(window,text='Player:'+' '+current_player,font=('Arial',15))
player_name.grid(row=0,column=0)

#Score code
score = tk.Label(window,text='Score:'+str(Score),font=('Arial',15))
score.grid(row=0,column=3)

#Fragen_funktion
question = tk.Label(window,text=frage,font=('Arial',20),bg="beige")
question.grid(row=1,column=0,columnspan=4)

#---------------------------------------------------------------------------------------------

#Tasten
Buttona= tk.Button(window,text='A: ich bin die richtige Antwort vertraue mir',font=('Arial',14),bg='#ff6666',width=40,height=1,command=lambda:(update_score('A'),antwort()))
Buttona.grid(row=2,column=0)

Buttonb= tk.Button(window,text='B: ich bin leider falsch',font=('Arial',14),bg='#458B74',width=40,height=1,command=lambda:(update_score('B'),falsche_antwort()))
Buttonb.grid(row=2,column=3)

Buttonc= tk.Button(window,text='C: ich bin auch leider falsch',font=('Arial',14),bg='skyblue',width=40,height=1,command=lambda:(update_score('C'),falsche_antwort()))
Buttonc.grid(row=3,column=0)

Buttond= tk.Button(window,text='D: versuch mich nicht',font=('Arial',14),bg='#a37d00',width=40,height=1,command=lambda:(update_score('D'),falsche_antwort()))
Buttond.grid(row=3,column=3)



#diese funktion ruft jede sekunde die update_score funktion auf
window.after(1500,reset_frage)

window.mainloop()








