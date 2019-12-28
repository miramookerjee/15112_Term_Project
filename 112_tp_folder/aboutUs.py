# Tells user about app

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass
    
def text1():
    result = '''Hi! Welcome to CMU Balance, a personalized app meant to help you plan out your meals and keep track of the food you consume at CMU! '''
    result = rightJustifyText(result, 50)
    return result
    
def text2():
    result = '''Use this app to see nutritional data for CMU foods, plan out your meals, see your health trajectory throughout the week, keep a log of the foods you have eaten, get recommendations on what to eat next, share what you've eaten today with your Facebook friends, and more!'''
    result = rightJustifyText(result, 50)
    return result
    
def text3():
    result = '''    
    I hope you enjoy the app! For questions, comments, or concerns, do not hesistate to reach out to my creator at mmookerj@andrew.cmu.edu :)'''
    result = rightJustifyText(result, 50)
    return result
    
def breakText(text, width):
    #from hw3, used in rightJustify
    #break text on last possible space given width constraints
    result = ''
    prevSpace = 0
    prevIndex = 0
    constraints = width
    spaces = 2 
    #one for end of line, one for beginning of line. Will be stripped later
    for i in range(len(text)):
        if text[i].isspace() or i == len(text)-1:
            if i >= constraints:
                result += text[prevIndex:prevSpace] + '\n'
                constraints = prevSpace + width + spaces
                prevIndex = prevSpace
            prevSpace = i
    result += text[prevIndex:] #last line
    return result
    
def singleSpace(text):
    #from hw3, used in rightJustify
    #turns all blocks of whitespace in a string into a single space
    result = ''
    for i in range(len(text)):
        if text[i].isspace():
            if i < len(text) - 1 and text[i+1].isspace():
                continue
            else:
                result += ' '
        else:
            result += text[i]
    return result
    
def rightJustifyText(text, width):
    #from hw3
    result = ''
    text = (breakText(singleSpace(text), width)).splitlines()
    for line in text:
        line = line.strip()
        #add extra spaces to left of line to fit width

        while len(line) < width:
            line = ' ' + line
        result += line + '\n'
    return  result

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill = 'plum1')
    x = data.width // 2
    y  = data.width // 4
    canvas.create_text(x, y, text=text1(), font = 'Arial 15')
    canvas.create_text(x, 2*y, text=text2(), font = 'Arial 15')
    canvas.create_text(x, 3*y, text=text3(), font = 'Arial 15')

####################################
# use the run function as-is from cs.cmu.edu/~112/
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
