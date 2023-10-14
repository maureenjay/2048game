#this game is optimized on screensize 1440x900
from tkinter import Tk, Frame, Label, PhotoImage, Canvas, Entry, Button, messagebox
from PIL import ImageTk, Image
from menu import mainMenu , gameOver
import random

global gameGrid, cells, gridSize, window, sec, min, pause, level, score, tempScore, flag 


#contains all the colours to be used in the game
colours = [
        "#d3d3d3","#fefadc", "#ffd7b3", "#ffc7c6", "#fff0f1", "#fdc6e6", 
        "#ead9fe","#dae1fe", "#d4ecff", "#c7fdff", "#d1ffe9", "#e9fff3", 
        "#eefadb","#e9f8cf", "#fff6ba", "#fff29c", "#ffcea2", "#ffacab", 
        "#ffb7e1", "#ddc4fc", "#c4d1fe", "#c5e5fe", "#abfcfe", "#c2ffe1", 
        "#e4febd" ]

######################################## FUNCTIONS ################################################

############################ for the creation of the main parts of the game ######################
def createFrame():
    """creates the main frame that the game will sit on"""
    global myFrame
    myFrame = Frame(window, height=900, width=1440)
    myFrame.pack()

def initializeWindow():
    """edits the shape and size of the window"""
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    window.geometry(str(screenWidth)+"x"+str(screenHeight)) 
    window.title("2048 game")
    createFrame()
###################################################################################################

##################################### to save to text files ##########################################
def saveGame(): 
    """This method saves user's progress"""
    tf = open("savedGames.txt")
    #initialisations
    array = []
    tempGameGridStr =""
    updateFileEntry = False
    #stores the 2d grid array as a plaintext string

    for i in range(gridSize):
            for j in range(gridSize):
                if (i==0 and j==0): tempGameGridStr=str(gameGrid[i][j])
                else: tempGameGridStr = tempGameGridStr+"."+str(gameGrid[i][j])

    tmp=pName.lower()+","+str(score)+","+str(level)+","+tempGameGridStr+","+str(min)+","+str(sec)


    #adds the rest of the contents in the file in after
    for line in tf:
        lineContents = line.split(",")
        if lineContents[0]==pName.lower(): updateFileEntry=True # doesn't store user previous saved game entry in the array
        else: array.append(line)

    if updateFileEntry == True:
        array.append(tmp)#adds user results to the top of the array
        #overwrites the text file 
        tf = open("savedGames.txt", "w")
        tf.write(array[0])
        for i in range(1,len(array)):
            a = array[i-1]
            if(a[-1]=="\n"): tf.write(array[i])
            else: tf.write("\n"+array[i])
    else: # appends file if the user doesn't have previous game records
        tf = open("savedGames.txt", "a")
        tf.write("\n"+tmp)
    tf.close()
    return

def updateLeaderboard():
    """This method updates the leaderboard"""
    tf = open("leaderboard.txt")

    #initialisations
    array = []
    tmp = []
    tmp.append(pName.lower())
    tmp.append(str(score))
    newArray =[]
    isInLB=False

    #adds contents from the txt file into an array, removing any past record of the current player
    for line in tf:
        lineContents = line.split(",")
        if lineContents[0]==pName.lower(): continue
        else: array.append(lineContents)

    #adds the current score of the player in the correct position
    for i in range(len(array)):
        if int(array[i][1])< score and isInLB==False:
            tmp[1]=tmp[1]+"\n"
            newArray.append(tmp)
            newArray.append(array[i])
            isInLB = True
        elif(i==len(array)-1 and isInLB==False): #adds a new line key if adding the new score to the end of the list
            array[i][1]=array[i][1]+"\n"
            newArray.append(array[i])
        else:newArray.append(array[i])

    if isInLB==False: newArray.append(tmp)

    #writes the updated leaderboard to the text file
    tf = open("leaderboard.txt", "w")

    for i in range(len(newArray)):
        tf.write(newArray[i][0]+","+newArray[i][1])
    tf.close()
    return
#######################################################################################################

