import tkinter as tk

spielername=input('ihr name:')
window = tk.Tk()
window.geometry('600x400')
window.title('Wissen ist Macht')
label = tk.Label(window,text='Spieler:'+spielername,font=('Arial',15))
label.place(anchor="nw")






















window.mainloop()