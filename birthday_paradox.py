#Hello thank you for using my program
#This works with Python3
#What does this program do?: This program performs several probability experimints to determine the percentages of people who have the same birthday in N sized group
#This is project 2 or chapter 2 from "THE BIG BOOK OF SMALL PYHTON PROJECTS"
#Thanks for using!
import datetime, random
print("Birthday Paradox, by bledrummer or https://github.com/bluedrummer")
print("Explore the surprising probabilities of the Birthday Paradox")
print("There are no leap years")
print("Here is a test")
print()
print("How many birthdays shall i generate? (Max 100)")
birthay_count = 0
while True:
    birthday_count = int(input())
    if birthday_count < 100 and birthday_count:
        break
    print("Please retry as the number of birthdays you like me to generate is to much.")
print()
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
birthdays = []

def generate_random_birthdays(number_of_birthdays):


    birthdays_generated = []
    for i in range(0, number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        month = birthday.month
        birthdays_generated.append(f"{months[month-1]} {birthday.day}")
    return birthdays_generated

def getMatch(birthdays_list):
    count = 0
    if len(birthdays_list) == len(set(birthdays_list)):
        return None
    for a in range(0, len(birthdays_list)):
        count = 0
        for b in range(0, len(birthdays_list)):
            if birthdays_list[a] == birthdays_list[b]:
                count += 1
                if count == 2:
                    return birthdays_list[a]


birthdays = generate_random_birthdays(birthday_count)

print(f"Here are {birthday_count} birthdays")
print(birthdays)
match = getMatch(birthdays)
if match == None:
    print("In this sample simulation, nobody has the same birthday.")
if match != None:
    print(f"In this sample simulation, multiple people have a birthday on {match}.")
print()
print("How many simulations would you like to run? Note: If the desired amount of simulations is over 10,000 may take more take more then 60 seconds so please do not quit the code")
simulation_count = int(input())
print(f"Generating {birthday_count} random birthdays {simulation_count} times")
full_count = 0
for i in range(0, simulation_count):
    birthdays = generate_random_birthdays(birthday_count)
    match = getMatch(birthdays)
    if match != None:
        full_count += 1
    print(f"{i  + 1 } simulations complete.")
calculation = full_count / simulation_count * 100
print("The simulations are done!")
print()
print("Here are the results:")
print(f"Out of {simulation_count} simulations of {birthday_count} people, there was a")
print(f"matching birthday in that group {full_count} times. This means")
print(f"that {birthday_count} people have a {calculation} % chance of")
print("having a matching birthday in their group.")
print("Thats probably more then what you think!")
print("Thanks for using (bluedrummer at github)")
