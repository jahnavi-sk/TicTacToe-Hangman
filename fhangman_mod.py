import random
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
from tkinter import font 
root= Tk()
root['bg']= '#490206'

root.geometry("1550x900")
score=0
myFont30 = font.Font(size=30)
myFont20 = font.Font(size =20 )
myFont10 = font.Font(size=10)
myFont15 = font.Font(size=15)

def startb():
        for widgets in root.winfo_children():
            widgets.destroy()

def delete_text():
    name_entry.delete("1.0", "end")

def game_over(): 
    scorestr= str(score)
    scorestr = username + ":" + str(score)
    import re
    with open("username.txt", "a") as myfile:

        with open('usernames.txt') as f:
            lines = f.readlines()
            for line in lines:
                ret = re.sub(username,scorestr,line)
                myfile.write(ret+'\n')
    root.destroy()
    
def on_click():
    l1.grid_forget()
    e1.grid_forget()
    e2.grid_forget()

def button_click_hard():
    global photo
    f = open("hard.txt","r")
    l = f.read()
    words = l.split()
    pos= random.randint(0,len(words))
    x= words[pos]
    Z=[*range(0,len(x))]

    missing=[]  
    for i in range(len(x)):
        missing.append(x[i])



    b=[]

    for i in range(0,len(x)):
        b.append('*')
    
    blank = len(x)//2

    for i in range(0,blank):
        z= random.choice(Z)           
        Z.remove(z)
        b[z]=missing[z]
        missing[z] = "*"

            
    


    l3 = Label(root,bg="#FAB069", text="Here is the word")
    l3['font']=myFont10
    l3.grid(row =1, column = 1, padx=625, pady=10)
    l4= Label(root,bg="#FAB069", text = missing)
    l4['font'] = myFont10
    l4.grid(row =2, column =1, padx=625, pady=10)
    l5= Label(root,bg="#FAB069", text= "Wrong guesses")
    l5['font']=myFont10
    l5.grid(row=1, column=0)
    
    def askagain():
        l2 = Label(root,bg="#FAB069",text="Would you like to play again?")
        l2['font']=myFont20
        l2.grid(row=3,column=3,sticky=N,padx=500,pady=300)
        b1 = Button(root,text="Yes",height = 3, width = 7,bg="#FB5A55", command = lambda: [next(),start()]  )
        b1['font']=myFont20
        b1.grid(row=3,column=3,sticky=SW, padx=750,pady=400)
        b2= Button(root,text="No",height = 3, width = 7,bg="#FB5A55", command = lambda:[startb(),game_over()])
        b2['font']=myFont20
        b2.grid(row=3,column=3,sticky= SE, padx=750, pady=500)

    def next():
        for widgets in root.winfo_children():
            widgets.destroy()


    def printInput():
        global lll
        global lll1
        global lll2
        global lll3
        global lll4
        global lll5
        global lll6
        global lll7
        global lll8
        global lll9
        nonlocal submit
        nonlocal count
        global photo
        nonlocal txtbox
        global txtvalu
        global score

        txtvalu = txtbox.get(1.0,"end-1c")
        if txtvalu[0] not in b:
            guess1 = Label(root,bg="#FAB069",text= txtvalu[0])
            guess1['font']=myFont10
            guess1.grid(column=0)


        
            

        if txtvalu[0] in b:
            while txtvalu[0] in b:
                index=b.index(txtvalu[0])
                missing[index] = txtvalu[0]
                b[index] = '*'
            r =Label(root,bg="#FAB069", text= missing)
            r['font']=myFont10
            r.grid(row=2,column=1, padx=625,pady=10)

            if b.count('*') == len(x):
                won = Label(root, bg="#FAB069",text="Congrats!You won!!!")
                won['font']=myFont15
                won.grid(column=1)
                score=score+1
                s1 = Label(root,bg="#FAB069", text ="Your score is:")
                s1['font']= myFont15
                s1.grid(column=1)
                s = Label(root,bg="#FAB069",text = score)
                s['font']= myFont15
                s.grid(column=1)
                b1= Button(root, text="Next", height =2, width = 10,bg="#FB5A55", command = lambda : [next(), askagain()])
                b1['font']=myFont10
                b1.grid(column=1)
                return

        else:
            
            if count==0:
                photo = ImageTk.PhotoImage(file = "1.png", size="4x4")
                lll = Label(root, image = photo)
                lll.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            
            elif count==1:
                photo = ImageTk.PhotoImage(file = "2.png", size="4x4")
                lll1= Label(root, image = photo, command = lll.grid_forget())
                lll1.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==2:
                photo = ImageTk.PhotoImage(file = "3.png", size="4x4")
                lll2= Label(root, image = photo,command = lll1.grid_forget())
                lll2.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==3:
                photo = ImageTk.PhotoImage(file = "4.png", size="4x4")
                lll3 = Label(root, image = photo,command = lll2.grid_forget())
                lll3.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==4:
                photo = ImageTk.PhotoImage(file = "5.png", size="4x4")
                lll4 = Label(root, image = photo,command = lll3.grid_forget())
                lll4.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==5:
                photo = ImageTk.PhotoImage(file = "6.png", size="4x4")
                lll5= Label(root, image = photo,command = lll4.grid_forget())
                lll5.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==6:
                photo = ImageTk.PhotoImage(file = "7.png", size="4x4")
                lll6 = Label(root, image = photo,command = lll5.grid_forget())
                lll6.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==7:
                photo = ImageTk.PhotoImage(file = "8.png", size="4x4")
                lll7= Label(root, image = photo,command = lll6.grid_forget())
                lll7.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count==8:
                photo = ImageTk.PhotoImage(file = "9.png", size="4x4")
                lll8= Label(root, image = photo,command = lll7.grid_forget())
                lll8.grid(column=1,padx=100)
                txtbox.destroy()
                submit.destroy()
            elif count ==9:
                photo = ImageTk.PhotoImage(file = "10.png", size="4x4")
                lll9= Label(root, image = photo)
                lll9.grid(column=1,padx=100,command = lll8.grid_forget())
                txtbox.destroy()
                submit.destroy()
                ans = Label(root,bg="#FAB069", text ="The correct answer was:" )
                ans['font']= myFont10
                ans.grid(column=1)
                ans1 = Label(root,bg="#FAB069", text =x )
                ans1['font']= myFont15
                ans1.grid(column=1)
                loss= Label(root,bg="#FAB069", text = "You lost ! Better luck next time!")
                loss['font']= myFont15
                loss.grid(column=1)
                s1 = Label(root,bg="#FAB069", text ="Your score is:")
                s1['font']= myFont15
                s1.grid(column=1)
                s = Label(root,bg="#FAB069",text = score)
                s['font']= myFont15
                s.grid(column=1)
                b1= Button(root, text = "next", bg="#FB5A55",command = lambda:[ next(), askagain()])
                b1['font']= myFont30
                b1.grid(column=1)
                return
            


            count+=1

        
            
        
        txtbox = Text(root,height=1,width=5)
        txtbox['font']= myFont10
        txtbox.grid(row=3,column=1,padx=625,pady=10,sticky=S)
        submit=Button(root,text="submit",bg="#FB5A55",command = printInput)
        submit['font']= myFont10
        submit.grid(row=4,column=1)
        
        
                
                
    txtbox = Text(root,height=1,width=5)
    txtbox['font']= myFont10
    txtbox.grid(sticky = S,row=3,column=1,padx=625,pady=10)
    count=0
    
    submit = Button(root,text="submit",bg="#FB5A55",command = printInput)
    submit['font'] = myFont10
    submit.grid(row=4,column=1)

