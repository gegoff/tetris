from tkinter import *

class piece:

    def __init__(self, window, labels,num,r,c):
        self.window=window
        self.labels=labels
        self.pieceNum=num
        self.row=r
        self.col=c
        self.orientation=0
        self.color=''
        if(num==0):
            self.color='yellow'
        if (num == 1):
            self.color = 'blue'
        if (num == 2):
            self.color = 'green'
        if (num == 3):
            self.color = 'red'
        self.curr=[r*10+c, r*10+c+1, (r+1)*10+c, (r+1)*10+c+1]

    def draw(self):
        for i in range(4):
            self.labels[i].config(bg='yellow')

    def rotate(self):



