from tkinter import *
from PIL import Image, ImageTk
from string import ascii_uppercase
import random
from tkinter import messagebox


root=Tk()
root.geometry("1050x550")
root.title('Hangman')
bg=ImageTk.PhotoImage(Image.open('BG.png'))
a=Label(root,image=bg)
a.place(x=0,y=0)

l=['apple','banana','orange','watermelon','cherry','strawberry','bottle','ball']
s='.png'


score=0
word='a'


def update():
    global word
    num=random.randint(1,7)
    word=l[num]+s
    img = PhotoImage(file=word) 
    imcon=canvas.create_image(20,20, anchor=NW, image=img)
    canvas.itemconfig(imcon,image=word)
    return word
 

canvas = Canvas(root, width = 140, height = 140)      
canvas.place(x=820,y=90)


namevalue= StringVar()
ent_name = Entry(root, width=70, borderwidth=10, textvariable=namevalue)
ent_name.place(x=150, y=150)


def check():
    global score
    value=ent_name.get()
    a=word.rstrip('.png')
    from PIL import Image, ImageTk
    from string import ascii_uppercase
    import random
    from tkinter import messagebox

    root = Tk()
    root.title(' RESULT ')
    root.geometry('250x100')
    root.resizable(0, 0)
    root.configure(bg='grey')

    
    if value==a:
        lab = Label(root, text='YOU\n WON\n :)', bg='black', fg='white', width=25, font=('Arial', 13))
        lab.place(x=10,y=15)
        score+=1
    else:
        lab = Label(root, text='YOU\n LOSE\n :(', bg='black', fg='white', width=25, font=('Arial', 13))
        lab.place(x=10,y=15)



    root.mainloop()


def clear():
    namevalue.set('')

def win():
    global score
    a='Your Score: '+str(score)
    labe = Label(root, text=a, bg='black', fg='white', width=25, font=('Arial', 13))
    labe.place(x=10,y=15)



button = Button(root, text='CHECK',command=check,font=("impact", 20), bg='orange', fg='white', bd=0)
button.place(x=750, y=440)

button1 = Button(root, text='VIEW SCORE',command=win, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
button1.place(x=850, y=440)

button2 = Button(root, text='CLEAR ENTRY',command=clear, font=("impact", 15), bg='red', fg='white', bd=0)
button2.place(x=300, y=200)


button3 = Button(root, text='CHANGE IMAGE',command=update, font=("impact", 15), bg='GREEN', fg='white', bd=0)
button3.place(x=830, y=240)



root.mainloop()
