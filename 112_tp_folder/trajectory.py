#Shows the trajectory throughout the week of calorie, carb, protein, fat intake
#Got info on how to use matplot from https://matplotlib.org/users/pyplot_tutorial.html

import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
from mealHistory import getInfoToRemove, findUser, getMeals

def week():
    #get all dates in the last week
    today = datetime.date.today()
    result =  [ ]
    for i in range(7, -1, -1):
        day = today - timedelta(days=i)
        result.append(day)
    return result
 
def timeList():
    #list of months/dates for x-axis
    today = datetime.date.today()
    result = [ ]
    for i in range(7, -1, -1):
        day = today - timedelta(days=i)
        day = str(day)
        day = day[-5:]
        result.append(day)
    return result
    
def run(user):
    meals = getMeals(user)  
    cals, carbs, protein, fat = getDataToPlot(meals)
    plt.plot(timeList(), cals, label = 'Calories (cals)')
    plt.plot(timeList(), carbs, label  = 'Carbs (g)')
    plt.plot(timeList(), protein, label = 'Protein (g)')
    plt.plot(timeList(), fat, label  = 'Fat (g)')
    plt.ylabel('Nutrients')
    plt.xlabel('Time')
    plt.legend()
    plt.show()
    
def getDataToPlot(meals):
    #get data that will be plotted
    cals = [ ]
    carbs = [ ]
    protein = [ ]
    fat = [ ]
    for day in week():
        todayCals, todayCarbs, todayProtein, todayFat = 0, 0, 0, 0
        day = str(day)
        todayMeals = meals[day]
        for meal in todayMeals:
            nutrition = meal[1].split(',')
            for i in range(len(nutrition)):
                amount = nutrition[i]
                if i == 0:
                    todayCals += int(float((amount)))
                elif i == 1:
                    todayCarbs += int(float((amount)))
                elif i == 2:
                    todayProtein += int(float(amount))
                elif i == 3:
                    todayFat += int(float(amount))
        cals.append(todayCals)
        carbs.append(todayCarbs)
        protein.append(todayProtein)
        fat.append(todayFat)
    return (cals, carbs, protein, fat)