####################### for the creation of the grid upon the start of the game ################################
def makeGrid():
    """This is responsible for generating the grid within the GUI"""
    global cells, gridSize
   # gridSize=4
    mainFrame = Frame(myFrame, bg="white",bd=5,  width=800, height=800) #holds the grid
    mainFrame.pack(pady=75) #padding leaves space at the top for the header
    if (gridSize==3): b=200 #first few levels use a 3x3 grid
    else: b=150#harder levels use a 4x4 grid

    cells =[]#stores the information about how the squares in the grid should look

    #loops through each square on the grid to place 
    for i in range(gridSize):
        rows=[]
        for j in range(gridSize):
            square = Frame(mainFrame,bg=colours[0], width=b, height =b)
            square.grid(row=i,column=j,padx=5,pady=5)
            noInSquare = Label(mainFrame, bg=colours[0], text="", font=('arial',40,'bold'))
            noInSquare.grid(row=i, column=j)
            data = [square,noInSquare]
            rows.append(data) # needs both the frame container and the label
        cells.append(rows)
    return
    
def makeHeader():
    """This method makes the header which sits on the main game grid"""
    global  scoreLabel, timerLabel, pause
    headerFrame = Frame(myFrame)
    headerFrame.place(relx=0.5, y=45, anchor = "center")
    scoreLabel= Label(headerFrame, text="Score: 0",font=('arial',20)) #label stores the score
    scoreLabel.grid(row=1, column=0)

    def pauseGame():
        global pause
        pause = True
        a = messagebox.showinfo("","Game paused, press ok to resume")
        if (a == "ok"):  
            pause=False
            clock() 
    pauseBtn = Button(headerFrame, text = "pause",  font=('arial',20),command = pauseGame)
    pauseBtn.grid(row=1,column=2, padx=50)


    timerLabel = Label(headerFrame, text="", font=('arial',20))

    # clock is recursive so constantly runs even if the main loop isn't called
    def clock():
        global sec, min
        if (sec<60): sec+=1
        else: 
            sec=0
            min+=1
        if (sec<10): timerLabel.configure(text ="Time:0"+str(min)+":0"+str(sec))
        else: timerLabel.configure(text ="Time:0"+str(min)+":"+str(sec))
        if (pause == False): timerLabel.after(1000,clock) 
    clock()
    timerLabel.grid(row=1,column=1, padx=50)

    return

def initialiseGame():
    """This method generates the first two items in the grid at the start of the game"""
    global gridSize, cells, gameGrid

    #generates a random position for the first 2 numbers to begin the game
    for i in range(2):
        row=random.randint(0,gridSize-1)
        col=random.randint(0,gridSize-1)
        while(gameGrid[row][col]!=0): # ensures the same square isn't chosen twice
            row =random.randint(0,gridSize-1)
            col =random.randint(0,gridSize-1)
        gameGrid[row][col]=2
        data = cells[row][col]
        s=data[0]
        noInS=data[1]
        s.configure(bg=colours[1]) #the exponent in base 2 is the index for the colour
        #e.g. 4 = 2^2 so the colour for 4 is held in colours[2]
        noInS.configure(text="2", bg=colours[1]) #sets label text to 2
        data = [s,noInS] #overwrites the variable in cells
        cells[row][col]=data
    return
################################################################################################################

def configureGrid(gameGridStr):
    """This method is responsible for placing the game frame and header onto the window  using the methods defined in 
    the previous section"""
    global gridSize, gameGrid, level, window,flag

    if (level<4): gridSize=3 #the size of the grid is dependant on the level
    else: gridSize=4
    gameGrid=[[0]*gridSize for i in range(gridSize)]# instanitalises every item in the grid to be zero
    #makes grid
   
    makeGrid()


    #saveGameButton=Button(window,text="Save Game", command=lambda:saveGame(playerName)) 
    #saveGameButton.pack()

    #make header - contains score and timer
    makeHeader()
    
    if (flag==False): initialiseGame() #places the starting 2s
    else:
        temp = gameGridStr.split(".")
        #converts fields within the array to integers
        count=0
        for i in range(gridSize):
            for j in range(gridSize):
                gameGrid[i][j]=int(temp[count])
                count+=1

    #if pName!="guest":
     #   f = open("userProgress.txt", "r") #opens the file storing user's history

    return 

######################## responsible for the actions that take place after a move is made #################
def addsNewSquare():
    """adds a new number in a random position to a 2D ARRAY"""
    global gridSize

    row =random.randint(0,gridSize-1)
    col =random.randint(0,gridSize-1)

    while(gameGrid[row][col]!=0): #ensures the square is empty
        row =random.randint(0,gridSize-1)
        col =random.randint(0,gridSize-1)
        
    gameGrid[row][col]=random.choice([2,4]) # adds a new value

    return

