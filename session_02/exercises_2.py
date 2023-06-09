# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
width =10
height = 20
area =  width * height
print("Rectangle of width "+str(width)   + " and height " +str(height)+ " has an area of " + str(area))


# 2. Write code that prints the length of the string, 'python'.
print(len("python"))


# 3. Print out the first and third letter of the word 'python'.
name = "python"
print(name[0])

print (name[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
#name = input("What is your name?")
#print ("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

#age = int(input ("What is your age?"))
#age_15 = age + 15
#print ("You will be " + str(age_15) + " in 15 years time")



# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
""""name = input("What is your name? ")
age = int(input ("What is your age?"))
new_age = age + 15

print ("Hello " + name + " you are currently" + str(age) + " in 15 years time you will be " + str(new_age))"""

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
"""hometown = input("Where is your hometown?\n")

print ("Your hometown is in "+ hometown.upper())"""


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
"""colour = input ("What is your favourite colour?\n")
print (len(str(colour)))"""


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
"""weather = input("What is the weather today?\n")
month = input ("What month are we in?\n")

print ("It is " + month + " and it is " + str(weather) + " today")
"""
# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
"""
temp1 = int(input("What is the temp today?\n"))
temp2 = int(input("What is the temp on Monday?\n"))
temp3 = int(input("What is the temp on Tuesday?\n"))
temp4 = int(input("What is the temp on Wednesday?\n"))
temp5 = int(input("What is the temp on Thursday?\n"))
month = input("What month are we in?\n")
avgtemp = (temp1 + temp2 + temp3 + temp4 + temp5) / 5

print ("It is " + month +  " and the average temperature is " + str(avgtemp)+ "degree celcius")

"""

# 11. Print out the above sentence but make the month upper case.
"""print ("It is " + month.upper() +  " and the average temperature is " + str(avgtemp)+ " degree celcius")
"""

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
"""
animals = "My favourite animals are \n\t dogs \n\t penguins \n\t dolphins \n\t whales"

print (animals)

"""
# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
"""
name = input("What is your name?\n")
number = int(input("Give me a number\n"))

print (name[number].upper())
"""
# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

text="WelcometoPython"
print (len(text))

print(text[1:14:2])
