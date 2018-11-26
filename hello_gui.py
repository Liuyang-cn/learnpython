#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import tkinter
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets():
        self.helloLabel = Lable(self,text='Hello,world!')
        self.hellobale.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()
        

app=Application()
app.master.title('Hello World')
app.manloop()