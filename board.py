from tkinter import *
from piece import piece
window = Tk()
labels=[0]*240
for r in range(24):
    for c in range(10):
        labels[r*10+c]=Label(window, bg='black', height=1, width=2)
        labels[r *10+c].grid(row=r,column=c, sticky=S+N+E+W)

firstSquare=piece(window, labels, 0, 10,5)
window.mainloop()

