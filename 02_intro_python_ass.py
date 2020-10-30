#guessing game
#assignment 2


from datetime import date
import random
import csv


today = date.today()
print(today)

name = input("Please, what's your name: \n>>> ")
print(f"Hi! {name}, you are welcome to the game hub.")
print("""Here's list of the available games to be played.  
    1. the colour guess
    2. the even number between 2 to 20 guess
    3. favourite fruit guess
    4. the bosses favourite cereal
    5. the available native soup guess
    """)
while 1:
    try:
        player_choice = int(input("Enter the number corresponding to the one you would like to play. \n>>> "))
        break

    except ValueError:   
        print("response must be an integer. please enter a number between 1 and 5.")
        
          
colours = random.choice(["green", "gray", "black", "white", "purple", "nude", "orange"])
numbers = random.choice([v  for v in range(21  ) if v % 2 == 0 ])
fruits = random.choice(["bannana", "orange", "apple", "mango", "pear", "guava", "strawberry"])
soups = random.choice(["afang", "egusi", "okra", "oha", "bitterleaf", "editan", "atama"])
cereals = random.choice(["oat", "maize", "wheat", "sorghum", "rice", "millet"])

class GuessingGame:
    """" defines a class of games where a
    user gets to guess something to get a reward"""
    def __init__(self, right_choice, reward,title):
        self.right_choice = right_choice 
        self.reward = reward
        self.title = title

    def __str__(self):
        print("At the game hub, you are rewarded for the right intuition")
        
    def the_guess(self):
        print(self.right_choice)
        wrong_guesses = []

        user_input = input("Take a guess:  \n>>> ")
            
        x = 0
        while x < 10:
            if user_input.lower() == self.right_choice:
                 print(f"waw! you are a guessing genuis! you just earned {self.reward}")
                 break
            else:
                wrong_guesses.append(user_input)
                user_input = input(f"oh no! you are almost there. try again...")
                
         
              x += 1
        self.response = x
        self.wrong_guesses =  str(wrong_guesses)

the_game = {1:[colours, "$10",'colour game'], 2:[str(numbers), "$50", 'number game'],
            3:[fruits, "$25", 'fruit game'], 4:[cereals, "$50", 'cereal game'],
            5:[soups, f"a plate of soup {soups}", 'soup game']}

if player_choice in the_game:
    my_game = GuessingGame(*the_game[player_choice])
    
else:
    print("sorry, your response is invalid. kindly pick a number within the listed range")
    exit()

my_game.the_guess()

print("Thanks for playing my game")
    

response_path = "C:\\Users\\Ugochi\\Desktop\\PPython tutorials\\Python\\python_example\\guess_game.csv"
with open(response_path, 'a') as file:
    writer = csv.writer(file)
   # writer.writerow(["Date", "user", "respone", "right_choice"])
    writer.writerow([today, name, my_game.response, my_game.right_choice, my_game.wrong_guesses, my_game.title])
  