def button_click_easy():
    global photo
    f = open("easy.txt","r")
    l = f.read()
    words = l.split()
    pos= random.randint(0,len(words))
    x= words[pos]
    Z=[*range(0,len(x))]

    missing=[]  
    for i in range(len(x)):
        missing.append(x[i])



    b=[]

    for i in range(0,len(x)):
        b.append('*')
    
    blank = len(x)//2

    for i in range(0,blank):
        z= random.choice(Z)           
        Z.remove(z)
        b[z]=missing[z]
        missing[z] = "*"

            
    


    l3 = Label(root,bg="#FAB069", text="Here is the word")
    l3['font'] = myFont10
    l3.grid(column = 1, row = 1 ,padx = 625, pady = 10)
    l4= Label(root,bg="#FAB069", text = missing)
    l4['font'] = myFont10
    l4.grid(column = 1, row =2, padx = 625, pady = 10)
    l5 =Label(root,bg="#FAB069", text = " Wrong Guesses")
    l5['font'] = myFont10
    l5.grid( row=1, column = 0)
    
    def askagain():
        l2 = Label(root,bg="#FAB069",text="Would you like to play again?")
        l2['font'] = myFont20
        l2.grid(row = 3, column = 3, sticky =N, padx = 500, pady =300)
        bu1 = Button(root,text="Yes",bg="#FB5A55", command = lambda: [next(),start()]  )
        bu1['font'] = myFont20
        bu1.grid(row=3, column =3, sticky = SW,padx = 750, pady = 400)
        bu2 = Button(root,text="No",bg="#FB5A55", command = lambda: [startb(),game_over()])
        bu2['font'] = myFont20
        bu2.grid(row=3, column =3, sticky = SE,padx = 750, pady = 500)
    def next():
        for widgets in root.winfo_children():
            widgets.destroy()
    def printInputz():
        global lll
        global lll1
        global lll2
        global lll3 
        global lll4
        nonlocal submit
        nonlocal count
        global photo
        nonlocal txtbox 
        global txtvalu
        global score
            
        txtvalu = txtbox.get(1.0,"end-1c")
        if txtvalu[0] not in b:
            guess1 = Label(root,bg="#FAB069", text = txtvalu[0])
            guess1['font'] = myFont10
            guess1.grid(column=0)
        
        if txtvalu[0] in b:
            while txtvalu[0] in b:
                index=b.index(txtvalu[0])
                missing[index] = txtvalu[0]
                b[index] = '*'
            r = Label(root,bg="#FAB069", text= missing)
            r['font'] = myFont10
            r.grid(column = 1, row =2, padx = 625, pady = 10)

            if b.count('*') == len(x):
                won = Label(root, bg="#FAB069",text="Congrats!You won!!!")
                won['font'] = myFont15
                won.grid(column =1)
                score=score+1
                s1 = Label(root,bg="#FAB069", text ="Your score is:")
                s1['font']= myFont15
                s1.grid(column=1)
                s = Label(root,bg="#FAB069",text = score)
                s['font']= myFont15
                s.grid(column=1)

                b1 = Button(root, text = "next", height= 2, width =10, bg="#FB5A55",command = lambda:[ next(), askagain()])
                b1['font'] = myFont30
                b1.grid(column =1)
                return


        else:
        
            if count==0:
                photo = ImageTk.PhotoImage(file = "easy1.png", size="4x4")
                lll = Label(root, image = photo)
                lll.grid(column = 1, padx = 100)
                txtbox.destroy()
                submit.destroy()
            
            elif count==1:
                photo = ImageTk.PhotoImage(file = "easy2.png", size="4x4")
                lll1 = Label(root, image = photo, command = lll.grid_forget())
                lll1.grid(column = 1, padx = 100)
                txtbox.destroy()
                submit.destroy()
            elif count==2:
                photo = ImageTk.PhotoImage(file = "easy3.png", size="4x4")
                lll2 = Label(root, image = photo,command = lll1.grid_forget())
                lll2.grid(column = 1, padx = 100)
                txtbox.destroy()
                submit.destroy()
            elif count==3:
                photo = ImageTk.PhotoImage(file = "easy4.png", size="4x4")
                lll3 = Label(root, image = photo,command = lll2.grid_forget())
                lll3.grid(column = 1, padx = 100)
                txtbox.destroy()
                submit.destroy()
            elif count ==4:
                photo = ImageTk.PhotoImage(file = "easy5.png", size="4x4")
                lll4=Label(root, image = photo,command = lll3.grid_forget())
                lll4.grid(column = 1, padx = 100)
                txtbox.destroy()
                submit.destroy()
                ans = Label(root,bg="#FAB069", text ="The correct answer was: " )
                ans['font']= myFont10
                ans.grid(column=1)
                ans1= Label(root,bg="#FAB069",text = x)
                ans1['font']= myFont15
                ans1.grid(column=1)
                loss = Label(root,bg="#FAB069", text = "You lost ! Better luck next time!")
                loss['font']= myFont15
                loss.grid(column =1)
                s1 = Label(root,bg="#FAB069", text ="Your score is:")
                s1['font']= myFont15
                s1.grid(column=1)
                s = Label(root,bg="#FAB069",text = score)
                s['font']= myFont15
                s.grid(column=1)
                b1 = Button(root, text = "next", height= 2, width =10,bg="#FB5A55", command = lambda:[ next(), askagain()])
                b1['font'] = myFont30
                b1.grid(column =1)
                return 
                
            count+=1
            
        
        txtbox = Text(root,height=1,width=5)
        txtbox['font'] = myFont10
        txtbox.grid(sticky = S,row = 3, column = 1, padx =625, pady = 10)
        submit=Button(root,text="submit", bg="#FB5A55",command = printInputz)
        submit['font'] = myFont10
        submit.grid(row=4,column=1)

            

    
    txtbox = Text(root,height=1,width=5)
    txtbox['font'] = myFont10
    txtbox.grid(sticky = S,row = 3, column = 1, padx =625, pady = 10)
    count=0
    submit = Button(root,text="submit",bg="#FB5A55", command = printInputz)
    submit['font'] = myFont10
    submit.grid(row=4,column=1)