def generateExponent(n):
    e = 1
    while n>2:
        n=n/2
        e+=1
    return e

def updateCellsAndScore(): 
    """"Responsible for reflecting changes in the 2D in the GUI"""
    global cells, tempScore, gameGrid, gridSize

    for i in range(gridSize):
        for j in range(gridSize):
            if (gameGrid[i][j]!=0):
                exp = generateExponent(gameGrid[i][j])
                data = cells[i][j] # contents are overwritten in data
                sq=data[0] #square - this is a frame
                noInS=data[1] # no in square - this is a label
                sq.configure(bg=colours[exp]) #the exponent in base 2 is the index for the colour
                noInS.configure(text=str(gameGrid[i][j]), bg=colours[exp]) #sets label text to 2
                data = [sq,noInS] #stores updates frame in data
                cells[i][j]=data # overwrites this in variable cells
            elif (gameGrid[i][j]==0):
                data = cells[i][j] # contents are overwritten in data
                sq=data[0] #square - this is a frame
                noInS=data[1] # no in square - this is a label
                sq.configure(bg=colours[0]) #the exponent in base 2 is the index for the colour
                noInS.configure(text="", bg=colours[0]) #sets label text to 2
                data = [sq,noInS] #stores updates frame in data
                cells[i][j]=data # overwrites this in variable cells

    scoreLabel.configure(text="score:"+str(tempScore))

    return
#########################################################################################################

###################### responsible for displaying the boss key and returning to the game after ###############
def loadGridWhileInGame():
    """loads the current grid that was deleted when boss key is shown"""

    global gameGrid
    configureGrid(None) #instantialises an empty screen 

    f = open("tempTxtFile.txt", "r") #overwrites grid
    for i in range(gridSize):
        line=f.readline().split(",")
        for j in range(gridSize):
            gameGrid[i][j]=int(line[j])
    f.close()
    updateCellsAndScore()

    return

def bossKey(e):
    """opens the boss key image"""
    global myFrame, gameGrid
    f = open("tempTxtFile.txt", "w")
    for i in range(gridSize):
        line=""
        for j in range(gridSize):
            if(j<gridSize-1):line=line+str(gameGrid[i][j])+","
            else: line=line+str(gameGrid[i][j])
        if (i<gridSize-1):f.write(line+"\n")
        else: f.write(line)
    f.close()
    myFrame.destroy() # removes the main frame from window 

    def removeBossKey(e):
        """makes the main frame reappear"""
        bkFrame.destroy() 
        window.title("2048 Game")
        createFrame()
        loadGridWhileInGame()
        updateCellsAndScore()

    #codes the widgets to show the boss key widgets
    window.title("Boss Key")
    bkFrame = Frame(window, bg="black")
    bkFrame.tkraise()
    bkFrame.pack()
    img=ImageTk.PhotoImage(Image.open("bossKey.png").resize((1440,900), Image.ANTIALIAS))
    lblBossKey = Label(bkFrame, image=img)
    lblBossKey.pack()
    window.bind("<Return>", removeBossKey)
    window.mainloop()
    return
####################################################################################################

############# functions for movements within the grid according to player input ####################
def moveToOneSide(start,stop,jump):
    """moves all the squares horizontally in one direction"""
    hasMoveTakenPlace=False
    for i in range(gridSize):
        if (jump==1):isZero = 0
        else: isZero=gridSize-1
        for j in range(start,stop,jump):
            if (gameGrid[i][j]!=0):
                if (j!=isZero):
                    gameGrid[i][isZero]=gameGrid[i][j]
                    gameGrid[i][j] = 0
                    hasMoveTakenPlace=True
                if(jump==1): isZero+=1
                else: isZero-=1
    return hasMoveTakenPlace

def moveUpOrDown(start,stop,jump):
    """moves all the squares vertically in one direction"""
    hasMoveTakenPlace=False
    for i in range(gridSize):
        if (jump==1):isZero = 0
        else: isZero=gridSize-1
        for j in range(start,stop,jump):
            if (gameGrid[j][i]!=0):
                if (j!=isZero):
                    gameGrid[isZero][i]=gameGrid[j][i]
                    gameGrid[j][i] = 0
                    hasMoveTakenPlace=True
                if(jump==1): isZero+=1
                else: isZero-=1
    return hasMoveTakenPlace

