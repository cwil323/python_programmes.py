"""
Draws a pattern of red circles and black crosses with a white background.
Date-written: May, 2016.
Author: Charlotte Wilson
"""

from tkinter import *

def main():
    window = Tk()  
    window.title("Red and White Pattern")  
    window.config(background = 'white')   
    window.geometry("500x350+10+20") 
    a_canvas = Canvas(window) 
    a_canvas.config(background = "white")   
    a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas) 
    window.mainloop()

def draw_grid(a_canvas):
    for row in range(50, 350, 50):
        a_canvas.create_line(-1, row, 501, row, fill = "lightblue")
    for column in range(50, 500, 50):
        a_canvas.create_line(column, -1, column, 351, fill = "lightblue")

def draw_pattern_in_canvas(a_canvas):
    size = 50
    y = 0
    for row in range(7):
        fill_in = row % 2 == 0
        x = 0
        for column in range(10):
            if fill_in:
                a_canvas.create_oval(x,y,x + size,y + size,fill = "red", outline = "black", width = 3)
            else:
                a_canvas.create_line(x,y,x + size,y + size,width = 3)
                a_canvas.create_line(x + size,y,x,y + size,width = 3)
                a_canvas.create_rectangle(x,y,x + size,y + size,width = 3)
            x += size
            fill_in = not fill_in
        y += size
main()
    

    
            
    
		
    
    
