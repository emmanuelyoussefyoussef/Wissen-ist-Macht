import tkinter as tk
import random
import time
from questions_folder.questions import *
import os
#Variabeln
Score = 0 
richtige_antwort=''
index=0
boole=True




#imported_questions=questions_dict[random_num()]
def random_num():
    num=random.random()*99 +1
    return int(num)





#diese variabel speichert 10 importierte fragen 
key,imported_questions=get_random_questions()

#dies ist die Liste mit den 10 fragen die angezeigt werden sollen
shown_questions=''
correct_questions=''
answer=''
possible_answer=''

def auswahl():
    global possible_answer
    possible_answer=imported_questions[key[index]]['possible_answers']
    Buttona.config(text=possible_answer[0])
    Buttonb.config(text=possible_answer[1])
    Buttonc.config(text=possible_answer[2])
    Buttond.config(text=possible_answer[3])



def neue_frage():
    global imported_questions
    global correct_questions
    global answer
    shown_questions=imported_questions[key[index]]['question']
    print(index,key[index],shown_questions)
    question.config(text=shown_questions)
    auswahl()
    



def erste_frage():
    global boole
    global possible_answer
    if boole ==True:
        neue_frage()
        boole=False
        possible_answer=imported_questions[key[index]]['possible_answers']


#Score update funktion
def update_score(key):
    global Score
    if key == 'A':
        Score = Score+1
        score.config(text='Score: ' + str(Score))



#Diese Funktion zeigt das Ergebnis Richtig an
def richtige_antwort():
    window.bell()
    update_score('A')
    question.config(text="Richtig")
    window.after(1000,neue_frage)
    if index ==9:
        window.after(2000, ende)#Am ende wird Richtig oder falsch angezeigt und erst nach 2 sekunden wird das Ergebnis angezeigt




#diese funktion prüft ab ob die eingabe des spielers richtig ist    
def scanner(var):
    global index
    if index<=9:
        if var==imported_questions[key[index]]['question_answer']:
            richtige_antwort()
        else:falsche_antwort()
    else:
        ende()
    index = index +1




#Diese Funktion zeigt das Ergebnis Falsch an
def falsche_antwort():
    global index
    window.bell()
    question.config(text="Falsch HAHAHAHAHA")
    #score.config(text='Score: ' + str(Score))
    window.after(1000,neue_frage)
    if index ==9:
        window.after(2000,ende)




#Diese Funktion zeigt wieder die Nächste frage an
def reset_frage():
    imported_questions="placeholder for the question"
    question.config(text=imported_questions)
    window.after(1500,reset_frage)

def ende():
    endergebnis=Score
    question.config(text='Dein Score beträgt:'+str(endergebnis))
    #window.after(5000,window.destroy)
    

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
question = tk.Label(window,text=shown_questions,font=('Arial',20),bg="beige")
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
Buttona= tk.Button(window,text='A: ich bin die richtige Antwort vertraue mir',font=('Arial',14),bg='#ff6666',width=40,height=5,command=lambda:(scanner(possible_answer[0])))
Buttona.grid(row=4,column=0,padx=30)

Buttonb= tk.Button(window,text='B: ich bin leider falsch',font=('Arial',14),bg='#458B74',width=40,height=5,command=lambda:scanner(possible_answer[1]))
Buttonb.grid(row=4,column=4)

Buttonc= tk.Button(window,text='C: ich bin auch leider falsch',font=('Arial',14),bg='skyblue',width=40,height=5,command=lambda:scanner(possible_answer[2]))
Buttonc.grid(row=5,column=0)

Buttond= tk.Button(window,text='D: versuch mich nicht',font=('Arial',14),bg='#a37d00',width=40,height=5,command=lambda:scanner(possible_answer[3]))
Buttond.grid(row=5,column=4)




erste_frage()
window.mainloop()









