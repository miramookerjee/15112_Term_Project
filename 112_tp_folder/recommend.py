#algorithm for recommending foods to user
from userStats import *
from collections import Counter
import json
import ast
#############################################
#unhealthy foods removed from dictionary

def mainDict():
    return  {'Breakfast': breakfastDict(), 
            'Lunch': lunchDict(),
            'Dinner': dinnerDict(),
            'Late Night': lateNightDict()}
            
def breakfastDict():
    return      {"Tazza D' Oro": tazzaDict(),
                "Schatz Breakfast": schatzBfastDict(),
                "The Underground": ugDict(),
                "The Exchange": exchangeDict()}
                
def lunchDict():
    return   {"Tazza D' Oro": tazzaDict(),
             "El Gallo de Oro": galloDict(),
             "Pomegranate": pomegranateDict(),
             "Underground": ugDict(),
             "The Exchange": exchangeDict(),
             "Nakama Express": nakamaDict(),
             "Taste of India": indiaDict()}
             
def dinnerDict():
    return  {"Tazza D' Oro": tazzaDict(),
             "El Gallo de Oro": galloDict(),
             "Pomegranate": pomegranateDict(),
             "Underground": ugDict(),
             "The Exchange": exchangeDict(),
             "Nakama Express": nakamaDict(),
             "Taste of India": indiaDict()}
             
def lateNightDict(): 
    return   {"Tazza D' Oro": tazzaDict(),
             "El Gallo de Oro": galloDict(),
             "Pomegranate": pomegranateDict(),
             "Underground": ugDict(),
             "The Exchange": exchangeDict(),
             "Nakama Express": nakamaDict(),
             "Taste of India": indiaDict()}
             
def tazzaDict():
    return {'Bakery Items': tazzaBakery(),
            'Salads': tazzaSalads(),
            'Sandwiches/Wraps': tazzaSandwiches(),
            "Grab 'n' Go Items": tazzaGrabNGo()}
    
def tazzaBakery():
    #food item: calories (cal), carbs (g), proteins (g), fat (g)
    #this is the structure for all
    return {'Blueberry Muffin': '440,57,5,21',
            'Cranberry Scone':'500,71,5,23',
            'Raisin Scone': '570,93,10,24',
            'Supergrain Bagel': '400,62,12,10'}
    
def tazzaSalads():
    return {'Mediterranean Salad': '600,25,31,44',
            'Side Salad': '140,7,7,9',
            'Side of Greens (Served with Panini': '180,10,1,14'}
    
def tazzaSandwiches():
    return {'Roasted Turkey Panini': '460,55,38,10',
            'Winter Proscuitto Panini': '430,49,29,13'}
    
def tazzaGrabNGo():
    return {'Beans and Greens Panini': '430,76,18,10',
            'Sopressata and Olive Spread Panini': '890,48,52,52',
            'Winter Kale Salad': '430,43,5,30'}
    
def schatzBfastDict():
    return {'Breakfast Entrees': schatzBfastEntrees(),
            'Breakfast Sides': schatzBfastSides()}
            
def schatzBfastEntrees():
    return {'Egg White for Omelet': '90,2,18,0',
            'Egg for Omelet': '260,2,22,17',
            'Lox and Bagels': '490,24,36,28'}
            
def fruits():
    return {'Apple': '90,25,0,0',
            'Banana': '110,27,1,0',
            'Orange': '60,15,1,0',
            'Pear': '100,28,1,0'}
    
def schatzBfastSides():
    return {'Apple': fruits()['Apple'],
            'Banana': fruits()['Banana'],
            'Orange': fruits()['Orange'],
            'Pear': fruits()['Pear'],
            'Scrambled Eggs for Breakfast Sandwich': '140,1,12,9',
            'Turkey Sausage Side': '160,0,14,12'}
    
def ugDict():
    return {'Breakfast Entrees': ugBfast(),
            'Desserts': ugDesserts(),
            'Pasta': ugPasta(),
            'Entrees': ugEntrees(),
            'Salads': ugSalads(),
            'Sandwiches/Wraps': ugSandwiches(),
            'Sides': ugSides(),
            'Soups': ugSoups(),
            'Specialties': ugSpecialties()}
            
