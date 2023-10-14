# from tkinter import Tk, PhotoImage, Label, Canvas
# def b():
#     bkWindow= Tk()
#     bkWindow.geometry("1440x900")
#     bkWindow.title("Boss Key")
#     bkCanvas = Canvas(window, height = 900, width =1440)
#     img = PhotoImage(file ="img.png")
#     bkLabel = Label(bkWindow, image=img)
#     bkLabel.place(x=0, y=0, relwidth=1, relheight=1)
#     bkCanvas.pack()
#     bkWindow.focus_set()
#     bkWindow.mainloop()
# b()
# # # def here():
# # #     bkWindow= Tk()
# # #     bkWindow.geometry("1400x900")
# # #     bkWindow.title("BossKey")

# # #     bkCanvas = Canvas(bkWindow, height = 900, width =1400)
# # #     fileName = PhotoImage(file ="bossKey.png")
# # #     bkLabel = Label(bkWindow, image=fileName)
# # #     bkLabel.place(x=0, y=0, relwidth=1, relheight=1)
# # #     bkCanvas.pack()
# # #     bkWindow.mainloop()
# # # def there():
# # #     t=Tk()
# # #     t.geometry("600x600")
# # #     t.attributes("-topmost", True) # ensures that the window sits on top of the game

# # #     t.mainloop()

# # from tkinter import Tk , Label
# # from PIL import ImageTk, Image
# # global root
# # root = Tk()
# # def here():
# #    # root=Tk()
# #     root.geometry("1440x900")
# #    #mycanvas = (root)
# #     myImg = ImageTk.PhotoImage(Image.open("bossKey.png"))
# #     myLabel = Label(root,image=myImg)
# #     myLabel.pack()
# #     root.mainloop()

# # here()
# # root.mainloop()

# # #this game is made for a screen of resolution 1440x900
# # from tkinter import Tk, Frame, Label, PhotoImage, Canvas, Entry, Button
# # #from testnew import here
# # from PIL import ImageTk, Image

# # import random 
# # global gameGrid, score, cells, level
# # colours = [
# #         "#d3d3d3","#fefadc", "#ffd7b3", "#ffc7c6", "#fff0f1", "#fdc6e6", 
# #         "#ead9fe","#dae1fe", "#d4ecff", "#c7fdff", "#d1ffe9", "#e9fff3", 
# #         "#eefadb","#e9f8cf", "#fff6ba", "#fff29c", "#ffcea2", "#ffacab", 
# #         "#ffb7e1", "#ddc4fc", "#c4d1fe", "#c5e5fe", "#abfcfe", "#c2ffe1", 
# #         "#e4febd" ]
# # level = 1
# # if (level<3): gridSize=3 #the size of the grid is dependant on the level
# # else: gridSize=4
# # gameGrid=[[0]*gridSize for i in range(gridSize)]# instanitalises every item in the grid to be zero
# # score = 0
# # def confifureMainMenu():
# #     """This method is responsible for configuring the main menu"""
# #     leaderboard = open("leaderboard.txt")
# #     line = leaderboard.split("\t")

# # gameWindow = Tk()
# # #settingsWindow =Tk()

# # def bossKey(e):
# #      bkWindow= Tk()
# #      bkWindow.geometry("1440x900")
# #      bkWindow.title("Boss Key")
# #      bkCanvas = Canvas(gameWindow, height = 900, width =1440)
# #      img = PhotoImage(file ="img.png")
# #      bkLabel = Label(bkWindow, image=img)
# #      bkLabel.place(x=0, y=0, relwidth=1, relheight=1)
# #      bkCanvas.pack()
# #      bkWindow.mainloop()

# # #def customiseKeys():
# #     # changeKeyLabel = Label("Enter the key you wish to use instead of the default keys")
# #     # changeKeyLabel.grid(row=0, column=0, columnspan=2)
# #     # up = Entry(settingsWindow,width=50)
# #     # up.insert(0,"replace up key")
# #     # up.grid(row=1,column=0)
# #     # u=up.get()

# #     # down = Entry(settingsWindow,width=50)
# #     # down.insert(0,"replace down key")
# #     # down.grid(row=1, column=1)
# #     # d=down.get()

# #     # left = Entry(settingsWindow,width=50)
# #     # left.insert(0,"replace left key")
# #     # left.grid(row=2, column=0)
# #     # l=left.get()

