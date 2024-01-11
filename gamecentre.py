
from tkinter import *
from tkinter import Tk

root=Tk()
root.geometry("400x1010")
root.title("Game Center")

def kill():
    root.destroy()
    import fhangman_mod
def startb():
    for widgets in root.winfo_children():
        widgets.destroy()


def start():
    global l1
    global l2

    global hangman
    global tictactoe


    intro.after(1, intro.destroy)
    

    def Hangman():
        global l3
        l3= Label(root, text="You've chosen HANGMAN!").pack()

        l1.after(1,l1.destroy)
        hangman.after(1, hangman.destroy)
        tictactoe.after(1, tictactoe.destroy)
        
        
        global signup
        global name_var
 
        

        def delete_text():
            new_name.delete("1.0", "end")
        def new_file():
            username = new_name.get(1.0,"end-1c")

            with open("usernames.txt", "r") as file:
                words = file.read().split()
            
            with open('usernames.txt') as fobj:
                text = fobj.read()
            
            if username not in words:
                with open('usernames.txt', 'a') as fobj:
                    if not text.endswith('\n'):
                        fobj.write('\n')
                    fobj.write(username)
                b2 = Button(root, text="Next", command = kill())
                b2.pack()
            
            
            else:
                l1 = Label(root, text = "Username already exists, try other name")
                l1.pack()
                b1 = Button(root, text="Try again", command = lambda :[delete_text(), l1.pack_forget(),b1.pack_forget()])
                b1.pack()

        def signin():   
            import fhangman_mod
                    
        def signup():

            global new_name

            name_label = Label(root, text = 'Enter a Username:', font=('calibre',10, 'bold'))
            name_label.pack()
            signup.after(1,signup.destroy)
            

            new_name= Text(root, height =1, width = 20)
            new_name.pack()
            submit_name = Button(root, text ="Submit", command = new_file)
            submit_name.pack()

        signup= Button(root, text="Sign Up", command= signup)
        signup.pack(pady=5)
        signin = Button(root,text = "Sign in", command = kill )
        signin.pack(pady=5)

        
    def Tictactoe():

        import ttt_mod
        
    l1= Label(root, text="Welcome to Game center \nChoose a game! \n",font=("Arial Bold",15))
    l1.pack(pady=10)

    hangman= Button(root, text="Hangman",command= Hangman)
    hangman.pack(pady=10)

    tictactoe= Button(root, text="Tic-Tac-Toe", command= Tictactoe)
    tictactoe.pack(pady=10)

intro=Button(root, text = "START", command = start)
intro.pack()

root.mainloop()