def ugBfast():
    return {'3 Egg Omelette': '640,16,26,51',
            'Breakfast Quesadilla': '530,35,25,32',
            'Breakfast Sandwich Bagel': '520,65,29,16',
            'Breakfast Sandwich English Muffin': '350,27,23,17',
            'French Toast': '880,116,22,38',
            'PB Banana Crunch': '790,114,22,33',
            'Plain Bagel': '300,64,10,1',
            'Yogurt Parfait': '240,67,12,4'}
    
def ugDesserts():
    return {'Lime Jello': '70,17,2,0',
            'Orange Jello': '70,17,2,0',}
    
def ugPasta():
    return {'Pasta Alfredo': '670,73,14,32',
            'Pasta Marinara': '430,82,14,5'}
    
def ugEntrees():
    return {'BBQ Pulled Pork Quesadilla': '590,55,36,25',
            'Chicken Quesadilla': '480,33,39,22',
            'Mushroom Quesadilla': '420,34,13,26',
            'Vegetable Quesadilla': '400,45,15,19'}
    
def ugSalads():
    return {'Caesar Side Salad': '60,6,4,2.5',
            'Classic Caesar Salad': '120,13,7,5',
            'Crunchy Quinoa Salad': '260,35,9,11',
            'Garlic Pepper Tuna Salad': '600,48,55,18',
            'Mediterranean Cous Cous Salad': '420,54,12,17',
            'Pittsburgh Chicken Salad': '540,37,48,22',
            'Salmon Nicoise Salad': '670,49,40,32',
            'TexiCobb Salad': '760,47,67,35',
            'UG Fruit and Nut Salad': '450,50,14,25',
            'Very Veggie Wedgie': '470,24,8,39'}
    
def ugSandwiches():
    return {'Artichoke Melt': '780,93,34,34',
            'Bayou Tilapia Wrap': '990,70,43,61',
            'Black Bean Quinoa Burger': '330,56,12,7',
            'Fajita Chicken Wrap': '810,71,48,37',
            'Garden Veggie Club': '630,89,24,23',
            'Grilled Chicken Breast Sandwich': '410,33,42,11',
            'Jamaican Chicken Wrap': '690,74,49,10',
            'Reuben': '530,38,28,28',
            'Sliced Turkey Deli Sandwich': '370,38,30,12',
            'Tuna Salad Deli Sandwich': '410,34,29,18'}
    
def ugSides():
    return {'Applesauce': '80,22,0,0',
            'Chips and Salsa': '160,23,2,6',
            'Chips, Salsa, and Sour Cream': '250,25,3,16',
            'Cole Slaw': '220,14,1,18',
            'Cottage Cheese': '130,5,12,5',
            'Fruit Cup': '50,13,0,0',
            'Steamed Vegetables': '60,11,4,0.5',
            'Sweet Potato Fries Appetizer': '350,43,3,22',
            'Sweet Potato Fries Side': '190,21,1,13',
            'Veggie Container': '10,2,0,0',
            'Yogurt Parfait': ugBfast()['Yogurt Parfait']}
    
def ugSoups():
    return {'Boston Clam Chowder Soup': '380,42,12,18',
            'Broccoli Cheese Soup': '430,26,16,32'}
    
def ugSpecialties():
    return {'Blackened Salmon Fillet': '550,33,38,28',
            'Chicken Strip with Fries': '640,68,12,28',
            'Cuban Sandwich': '620,54,40,28'}
    
def exchangeDict():
    return {'Sandwiches/Wraps': exchangeSandwiches(),
            'Breakfast Sandwiches': exchangeBreakfast(),
            'Desserts': exchangeDesserts(),
            'Entrees': exchangeEntrees(),
            "Pasta": exchangePasta(),
            "Salads": exchangeSalads(),
            "Soups": exchangeSoups()}
            
def exchangeSandwiches():
    return {"Bacon Lettuce Tomato Sandwich":"230,26,12,8",
            "Bacon Lettuce Tomato Sandwich with Cheese": "400,27,22,23",
            "Buffalo Chicken Wrap": "480,41,34,21",
            "Cajun Turkey Sandwich": "400,28,34,17",
            "Chicken Salad Sandwich": "470,27,37,24",
            "Classic Italian": '1070,164,54,19',
            "Corned Beef Sandwich": "430,27,33,22",
            "Egg Salad Sandwich": "440,28,25,25",
            "Free Market": '560,35,39,29',
            "Grilled Cheese": "430,31,21,25",
            "Ham Sandwiches": "400,29,30,18",
            "Roast Beef Sandwich": "430,27,36,19",
            "Southwest Chicken Wrap": "490,56,26,18",
            "Taste Sensation": "430,40,32,15",
            "Tuna Salad Sandwich": "410,28,33,19",
            "Turkey Sandwich": "400,27,33,17",
            "Vegetable Wrap": "300,52,10,7",
            "Wall Street": "560,28,30,37"}
    