# #     # right = Entry(settingsWindow,width=50)
# #     # right.insert(0,"replace right key")
# #     # right.grid(row=2,column=1)
# #     # r=right.get()

# #     # return u,d,l,r


# # def configureGameWindow():
# #     """This method is responsible for configuring the window"""
# #     screenWidth = gameWindow.winfo_screenwidth()
# #     screenHeight = gameWindow.winfo_screenheight()
# #     gameWindow.geometry(str(screenWidth)+"x"+str(screenHeight)) 
# #     gameWindow.title("2048 game")
# #     return gameWindow

# # def initialiseGame():
# #     global gridSize, cells, gameGrid
# #     """This method generates the first two items in the grid at the start of the game"""
# #     #generates a random position for the first 2 numbers to begin the game
# #     for i in range(2):
# #         row=random.randint(0,gridSize-1)
# #         col=random.randint(0,gridSize-1)
# #         while(gameGrid[row][col]!=0): # ensures the same square isn't chosen twice
# #             row =random.randint(0,gridSize-1)
# #             col =random.randint(0,gridSize-1)
# #         gameGrid[row][col]=2
# #         data = cells[row][col]
# #         s=data[0]
# #         noInS=data[1]
# #         s.configure(bg=colours[1]) #the exponent in base 2 is the index for the colour
# #         #e.g. 4 = 2^2 so the colour for 4 is held in colours[2]
# #         noInS.configure(text="2", bg=colours[1]) #sets label text to 2
# #         data = [s,noInS] #overwrites the variable in cells
# #         cells[row][col]=data
        
# # def saveGame(pName):
# #     #get player name from somewhere
# #     playersSavedGames = open("savedGames.txt","a")
# #     playersSavedGames.append(pName+"\t"+level+"\t"+gameGrid)

# # def configureMainFrame():
# #     """ codes the formation of the cells within the frame of the GUI"""
# #     #global mainFrame, gridSize
# #     if gridSize==3: b=200 #first few levels use a 3x3 grid
# #     else: b=150#harder levels use a 4x4 grid
# #     cells =[]#stores the information about how the squares in the grid should look

# #     #loops through each square on the grid to place 
# #     for i in range(gridSize):
# #         rows=[]
# #         for j in range(gridSize):
# #             square = Frame(mainFrame,bg=colours[0], width=b, height =b)
# #             square.grid(row=i,column=j,padx=5,pady=5)
# #             noInSquare = Label(mainFrame, bg=colours[0], text="", font=('arial',40,'bold'))
# #             noInSquare.grid(row=i, column=j)
# #             data = [square,noInSquare]
# #             rows.append(data) # needs both the frame container and the label
# #         c.append(rows)
# #     return c


# # def configureGrid(gameWindow):
# #     global gridSize, cells, scoreLabel, timerLabel, mainFrame
# #     """This method is responsible for initialising an empty grid"""
# #     mainFrame = Frame(gameWindow, bg="white",bd=5,  width=800, height=800) #holds the grid
# #     mainFrame.pack(pady=75) #padding leaves space at the top for the header
# #     cells = configureCells()
    
# #     inputPlayerName = Entry(gameWindow, width=30)
# #     inputPlayerName.insert(0,"enter your name")
# #     inputPlayerName.place(relx=0.5,y=800, anchor="center")
# #     playerName = inputPlayerName.get()
# #     saveGameButton=Button(gameWindow,text="Save Game", command=lambda:saveGame(playerName)) 
# #     saveGameButton.pack()
# #     #make header - contains score and timer
# #     headerFrame = Frame(gameWindow)
# #     headerFrame.place(relx=0.5, y=45, anchor = "center")
# #     scoreLabel= Label(headerFrame, text="Score: 0") #label stores the score
# #     scoreLabel.grid(row=1, column=0)
# #     timerLabel = Label(headerFrame, text="Time: 0:00",)
# #     timerLabel.grid(row=1,column=1, padx=50)
# #     pauseBtn = Button(headerFrame)
# #     pauseBtn.grid(row=1,column=2, padx=50)
# #     gameGrid = initialiseGame()
    

# # def addsNewSquare():
# #     global gridSize
# #     row =random.randint(0,gridSize-1)
# #     col =random.randint(0,gridSize-1)
# #     while(gameGrid[row][col]!=0): #ensures the square is empty
# #         row =random.randint(0,gridSize-1)
# #         col =random.randint(0,gridSize-1)
# #     gameGrid[row][col]=random.choice([2,4]) # adds a new value
    

