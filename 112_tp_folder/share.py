#share what you've eaten today on Facebook
from tkinter import *
import fbchat 
from getpass import getpass 
from fbchat import Client
from fbchat import Message as fbMessage
from fbchat.models import * 
from mealHistory import *
from recommend import *
#################
#meal dictionaries
#################

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

####################################
# customize these functions from cs.cmu.edu/~112/
####################################

def init(data):
    # load data.xyz as appropriate
    data.button = ShareButton(data)
    data.sendFBMsg = False

def mousePressed(event, data):
    # use event.x and event.y
    if data.button.clicked(event.x, event.y):
        data.sendFBMsg = True
        
def connectToFacebook(username, password, name, msg):
    #code modified from https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/
    #with help of https://fbchat.readthedocs.io/en/master/examples.html
    client = fbchat.Client(username, password) 
    friends = client.searchForUsers(name)  # return a list of names 
    friend = friends[0] 
    client.send(fbMessage(text=msg), thread_id=friend.uid, 
                                    thread_type=ThreadType.USER)

class SendFacebookMessage(Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.labelU = Label(self, text='Facebook Username: ')
        self.labelP = Label(self, text='Facebook Password: ')
        self.labelF = Label(self, text='Enter a friend: ')
        
        self.entryU = Entry(self)
        self.entryP = Entry(self, show='*')
        self.entryF = Entry(self)
        
        self.send = Button(self, text='Send', command=self.sendMessage )
        
        self.labelU.grid(row=0, sticky=E)
        self.labelP.grid(row=1, sticky=E)
        self.labelF.grid(row=2, sticky=E)
        
        self.entryU.grid(row=0, column=1)
        self.entryP.grid(row=1, column=1)
        self.entryF.grid(row=2, column=1)
        
        self.send.grid(row=3, column=1)
        
        self.master = master
        self.data = data
        
        self.pack()
        
    def sendMessage(self):
        username = self.entryU.get()
        password = self.entryP.get()
        friend = self.entryF.get()
        msg = message(self.data)
        try:
            connectToFacebook(username, password, friend, msg)
        except:
            tm.showerror('Error! :o', 'Looks like one of the fields you entered is invalid. Try again!')
        
def message(data):
    #construct message to share via Facebook
    meals = getMeals(data.user)
    date = str(datetime.date.today())
    todayMeals = meals[date]
    if len(todayMeals) == 0:
        tm.showerror('Oops!', "Looks like there's nothing to share. You haven't eaten today! Add to your meal log and come back later :)")
    mealList = [ ]
    for meal in todayMeals:
        #each meal will be in the message
        mealList.append(meal[0])
    #beginning of message
    msg = "Hey! Today I ate "
    for i in range(len(mealList)):
        msg += mealList[i] + ' and '
    msg = msg[:-5] #cut off last and
    #end of message
    msg += '. It was great! We should get it together sometime :)'
    return msg

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    if data.sendFBMsg:
        sendFBMsg = SendFacebookMessage(canvas, data)
        data.sendFBMsg = False
        return
    canvas.create_rectangle(0, 0, data.width, data.height,  fill='plum1')
    canvas.create_text(data.width//2, data.height//3, text='Click the button below to share what you ate today with your friends on Facebook!')
    data.button.draw(canvas)
    
    
class ShareButton(object):
    #button to press to share on Facebook
    
    def __init__(self, data):
        self.w = 100
        self.h = 40
        self.x = data.width//2
        self.y = data.width*2//3
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.w, self.y-self.h, self.x+self.w, self.y+self.h, fill='skyblue')
        canvas.create_text(self.x, self.y, text='Click me!')
        
    def clicked(self, x, y):
        leftBound = self.x - self.w
        rightBound = self.x + self.w
        topBound = self.y - self.h
        botBound = self.y + self.h
        return x > leftBound and x < rightBound and y > topBound and y < botBound

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
    