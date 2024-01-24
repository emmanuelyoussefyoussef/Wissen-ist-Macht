import tkinter as tk
import random
import time

Score = 0 
antworten=['a','b','c','d']
#Score update funktion
def update_score(key):
    global Score
    if key == 'A':
        Score = int(random.random()*100)
        score.config(text='Score: ' + str(Score))
    #window.after(1000,update_score)



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
question = tk.Label(window,text='placeholder for the question',font=('Arial',20),bg="beige")
question.grid(row=1,column=0,columnspan=4)

#---------------------------------------------------------------------------------------------

#Tasten
Buttona= tk.Button(window,text='Antowrt A',font=('Arial',14),width=25,height=1,command=lambda:update_score('A'))
Buttona.grid(row=2,column=0)

Buttonb= tk.Button(window,text='Antowrt B',font=('Arial',14),width=25,height=1,command=lambda:update_score('B'))
Buttonb.grid(row=2,column=3)

Buttonc= tk.Button(window,text='Antowrt C',font=('Arial',14),width=25,height=1,command=lambda:update_score('C'))
Buttonc.grid(row=3,column=0)

Buttond= tk.Button(window,text='Antowrt D',font=('Arial',14),width=25,height=1,command=lambda:update_score('D'))
Buttond.grid(row=3,column=3)



#diese funktion ruft jede sekunde die update_score funktion auf
#window.after(1000,update_score)

window.mainloop()