# # def generateExponent(n):
# #     e = 1
# #     while n>2:
# #         n=n/2
# #         e+=1
# #     return e

# # def updateCellsAndScore(): 
# #     global cells, score, gameGrid, gridSize, level
# #     if (level<3): a=3 #the size of the grid is dependant on the level
# #     else: a=4
# #     if a!=gridSize:
# #         temp = [[0]*a for i in range(a)]
# #         for i in range(gridSize):
# #             for j in range(gridSize):
# #                 temp[i][j]=gameGrid[i][j]
# #         gridSize=a
# #         gameGrid=temp
# #         temp=configureCells()
# #         cells=temp

# #     for i in range(gridSize):
# #         for j in range(gridSize):
# #          #   print(i,j,gameGrid[i][j])
# #             if gameGrid[i][j]!=0:
# #                 exp = generateExponent(gameGrid[i][j])
# #                 #print(exp)
# #                 data = cells[i][j] # contents are overwritten in data
# #                 sq=data[0] #square - this is a frame
# #                 noInS=data[1] # no in square - this is a label
# #                 sq.configure(bg=colours[exp]) #the exponent in base 2 is the index for the colour
# #                 noInS.configure(text=str(gameGrid[i][j]), bg=colours[exp]) #sets label text to 2
# #                 data = [sq,noInS] #stores updates frame in data
# #                 cells[i][j]=data # overwrites this in variable cells
# #             elif (gameGrid[i][j]==0):
# #                 data = cells[i][j] # contents are overwritten in data
# #                 sq=data[0] #square - this is a frame
# #                 noInS=data[1] # no in square - this is a label
# #                 sq.configure(bg=colours[0]) #the exponent in base 2 is the index for the colour
# #                 noInS.configure(text="", bg=colours[0]) #sets label text to 2
# #                 data = [sq,noInS] #stores updates frame in data
# #                 cells[i][j]=data # overwrites this in variable cells


# #     scoreLabel.configure(text="score:"+str(score))

# # def moveToOneSide(start,stop,jump):
# #     """moves all the squares horizontally in one direction"""
# #     for i in range(gridSize):
# #         if (jump==1):isZero = 0
# #         else: isZero=gridSize-1
# #         for j in range(start,stop,jump):
# #             if (gameGrid[i][j]!=0):
# #                 if (j!=isZero):
# #                     gameGrid[i][isZero]=gameGrid[i][j]
# #                     gameGrid[i][j] = 0
# #                 if(jump==1): isZero+=1
# #                 else: isZero-=1

# # def moveUpOrDown(start,stop,jump):
# #     """moves all the squares vertically in one direction"""
# #     for i in range(gridSize):
# #         if (jump==1):isZero = 0
# #         else: isZero=gridSize-1
# #         for j in range(start,stop,jump):
# #             if (gameGrid[j][i]!=0):
# #                 if (j!=isZero):
# #                     gameGrid[isZero][i]=gameGrid[j][i]
# #                     gameGrid[j][i] = 0
# #                 if(jump==1): isZero+=1
# #                 else: isZero-=1


# # def left(e):
# #     """Codes the movement of the squares when the left arrow is pressed"""
# #     global score, gridSize, cells, gameGrid
    
# #     moveToOneSide(0,gridSize,1) #moves all squares to the leftmost empty square

# #     #combines like squares
# #     for i in range(gridSize):
# #         for j in range(gridSize-1):
# #             if gameGrid[i][j]!=0 and gameGrid[i][j]==gameGrid[i][j+1]:
# #                 gameGrid[i][j]+=gameGrid[i][j]
# #                 gameGrid[i][j+1]=0
# #                 score += gameGrid[i][j]
    
# #     moveToOneSide(0,gridSize,1) # the above method results in some gaps so these need to be filled again

# #     addsNewSquare()
# #     updateCellsAndScore()
# #     isGameOver()


# # def right(e):
# #     """Codes the movement of the squares when the right arrow is pressed"""
# #     global score, gridSize, cells, gameGrid
# #     moveToOneSide(gridSize-1,-1,-1) #moves all squares to the rightmost empty square

# #     #combines like squares
# #     for i in range(gridSize):
# #         for j in range(gridSize-1,0,-1):
# #             if gameGrid[i][j]!=0 and gameGrid[i][j]==gameGrid[i][j-1]:
# #                 gameGrid[i][j]+=(gameGrid[i][j])
# #                 gameGrid[i][j-1]=0
# #                 score += gameGrid[i][j]

