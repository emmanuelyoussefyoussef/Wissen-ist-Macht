import tkinter as tk
import time as tm

Score = 0

current_player=input('Player name:')
window = tk.Tk()
window.geometry('600x400')
window.title('Wissen ist Macht')
player_name = tk.Label(window,text='Player:'+' '+current_player,font=('Arial',15))
player_name.place(anchor="nw")

score = tk.Label(window,text='Score:'+str(Score),font=('Arial',15))
score.pack(anchor="ne")

question = tk.Label(window,text='placeholder for the question',font=('Arial',30))
question.pack(anchor='center',pady=50)


















window.mainloop()
