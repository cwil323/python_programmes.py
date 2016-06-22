"""
Draws a Give Way sign and a set of traffic lights.
Date-written: May, 2016.
Author: Charlotte Wilson
"""

from tkinter import *

def main():
    window = Tk()  
    window.title("Road Signs")  
    window.config(background = 'white')   
    window.geometry("425x450+10+20") 

    a_canvas = Canvas(window) 
    a_canvas.config(background = "white")   
    a_canvas.pack(fill = BOTH, expand = True)
    draw_grid(a_canvas)
    draw_in_canvas(a_canvas) 
    window.mainloop()

def draw_grid(a_canvas):
    for row in range(50, 551, 50):
            a_canvas.create_line(-1, row, 451, row, fill = "white")
    for column in range(50, 451, 50):
            a_canvas.create_line(column, -1, column, 451, fill = "white")

def draw_in_canvas(a_canvas):
    size = 50
    a_canvas.create_rectangle(25,50,125,300,fill = "black")
    a_canvas.create_rectangle(62.5,300,87.5,437.5,fill = "grey", width = 1)
    a_canvas.create_oval(50,75,100,125,fill = "red")
    a_canvas.create_oval(50,150,100,200,fill = "orange")
    a_canvas.create_oval(50,225,100,275,fill = "green")

    a_canvas.create_rectangle(262.5,225,287.5,437.5,fill = "grey", width = 1)
    a_canvas.create_polygon(150,50,400,50,275,250,fill = "red")
    a_canvas.create_polygon(200,75,350,75,275,200,fill = "white", width = 1, outline = "black")
    a_canvas.create_text(275,100,text = "GIVE", font = ('Monaco', 22, 'bold'))
    a_canvas.create_text(275,137.5,text = "WAY", font = ('Monaco', 22, 'bold'))
      
main()
    
