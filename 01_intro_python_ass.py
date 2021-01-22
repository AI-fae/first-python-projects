'''01_intro_python_Assignment

Creating a story telling template that receives user input.
Concepts to be practiced in program: 1) datetime module 2) input 3)format
'''

from datetime import date

date = date.today()

print("\n...Hi! I'm FAE, I love storytelling, programming in python and sewing.")
print("How's today-", date, "going?")
print("\nI would like to know you more.")

name = input("What's your name? >>> ")
origin = input("where do you come from? >>> ")

print(f"\n{name} You are welcome to FAE's story crib. enjoy my world of imagery...\n")

age = input("are you above 18?  (my stories are censored for 18+) \n>>> yes/no: ")


Story = """\nThe most anticipated year of the century was finally here. year 2020
had come with so much anticipation. The people who lived in {origin} by this time must have felt the vibes too.
so much for mellinium goals, vision 2020, etc.
Looking back in retrospect, on this day {date}, {name} would you say the year went as expected?\n"""
print(Story.format(origin=origin,date=date,name=name))

feedback = input("Before I continue my story, let me hear your views about the year 2020... \n>>>")
closing = "\nThanks for reading and commenting, I will tell you about a country called Nigeria in 2020, the next time we meet. \nBYE!!"
print(closing)