def exchangeBreakfast():
    return {"Bagel Egg Sandwich": "440,46,22,18",
            "Croissant Egg Sandwich": "490,33,19,31",
            "English Muffin Egg Sandwich": "340,27,18,17",
            "Marble Toast Egg Sandwich": "270,13,16,17",
            "Wheat Toast Egg Sandwich": "290,15,18,18",
            "White Toast Egg Sandwich": "290,15,16,18"}
    
def exchangeDesserts():
    return {"Brownie": "220,36,4,8",
            "Chocolate Chip Cookie": "180,26,2,9"}
    
def exchangeEntrees():
    return {"Baked Chicken and Pierogies": "570,23,43,32",
            "Beef Stroganoff": "370,28,33,13",
            "Build a  Burger": "580,22,48,32",
            "Chicken Cacciatore with Buttered Egg Noodles": "330,26,32,9",
            "Chicken Gorgonzola with Orzo": "450,35,39,15",
            "Chicken Stir Fry with Fried Rice": "490,42,32,20",
            "English Cod with Tomato Sauce": "190,6,33,2.5",
            "Mac and Cheese": "410,30,16,24",
            "Meatloaf": "370,8,32,21",
            "Rosemary Crusted Pork": "170,1,26,6",
            "Sauerkraut and Kielbasa": "210,6,6,18",
            "Seafood  and Andouille Jambalaya w/ Cajun Rice": "320,21,29,13",
            "Stuffed Turkey Breast": "400,35,28,16",
            "Swedish Meatballs": "320,5,30,19",
            "Tomato Crusted Cod": "190,7,34,2.5",
            "Turkey a la King with Rice Pilaf": "330,19,29,13"}
    
def exchangePasta():
    return {"Baked Chicken and Pierogies": "57,23,43,32",
            "Beef Stroganoff": "370,28,33,13",
            "Buttered Egg Noodles": "150,24,5,3.5",
            "Chicken Cacciatore with Buttered Egg Noodles": "330,26,32,9",
            "Chicken Gorgonzola with Orzo": "450,35,39,15",
            "Mac and Cheese": "410,30,16,24",
            "Parmesan Noodles": "160,24,6,4",
            "Pesto Orzo with Veggies": "150,28,5,2"}
            
def exchangeSalads():
    return {"Bulgar Wheat Kale Salad": "280,30,6,16",
            "Cucumber Feta Olive Salad": "260,8,2,25",
            "Small Chicken Salad": "120,0,15,6",
            "Small Egg Salad": "90,1,6,6",
            "Small Tuna Salad":"70,1,12,1.5"}
            
def exchangeSoups():
    return {"Beef Barley Soup Large": "110,19,6,0.5",
            "Beef Barley Soup Small": "70,13,4,0",
            "Beef Chili Large": "440,11,44,23",
            "Beef Chili Small": "290,7,29,16",
            "Broccoli Cheddar Soup Large": "360,9,21,28",
            "Broccoli Cheddar Soup Small": "240,6,14,19",
            "Chicken Noodle Soup Large": "100,11,7,1",
            "Chicken Noodle Soup Small": "60,8,5,0.5",
            "Cream of Chicken and Rice Large": "190,17,8,9",
            "Cream of Chicken and Rice Small": "130,11,5,6",
            "Hearty Potato Bacon Chowder Large": "120,16,5,3.5",
            "Hearty Potato Bacon Chowder Small": "80,11,3,2",
            "Italian Wedding Soup Large": "110,7,12,3.5",
            "Italian Wedding Soup Small": "80,5,8,2.5",
            "Minestrone Soup Large": "270,10,11,20",
            "Minestrone Soup Small": "180,7,7,14",
            "Mushroom Bisque Large": "120,10,4,9",
            "Mushroom Bisque Small": "80,7,2,6",
            "New England Clam Chowder Large": "230,18,9,14",
            "New England Clam Chowder Small": "160,12,6,9",
            "Roasted Corn and Black Bean Soup Large": "130,21,6,4",
            "Roasted Corn and Black Bean Soup Small": "90,14,4,2.5",
            "Roasted Red Pepper Soup Large": "100,18,5,3.5",
            "Roasted Red Pepper Soup Small": "70,12,3,2.5",
            "Seafood Chowder Large": "310,17,25,14",
            "Seafood Chowder Small": "210,11,17,9",
            "Tomato Soup Large": "140,29,2,2.5",
            "Tomato Soup Small": "90,19,2,1.5"}
    
