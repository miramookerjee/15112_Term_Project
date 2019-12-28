# main file ; run this file

from tkinter import *
import tkinter.messagebox as tm
import homePage as hP
import datetime

####################################
# customize these functions
####################################
def readFile(path):
    #from cs.cmu.edu/~112/
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, contents):
    #from cs.cmu.edu/~112/
    with open(path, "wt") as f:
        f.write(contents)
        
def init(data):
    # load data.xyz as appropriate
    data.backgroundColor = 'chartreuse3'
    farLeft = 1 
    midLeft = 3 
    midRight = 5 
    farRight = 7 
    screenDiv = 8
    data.loginX1 = data.width * farLeft // screenDiv
    data.loginX2 = data.width * midLeft// screenDiv
    data.createAccX1 = data.width * midRight // screenDiv
    data.createAccX2 = data.width * farRight // screenDiv
    data.y1 = data.height // 2
    data.y2 = data.height * midRight // screenDiv
    data.login = False
    data.createAcc =  False
    data.background = PhotoImage(file="veggies.gif") #from https://www.shutterstock.com/vectors?kw=vector%20stock&ds_rl=1243394&gclid=EAIaIQobChMIm4qK3NHm4QIVjY2zCh3S6gvBEAAYASAAEgKsMfD_BwE&gclsrc=aw.ds

def mousePressed(event, data):
    # use event.x and event.y
    if not data.login and not data.createAcc:
        if loginClick(event, data):
            data.login = True
        elif createAccClick(event, data):
            data.createAcc = True
        
def loginClick(event, data):
    #user clicks in log in box
    return (event.x > data.loginX1 and event.x < data.loginX2 and 
                event.y  >  data.y1 and event.y < data.y2)
    
def createAccClick(event, data):
    #user clicks in create account box
    return (event.x > data.createAccX1 and event.x < data.createAccX2 and 
                event.y  >  data.y1 and event.y < data.y2)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    if not data.login and not data.createAcc: 
        drawOpenPage(canvas, data)
    elif data.login:
        userLogin = LoginFrame(canvas, data)
        data.login = False #prevent multiple login frames
    elif data.createAcc:
        userLogin = CreateAccount(canvas, data)
        data.createAcc = False #prevent multiple CA frames

class LoginFrame(Frame):
    #inspired by https://python-textbok.readthedocs.io/en/1.0/
    #Introduction_to_GUI_Programming.html
    
    def __init__(self, master, data):
        super().__init__(master)

        self.labelU = Label(self, text="Username")
        self.labelP = Label(self, text="Password")
  
        self.entryU = Entry(self)
        self.entryP = Entry(self, show="*")

        self.labelU.grid(row=0, sticky=E)
        self.labelP.grid(row=1, sticky=E)
        self.entryU.grid(row=0, column=1)
        self.entryP.grid(row=1, column=1)
        
        self.master = master
        self.data = data
        self.button1 = Button(self, text="Login!", 
                        command=self._login_btn_clicked)
        self.button1.grid(columnspan=2)
        self.button2 = Button(self, text = 'Back', command=self.run)
        self.button2.grid(columnspan=3)

        self.pack()
        
    def run(self):
        run(800, 800, True)
        
    def _login_btn_clicked(self):
        username = self.entryU.get()
        password = self.entryP.get()
        try:
            f = readFile('userInfo')
        except:
            writeFile('userInfo', '')
            f = readFile('userInfo')
        users = f.splitlines()
        for user in users:
            user = user.split(',')
            curUsername = user[0]
            curPassword = user[1]
            if username == curUsername and password == curPassword:
                user = makeUser(user)
                hP.homePage(user)
                return
        tm.showerror('Try again!', 'User does not exist!')
        
def makeUser(user):
    #make instance of User
    for i in range(len(user)):
        if i == 0:
            username = user[i]
        elif i == 1:
            password = user[i]
        elif i == 2:
            height = user[i]
        elif i== 3:
            weight = user[i]
        elif i == 4:
            sex = user[i].lower()
        elif i  == 5:
            age = user[i]
        elif i  == 6:
            activity = user[i].lower()
    return User(username, password, height,  weight, sex, age, 
                                        activity, makeEmptyMealsDict())
    
