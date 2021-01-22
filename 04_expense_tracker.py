from datetime import date, datetime
import csv

today = date.today()
t = datetime.now()
time = '%d:%d'%(t.hour,t.minute)

print(today, time)
name = input("how should I address you? >>> ")

class Expenses:

    def __init__(self,  name, items = "nothing", amount=0):
        
        self.items = items
        self.amount = amount       
        self.name = name
        
    def record(self):     
        path = f"C:\\Users\\Ugochi\\Desktop\\PPython tutorials\\Python\\python_example\Created files\\{self.name}.csv"
        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([today,time,self.items,self.amount,])

decision = input("would you like to keep a record of your expenses? \ntype y/n: ")

while True: 
    if decision.lower() == "y":
        item = input("what did you buy or pay for? ")
        
        while 1:
            try: 
                cost = int(input("how much did you spend on it? "))
                break
            except ValueError:
                print("cost must be a figure/number.")
                
        
        
        user = Expenses(name, item, cost)
        user.record()
        
        decision = input("are there anymore expenses you would like to keep track of? \ntype y/n: ")
    
    elif decision.lower() == "n":
        print("your expenses have been recorded. \ncheck the my_expense_tracker.csv directory in your local machine to view. \nThanks.")
        break
    else:
        print("response must be yes or no")
        break