def galloDict():
    return {"Entrees": galloEntree(),
            "Sides": galloSides()}
    
def galloEntree():
    return {"Barbacoa Burrito Bowl": "510,55,44,12",
            "Hard Tacos": "120,24,3,1.5",
            "Pork Burrito Bowl": "320,36,26,8",
            "Quesadilla": "350,44,14,14",
            "Soft Tacos": "300,48,9,8",
            "Vegetarian Burrito Bowl": "340,49,22,7"}
    
def galloSides():
    return {"Black Beans": "150,27,10,0.5",
            "Broccoli": "20,4,1,0",
            "Brown Rice": "90,17,2,2",
            "Chickpea Salad": "110,18,5,2",
            "Cilantro-Lime White Rice": "100,20,2,1.5",
            "Cucumber Salad": "15,3,1,0",
            "Eggplant Salad": "60,8,1,3",
            "Pinto Beans": "160,30,10,1",
            "Two Bean Salad": "80,13,2,2"}
    
def pomegranateDict():
    return {'Entrees': pomEntree(),
            "Sandwiches/Wraps": pomSand(),
            "Sides": pomSides()}
            
def pomEntree():
    return {"Beef and Lamb Kabob": "1330,51,113,71",
            "Grilled Chicken": "250,1,35,11",
            "Majadra": "320,70,9,0",
            "Spaghetti with Herb Meatballs": "1020,141,45,29"}
    
def pomSand():
    return {"Chicken Shnitzel Sandwich": "720,85,54,17",
            "Falafel Sandwich": "490,76,17,14",
            "Grilled Chicken Shishlik Sandwich": "600,55,40,25",
            "Shwarma Sandwich": "630,55,38,29",
            "Tuna Salad Wrap": "430,46,25,15"}
    
def pomSides():
    return {"Babaganoush Large": "90,9,2,5",
            "Babaganoush Small": "50,5,1,3",
            "Grape Leaves Large": "180,30,4,6",
            "Grape Leaves Small": "60,10,1,2",
            "Hummus and Tahini Large": "240,14,6,19",
            "Hummus and Tahini Small": "240,14,6,19",
            "Israeli Salad Large": "45,5,2,3",
            "Israeli Salad Small": "25,2,1,1.5",
            "Pita Bread": "230,47,8,1"}
    
def nakamaDict():
    return {'Entrees': nakamaEntree(),
            'Sushi': nakamaSushi(),
            'Sides': nakamaSides(),
            'Noodle Bowl Entrees': nakamaNoodle()}
            
def nakamaEntree():
    return {"Marinated Shrimp for Yaki Soba": "160,3,27,3.5",
            "Marinated Tofu": "90,2,5,7",
            "Spicy Ground Pork":"310,6,25,20",
            "Steamed Shrimp": "130,2,26,2",
            "Yaki Soba, Marinaded Chicken Thighs": "35,5,1,1"}
    
def nakamaSushi():
    return {"Avocado and Cucumber Roll": "400,78,6,7",
            "California Roll": "290,55,5,4.5",
            "California and Cucumber Roll": "430,79,8,9",
            "Pittsburgh Pens Roll": "530,67,17,20",
            "Rainbow Roll": "380,69,12,5",
            "Red Dragon Roll": "510,74,16,15",
            "Salmon and Avocado Roll": "480,76,16,12",
            "Spicy Crab Salad Roll": "530,60,10,27",
            "Spicy Tuna Roll": "380,51,11,14",
            "Spicy Tuna and California Roll": "620,78,14,27",
            "Veggie Combo": "480,79,13,12",
            "Veggie Roll": "320,53,9,6",
            "Boston and Salmon Roll": "540,75,17,19",
            "Spicy California and Boston Roll": "290,24,9,18"}
    
