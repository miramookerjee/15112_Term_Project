# Updated Animation Starter Code

from tkinter import *
import tkinter.messagebox as tm
from PIL import Image, ImageTk

####################################
# customize these functions
####################################
def readFile(path):
    #cs.cmu.edu/~112/
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, contents):
    #cs.cmu.edu/~112/
    with open(path, "wt") as f:
        f.write(contents)
        
def createImage(path, size):
    #create image to store in data
    image = Image.open(path)
    image = image.resize((size, size), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image
    
def init(data):
    # load data.xyz as appropriate
    data.image = createImage('voice.png', 250)

def mousePressed(event, data):
    # use event.x and event.y
    if data.on.clicked(event.x, event.y):
        f = readFile('voiceMode')
        f = f + 'ON' + '\n'
        writeFile('voiceMode', f)
        tm.showinfo('Success!', 'Voice Mode On!')
    elif data.off.clicked(event.x, event.y):
        f = readFile('voiceMode')
        f = f + 'OFF' + '\n'
        writeFile('voiceMode', f)
        tm.showinfo('Success!', 'Voice Mode Off!')
def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill='gray19')
    canvas.create_text(data.width//2, data.height//5, text='VOICE MODE', font='Courier 50 bold', fill='red')
    canvas.create_image(data.width//2, data.height//2, image=data.image)
    createButtons(canvas, data)
    
def createButtons(canvas, data):
    #create buttons to turn Voice Mode on/off
    data.on = Button(data.width//4, data.height*5//6, 'ON', 'green')
    data.off = Button(data.width*3//4, data.height*5//6, 'OFF', 'red')
    data.on.draw(canvas)
    data.off.draw(canvas)
    

class Button(object):
    #button to press to turn voice mode on/off
    def __init__(self, x, y, type, color):
        self.x = x
        self.y = y
        self.w = 150
        self.h = 20
        self.type = type
        self.color = color
        
    def clicked(self, x, y):
        leftBound = self.x - self.w
        rightBound = self.x + self.w
        topBound = self.y - self.h
        botBound = self.y + self.h
        return (x > leftBound and x < rightBound and 
                                        y > topBound and y < botBound)
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.w, self.y-self.h, self.x+self.w, self.y+self.h, fill=self.color)
        canvas.create_text(self.x, self.y, text=self.type)

####################################
# use the run function as-is
####################################

def run(width=800, height=800):
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
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Toplevel()
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