#show or add to what user has eaten today
import datetime
import copy
import math
import ast
from PIL import Image as Img
from PIL import ImageTk
import speech_recognition as sr
import pyaudio
import tkinter.messagebox as tm
###################
#Dictionaries of Data
####################
def mainDict():
    return  {'Breakfast': breakfastDict(), 
            'Lunch': lunchDict(),
            'Dinner': dinnerDict(),
            'Late Night': lateNightDict()}
            
def breakfastDict():
    return      {"Tazza D' Oro": tazzaDict(),
                "Schatz Breakfast": schatzBfastDict(),
                "The Underground": ugDict(),
                "The Exchange": exchangeDict(),
                "La Prima": primaDict()}
                
def lunchDict():
    return   {"Tazza D' Oro": tazzaDict(),
             "El Gallo de Oro": galloDict(),
             "Pomegranate": pomegranateDict(),
             "Underground": ugDict(),
             "The Exchange": exchangeDict(),
             "Nakama Express": nakamaDict(),
             "Taste of India": indiaDict(),
             "La Prima": primaDict()}
             
def dinnerDict():
    return  {"Tazza D' Oro": tazzaDict(),
             "El Gallo de Oro": galloDict(),
             "Pomegranate": pomegranateDict(),
             "Underground": ugDict(),
             "The Exchange": exchangeDict(),
             "Nakama Express": nakamaDict(),
             "Taste of India": indiaDict(),
             "La Prima": primaDict()}
             
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
    return {'Apple Dumpling': '570,87,6,23',
            'Asiago Cheese Bagel': '380,68,18,6',
            'Blueberry Muffin': '440,57,5,21',
            'Chocolate Chunk Brownie':'310,37,4,18',
            'Cranberry Scone':'500,71,5,23',
            'Large Chocolate Chip Cookie': '580,73,6,31',
            'Raisin Scone': '570,93,10,24',
            'Sfogliatelle': '180,25,5,7',
            'Small Chocolate Chip Cookie': '180,26,2,9',
            'Supergrain Bagel': '400,62,12,10',
            'Triple Berry Apple Tart': '470,63,4,23'}
    
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
    return {'Belgian Waffle': '260,58,7,3',
            'Belgian Waffle with Berries and Cream': '500,85,7,15',
            'Buttermilk Pancakes': '660,145,18,8',
            'Cafe French Toast': '430,63,16,13',
            'Chocolate Chip Pancakes': '930,181,20,25',
            'Egg White for Omelet': '90,2,18,0',
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
            'Breakfast Sausage Side':'360,0,12,34',
            'Hash Brown Patty': '140,16,1,9',
            'Home Fries': '130,20,2,5',
            'Orange': fruits()['Orange'],
            'Pear': fruits()['Pear'],
            'Pork Sausage Patty Topping': '180,0,6,17',
            'Scrambled Eggs for Breakfast Sandwich': '140,1,12,9',
            'Side of Bacon': '360,0,23,32',
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
    return {'Chocolate Chip Cookie': '640,83,5,29',
            'Chocolate Pudding': '120,22,2,2.5',
            'Lime Jello': '70,17,2,0',
            'Orange Jello': '70,17,2,0',
            'Red Raspberry Jello': '70,17,2,0',
            'Vanilla Pudding': '120,21,1,4'}
    
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
            'Cheeseburger': '540,33,38,27',
            'Cheesesteak': '670,39,32,45',
            'Chicken Cheesesteak': '500,39,41,22',
            'Colorado Wrap': '950,109,55,38',
            'Corned Beef Deli Sandwich': '370,34,28,13',
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
            'French Fries Appetizer': '770,84,8,45',
            'French Fries Side': '390,42,4,23',
            'Fruit Cup': '50,13,0,0',
            'Hash Browns':'170,14,1,13',
            'Lime Jello': '70,17,2,0',
            'Meat and Cheese Container': '410,2,26,33',
            'Onion Rings': '330,31,3,23',
            'Orange Jello': '70,17,2,0',
            'Provolone Sticks': '420,24,10,29',
            'Red Raspberry Jello': '70,17,2,0',
            'Steamed Vegetables': '60,11,4,0.5',
            'Sweet Potato Fries Appetizer': '350,43,3,22',
            'Sweet Potato Fries Side': '190,21,1,13',
            'Vanilla Pudding': ugDesserts()['Vanilla Pudding'],
            'Veggie Container': '10,2,0,0',
            'Yogurt Parfait': ugBfast()['Yogurt Parfait']}
    
