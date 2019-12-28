#shows all options/features in app
from tkinter import *
import tkinter.messagebox as tm
import userStats
import cmuNutritionData
import trajectory
import mealHistory
import todaysMealLog
import recommend
import share
import search
import aboutUs
from PIL import Image, ImageTk
import speech_recognition as sr
import pyaudio
####################################
# customize these functions from cs.cmu.edu/~112/
#antialias line from https://stackoverflow.com/questions/4066202/resizing-pictures-in-pil-in-tkinter
####################################
def init(data):
    # load data.xyz as appropriate
    data.options = createOptions(data)
    #image sources:http://www.pngmart.com
    size = 180
    data.statsImage = createImage('StatsImage.png', size)
    data.nutDataImage = createImage('nutDataImage.png', size)
    data.trajImage = createImage('trajectory.png', size)
    data.historyImage = createImage('history.png',  size)
    data.logImage = createImage('log.png', size)
    data.recImage = createImage('rec.png', size)
    data.shareImage = createImage('share.png', size)
    data.searchImage = createImage('search.png', size)
    data.aboutImage = createImage('about.png', size)
    data.voiceImage = createImage('voice.png', data.width//12)
    data.voiceIcon = VoiceIcon(data)

def createImage(path, size):
    #create image to store in data
    image = Image.open(path)
    image = image.resize((size, size), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image
    
def mousePressed(event, data):
    # use event.x and event.y
    for option in data.options:
        if option.clicked(event.x, event.y):
            option.doOption(data)
    if data.voiceIcon.clicked(event.x, event.y):
        voiceInput = getUserVoice()
        #run feature based on voice input
        if 'stats' in voiceInput.lower():
            userStats.run(data.user)
        elif 'nutrition' in voiceInput.lower():
            cmuNutritionData.run(data.width, data.height)
        elif 'trajectory' in voiceInput.lower():
            trajectory.run(data.user)
        elif 'meal history' in voiceInput.lower():
            mealHistory.run(data.user, data.width, data.height)
        elif 'log' in voiceInput.lower():
            todaysMealLog.run(data.user, data.width, data.height)
        elif 'recommend' in voiceInput.lower():
            recommend.run(data.user)
        elif 'facebook' in voiceInput.lower():
            share.run(data.user)
        elif 'search' in voiceInput.lower():
            search.run()
        elif 'about us' in voiceInput.lower():
            aboutUs.run()
        else:
            tm.showerror('Uh Oh! :(', "I can't understand what you're saying. Could you be a bit more specific?'")
            
def keyPressed(event, data):
    # use event.char and event.keysym
    pass
        
def getUserVoice():
    #code modified from https://www.youtube.com/watch?v=K_WbsFrPUCk
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio) #convert audio into text
            return text
        except:
            tm.showerror('Uh Oh! :(', 'Could not recognize your voice, please try again!')
        

def timerFired(data):
    pass
    
def redrawAll(canvas, data):
    # draw background
    canvas.create_rectangle(0, 0, data.width, data.height, fill='plum1')
    #draw welcome
    canvas.create_text(data.width // 2, data.height // 10,
            text = 'Welcome %s!' %(data.user.username), font = 'Arial 50 bold')
    #draw options
    for option in data.options:
        option.draw(canvas)
    data.voiceIcon.draw(canvas)
    
    
def createOptions(data):
    #create 9 instances of options
    result = [ ]
    rows = 3
    cols = 3
    for row in range(rows):
        for col in range(cols):
            y = data.height * (row + 1) // 4 + 20
            x = data.width * (col + 1) // 4
            newOption = Option(x, y, row, col, data) #new instance of option
            result.append(newOption)
    return result
    
class VoiceIcon(object):
    #icon that enables voice mode
    def __init__(self, data):
        #initialize variables
        self.x = data.width // 24
        self.y = data.height - (data.height // 24)
        self.size = data.width // 12
        self.leftBound = 0
        self.rightBound = self.size
        self.topBound = data.height - self.size
        self.botBound = data.height
        self.data = data
        
    def draw(self, canvas):
        #draw voice icon
        data = self.data
        canvas.create_rectangle(self.leftBound, self.topBound, self.rightBound,
                        self.botBound, width=5, fill='red', outline='gray19')
        canvas.create_image(self.x, self.y, image=data.voiceImage)
        
    def clicked(self, x, y):
        #when voice icon is clicked
        leftBound = self.leftBound
        rightBound = self.rightBound
        topBound = self.topBound
        botBound = self.botBound
        return (x > leftBound and x < rightBound and
                                    y > topBound and y < botBound)     
class Option(object):
    #option to click on home screen
    def __init__(self, x, y, r, c, data):
        #initialize variable
        self.x = x
        self.y = y
        self.row = r
        self.col = c
        self.data = data
        
    def draw(self, canvas):
        #draw option icon
        data = self.data
        x, y, r, c = self.x, self.y, self.row, self.col
        if r == 0 and c == 0: drawYourStats(x, y, canvas, data)
        elif r == 0 and c  == 1: drawCMUNutData(x, y, canvas, data) 
        elif r == 0 and c == 2: drawTrajectory(x, y, canvas, data) 
        elif r == 1 and c == 0: drawMealHistory(x, y, canvas, data)
        elif r == 1 and c == 1: drawTodaysMealLog(x, y, canvas, data)
        elif r == 1 and c == 2: drawRecommend(x, y, canvas, data)
        elif r == 2 and c == 0: drawFacebook(x, y, canvas, data)
        elif r == 2 and c == 1: drawSearch(x, y, canvas, data) 
        elif r == 2 and c == 2: drawAboutUs(x, y, canvas, data) 
        
    def clicked(self, x, y):
        #if user clicks in this option, return True
        cx, cy, r = self.x, self.y, 90
        return x > cx - r and  x < cx + r and y > cy - r and y < cy + r
        
    def doOption(self, data):
        #user has clicked on option, open new page according to option
        r, c = self.row, self.col
        if r == 0 and c == 0: userStats.run(data.user)
        elif r == 0 and c == 1: cmuNutritionData.run(data.width, data.height)
        elif r == 0 and c == 2: trajectory.run(data.user)
        elif r == 1 and c == 0: mealHistory.run(data.user, 
                                            data.width, data.height)
        elif r == 1 and c == 1: todaysMealLog.run(data.user, 
                                                data.width, data.height)
        elif r == 1 and c == 2: recommend.run(data.user)
        elif r == 2 and c == 0: share.run(data.user)
        elif r == 2 and c == 1: search.run(data.user)
        elif r == 2 and c == 2: aboutUs.run() 
        
def drawCMUNutData(x, y, canvas, data):
    #draw CMU Nutrition Data option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.nutDataImage)
    canvas.create_text(x, y + 100, text = 'CMU Nutritional Data', 
                                font = 'Arial 12 bold', fill = 'black')
    
def drawYourStats(x, y, canvas, data):
    #draw Your Stats option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.statsImage)
    canvas.create_text(x, y + 100, text = 'Your Stats', font = 'Arial 12 bold')
    
def drawSearch(x, y, canvas, data):
    #draw Non CMU Foods Search option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.searchImage)
    canvas.create_text(x, y + 100, text = 'Search Non-CMU Foods', 
                                            font = 'Arial 12 bold')
    
def drawMealHistory(x, y, canvas, data):
    #draw Meal History option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.historyImage)
    canvas.create_text(x, y + 100, text = 'Your Meal History', 
                                            font = 'Arial 12 bold')
    
def drawTodaysMealLog(x, y, canvas, data):
    #draw Today's Meal Log option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')  
    canvas.create_image(x, y, image=data.logImage)
    canvas.create_text(x, y + 100, text = "Today's Meal Log", 
                                                font = 'Arial 12 bold')
    
def drawRecommend(x, y, canvas, data):
    #draw Recommend option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.recImage)
    canvas.create_text(x, y + 100, text = 'Food Recommendations', 
                                                font = 'Arial 12 bold')
    
def drawFacebook(x, y, canvas, data):
    #draw Facebook option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.shareImage)
    canvas.create_text(x, y + 100, text = 'Share on Facebook', 
                                            font = 'Arial 12 bold')
    
def drawTrajectory(x, y, canvas, data):
    #draw Trajectory option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.trajImage)
    canvas.create_text(x, y + 100, text = 'Your Trajectory', 
                                            font = 'Arial 12 bold')
    
def drawAboutUs(x, y, canvas, data):
    #draw About Us option icon
    canvas.create_rectangle(x - 90, y - 90, x + 90, y + 90, fill='turquoise3')
    canvas.create_image(x, y, image=data.aboutImage)
    canvas.create_text(x, y + 100, text = 'About Us', font = 'Arial 12 bold')
    
def readFile(path):
    #cs.cmu.edu/~112/
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, contents):
    #cs.cmu.edu/~112/
    with open(path, "wt") as f:
        f.write(contents)
        
####################################
# code modified from cs.cmu.edu/~112/
####################################

def run(width, height, user):
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
    data.user = user #NEW LINE HERE
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

def homePage(user):
    run(800, 800, user)
    