def nakamaSides():
    return {"Seaweed Salad": "300,45,8,15",
            "Spicy Chicken Egg Roll": "320,46,17,7",
            "Vegetable Egg Roll": "290,43,8,9",
            "Sesame Thai Noodles": "160,21,4,7"}
    
def nakamaNoodle():
    return {"Bangkok Curry Bowl": "1000,146,29,33",
            "Marinated Shrimp for Yaki Soba": "160,3,27,3.5",
            "Marinated Tofu": "90,2,5,7",
            "Spicy Ground Pork":"310,6,25,20",
            "Steamed Shrimp": "130,2,26,2",
            "Yaki Soba, Marinaded Chicken Thighs": "35,5,1,1"}
    
def indiaDict():
    return {"Beverages": indiaBev(),
            "Entrees": indiaEntree()}
            
def indiaBev():
    return {"Mango Juice": "220,57,0,0",
            "Mango Lassi": "390,61,12,12"}
    
def indiaEntree():
    return {"Alu Baingan": "120,28,4,1",
            "Alu Carrot": "90,22,2,0",
            "Alu Ghobi": "80,18,3,0",
            "Alu Matar": "110,17,4,3.5",
            "Alu Matar Mushroom": "90,12,3,3.5",
            "Alu Palak": "130,17,3,6",
            "Alu Tomato": "110,26,3,0",
            "Alu Zucchini": "80,17,3,0",
            "Chana Masala": "130,21,6,3",
            "Chicken Biryani": "160,14,15,5",
            "Chicken Curry": "290,5,38,13",
            "Chicken Tikka Masala": "330,4,38,18",
            "Kheer": "110,16,4,3.5",
            "Matar Paneer": "150,13,7,8",
            "Navratan": "70,9,2,3",
            "Palak Paneer": "170,13,6,11",
            "Peas Pilav": "150,32,3,0.5",
            "Tandoori Chicken": "200,4,28,7"}
#############################################
    
def getAllNutrition(dct, result = [ ]):
    #get recommendation score based off of nutrition: recursive function
    for key in dct:
        try: 
            val = dct[key]
            getAllNutrition(val)
        except:
            result.append(val)
    return result
            
def getNutritionScore(user):
    result = [ ]
    nutritionList = getAllNutrition(mainDict())
    userCals, userCarbs, userProtein, userFat = getTodayStats(user)
    for nutrition in nutritionList:
        path = findCategoryPath(mainDict(), nutrition)
        nutrition = nutrition.split(',')
        for i in range(len(nutrition)):
            value = float(nutrition[i])
            if i == 0:
                calsLeft = userCals - value
            elif i == 1:
                carbsLeft = userCarbs - value
            elif i == 2:
                proteinLeft = userProtein - value
            elif i == 3:
                fatLeft = userFat - value
        score = calsLeft + carbsLeft + proteinLeft + fatLeft
        restaurant = path[1]
        food = path[-1]
        meal = "%s from %s" % (food, restaurant)
        result.append((meal, score))
    return result
    
def findCategoryPath(d, value):
    #from hw9
    #return a list of categories that lead to item
    if type(d) == str:
        if d == value:
            return []
        else:
            return None
    else:
        for key in d:
            result = findCategoryPath(d[key], value)
            if result != None:
                return [key] + result
                
def preferencesScore(user):
    #get score based off of user preferences
    preferencesFile = readFile('userPreferences')
    users = preferencesFile.splitlines()
    for i in range(len(users)):
        person = users[i]
        username = person.split(',')[0]
        if user.username == username:
            #user found in file
            foundIndex = i
    try:
        user = users[foundIndex]
        remove = infoToRemove(user)
        removeIndex = len(remove)
        preferences = user[removeIndex:]
        preferences = (ast.literal_eval(preferences)) #string to dictionary
        return preferences
    except:
        #user not yet in file
        preferences = getEmptyPreferencesDictionary()
        return preferences
    
def getEmptyPreferencesDictionary():
    result = { }
    nutritions = getAllNutrition(mainDict())
    for nutrition in nutritions:
        path = findCategoryPath(mainDict(), nutrition)
        restaurant = path[1]
        food = path[-1]
        meal = "%s from %s" % (food, restaurant)
        result[meal] = 0
    return result
    
def infoToRemove(user):
    items = user.split(',')
    result = items[0] + ',' +  items[1] + ','
    return result
    
