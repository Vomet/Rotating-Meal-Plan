from datetime import datetime, timedelta
import json


def markdown_formatting():
  # opens and reads meals.json
  with open('meals.json', 'r') as data:
    data = json.load(data)

    dates = []
    meals_data = []
    # organizing dates and meals into separate lists
    for date, meals in data.items():
      dates.append(date)
      meals_data.append(meals)

      
    #opens meals.md. outputs to file date and meal to cook on that day. '\n' to ensure string moves onto new line
    with open('meals.md', 'w') as meals:
      i = 0
      while i < len(data):
        # formatting strings to get data in lists. assigning to variables to writelines
        # date
        date = f'## {dates[i]}\n'
        # breakfast
        breakfast = f"- breakfast: {meals_data[i]['breakfast']}\n"
        # lunch
        lunch = f"- lunch: {meals_data[i]['lunch']}\n"
        # dinner
        dinner = f"- dinner: {meals_data[i]['dinner']}\n"

        # writing to meals.md. '\n' placed at end for better readability between days
        meals.writelines(date)        
        meals.writelines(breakfast)        
        meals.writelines(lunch)
        meals.writelines(dinner)
        meals.writelines('\n')

        i += 1
    


def assign_meals(dates, breakfast, lunch, dinner, num_days):
  # creating dictionary to store days as keys
  meals = {}
  
  for i in range(num_days):
    # using modulo operator to ensure each meal's list is iterated over and over again as i gets higher
    meals[dates[i]] = \
    {\
      'breakfast': breakfast[i % len(breakfast)],\
      'lunch': lunch[i % len(lunch)],\
      'dinner': dinner[i % len(dinner)]\
    }

  # outputting to json file
  with open('meals.json', 'w') as outfile:
    json.dump(meals, outfile)


def get_meals():
  # opens breakfast and puts all meals into list
  with open("breakfast.txt") as breakfast:
    breakfast = breakfast.readlines()
    # replacing "\n" that is appended to meal
    breakfast = [meal.replace('\n', '') for meal in breakfast]
    # removing any "\n" left over
    if '\n' in breakfast:
      breakfast.remove('\n')

  # opens lunch and puts all meals into list
  with open("lunch.txt") as lunch:
    lunch = lunch.readlines()
    # replacing "\n" that is appended to meal
    lunch = [meal.replace('\n', '') for meal in lunch]
    # removing any "\n" left over
    if '\n' in lunch:
      lunch.remove('\n')

  # opens dinner and puts all meals into list
  with open("dinner.txt") as dinner:
    dinner = dinner.readlines()
    # replacing "\n" that is appended to meal
    dinner = [meal.replace('\n', '') for meal in dinner]
    # removing any "\n" left over
    if '\n' in dinner:
      dinner.remove('\n')

  # returns as tuple
  return breakfast, lunch, dinner
  

def dates(num_days, date_format="%Y-%m-%d"):
  # defines list and grabs today's date
  today = datetime.today()
  dates = []

  # putting next num_days days after today into list
  i = 0
  while i < num_days:
    date = today + timedelta(days=i)
    dates.append(date.strftime(date_format))
    i += 1
    
  return dates


def start():
  # asks user how many days to meal plan in advance. adds 1 because it includes today
  num_days = int(input("Enter number of days you would like to plan for: ")) + 1
  
  # retrieves dates for program. You can also change your date format here
  next_num_days = dates(num_days, date_format="%Y-%m-%d")
  
  # get_meals returns as (breakfast, lunch, dinner). assigning to appropriate vars
	breakfast, lunch, dinner = get_meals()
  
  # assign_meals assigns each day with a rotating plan for breakfast, lunch, and dinner. It does this for num_days times. Also exports to meals.json
  assign_meals(next_num_days, breakfast, lunch, dinner, num_days)

  # takes data in meals.json and formats it neatly into meals.md
  markdown_formatting()


start()