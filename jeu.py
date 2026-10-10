import tkinter as tk
windows = tk.Tk()
windows.title("zone de jeu")
canvas=tk.Canvas(windows,width=500,height=500,bg="darkblue")
canvas.pack()
cible=canvas.create_rectangle(230,230,270,270,fill="yellow")
ennemi=canvas.create_rectangle(200,45,300,100,fill="red")
def depl(vent):
    if vent.keysym=="Left":
        canvas.move(cible,-10,0)
    elif vent.keysym=="Right":
        canvas.move(cible,10,0)
    elif vent.keysym=="Up":
        canvas.move(cible,0,-10)
    elif vent.keysym=="Down":
        canvas.move(cible,0,10)
windows.bind("<Key>",depl)
def boucle():
    canvas.move(ennemi,5,0)
    cord=canvas.coords(ennemi)
    col= canvas.find_overlapping(cord[0],cord[1],cord[2],cord[3])
    if cord[2]>500:
        canvas.moveto(ennemi,0,200)
    elif len(col)>1:
        print("game over")
        windows.destroy()
        return
    windows.after(20,boucle)
boucle()        


windows.mainloop()