# #     moveToOneSide(gridSize-1,-1,-1)

# #     addsNewSquare()
# #     updateCellsAndScore()
# #     isGameOver()

# # def up(e):
# #     """Codes the movement of the squares when the up arrow is pressed"""
# #     global score, gridSize, cells, gameGrid
 
# #     moveUpOrDown(0,gridSize,1)#moves all squares to the topmost empty square

# #     #combines like squares
# #     for i in range(gridSize):
# #         for j in range(gridSize-1):
# #             if gameGrid[j][i]!=0 and gameGrid[j][i]==gameGrid[j+1][i]:
# #                 gameGrid[j][i]+=(gameGrid[j][i])
# #                 gameGrid[j+1][i]=0
# #                 score += gameGrid[j][i]
    
# #     moveUpOrDown(0,gridSize,1)
    
# #     addsNewSquare()
# #     updateCellsAndScore()
# #     isGameOver()

# # def down(e):
# #     """Codes the movement of the squares when the up arrow is pressed"""
# #     global score, gridSize, cells, gameGrid
   
# #     moveUpOrDown(gridSize-1,-1,-1)#moves all squares to the bottommost empty square

# #     #combines like squares
# #     for i in range(gridSize):
# #         for j in range(gridSize-1,0,-1):
# #             if gameGrid[j][i]!=0 and gameGrid[j][i]==gameGrid[j-1][i]:
# #                 gameGrid[j][i]+=gameGrid[j][i]
# #                 gameGrid[j-1][i]=0
# #                 score += gameGrid[j][i]

# #     moveUpOrDown(gridSize-1,-1,-1)

    
# #     addsNewSquare()
# #     updateCellsAndScore()
# #     isGameOver()

# # def canMove():
# #     canMoveHorizontally = False
# #     canMoveVertically = False
# #     for i in range(gridSize):
# #         for j in range(gridSize-1):
# #             if gameGrid[i][j]==gameGrid[i][j+1]: canMoveHorizontally = True
# #             elif gameGrid[j][i]==gameGrid[j+1][i]: canMoveVertically = True
# #     return canMoveVertically, canMoveHorizontally


# # def isGameOver():
# #     def update():gameOverLabel.configure(text="", bg=colours[0])

# #     global level
# #     empty = False # checks if there are any spaces in the grid
# #     winValue = False

# #     #initialises the game over variables
# #     gameOverFrame = Frame(gameWindow)
# #     gameOverFrame.place(relx=0.5,rely=0.5, anchor="center")
# #     gameOverLabel = Label(gameOverFrame, text="", bg ="black", fg="white", font=("arial",30,"bold"))

# #     for i in range(gridSize):
# #         for j in range(gridSize):
# #             if gameGrid[i][j]==0: empty = True
# #             elif gameGrid[i][j]==2**(level+3): winValue = True

# #     if empty==False: 
# #         v , h = canMove()
# #         if (v==False and h==False): gameOverLabel.configure(text = "Game Over") 
# #     elif winValue ==True: 
# #         gameOverLabel.configure(text="Next level")
# #         level+=1
# #         gameOverLabel.after(3000, update)
# #         print (level)
# #         updateCellsAndScore()


# #     #else:
# #        ## gameOverLabel.configure(text = "Game Over")
# #     gameOverLabel.pack()

# # w = configureGameWindow()
# # configureGrid(w)
# # #for i in range(gridSize):
# #  #   for j in range(gridSize):
# #   #      print(i,j,gameGrid[i][j])
# # print("gap")
# # w.bind("<Left>", left)
# # w.bind("<Right>", right)
# # w.bind("<Up>", up)
# # w.bind("<Down>", down)
# # w.bind("<space>", bossKey)
# # w.focus_set()
# # w.mainloop()

from tkinter import Tk, Frame, Label, PhotoImage, Canvas
#from testnew import here
from PIL import ImageTk, Image

import random 
global gameGrid, score, cells, level
colours = [
        "#d3d3d3","#fefadc", "#ffd7b3", "#ffc7c6", "#fff0f1", "#fdc6e6", 
        "#ead9fe","#dae1fe", "#d4ecff", "#c7fdff", "#d1ffe9", "#e9fff3", 
        "#eefadb","#e9f8cf", "#fff6ba", "#fff29c", "#ffcea2", "#ffacab", 
        "#ffb7e1", "#ddc4fc", "#c4d1fe", "#c5e5fe", "#abfcfe", "#c2ffe1", 
        "#e4febd" ]
