# this line gets the date and time from the currnet os and imports it to the program
from datetime import datetime
# this line specifies that I would like it to pull the date and time from the current time that I am opening and running the program
now = datetime.now()
# this excutes the above commands in the format laid out and will display like so in the programm
print ("{}/{}/{}, {}:{}:{}".format(now.month, now.day, now.year, now.hour, now.minute, now.second))
# this will take user input and store to print the results the the user inputs
name = input("What is your name?")
# this takes user input and stores it to print the results from the users input
animal = input("What is your favorite animal?")
# this takes user input and stores it to print the results from user inputs
color = input("What is your favorite color?")
# this will print the messages along with all the users input  
print ("Ah, so your name is {}, your favorite animal is a {}, " \
"and your favorite color is {}.".format(name, animal, color))
# this defines the answer based on user inputs and gives them the commands the program wishes to excute
answer = input ("Type yes or no then hit enter")
# this is where the error occurs as unexpected indent even though I have four indent spaces
if answer == "yes" or answer == "y":
# this is supposed to print Okay great! if the user inputs yes or y
   print ("Okay great!")
# this is sppoused to take user input if answer is not yes or y but is no or n   
elif answer == "no" or answer == "n":
# this is suppoused to print Oh sorry about that. if user inputs no or n 
    print ("Oh sorry about that.")
#this supposed to excute and print You did not select yes or no please try againg if user answered in anyway besides yes, y, no, or n    
else:
    print ("You did not select yes or no please try again")