def totalScore(user):
    #combines nutrition score and user preference score
    result = { }
    nutritionScores = dict(getNutritionScore(user))
    prefScores = preferencesScore(user)
    scale = 1000 #scale preference score so it has a weight
    prefScores.update((next, prev*scale) for next, prev in prefScores.items())
    nutritionCounter = Counter(nutritionScores)
    preferenceCounter = Counter(prefScores)
    result = addVals(nutritionCounter, preferenceCounter)
    result = dict(result)
    return result

def addVals(dct1, dct2):
    #return new dct with values added together
    result = { }
    for key in dct1:
        val = dct1[key]
        val += dct2[key]
        result[key] = val
    return result
        
def getRecommendations(user):
    scores = totalScore(user)
    max1 = None
    max2 = None
    max3 = None
    max1Meal = None
    max2Meal = None
    max3Meal = None
    for meal in scores:
        score = scores[meal]
        if max1 == None or score > max1:
            max1 = score
            max1Meal = meal
        elif max2 == None or score > max2:
            max2 = score
            max2Meal = meal
        elif max3 == None or score > max3:
            max3 = score
            max3Meal = meal
    return max1Meal, max2Meal, max3Meal
    
def readFile(path):
    #from cs.cmu.edu/~112/
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, contents):
    #from cs.cmu.edu/~112/
    with open(path, "wt") as f:
        f.write(contents)
        
from tkinter import *

####################################
# customize these functions from cs.cmu,edu/~112/
####################################

def init(data):
    # load data.xyz as appropriate
    data.recommendations = getRecommendations(data.user)
    data.recObjects = [ ]
    for i in range(len(data.recommendations)):
        name =  data.recommendations[i]
        recommendation = Recommendation(i, data, name)
        data.recObjects.append(recommendation)
    data.chosen = False

def mousePressed(event, data):
    # use event.x and event.y
    for recommendation in data.recObjects:
        if recommendation.clicked(event.x, event.y):
            data.chosen = True
            recommendation.chosen = True

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    if data.chosen:
        savePreferences(data)
        return 
        
def preferencesToSave(data):
    #save user preferences based on what they have chosen
    chosen = None
    for recommendation in data.recObjects:
        if recommendation.chosen == True:
            choice = recommendation
            chosen = recommendation.name
            data.recObjects.remove(choice)
    unchosen = [ ]
    for item in data.recObjects:
        unchosen.append(item.name)
    return chosen, unchosen
    
def savePreferences(data):
    #save user preferences in file
    user = data.user
    chosen, unchosen = preferencesToSave(data)
    prefScore = dict(preferencesScore(user))
    for key in prefScore:
        if key == chosen:
            prefScore[key] += 1
        elif key in unchosen:
            prefScore[key] -= 1
    preferencesFile = readFile('userPreferences')
    users = preferencesFile.splitlines() 
    for i in range(len(users)):
        person = users[i]
        username =  person.split(',')[0]
        if user.username == username:
            #user found in file
            foundIndex = i
    try:
        users.pop(foundIndex)
    except:
        #not in file
        pass
    newLine = "%s,%s,%s" % (user.username, user.password, prefScore)
    users.append(newLine)
    result = '\n'.join(users)
    writeFile('userPreferences', result)

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill='plum1')
    if not data.chosen:
        text = "Here's a personalized recommendation on what to eat next!"
        canvas.create_text(data.width // 2, data.height // 10, 
                                            text = text, font='Arial 15')
        for recommendation in data.recObjects:
            recommendation.draw(canvas)
    else:
        text = "Thanks for choosing!\nWe have taken your choice into account, and will\nconsider it next time you make a recommendation!"
        canvas.create_text(data.width // 2, data.height // 2, 
                                            text = text, font='Arial 20')
            
class Recommendation(object):
    
    def __init__(self, i, data, name):
        self.w = 200
        self.h = 50
        self.x = data.width // 2
        self.y = data.width * (i+1) // 4
        self.text = data.recommendations[i]
        self.chosen = False
        self.name = name
        
    def clicked(self, x, y):
        return (x > self.x - self.w and x < self.x + self.w and 
                                y > self.y - self.h and y < self.y + self.h)
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x - self.w, self.y - self.h, 
                    self.x + self.w, self.y + self.h, fill='turquoise3')
        canvas.create_text(self.x, self.y, text=self.text)
       
####################################
# use the run function as-is: from cs.cmu.edu/~112/
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