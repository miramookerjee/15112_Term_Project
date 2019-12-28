#shows how much user should eat in a day, how much user has eaten, and percent
#Source for how I determined formulas: https://mybodymykitchen.com/calculate-your-macronutrients-protein-fats-carbs/
from mealHistory import *
import datetime

def weight(user):
    #return weight in kg
    return user.weight / 2.20462
    
def height(user):
    #return height in cm
    return user.height / 0.393701
    
def BMR(user):
    #calculate basal metabolic rate
    if user.sex == 'f':
        return 655 + 9.6*weight(user) + 1.8*height(user) - 4.7*user.age
    else:
        return 66 + 13.7*weight(user) + 5*height(user) - 6.8*user.age
        
def TDEE(user):
    #calculate total daily energy expenditure (# of calories to eat per day)
    if user.activity == 'low': return int(1.2*BMR(user))
    elif user.activity == 'medium': return int(1.55*BMR(user))
    elif user.activity == 'high':  return int(1.725*BMR(user))
    elif user.activity == 'athlete': return int(1.9*BMR(user))
    
def dailyProtein(user):
    #g of protein user should eat per day
    #pgp = protein in grams per pound
    if user.activity == 'low': pgp = 0.4
    elif user.activity == 'medium': pgp = 0.75
    elif user.activity == 'high': pgp = 0.8
    elif user.activity == 'athlete': pgp = 0.9
    return pgp * user.weight
    
def dailyFat(user):
    #g of fat user should eat per day
    fatPerc = 0.2 #percent of diet that is fat
    calsFromFat = fatPerc * TDEE(user)
    calsFatPerGram = 9
    return calsFromFat / calsFatPerGram
    
def dailyCarbs(user):
    #g of carbs user should eat per day
    calsProtPerGram = 4
    calsFatPerGram = 9
    calsCarbsPerGram = 4
    calsFromProt = dailyProtein(user) * calsProtPerGram
    calsFromFat = dailyFat(user) * calsFatPerGram
    calsFromCarbs =  TDEE(user) - calsFromProt - calsFromFat
    return calsFromCarbs / calsCarbsPerGram
    
def getTodayStats(user):
    meals = getMeals(user) 
    cals, carbs, protein, fat = 0, 0, 0, 0
    day = str(datetime.date.today())
    try: 
        for meal in meals[day]:
            nutrition = meal[1].split(',')
            for i in range(len(nutrition)):
                amount = nutrition[i]
                if i == 0:
                    cals += int(float((amount)))
                elif i == 1:
                    carbs += int(float(amount))
                elif i == 2:
                    protein += int(float(amount))
                elif i == 3:
                    fat += int(float(amount))
    except:
        #nothing eaten today
        return 0, 0, 0, 0
    return cals, carbs, protein, fat
    
# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions from cs.cmu.edu/~112/
####################################

def init(data):
    # load data.xyz as appropriate
    data.cals, data.carbs, data.protein, data.fat = getTodayStats(data.user)
    data.r = 175
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill = 'plum1')
    drawCals(canvas, data)
    drawCarbs(canvas, data)
    drawProtein(canvas, data)
    drawFat(canvas, data)
    
def drawCals(canvas, data):
    cx = data.width // 4
    cy =  data.height // 4
    cals = (TDEE(data.user))
    perc = int(float(data.cals/cals*100))
    color = getColor(perc)
    r = data.r
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = color)
    text= "%d CALORIES EATEN TODAY\n%d CALORIES SUGGESTED PER DAY\n%d %% OF SUGGESTED VALUE EATEN" % (data.cals, cals, perc)
    canvas.create_text(cx, cy, text=text, font='Arial 16 bold', fill = 'black')
    
def drawCarbs(canvas, data):
    cx = data.width * 3  // 4
    cy = data.height // 4
    carbs = dailyCarbs(data.user)
    perc = int(float(data.carbs/carbs*100))
    color = getColor(perc)
    r = data.r
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = color)
    text= "%d g CARBS EATEN TODAY\n%d g CARBS SUGGESTED PER DAY\n%d %% OF SUGGESTED VALUE EATEN" % (data.carbs, carbs, perc)
    canvas.create_text(cx, cy, text=text, font='Arial 16 bold', fill = 'black')
    
def drawProtein(canvas, data):
    cx = data.width // 4
    cy = data.height * 3 // 4
    protein = dailyProtein(data.user)
    perc = int(float(data.protein/protein*100))
    color = getColor(perc)
    r = data.r
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = color)
    text= "%d g PROTEIN EATEN TODAY\n%d g PROTEIN SUGGESTED PER DAY\n%d %% OF SUGGESTED VALUE EATEN" % (data.protein, protein, perc)
    canvas.create_text(cx, cy, text=text, font='Arial 16 bold', fill = 'black')
    
def drawFat(canvas, data):
    cx =  data.width * 3 // 4
    cy = data.height  * 3 // 4
    fat = dailyFat(data.user)
    perc = int((float(data.fat/fat*100)))
    color = getColor(perc)
    r = data.r
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = color)
    text= "%d g FATS EATEN TODAY\n%d g FATS SUGGESTED PER DAY\n%d %% OF SUGGESTED VALUE EATEN" % (data.fat, fat, perc)
    canvas.create_text(cx, cy, text=text, font='Arial 16 bold', fill = 'black')
    
def getColor(perc):
    #get color based on percent of daily value eaten
    if perc < 50:
        return 'green'
    elif perc < 100:
        return 'yellow'
    elif perc > 100:
        return 'red'
    
def getTodayStats(user):
    meals = getMeals(user)
    date = str(datetime.date.today())
    try:
        todayMeals = meals[date]
    except: #no meals recorded for today
        return 0, 0, 0, 0
    mealList= [ ]
    cals = 0
    carbs = 0
    protein = 0
    fat = 0
    for meal in todayMeals:
        nutrition = meal[1]
        nutrition = nutrition.split(',')
        for i in range(len(nutrition)):
            amount = int(float((nutrition[i])))
            if i == 0:
                cals += amount
            elif  i == 1:
                carbs += amount
            elif i == 2:
                protein += amount
            elif i == 3:
                fat += amount
    return (cals, carbs, protein, fat)
    
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

