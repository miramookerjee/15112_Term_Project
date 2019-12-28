#show results from searching for Non-CMU foods

from tkinter import *
import showNonCMUNutInfo

class Food(object):
    def __init__(self, food, pos):
        self.food = food
        self.pos = pos
        self.scroll = 0
        
    def draw(self, canvas, data):
        x = data.width // 2
        scale = 100
        y = scale * (self.pos + 1) 
        hW = 325 #half width is 325 pixels
        hH = 20 #half height is 20 pixels
        self.lB = x - hW #left bound
        self.rB = x + hW #right bound
        self.tB = y - hH + self.scroll #top bound
        self.bB = y + hH + self.scroll #bottom bound
        canvas.create_rectangle(self.lB, self.tB, 
                            self.rB, self.bB, fill='turquoise3')
        canvas.create_text(x, y + self.scroll, text=self.food)
        
    def clicked(self, x, y):
        return x > self.lB and x < self.rB and y > self.tB and y < self.bB
        

def getFoodObjects(foodDict):
    #get list of instances of Food
    foodText = list(foodDict.keys()) #list of strings of foods
    foodObjects = [ ]
    for i in range(len(foodText)):
        item = foodText[i]
        foodObjects.append(Food(item, i))
    return foodObjects
    
def readFile(path):
    #from cs.cmu.edu/~112/
    with open(path, "rt") as f:
        return f.read()
        
####################################
# customize these functions 
####################################

def init(data):
    # load data.xyz as appropriate
    data.foodObjects = getFoodObjects(data.foodDict)
    data.scrollY = 0
    
def mousePressed(event, data):
    # use event.x and event.y
    for foodItem in data.foodObjects:
        if foodItem.clicked(event.x, event.y):
            food = foodItem.food
            nutrition = data.foodDict[food]
            showNonCMUNutInfo.run(data.user, food, nutrition)

def keyPressed(event, data):
    # use event.char and event.keysym
    speed = 30
    if event.keysym == 'Down':
        for item in data.foodObjects:
            item.scroll -= speed  
    elif event.keysym == 'Up':
        for item in data.foodObjects:
            item.scroll += speed  

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill='plum1')
    if data.foodObjects == []:
        canvas.create_text(data.width//2, data.height//2, 
                                    text='No results match your search! :(')
    for foodItem in data.foodObjects:
        foodItem.draw(canvas, data)

####################################
# use the run function as-is from cs.cmu.edu/~112/
####################################

def run(user, foodDict, width=800, height=800):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.user = user
    data.foodDict = foodDict
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")