level = 1
if (level<7): gridSize=3 #the size of the grid is dependant on the level
else: gridSize=4
gameGrid=[[0]*gridSize for i in range(gridSize)]# instanitalises every item in the grid to be zero
score = 0
mainMenuWindow =Tk()
def confifureMainMenu():
    """This method is responsible for configuring the main menu"""
    leaderboard = open("leaderboard.txt")
    line = leaderboard.split("\t")

gameWindow = Tk()

def bossKey(e):
     bkWindow= Tk()
     bkWindow.geometry("1400x900")
     bkWindow.title("Boss Key")
     bkCanvas = Canvas(gameWindow, height = 900, width =1440)
     img = PhotoImage(file ="img.png")
     #img = img.resize(1440,900)
     #fileName.resize((1440,900))
     bkLabel = Label(bkWindow, image=img)
     bkLabel.place(x=0, y=0, relwidth=1, relheight=1)
     bkCanvas.pack()
     bkWindow.mainloop()

def configureGameWindow():
    """This method is responsible for configuring the window"""
    screenWidth = gameWindow.winfo_screenwidth()
    screenHeight = gameWindow.winfo_screenheight()
    gameWindow.geometry(str(screenWidth)+"x"+str(screenHeight)) 
    gameWindow.title("2048 game")
    return gameWindow

def initialiseGame():
    global gridSize, cells, gameGrid
        data = [s,noInS] #overwrites the variable in cells
        cells[row][col]=data

def configureGrid(gameWindow):
    global gridSize, cells, scoreLabel, timerLabel
    """This method is responsible for initialising an empty grid"""
    mainFrame = Frame(gameWindow, bg="white",bd=5,  width=800, height=800) #holds the grid
    mainFrame.pack(pady=75) #padding leaves space at the top for the header
    if gridSize==3: b=200 #first few levels use a 3x3 grid
    else: b=150#harder levels use a 4x4 grid

    cells =[]#stores the information about how the squares in the grid should look

        cells.append(rows)
    
    #make header - contains score and timer
    headerFrame = Frame(gameWindow)
    headerFrame.place(relx=0.5, y=45, anchor = "center")
    scoreLabel= Label(headerFrame, text="Score: 0") #label stores the score
    scoreLabel.grid(row=1, column=0)

    addsNewSquare()
    updateCellsAndScore()
    isGameOver()


def right(e):

    addsNewSquare()
    updateCellsAndScore()
    isGameOver()

def up(e):
    """Codes the movement of the squares when the up arrow is pressed"""
    
    addsNewSquare()
    updateCellsAndScore()
    isGameOver()

def down(e):
    """Codes the movement of the squares when the up arrow is pressed"""
    
    addsNewSquare()
    updateCellsAndScore()
    isGameOver()

def canMove():
    canMoveHorizontally = False
    canMoveVertically = False
    for i in range(gridSize):
        for j in range(gridSize-1):
            if gameGrid[i][j]==gameGrid[i][j+1]: canMoveHorizontally = True
            elif gameGrid[j][i]==gameGrid[j+1][i]: canMoveVertically = True
    return canMoveVertically, canMoveHorizontally


def isGameOver():
    global level
    empty = False # checks if there are any spaces in the grid
    winValue = False

    #initialises the game over variables
    gameOverFrame = Frame(gameWindow)
    gameOverFrame.place(relx=0.5,rely=0.5, anchor="center")
    gameOverLabel = Label(gameOverFrame, text="", bg ="black", fg="white", font=("arial",30,"bold"))

    for i in range(gridSize):
        for j in range(gridSize):
            if gameGrid[i][j]==0: empty = True
            elif gameGrid[i][j]==2**(level+3): winValue = True

    if empty==False: 
        v , h = canMove()
        if (v==False and h==False): gameOverLabel.configure(text = "Game Over") 
    elif winValue ==True: 
        gameOverLabel.configure(text="Next level")
        level+=1
        gameOverLabel.configure(text="")


    #else:
       ## gameOverLabel.configure(text = "Game Over")
    gameOverLabel.pack()

w = configureGameWindow()
configureGrid(w)
#for i in range(gridSize):
 #   for j in range(gridSize):
w.bind("<Right>", right)
w.bind("<Up>", up)
w.bind("<Down>", down)
w.bind("<space>", bossKey)
w.focus_set()
