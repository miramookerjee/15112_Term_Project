# show the nutrition information for some food in the USDA API

from tkinter import *
import ast
import datetime
import tkinter.messagebox as tm

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
    print('NUTRITION', data.nutrition)
    data.add = AddToMealLog()
    data.meals = updateMealDict(getMeals(data))
    data.today = datetime.date.today()
    
def getMeals(data):
    #get meals as written in text file
    user = findUser(data.user)
    infoToRemove = getInfoToRemove(user)
    end = user.find('}') #find end of dictionary
    foodDict = user[len(infoToRemove):end+1]
    return ast.literal_eval(foodDict) #nicer version of eval
    
def getInfoToRemove(user):
    #gets information to remove in order to isolate food dictionary
    info = user.split(',')
    infoToRemove = info[:7]
    infoToRemove = ','.join(infoToRemove) + ','
    return infoToRemove
    
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

def mousePressed(event, data):
    # use event.x and event.y
    if data.add.clicked(event.x, event.y):
        food = data.food
        nutrition = getNutritionString(data.nutrition)
        data.meals[str(data.today)].append([food, nutrition]) #nicer version of eval
        updateUserInfo(data)
        tm.showinfo('Success! :)', 'Successfully added %s to meal log' % food) 
        init(data)
        
def getNutritionString(nutrition):
    #get nutrition string to add to user info file
    cals = 0
    carbs = 0
    protein = 0
    fat = 0
    for item in nutrition:
        item = item[0]
        nutritionList = item.split(':')
        value = nutritionList[0]
        amount = nutritionList[1]
        res = ''
        for c in amount:
            if c == '.' or c.isdigit():
                res += c
        print('RES', repr(res))
        try:
            amount = int(res)
        except:
            try:
                amount = float(res)
            except: #no data
                amount = 0
        if value == 'Calories': 
            cals += amount
        elif value == 'Carbs': 
            carbs += amount
        elif value == 'Fat':
            fat += amount
    cals = str(cals)
    carbs = str(carbs)
    protein = str(protein)
    fat = str(fat)
    result = '%s,%s,%s,%s' % (cals, carbs, protein, fat)
    return result
    
def updateUserInfo(data):
    #updates file containing user info with meal info
    f =  readFile('userInfo')
    users = f.splitlines()
    for i in range(len(users)):
        user = users[i].split(',')
        curUsername = user[0]
        curPassword = user[1]
        if (data.user.username == curUsername and 
                                    data.user.password == curPassword):
            foundUserIndex = i #we have found user in file at this index
    #remove user from file
    user = users.pop(foundUserIndex) 
    user = user.split(',')
    #remove existing food dictionary
    user =  user[:7] 
    #add new food dictionary
    user.append(str(data.meals)) 
    user = ','.join(user)
    #re-add user with modified food dictionary
    users.append(user) 
    #convert back to string
    contents = '\n'.join(users) 
    #write back into file
    writeFile('userInfo', contents) 

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill='plum1')
    if len(data.nutrition) == 0:
        text = "Sorry, no recorded information for this food!"
        canvas.create_text(data.width//2, data.height//2, text=text)
        return
    text = getText(data)
    canvas.create_text(data.width//2, data.height//2, text=text, font='Arial 20')
    data.add.draw(canvas)
    
def getText(data):
    #get text to display on screen
    result = ''
    for nutrition in data.nutrition:
        nutrition = nutrition[0]
        nutritionList = nutrition.split(':')
        value = nutritionList[0]
        amount = nutritionList[1]
        res = ''
        for c in amount:
            if c == '.' or c.isdigit() or c == 'g':
                res += c
        amount = res
        result += amount + ' ' + value + '\n'
    return result
    
class Icon(object):
    #icon on screen
    def __init__(self, x, y, size, vMarg, item, innerDict):
        self.x = x
        self.y = y
        self.size = size
        self.vMarg = vMarg
        strLen = len(item)
        self.item = item[:strLen] + '\n' + item[strLen+1:] #for text display
        self.innerDict = innerDict
               
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, 
                    self.x + self.size, self.y + self.size, 
                                            fill='turquoise3', width=5)
        strLen = len(self.item)
        canvas.create_text(self.x + self.size  // 2, 
                    self.y + self.size + self.vMarg // 2, 
                                text = self.item, font = 'Arial 10 bold')
        
    def clicked(self, x, y):
        return (x > self.x and x < self.x + self.size 
                and y > self.y and y < self.y +  self.size)
                
        
class AddToMealLog(Icon):
    #type of icon that lets you add food to plan
    def __init__(Icon):
        r = 50
        width, height = 800, 800
        super().__init__(width//2 - r, height*7//10 + r, 
                                2*r, 0, "ADD TO\nTODAY'S\nMEAL LOG", {})
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, 
                    self.x + self.size, self.y + self.size, 
                                        fill='turquoise3', width=5)
        strLen = len(self.item)
        canvas.create_text(self.x + self.size  // 2, 
                    self.y + self.size // 2, 
                                text = self.item, font = 'Arial 15 bold')
                    

####################################
# use the run function as-is
####################################

def run(user, food, nutrition, width=800, height=800):
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
    data.food = food
    data.nutrition = nutrition
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
    
