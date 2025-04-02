#Libraries
#Look into potential Python GUI libraries
import calendar
import re

expenses = []
budget = 1000

def get_valid_month():
    while True:
        month = input("Enter a month (January - December): ").strip().capitalize()
        # Check if month is valid
        if month in calendar.month_name[1:]: # Convert month name to number                                                            
            month = str(list(calendar.month_name).index(month)) # if month number single digit add '0' so it fits 'DD' format                                         
            if len(month) != 2:                                                                         
                month = "0" + month 
            return month
        else:
            print("Invalid or Misspelled month. Please enter a valid month name.")

def get_valid_year():
    while True:
        year = input("Enter a year (YYYY): ").strip()
        if year.isdigit() and len(year) == 4:
            return year
        else:
            print("Invalid year format. Please enter a four-digit year (YYYY).")

def get_valid_day(month, year):
    while True:
        day = input(f"Enter a day for {list(calendar.month_name)[int(month)]} (DD): ").strip()
        if not day.isdigit() or len(day) != 2:
            print("Invalid format. Please enter the day in 'DD' format.")
            continue
        
        #Check if month and year has given number of days, good for checking leap years as well
        if 1 <= int(day) <= calendar.monthrange(int(year), int(month))[1]:                                
            return day
        
        else:
            print(f"Invalid day. {list(calendar.month_name)[int(month)]} {year} does not have {day} days.")

def addExpense():
    categories = {"Food" , "Travel", "Games", "Clothing", "Technology", "Emergency"}

    #Extract date data (YYYY-MM-DD)
    month = get_valid_month()
    year = get_valid_year()
    day = get_valid_day(month, year)
    date = f"{year}-{month}-{day}"

    #Extracting expense category data 
    while True:
        category = input(f"What type of purchase are you making ({', '.join(categories)}): ").strip().capitalize()

        if category in categories:
            break
        else:
            print(f"'{category}' is not a valid type of purchase.")
    
    #Extracting amount spent data 
    while True: 
        money_amount = input("How much money did you spend? (##.##): ")
        pattern = r"^\d+\.\d{2}$"
        
        if bool(re.match(pattern, money_amount)):
            money_amount = float(money_amount)
            break
        else:
            print("That isn't a valid money amount.")

    #Extracting brief description data 
    purchase_description = input("Briefly explain the purpose of the purchase: ")

    try:
        if budget - money_amount >= 0:
            print(f"Purchase recorded. You have ${budget - money_amount} left this month.")
        else:
            print(f"Purchase recorded. It looks like you have exceeded your monthy budget by ${abs(budget - money_amount)}")
    except:
        print("Purchase recorded.")

    expense = {'date': date , 'category':category , 'amount':money_amount , 'description':purchase_description}
    expenses.append(expense)
 

def viewExpense():
    #Iterate through 'expenses' array and display the date, category, amount, and description for each entry
    #Skip each entry that have any missing details and inform user which ones are incomplete afterwards
    print("lorem ipsum")
    missing_details = []
    for expense in expenses:
        if any(not bool(value) for value in expense.values()):
            missing_details.append(expense)
        else:
            date = expense['date'].split('-')
            print(f"Date: {list(calendar.month_name)[int(date[1])]} {date[2]}, {date[0]} | Category: {expense['category']} | Amount: ${expense['amount']} | Description: {expense['expense']}")
    if len(missing_details) > 0:
        print("Some entries contain missing information")


def setBudget(value):
    budget = value
    print(f"Monthly budget is now set to: {budget}")

def trackBudget():
    #Calculates the total expenses recorded so far 
    #If the total expenses exceed the budget, display a warning (Example: You have exceeded your budget!)
    #If the expenses are within the budget, display the remaining balance (Example: You have 150 left for the month)
    print("lorem ipsum")

def saveCSV():
    #Save every entry in the expenses array into a CSV file (Date , Category , Amount , Description)
    print("lorem ipsum")

def loadCSV():
    #Reads saved CSV file and uploads data to user is GUI
    print("lorem ipsum")

addExpense()


