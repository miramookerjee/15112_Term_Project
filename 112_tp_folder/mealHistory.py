# User can input date and get meal history

from tkinter import *
import ast
import datetime
import tkinter.messagebox as tm
import showInfoPage
###################################
#read and write files: functions from cs.cmu.edu/~112/
###################################

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.shown = False #entry widget not yet shown

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    #draw on canvas
    if not data.shown:
        InputDate(canvas, data)
        data.shown = True
    
    
def getInfoToRemove(user):
    #gets information to remove in order to isolate food dictionary
    info = user.split(',')
    infoToRemove = info[:7]
    infoToRemove = ','.join(infoToRemove) + ','
    return infoToRemove
    
def getMeals(user):
    #get meals as written in text file
    user = findUser(user)
    infoToRemove = getInfoToRemove(user)
    end = user.find('}') #find end of dictionary
    foodDict = ast.literal_eval(user[len(infoToRemove):end+1])
    foodDict = updateMealDict(foodDict)
    return foodDict
    
def updateMealDict(meals):
    #takes in meal dictionary and updates missing days
    days = meals.keys()
    maxDay = None
    for date in days:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        date = datetime.date(year, month, day)
        if maxDay == None or date - maxDay > datetime.timedelta(0):
            maxDay = date #finding most recent date in dictionary
    today = datetime.date.today()
    daysToAdd = (today - maxDay).days + 1
    for delta in range (1, daysToAdd):
        dayToAdd = str(maxDay + datetime.timedelta(delta))
        meals[dayToAdd] = [ ] #no recorded info on added date
    return meals
    
def findUser(user):
    #find user in userInfo file
    f =  readFile('userInfo')
    users = f.splitlines()
    for i in range(len(users)):
        curUser = users[i].split(',')
        curUsername = curUser[0]
        curPassword = curUser[1]
        if user.username == curUsername and user.password == curPassword:
            return users[i]
    
class InputDate(Frame):
    #input date to see what you ate on that date
    def __init__(self, master, data):
        super().__init__(master)
        self.labelY = Label(self, text="Year (YYYY)")
        self.labelM = Label(self, text="Month (MM)")
        self.labelD = Label(self, text="Day (DD)")
        self.labelText = Label(self, text='Enter a date to see what you ate on that day!')
        
        self.entryY = Entry(self)
        self.entryM = Entry(self)
        self.entryD = Entry(self)
        self.button = Button(self, text='Continue', command = self.showInfo)
        
        self.labelText.grid(row=0, sticky=W)
        self.labelY.grid(row=1, sticky=E)
        self.labelM.grid(row=2, sticky=E)
        self.labelD.grid(row=3, sticky=E)
    
        self.entryY.grid(row=1, column=1)
        self.entryM.grid(row=2, column=1)
        self.entryD.grid(row=3, column=1)
        self.button.grid(row=4, column=1)
            
        self.master = master
        self.data = data
        
        self.pack()
        
    def showInfo(self):
        #shows meal information from that date
        meals = getMeals(self.data.user)
        date = getDate(self.entryY.get(), self.entryM.get(), self.entryD.get())
        try:
            food = meals[date]
        except:
            tm.showerror(title='Oops! :(', message='No recorded information on this date!')
        showInfoPage.run(food)
        
def getDate(year, month, day):
    #get date based on user entry
    year = int(year)
    month = int(month)
    day = int(day)
    date = datetime.date(year, month, day)
    return str(date)
        
####################################
# use the run function as-is
####################################

def run(user, width=800, height=800):
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
    