#Libraries
import calendar , csv , os , re
import pandas as pd

filepath = "tracker_save_file.csv"
expenses = [{'date' : '2024-04-20' , 'category' : 'Weed' , 'amount' : 90 , 'description' : 'Smoke weed erryday'} , 
            {'date' : '2025-04-01' , 'category' : 'Food' , 'amount' : 20 , 'description' : 'Chinese take-out'} ,
            {'date' : '2024-12-25' , 'category' : 'Holiday' , 'amount' : 2000 , 'description' : 'Holiday Shopping'} ,
            {'date' : '2002-09-11' , 'category' : 'Holiday' , 'amount' : 100 , 'description' : 'B-day'} ,
            {'date' : '2020-07-04' , 'category' : 'Travel' , 'amount' : 70 , 'description' : 'Amtrack fare'} ]
header = ['Date' , 'Category' , 'Amount' , 'Description']
budget = 5000


def initial():
    if not os.path.exists(filepath):  #Creates new save file at start
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        print(f"'{filepath}' created successfully.")
    else:
        print(f"'{filepath}' already exists.")

def setBudget(value):
    budget = round(value , 2)
    print(f"Monthly budget is now set to: ${budget}")

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
    
    print("Purchase recorded.")

    expense = {'date': date , 'category':category , 'amount':money_amount , 'description':purchase_description}
    expenses.append(expense)
 
def viewExpenses():
    #Iterate through 'expenses' array and display the date, category, amount, and description for each entry
    #Skip each entry that have any missing details and inform user which ones are incomplete afterwards
    missing_details = []
    for expense in expenses:
        if any(not bool(value) for value in expense.values()): #Check if expense entry has any empty values. Skip if so
            missing_details.append(expense)
        else:
            date = expense['date'].split('-')
            print(f"Date: {list(calendar.month_name)[int(date[1])]} {date[2]}, {date[0]} | Category: {expense['category']} | Amount: ${expense['amount']} | Description: {expense['description']}") #Print out expense entry for user
    if len(missing_details) > 0:
        print("Some entries contain missing information")

def trackBudget(): 
    try:
        data = pd.read_csv(filepath)
        total_expenses = data['Amount'].sum()
        print(f'You have spent ${total_expenses} in total this month.')
        
        
        if total_expenses > budget: # If user goes over budget 
            print("You have exceeded your monthly budget!")
        elif total_expenses <= budget: # If user is still within budget
            print(f'You have ${budget - total_expenses} left for the month.')

    except FileNotFoundError:
        print("Save file not found. Creating new save file")
        initial()

def saveCSV():
    global expenses

    with open(filepath, mode='a' , newline= '', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        
        for expense in expenses:  #Appends every entry in the expenses array into a CSV file
            writer.writerow({
            'Date': expense['date'],
            'Category': expense['category'],
            'Amount': expense['amount'],
            'Description': expense['description']
        })
            
    expenses = []  #Resets expenses array so that old values don't get appended twice
    print("\nExpenses saved successfully.\n")

def loadCSV():
    #Reads saved CSV file and uploads data to user in GUI
    missing_details = []
    sorted_data = pd.read_csv(filepath).sort_values(by='Date')

    for index, row in sorted_data.iterrows():
        if row.isnull().any():
            missing_details.append(f"Date: {row.get('Date', '')}, Category: {row.get('Category', '')}, Amount: {row.get('Amount', '')}, Description: {row.get('Description', '')}")
        else:
            print(f"Date: {row['Date']}, Category: {row['Category']}, Amount: {row['Amount']}, Description: {row['Description']}")

    if len(missing_details) > 0:
        print("!!!Warning!!! \nSome entries are missing critical information")

        for entry in missing_details:
            print(entry)

def menu():
    while True:
        option = input("What would you like to do?\n\n>Press '1' to add an expense\n>Press '2' to view expenses\n>Press '3' to track a monthly budget\n>Press '4' to save your expenses\n>Press '5' to quit")
        if option not in ["1" , "2" , "3" , "4" , "5"]:
            print("\nThat is not an option.\nPlease try again\n")
        elif option == "5":
            break
        elif option == "1":
            addExpense()
        elif option == "2":
            loadCSV()
        elif option == "3":
            trackBudget()
        elif option == "4":
            saveCSV()
        


initial()
menu()