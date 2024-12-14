import tkinter as tk

def draw_rectangle(canvas,rectangle,colour):
    x1,x2,y1,y2=rectangle
    canvas.create_rectangle(x1,y1,x2,y2,fill=colour,width=2,outline='black')

def point(canvas,point,colour):
    x,y=point
    canvas.create_oval(x-5,y-5,x+5,y+5,fill=colour,width=2,outline='black')

def circle(canvas,radius,colour):
    x,y,radius=radius
    canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill=colour,width=2,outline='black')


root=tk.Tk()
root.title("rectangle")
canvas=tk.Canvas(root,width=500,height=500,bg='white')
canvas.pack()


draw_rectangle(canvas,rectangle=(100,200,300,400),colour='red')
point(canvas,point=(100,100),colour='blue')
circle(canvas,radius=(100,100,50),colour='green')



root.mainloop()