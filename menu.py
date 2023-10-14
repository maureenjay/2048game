from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
def mainMenu():
    """This method is responsible for configuring the main menu"""
    global playerName
    playerName= None
    mainMenu = Tk()
    mainMenu.geometry("1440x900")
    mainMenu.title("Main Menu")
    mainMenuFrame = Frame(mainMenu, bd=5,  width=700, height=300) #holds the grid
    mainMenuFrame.pack(pady=125,padx=50, anchor="center") #padding leaves space at the top for the header

    #loop places images
    lblLBTitle = Label (mainMenuFrame, text = "Leaderboard",font=('arial',40), 
                padx=30, pady=10 )
    lblLBTitle.grid(row=0, column=0, columnspan=4)

    img0=ImageTk.PhotoImage(Image.open("img0.png").resize((60,60), Image.ANTIALIAS))
    lblLeaderboard = Label(mainMenuFrame, image=img0,padx=10, pady=20)
    lblLeaderboard.grid(row=1, column=1)

    img1=ImageTk.PhotoImage(Image.open("img1.png").resize((60,60), Image.ANTIALIAS))
    lblLeaderboard = Label(mainMenuFrame, image=img1,padx=10, pady=20)
    lblLeaderboard.grid(row=2, column=1)

    img2=ImageTk.PhotoImage(Image.open("img2.png").resize((60,60), Image.ANTIALIAS))
    lblLeaderboard = Label(mainMenuFrame, image=img2,padx=10, pady=20)
    lblLeaderboard.grid(row=3, column=1)

    img3=ImageTk.PhotoImage(Image.open("img3.png").resize((60,60), Image.ANTIALIAS))
    lblLeaderboard = Label(mainMenuFrame, image=img3,padx=10, pady=20)
    lblLeaderboard.grid(row=4, column=1)

    img4=ImageTk.PhotoImage(Image.open("img4.png").resize((60,60), Image.ANTIALIAS))
    lblLeaderboard = Label(mainMenuFrame, image=img4,padx=10, pady=20)
    lblLeaderboard.grid(row=5, column=1)

    leaderboard = open("leaderboard.txt")

    #places names and scores
    for i in range(5):
        line = leaderboard.readline().split(",")
        for j in range(len(line)):
                lblLeaderboard = Label(mainMenuFrame, text=line[j], font=('arial',18), 
                padx=30, pady=20)
                lblLeaderboard.grid(row=i+1, column=j+2)
    leaderboard.close()

    inputPlayerName = Entry(mainMenu, width=20, font=('arial',20))
    inputPlayerName.insert(0,"enter your name")
    inputPlayerName.place(relx=0.99,anchor="e",y=210)
    
    def next():
         global playerName
         playerName=inputPlayerName.get()
         messagebox.showinfo("", "The space bar is the Boss Key \nPress return to return to program")
         mainMenu.destroy()
    def exit():
         global playerName
         messagebox.showinfo("", "The space bar is the Boss Key \nPress return to return to program")
         mainMenu.destroy()
         playerName="guest"

    inputName = Button(mainMenu, width=20, text="log in",command=next, font=('arial',20))
    inputName.place(relx=0.99,y=280, anchor="e")
    guest=Button(mainMenu, width=20, text="play as guest",command=exit, font=('arial',20))
    guest.place(relx=0.99,y=350, anchor="e")

    headerFrame = Frame(mainMenu, pady=10)
    headerFrame.place(relx=0.5, y=60, anchor = "center", )

    img=ImageTk.PhotoImage(Image.open("logo.png").resize((450,150), Image.ANTIALIAS))
    lblGameName = Label(headerFrame, image=img,padx=10, pady=20)
    lblGameName.grid(row=1, column=0)

    lblGameInfo=Label(mainMenu, text="How to play:\n The aim of the game is to reach the highest power of 2 "+
         "by joining identical squares together using the arrow keys\nYou may quit at any time by pressing "+
         "the exit button, this will automatically save your progress if you enter your name on the left",
         wraplength=350, font=("arial",18))
    lblGameInfo.place(relx=0, y=200)

    mainMenu.mainloop()
    return playerName

def gameOver():
     """This method is responsible for configuring the main menu"""
     gameOver = Tk()
     gameOver.geometry("1440x900")
     gameOver.title("Main Menu")
     gameOverFrame = Frame(gameOver, bd=5,  width=700, height=300) #holds the grid
     gameOverFrame.pack(pady=125,padx=50, anchor="center") #padding leaves space at the top for the header

     #loop places images
     lblLBTitle = Label (gameOverFrame, text = "Leaderboard",font=('arial',40), 
               padx=30, pady=10 )
     lblLBTitle.grid(row=0, column=0, columnspan=4)

     img0=ImageTk.PhotoImage(Image.open("img0.png").resize((60,60), Image.ANTIALIAS))
     lblLB0 = Label(gameOverFrame, image=img0,padx=10, pady=20)
     lblLB0.grid(row=1, column=1)

     img1=ImageTk.PhotoImage(Image.open("img1.png").resize((60,60), Image.ANTIALIAS))
     lblLB1 = Label(gameOverFrame, image=img1,padx=10, pady=20)
     lblLB1.grid(row=2, column=1)

     img2=ImageTk.PhotoImage(Image.open("img2.png").resize((60,60), Image.ANTIALIAS))
     lblLB2 = Label(gameOverFrame, image=img2,padx=10, pady=20)
     lblLB2.grid(row=3, column=1)

     img3=ImageTk.PhotoImage(Image.open("img3.png").resize((60,60), Image.ANTIALIAS))
     lblLB3 = Label(gameOverFrame, image=img3,padx=10, pady=20)
     lblLB3.grid(row=4, column=1)

     img4=ImageTk.PhotoImage(Image.open("img4.png").resize((60,60), Image.ANTIALIAS))
     lblLB4= Label(gameOverFrame, image=img4,padx=10, pady=20)
     lblLB4.grid(row=5, column=1)

     leaderboard = open("leaderboard.txt")

     #places names and scores
     for i in range(5):
          line = leaderboard.readline().split(",")
          for j in range(len(line)):
                    lblLeaderboard = Label(gameOverFrame, text=line[j], font=('arial',18), 
                    padx=30, pady=20)
                    lblLeaderboard.grid(row=i+1, column=j+2)
     leaderboard.close()
     

     headerFrame = Frame(gameOver, pady=20)
     headerFrame.place(relx=0.5, y=60, anchor = "center", )

     img=ImageTk.PhotoImage(Image.open("logo.png").resize((450,150), Image.ANTIALIAS))
     lblGameName = Label(headerFrame, image=img,padx=10, pady=20)
     lblGameName.grid(row=1, column=0)


     gameOver.mainloop()
