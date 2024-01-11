from tkinter import * #type:ignore
from tkinter import messagebox

root=Tk()
root.title("Welcome to Tic Tac Toe!")

namebox = Text(root,height=5,width=5)
namebox.grid()
namebox2 = Text(root,height=5,width=5)
namebox2.grid()

def clicking():
    global txtvalu, txtvalu2
    txtvalu = namebox.get(1.0,END)
    txtvalu2 = namebox2.get(1.0,END)
    Label(root, text = namebox)

submit=Button(root,text="submit", command = clicking )
submit.grid()
#root.geometry("1200x710")

#X starts first so true
clicked=True
count=0

#disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def conditionX(B,C,D,E):
    if E=='X':
        if B["text"]=="X"and C["text"]=="X" and D["text"]=="X":
            B.config(bg="green")
            C.config(bg="green")
            D.config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!!! X wins")
            disable_all_buttons()
    elif E=='O':
        if B["text"]=="O"and C["text"]=="O" and D["text"]=="O":
            B.config(bg="green")
            C.config(bg="green")
            D.config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!!! O wins")
            disable_all_buttons()

#check to see if someone won

d=['X','O']
def checkifwon():
    global winner
    winner=False

    for i in d:
        conditionX(b1,b2,b3,i)
        conditionX(b4,b5,b6,i)
        conditionX(b7,b8,b9,i)
        conditionX(b1,b4,b7,i)
        conditionX(b2,b5,b8,i)
        conditionX(b3,b6,b9,i)
        conditionX(b1,b5,b9,i)
        conditionX(b3,b5,b7,i)
       


#Check if tie
    if count==9 and winner ==False:
        messagebox.showinfo("Tic Tac Toe","It's a Tie!\n No one Wins")
        disable_all_buttons()

#Button clicked function
def b_click(b):
    global clicked,count
    if b ["text"]==" "and clicked ==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkifwon()
    elif b ["text"]==" "and clicked ==False:
        b["text"]="O"
        clicked=True
        count+=1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe","The box has already been selected\npick another box")

#Start the game over
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0

#build buttons
    b1=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b1))
    b2=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b2))
    b3=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b3))

    b4=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b4))
    b5=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b5))
    b6=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b6))

    b7=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b7))
    b8=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b8))
    b9=Button(root, text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b9))

    #grid buttons to screen
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create options
option_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="option",menu=option_menu)
option_menu.add_command(label="Reset Game",command=reset)


reset()
root.mainloop()