class CreateAccount(Frame):
    def __init__(self, master, data):
        
        super().__init__(master)
        self.labelU = Label(self, text="Username")
        self.labelP = Label(self, text="Password")
        self.labelH = Label(self, text="Height (inches):")
        self.labelW = Label(self, text="Weight (pounds) ")
        self.labelS = Label(self, text = 'Sex: "F" or "M"')
        self.labelAge =  Label(self, text = 'Age:')
        text = 'Activity Level: Enter "Low", "Medium", "High", or "Athlete"'
        self.labelAct = Label(self, text = text)
        
        self.entryU = Entry(self)
        self.entryP = Entry(self, show="*")
        self.entryH = Entry(self)
        self.entryW = Entry(self)
        self.entryS = Entry(self)
        self.entryAge = Entry(self)
        self.entryAct = Entry(self)
        
        self.labelU.grid(row=0, sticky=E)
        self.labelP.grid(row=1, sticky=E)
        self.labelH.grid(row=2, sticky=E)
        self.labelW.grid(row=3, sticky=E)
        self.labelS.grid(row=4, sticky=E)
        self.labelAge.grid(row=5, sticky=E)
        self.labelAge.grid(row=5, sticky=E)
        self.labelAct.grid(row=6, sticky=E)
        
        self.entryU.grid(row=0, column=1)
        self.entryP.grid(row=1, column=1)
        self.entryH.grid(row=2, column=1)
        self.entryW.grid(row=3, column=1)
        self.entryS.grid(row=4, column=1)
        self.entryAge.grid(row=5, column=1)
        self.entryAct.grid(row=6, column=1)
        self.create = Button(self, text = 'Continue', command = self.update)
        self.back = Button(self, text = 'Back', command = self.run)
        self.create.grid(row=7, sticky=E)
        self.back.grid(row=8, sticky=E)
        
        self.master = master
        self.data = data
        
        self.pack()
        
    def run(self):
        run(800, 800, True)
        
    def update(self):
        #update file that tracks seen usernames and passwords
        print('click!')
        username = self.entryU.get()
        password = self.entryP.get()
        height = self.entryH.get()
        weight  =  self.entryW.get()
        sex = self.entryS.get()
        age = self.entryAge.get()
        activity = self.entryAct.get()
        if not isValid(height, weight, sex, age, activity):
            tm.showerror('Oops!', 'One of the fields you entered is invalid. Please try again!')
            return
        elif usernameUsed(username):
            tm.showerror('Try again!', 'User already exists!')
            return
        f = readFile('userInfo')
        #update file
        if f[-1] == '\n':
            f += (username  +  ',' + password + ',' + height + ',' + 
                    weight + ',' + sex + ',' + age + ',' +  activity + ',' + 
                                            str(makeEmptyMealsDict()) + '\n')
        else:
            f += ('\n' + username  +  ',' + password + ',' + height + ',' + 
                    weight + ',' + sex + ',' + age + ',' +  activity + ',' + 
                                            str(makeEmptyMealsDict()) + '\n')
        writeFile('userInfo', f)
        self.run()
        self.destroy()
        
def isValid(height, weight, sex, age, activity):
    #returns true if user input is valid for these fields
    h = height.isdigit()
    w = weight.isdigit()
    s = sex.lower() == 'f' or sex.lower() == 'm'
    ag = age.isdigit()
    ac = (activity.lower() == 'low' or activity.lower() == 'medium' or 
                activity.lower() == 'high' or activity.lower() == 'athlete')
    return h and w and s and ag and ac
        
def usernameUsed(username):
    #return True if username already in system
    f = readFile('userInfo')
    users = f.splitlines()
    for user in users:
        user = user.split(',')
        if username == user[0]:
            return True
            
def daterange(start_date, end_date):
    #code from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)
        
def makeEmptyMealsDict():
    #make a meals dictionary that is empty for a new user
    result = {}
    start = datetime.date(2019, 4, 1)
    today = datetime.date.today()
    #get tomorrow's date so today is included in for loop
    year = today.year
    month = today.month
    day = today.day + 1
    tomorrow = datetime.date(year, month, day) 
    for date in daterange(start, tomorrow):
        result[date.strftime("%Y-%m-%d")] = [ ]
    return result
    
class User(object):
    def __init__(self, username, password, height, weight, sex, age, activity, meals):
        self.username = username
        self.password = password 
        self.height = int(height)
        self.weight = int(weight)
        self.sex = sex
        self.age = int(age)
        self.activity = activity
        self.meals = str(makeEmptyMealsDict())
        
def drawOpenPage(canvas, data):
    #draw the first page that opens when using app
    canvas.create_image(data.width//2, data.height//2, image=data.background)
    canvas.create_text(data.width // 2, data.height // 5, 
                    text = 'Welcome to BalanceCMU!', font  = 'Courier 50 bold',
                                                    fill = 'black')
    font = 'Arial 20 bold'
    canvas.create_rectangle(data.loginX1, data.y1, data.loginX2, data.y2, 
                                                            fill = 'plum1' )
    canvas.create_text((data.loginX1 + data.loginX2) / 2, 
                        (data.y1 + data.y2) / 2,  text = 'LOG IN', font = font)
    canvas.create_rectangle(data.createAccX1, data.y1, 
                                    data.createAccX2, data.y2, fill = 'plum1' )
    canvas.create_text((data.createAccX1 + data.createAccX2) / 2, 
                (data.y1 + data.y2) / 2, text = 'CREATE ACCOUNT', font = font)


####################################
#from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################

def run(width=300, height=300, again=False):
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
    if again:
        root = Toplevel()
    else:
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

run(800, 800)