def start():
    
    global l1
    global e1
    global e2

    
    l1= Label(root, bg="#FAB069",text="Would you like the easy or the hard level")
    l1['font']= myFont20
    l1.grid( column = 1, padx=550,pady=200)
    easyinfo = Label(root,bg="#FAB069", text ="On choosing easy, you are allowed 5 wrong choices, before the man is hanged!")
    easyinfo['font'] = myFont15
    easyinfo.grid(column=1)
    hardinfo = Label(root,bg="#FAB069", text= "On choosing hard, you are allowed 10 wrong choices, before the man is hanged!")
    hardinfo['font']=myFont15
    hardinfo.grid(column=1)
    e2= Button(root,text="Hard",bg="#FB5A55", height = 3, width = 7,command= lambda: [startb(),button_click_hard(), on_click()] )
    e2['font']= myFont15
    e2.grid(column =1)
    e1= Button(root, text="Easy",height = 3, width = 7,bg="#FB5A55", command = lambda:[startb(),button_click_easy(), on_click()])
    e1['font']= myFont15
    e1.grid(column=1)

def submit():
    global username
    username = name_entry.get(1.0,"end-1c")
    with open("usernames.txt", "r") as file:
        words = file.read().split()
    if username not in words:
        l1 = Label(root,bg="#FAB069", text="Username does not exist, try a differnet username ")
        l1['font']= myFont20
        l1.grid(column=1,padx=150)
        b1 = Button(root, text="Try again",bg="#FB5A55", command = lambda :[delete_text(), l1.grid_forget(),b1.grid_forget()])
        b1['font']= myFont20
        b1.grid(column=1, padx=150)
    else:
        next2 = Button(root, text="Next",bg="#FB5A55", command = lambda:[startb(), game_start()])
        next2['font']= myFont20
        next2.grid(column=1)

def game_start():
    b1 = Button(root,  text = "START",bg="#FB5A55",height =10,width=20,command =lambda:[startb(),start()])
    b1['font'] =  myFont20 
    b1.grid(row = 2, column = 1, padx = 600, pady = 250)

def login():
    global name_entry
    name_label = Label(root, text = 'Enter Username:', bg="#FAB069", font=('calibre',10, 'bold'))
    name_label['font']= myFont20
    name_label.grid(column=1, padx= 650)
    name_entry = Text(root, font=('calibre',10,'normal'), height =2 , width = 20)
    name_entry.grid(column=1)
    sub_btn=Button(root,text = 'Submit', bg="#FB5A55",command = submit)
    sub_btn['font']= myFont20
    sub_btn.grid(column=1)
    
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

login_name = Button(root, text='Login', bg="#FB5A55", command = lambda: [startb(), login()])
login_name['font']= myFont30
# login_name.grid(column =2, padx= 700, pady = 350 )
login_name.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")


root.mainloop()
