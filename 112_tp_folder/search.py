# search for foods that are not CMU affiliated, add to meal log if desired

from tkinter import *
import tkinter.messagebox as tm
from PIL import Image, ImageTk
import requests, os
import showSearchResults

####################################
# customize these functions
####################################
    
def init(data):
    # load data.xyz as appropriate
    data.searchImage = createImage('search.png', data.width // 4)
    data.searchButton = SearchButton(data)
    data.search = False

def mousePressed(event, data):
    # use event.x and event.y
    if data.searchButton.clicked(event.x, event.y):
        data.search = True
    
def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill='plum1')
    text = 'Click the button below to search nutrition facts for non-CMU foods!'
    canvas.create_text(data.width//2, data.height//4, text=text, font='Arial 20')
    data.searchButton.draw(canvas)
    if data.search:
        data.searchWidget = EntrySearch(canvas, data)
        data.search = False

def readFile(path):
    #from http://www.cs.cmu.edu/~112/notes/notes-strings.html
    with open(path, "rt", encoding = "ISO-8859-1") as f:
        return f.read()

def extractData():
    #extract NDB no. (identifier) and food name, put into list
    contents = readFile('/Users/miramookerjee/Downloads/112tpTechDemos/FOOD_DES.txt')
    result = []
    for line in contents.splitlines():
        ndb = line[1:6]  #identifier
        for i in range(len(line)):
            begin = i
            if line[i].isupper():
                #we have found the food in the line!
                end = i + 1
                while line[end] != '~':
                    end += 1
                food = line[begin:end] 
                result.append([ndb, food])
                break
    return result

def getIdentifier(input):
    result = [ ]
    #get nbd no identifier of apple
    data = extractData()
    for foodItem in data:
        food = foodItem[1]
        try:
            if input.lower() in food.lower():
                result.append(foodItem[0])
        except:
            pass #not a food
    return result

#API Source: https://ndb.nal.usda.gov/ndb/nutrients/index
#https://technologyadvice.com/blog/information-technology/how-to-use-an-api/ taught me how to use  API
def potentialResults(input):
    options = getIdentifier(input)
    result = [ ]
    for identifier in options:
        response = requests.get('https://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=2SBgtmJ9TUYlHdqFnYOrSOXXHHu8M048uPnR0s8F&nutrients=205&nutrients=204&nutrients=208&nutrients=269&ndbno=' + identifier)

        nutrition = response.json()
        result.append(nutrition)
    return result
 
def giveNutFacts(nutrition):  
    #creates dictionary mapping foods to nutrition facts 
    result = { }
    for food in nutrition:
        name = food['report']['foods'][0]['name']   
        nutritionFacts = food['report']['foods'][0]['nutrients']
        nFactsList = [ ] #list of nutrition facts for food
        for i in range(len(nutritionFacts)):
            typeOfNutrient = getNutrient(i)
            amount = nutritionFacts[i]['value'] + nutritionFacts[i]['unit']
            nFactsList.append(['%s:  %s' % (typeOfNutrient, amount)])
        result[name] = nFactsList
    return result
    
def getNutrient(i):
    #uses index to determinew what nutrient is being measured
    if i == 0: return 'Calories'
    elif i == 1: return 'Sugar'
    elif i == 2: return 'Fat'
    elif i == 3: return 'Carbs'
    
def getFoodsBySearch(input):
    #get foods containing search input from USDA API; main function
    nutrition = potentialResults(input)
    return(giveNutFacts(nutrition))

def createImage(path, size):
    #create image to store in data
    image = Image.open(path)
    image = image.resize((size, size), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image
    
class SearchButton(object):
    #user clicks to search
    def __init__(self, data):
        self.data = data
        self.x = data.width // 2
        self.y = data.height // 2
        self.size = data.width // 4
        r = self.size // 2 #'radius' of square
        self.leftBound = self.x - r
        self.rightBound = self.x + r
        self.topBound = self.y - r
        self.botBound = self.y + r
        
    def draw(self, canvas):
        lB = self.leftBound
        rB = self.rightBound
        tB = self.topBound
        bB = self.botBound
        canvas.create_rectangle(lB, tB, rB, bB, fill='turquoise3')
        canvas.create_image(self.x, self.y, image=self.data.searchImage)
        
    def clicked(self, x, y):
        lB = self.leftBound
        rB = self.rightBound
        tB = self.topBound
        bB = self.botBound
        return x > lB and x < rB and y > tB and y < bB
        
class EntrySearch(Frame):
    #create widget to search for foods
    def __init__(self, master, data):
        super().__init__(master)
        
        self.label = Label(self, text='Enter your food here!')
        self.entry = Entry(self)
        
        self.label.grid(row=0, sticky=E)
        self.entry.grid(row=0, column=1)
        
        self.master = master
        self.data = data
        
        self.button = Button(self, text='Search!', command = self.search)
        self.button.grid(columnspan=2)
        
        self.pack()
        
    def search(self):
        entry = self.entry.get()
        foodDict = getFoodsBySearch(entry)
        showSearchResults.run(self.data.user, foodDict)
        

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