def left(e):
    """Codes the movement of the squares when the left arrow is pressed"""
    global tempScore, gridSize, cells, gameGrid

    isLegal = moveToOneSide(0,gridSize,1) #moves all squares to the leftmost empty square

    #combines like squares
    for i in range(gridSize):
        for j in range(gridSize-1):
            if (gameGrid[i][j]!=0 and gameGrid[i][j]==gameGrid[i][j+1]):
                gameGrid[i][j]+=gameGrid[i][j]
                gameGrid[i][j+1]=0
                tempScore += gameGrid[i][j]
                isLegal=True

    dc = moveToOneSide(0,gridSize,1) # the above method results in some gaps so these need to be filled again

    # i.e. if grid has been changed
    if (isLegal==True):
        addsNewSquare()
        updateCellsAndScore()
        isGameOver()
    else:
        messagebox.showerror("", "invalid move try again")
    return

def right(e):
    """Codes the movement of the squares when the right arrow is pressed"""
    global tempScore, gridSize, cells, gameGrid
    isLegal = moveToOneSide(gridSize-1,-1,-1) #moves all squares to the rightmost empty square

    #combines like squares
    for i in range(gridSize):
        for j in range(gridSize-1,0,-1):
            if (gameGrid[i][j]!=0 and gameGrid[i][j]==gameGrid[i][j-1]):
                gameGrid[i][j]+=(gameGrid[i][j])
                gameGrid[i][j-1]=0
                tempScore += gameGrid[i][j]
                isLegal = True

    moveToOneSide(gridSize-1,-1,-1) #deoesnt capture return value because it would already have been affected above

    if (isLegal==True):
        addsNewSquare()
        updateCellsAndScore()
        isGameOver()
    else:
        messagebox.showerror("", "invalid move try again")
    return

def up(e):
    """Codes the movement of the squares when the up arrow is pressed"""
    global tempScore, gridSize, cells, gameGrid

    isLegal = moveUpOrDown(0,gridSize,1)#moves all squares to the topmost empty square

    #combines like squares
    for i in range(gridSize):
        for j in range(gridSize-1):
            if (gameGrid[j][i]!=0 and gameGrid[j][i]==gameGrid[j+1][i]):
                gameGrid[j][i]+=(gameGrid[j][i])
                gameGrid[j+1][i]=0
                tempScore += gameGrid[j][i]
                isLegal = True

    moveUpOrDown(0,gridSize,1)

    if (isLegal==True):
        addsNewSquare()
        updateCellsAndScore()
        isGameOver()
    else:
        messagebox.showerror("", "invalid move try again")
    return

def down(e):
    """Codes the movement of the squares when the up arrow is pressed"""
    global tempScore, gridSize, cells, gameGrid

    isLegal = moveUpOrDown(gridSize-1,-1,-1)#moves all squares to the bottommost empty square

    #combines like squares
    for i in range(gridSize):
        for j in range(gridSize-1,0,-1):
            if (gameGrid[j][i]!=0 and gameGrid[j][i]==gameGrid[j-1][i]):
                gameGrid[j][i]+=gameGrid[j][i]
                gameGrid[j-1][i]=0
                tempScore += gameGrid[j][i]
                isLegal = True

    moveUpOrDown(gridSize-1,-1,-1)

    if (isLegal==True):
        addsNewSquare()
        updateCellsAndScore()
        isGameOver()
    else:
        messagebox.showerror("", "invalid move try again")
    return
#####################################################################################################

############## code checking when to end game or move onto the next stage ###########################
def canMove():
    canMoveHorizontally = False
    canMoveVertically = False
    for i in range(gridSize):
        for j in range(gridSize-1):
            if (gameGrid[i][j]==gameGrid[i][j+1]): canMoveHorizontally = True
            elif (gameGrid[j][i]==gameGrid[j+1][i]): canMoveVertically = True
    return canMoveVertically, canMoveHorizontally