def ugSoups():
    return {'Boston Clam Chowder Soup': '380,42,12,18',
            'Broccoli Cheese Soup': '430,26,16,32'}
    
def ugSpecialties():
    return {'BBQ Pulled Pork Sandwich':'670,65,38,28',
            'Blackened Salmon Fillet': '550,33,38,28',
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
            "Cheezy Beef Melt": "1080,15,55,29",
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
    
def primaDict():
    return {"Americanos": primaAmericanos(),
            "Capuccinos": primaCap(),
            "Baked Goods": primaBaked(),
            "Espressos": primaEsp(),
            "Hot Chocolate": primaHotChoc(),
            "Lattes": primaLatte(),
            "Macchiatos": primaMacch()}
            
def primaAmericanos():
    return {"Americano": "0,0,0,0",
            "Double Americano": "0,0,1,0"}
    
def primaCap():
    return {"Capp. with 2% milk": "70,7,5,3",
            "Capp. with Almond milk": "40,5,1,1.5",
            "Capp. with Skim milk": "50,7,5,0",
            "Capp. with Whole milk": "90,7,5,4.5",
            "Capp. with Soy milk": "80,9,5,2.5"}
    
def primaBaked():
    return {"Butter Croissant": "330,41,7,15",
            "Chocolate Chip Cookie": "380,43,5,22",
            "Chocolate Croissant": "360,46,7,17",
            "Chocolate Macaroon": "410,48,6,25",
            "Coconut Macaroon": "330,38,6,19"}
    
def primaEsp():
    return {"Double Espresso": "0,0,1,0",
            "Espresso Shot": "0,0,0,0"}
    
def primaHotChoc():
    return {"HC with 2% milk": "170,25,9,5",
            "HC with Almond milk": "110,22,1,3",
            "HC with Skim milk": "130,26,9,0",
            "HC with Soy milk": "190,29,8,4.5",
            "HC with Whole milk": "200,25,8,8"}
    
def primaLatte():
    return {"Latte with 2% milk": "110,11,8,4.5",
            "Latte with Almond milk": "60,8,2,2.5",
            "Latte with Skim milk": "80,11,8,0",
            "Latte with Soy milk": "120,14,8,4",
            "Latte with Whole Milk": "140,11,8,7"}
    
def primaMacch():
    return {"Macchiato with 2% milk": "10,1,1,0",
            "Macchiato with Almond milk": "5,0,0,0",
            "Macchiato with Skim milk": "5,1,1,0",
            "Macchiato with Soy milk": "10,1,1,0",
            "Macchiato with Whole milk": "10,1,1,0"}
    
def galloDict():
    return {"Sweet Treats and Fruit": galloSweet(),
            "Entrees": galloEntree(),
            "Sides": galloSides()}
            
def galloSweet():
    return {"Apple": fruits()["Apple"],
            "Cake": "270,32,3,14",
            "Banana": fruits()["Banana"],
            "Churro": "250,36,4,10",
            "Macaron": "60,7,1,2.5",
            "Mango": "200,50,3,1.5",
            "Orange": fruits()["Orange"],
            "Tres Leches Cake": "410,43,7,23"}
    
def galloEntree():
    return {"Barbacoa Burrito Bowl": "510,55,44,12",
            "Hard Tacos": "120,24,3,1.5",
            "Pork Burrito Bowl": "320,36,26,8",
            "Quesadilla": "350,44,14,14",
            "Shredded Lettuce": "20,4,1,0",
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
            "French Fries": "250,39,4,9",
            "Guacamole": "210,12,4,18",
            "Mild Salsa": "25,5,1,0",
            "Mushrooms": "20,3,3,0",
            "Pinto Beans": "160,30,10,1",
            "Tortilla Chips": "220,37,5,7",
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
            
#########################################
#Read/write file functions from cs.cmu.edu/~112/
#########################################
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
            
####################################
# Updated Animation Starter Code from cs.cmu.edu/~112/

from tkinter import *
####################################
            
 
    
def init(data):
    # load data.xyz as appropriate
    data.today = datetime.date.today()
    #updateDay(data)
    data.icons = [ ]
    data.page = mainDict()
    data.prevPage = None
    data.add = None #used to add food to plan
    data.addToMealLog = False #keep track of when user wants to add to meal plan
    data.meals = getMeals(data)
    data.todaysMeal = 'None'
    data.home = Return()
    data.voice = VoiceIcon(data)
    data.voiceImage = createImage('voice.png', data.width//12)
    
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
    
def getFood(dct, nutData):
    #get the food that was clicked on
    for key in dct:
        if dct[key] == nutData:
            return key
    
def createImage(path, size):
    #create image to store in data
    image = Img.open(path)
    image = image.resize((size, size), Img.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image
    
def changePage(data, icon):
    data.prevPage = data.page #store previous state
    data.page = icon.innerDict
    
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
            
def mousePressed(event, data):
    # use event.x and event.y
    for icon in data.icons:
        if icon.clicked(event.x, event.y):
            changePage(data, icon)
    if data.add != None and data.add.clicked(event.x, event.y):
        update(data)
    elif (data.addToMealLogButton != None and 
                        data.addToMealLogButton.clicked(event.x,  event.y)):
        data.addToMealLog = True
    elif data.home.clicked(event.x, event.y):
        init(data)
    elif data.voice.clicked(event.x, event.y):
        voiceInput = getUserVoice().lower()
        print('voice input: ', voiceInput)
        if voiceInput.lower() == None:
            tm.showerror('Uh oh :(', 'Could not understand  your command!')
        try:
            for icon in data.icons:
                item = icon.item.lower().strip()
                if item in voiceInput:
                    changePage(data, icon)
            if 'meal log' in voiceInput.lower():
                data.addToMealLog = True
            elif 'return' in voiceInput.lower():
                init(data)
            elif 'add' in voiceInput.lower():
                update(data)
        except:
            tm.showerror('Uh oh :(', 'Could not understand  your command!')
        
def update(data):
    #update page and meal log
    nutrition = data.page
    food = getFood(data.prevPage, data.page)
    data.meals[str(data.today)].append([food, nutrition]) #nicer version of eval
    updateUserInfo(data)
    init(data)
        
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

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill = 'plum1')
    if data.addToMealLog == False:
        drawTodaysMealLog(canvas, data)
    else:
        drawIcons(canvas, data, data.page)
    data.home.draw(canvas)
    data.voice.draw(canvas)
        
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
        
def drawTodaysMealLog(canvas, data):
    #draw today's meal log information
    today = str(data.today)
    try:
        todaysMeal = data.meals[today]
    except:
        #no recorded meal info today!
        data.meals = updateMealDict(data.meals)
        todaysMeal = data.meals[today]
        data.todaysMeal = todaysMeal 
    if todaysMeal == []:
        text = "Looks like you haven't eaten anything today!"
    else:
        text = getMealLogText(todaysMeal)
    canvas.create_text(data.width // 2, data.height // 2, text=text)
    data.addToMealLogButton = AddToMealLog()
    data.addToMealLogButton.draw(canvas)
    
def timerFired(data):
    writeFile('mealToShare', data.todaysMeal)
    
def getMealLogText(meals):
    #get text to display in meal log
    result = ''
    cals = 0
    carbs = 0
    protein = 0
    fat = 0
    for meal in meals:
        food = meal[0]
        result += food + '\n'
        nutrition = meal[1].split(',')
        for i in range(len(nutrition)):
            amount = nutrition[i]
            if i == 0:
                label = ' calories'
                cals += float(amount)
            elif i == 1:
                label = 'g carbs'
                carbs += float(amount)
            elif i == 2:
                label = 'g protein'
                protein += float(amount)
            elif i == 3:
                label = 'g fat'
                fat += float(amount)
            result += amount + label + '\n'
        result += '\n' + '\n'
    totals = 'TOTALS: %d CALORIES, %d CARBS, %d PROTEIN, %d FATS\n\n' % (cals, carbs, protein, fat)
    result = totals + result
    return result

def drawIcons(canvas, data, dct):
    #draw icons for page we are on, recursive when combined with helper fcns
    data.icons = [ ]
    
    if type(dct) != dict:
        #base case
        nutritionInfo = getNutInfo(dct)
        canvas.create_text(data.width//2, data.height//2, 
                            text=nutritionInfo, font = 'Arial 20 bold')
        data.add = Add()
        data.add.draw(canvas)
        return
    
    tmpDict = copy.deepcopy(dct) #prevent aliasing
    #get configuration of icons
    if len(dct) < 4: 
        #vertical icons, for aesthetic reasons
        rows = len(dct)
        cols = 1
    #otherwise get semi-square configurations of icons 
    else:
        if isPerfectSquare(len(dct)):
            rows = int(len(dct) ** 0.5)
        else:
            rows = int(nearestPerfectSquare(len(dct))**0.5) + 1
        cols = getCols(rows, len(dct))
    iconSize = data.height // rows // 2
        
    #get margin sizes
    horizMargin = (data.width - iconSize * cols) // (cols + 1)
    vertMargin  = (data.height - iconSize *  rows) // (rows + 1)
    
    #create icon instances, draw
    for row in range(rows):
        for col in range (cols):
            
            #coordinate = margin + square lengths 
            x = horizMargin * (col + 1) + col * iconSize
            y = vertMargin * (row + 1) + row * iconSize
            try:
                item = list(tmpDict.keys())[0]
            except:
                #base case
                continue
            innerDict = tmpDict.pop(item) #next item in dict
            icon = Icon(x, y, iconSize, vertMargin, item, innerDict)
            data.icons.append(icon)
            icon.draw(canvas)
            
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
        x = self.x + self.size // 2
        y = self.y + self.size // 2
        drawApple(canvas, x, y, self.size)
        
    def clicked(self, x, y):
        return (x > self.x and x < self.x + self.size 
                and y > self.y and y < self.y +  self.size)
                
def drawApple(canvas, x, y, size):
    #draw apple on each icon
    r = size // 4
    y = y + (size // 15)
    margin = size  // 7
    canvas.create_oval(x - r - margin, y - r, x + r - margin, y + r, fill='red')
    canvas.create_line(x - margin, y - size // 5, x - margin, y - size // 3, fill='brown', width=5, smooth=True)
    canvas.create_oval(x - r + margin, y - r, x + r + margin, y + r, fill='green')
    canvas.create_line(x + margin, y - size // 5, x + margin, y - size // 3, fill='brown', width=5, smooth=True)
                
class VoiceIcon(object):

    def __init__(self, data):
        self.x = data.width // 24
        self.y = data.height - (data.height // 24)
        self.size = data.width // 12
        self.leftBound = 0
        self.rightBound = self.size
        self.topBound = data.height - self.size
        self.botBound = data.height
        self.data = data
        
    def draw(self, canvas):
        data = self.data
        canvas.create_rectangle(self.leftBound, self.topBound, self.rightBound, 
                        self.botBound, width=5, fill='red', outline='gray19')
        canvas.create_image(self.x, self.y, image=data.voiceImage)
        
    def clicked(self, x, y):
        leftBound = self.leftBound
        rightBound = self.rightBound
        topBound = self.topBound
        botBound = self.botBound
        return (x > leftBound and x < rightBound and
                                    y > topBound and y < botBound) 
        
class Add(Icon):
    #type of icon that lets you add food to plan
    def __init__(self):
        r = 50
        width, height = 800, 800
        super().__init__(width//2 - r, height*7//10 + r, 
                                            2*r, 0, 'ADD\nITEM', {})
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, 
                    self.x + self.size, self.y + self.size, 
                                                fill='turquoise3', width=5)
        strLen = len(self.item)
        canvas.create_text(self.x + self.size  // 2, 
                    self.y + self.size // 2, 
                                text = self.item, font = 'Arial 15 bold')
                    
class Return(object):
    def __init__(self):
        self.size = 50
        
    def draw(self, canvas):
        canvas.create_rectangle(0, 0, self.size, 
                                self.size, fill='turquoise3', width=3)
        canvas.create_text(self.size//2, self.size//2, text='Return')
        
    def clicked(self, x, y):
        return x > 0 and x < self.size and y > 0 and y < self.size
        
class AddToMealLog(Icon):
    #type of icon that navigates to page that allows you to add to meal log
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
                    
def isPerfectSquare(n):
    #returns true if is perfect square, else false
    return math.isclose(n**0.5, int(n**0.5))

def nearestPerfectSquare(n):
    #returns nearest perfect square below n, for pos int n
    max = 1 #return 1 if less than 4
    for i in range (1, n+1):
        if isPerfectSquare(i):
            max = i
    return max
    
def getUnit(ind):
    #turn index into corresponding unit
    if ind == 0: return 'cals'
    elif ind == 1: return 'g carbs'
    elif ind == 2: return 'g protein'
    elif ind == 3: return 'g fat'
    
def getNutInfo(dct):
    #turn comma separated string into Nutrition Info string
    result = ""
    nutrients = dct.split(',')
    for i in range (len(nutrients)):
        value = nutrients[i]
        unit = getUnit(i)
        result += '%s %s' %(value, unit) + '\n'
    return result
    
def getCols(rows, n):
    #get number of cols on screen
    cols = 0
    while rows*cols < n:
        cols += 1
    return cols

####################################
# use the run function as-is
####################################

def run(user, width=300, height=300):
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