def isGameOver():
    #def update():gameOverLabel.configure(text="", bg=colours[0])

    global level, window, score, gameGrid, min, sec
    empty = False # checks if there are any spaces in the grid
    winValue = False

    #initialises the game over variables
    #gameOverFrame = Frame(gameWindow)
    #gameOverFrame.place(relx=0.5,rely=0.5, anchor="center")

    for i in range(gridSize):
        for j in range(gridSize):
            if (gameGrid[i][j]==0): empty = True # checks for zeros
            elif (gameGrid[i][j]==2**(level+3)): winValue = True #checks if the user has completed the current level

    if (empty==False):
        v , h = canMove()
        # game is over if grid is full or 
        if (v==False and h==False):
            messagebox.showinfo("", "Grid is full, Game Over")
            window.destroy()
            updateLeaderboard()
            gameOver()# calls display leaderboard method
            gameGrid=[[0]*gridSize for i in range(gridSize)] #resets grid to zeros
            #adds the starting 2's 
            for i in range(2):
                row=random.randint(0,gridSize-1)
                col=random.randint(0,gridSize-1)
                while(gameGrid[row][col]!=0): # ensures the same square isn't chosen twice
                    row =random.randint(0,gridSize-1)
                    col =random.randint(0,gridSize-1)
                gameGrid[row][col]=2
            min =0
            sec=0
            #saves progress if username entered
            if (pName!="guest"):saveGame()

    elif (winValue ==True):
        score=tempScore # doesn't overwrite score until you've moved to the next level
        if (level<10): 
            nextStep = messagebox.showinfo("", "You have moved onto level "+str(level)+"\nNew Goal "+str(2**(level+4)))
            min = 0
            sec =0
        level+=1
        if (level>3 and level<10):
            myFrame.destroy()
            createFrame()
            configureGrid(None)

            #initialise()
            window.bind("<Left>", left)
            window.bind("<Right>", right)
            window.bind("<Up>", up)
            window.bind("<Down>", down)
            window.bind("<space>", bossKey)
            window.focus_set()
            window.mainloop()
            updateLeaderboard()
            if (pName!="guest"): saveGame()
        if(level==10): nextStep = messagebox.showinfo("", "You have Won!!")

    elif ( (sec>=30 and level<4) or (min>=(level-3) and level>3)):
            messagebox.showinfo("", "Game Over, Time Up ") #pop up game over message
            window.destroy()
            updateLeaderboard()
            gameOver()# calls display leaderboard method
            gameGrid=[[0]*gridSize for i in range(gridSize)] #resets grid to zeros 
            #saves progress if username entered
            #adds the starting 2's 
            for i in range(2):
                row=random.randint(0,gridSize-1)
                col=random.randint(0,gridSize-1)
                while(gameGrid[row][col]!=0): # ensures the same square isn't chosen twice
                    row =random.randint(0,gridSize-1)
                    col =random.randint(0,gridSize-1)
                gameGrid[row][col]=2
            min=0
            sec=0
            if (pName!="guest"):saveGame()
    return
########################################################################################################

################ functions determine whether to load saved game or start a new one #####################
def guestInit():
    global level, score, tempScore, sec, min, pause
    level = 1
    score = 0
    tempScore=0
    sec =0
    min =0
    pause =False
    
def searchForPlayer():
    global level, score, tempScore, flag, min, sec
    flag=False
    f = open("savedGames.txt", "r")
    for l in f:
        line = l.split(",")
        if (line[0]==str(pName).lower()):
            score =int(line[1])
            tempScore=int(line[1])
            level = int(line[2])
            gameGridStr = line[3]
            min = int(line[4])
            sec = int(line[5])
            flag=True
            return gameGridStr
    f.close
    return 


################################################## main ################################################

#calls the method that makes the menu 
pName = mainMenu()

window=Tk() # main game window
initializeWindow() #configures the window

# instantiates variables that will be used in many funtionsas global to avoid having multiple returns

if (pName==None): window.destroy()

elif (pName!="guest"):
    ggstr=searchForPlayer()#search the saved games list for player name 
    if (flag ==False): 
        guestInit()
        messagebox.showerror("","No game history found") #i.e player hasn't played before
        configureGrid(None)
        updateCellsAndScore()
    else:
        pause =False
        configureGrid(ggstr)
        updateCellsAndScore()
        flag=False#sets flag back to false so it doesn't affect the rest of the game

else:
    flag=False 
    guestInit()
    configureGrid(None)

#allows keys pressed while in the window to call methods that do something in response to the key pressed
if (pName!=None):
    window.bind("<Left>", left)
    window.bind("<Right>", right)
    window.bind("<Up>", up)
    window.bind("<Down>", down)
    window.bind("<space>", bossKey)
    window.focus_set()
    window.mainloop()

    ############ the exiting of main loop indicates user wishes to end game so progress is saved
    if (level<=3):
        updateLeaderboard() # unknown users will still appear on the leaderboard as guest 
        if pName!="guest": saveGame()