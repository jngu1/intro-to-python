# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
#name = input("What is your name?")
#print("Welcome " + name + "!")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
#name = input ("What is your name?")
#if name != "Alice": print("You're not Alice!")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
#password = input("Please enter password\n")
#if password == "qwerty123" : print("You have successfully logged in")
#if password != "qwerty123": print ("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
#number = int(input("Please enter a number to know if it's even or odd\n"))
#if number % 2 == 0:
 #   print(str(number) + " is Even")
#else:
 #   print(str(number) + " is odd")



# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
#num_1 = int(input("Please provide a number\n"))
#num_2 = int (input( "please provide another number\n"))

#if num_1 + num_2 > 21: print ("bust")
#else: print("safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
#LENGTH= int(input("Enter length\n"))
#Width = int(input("enter width\n"))

#if Width == LENGTH: print("it's a square!")
#else: print ("it's not a square")


# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
#salary = int (input("Please provide salary\n"))
#years = int (input("How many years have you worked for?\n"))
#bonus = salary * 0.1
#if years > 3: print ("Your current salary is" + str (salary) +" Your bonus is " + str(bonus))
#else: print ("Your current salary is" + str (salary) + " and you do not get a bonus")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
#number = int(input("give me a number\n"))
#calc = number **3
#if number >0: print (calc)
#else: print (number/2)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
#name= input("What is yout name?\n")
#if name == "Alice": print("Hello Alice")
#elif name =="Bob": print("You're not Bob! I'm Bob")
#else: print("You must be Charlie")


# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

#age= int(input("What is your age?\n"))
#if  age ==0: print("You're not born yet!")
#elif age <=11 :print ("You're too young to go to this school")
#elif age <=16: print("You can come to this school")
#elif age >16: print("You're too old for school")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
#month = input("What month is it?\n")
#if month == "March" or month == "April" or month == "May" :print (month + " is in Spring")
#elif month == "June" or month == "July" or month == "August": print(month + " is in Summer")
#elif month == "Sept" or month == "Oct" or month == "Nov": print(month + " is in Autumn")
#elif month == "Dec" or month == "Jan" or month == "Feb": print(month + " is in Winter")
#else: print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

#number = int(input("give me a number\n"))
#number_2 =int(input("give me another number\n"))
#if number%2 == 0 and number_2%2 == 0: print ("even")
#elif number %2 != 0 and number_2%2 !=0: print ("odd")
#else: print (number * number_2)

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
#num_1 = int(input("give me a number\n"))
#num_2 = int(input("give me another number\n"))
#if num_1 > num_2: print (num_1)
#elif num_2 > num_1: print (num_2)
#else: print("same number")

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
#salary = int(input("What is your salary?\n"))
#years = int (input("How many years of service at the firm?\n"))
#if years >= 7: print ("Your salary is" + str(salary) + " and your bonus is" + str(salary * 0.2))
#elif years >= 5: print ("Your salary is " + str(salary) + " and your bonus is" + str(salary *0.15))
#elif years >=3: print ("Your salary is " + str(salary) + " and your bonus is" + str(salary * 0.1))
#else: print ("Your salary is " + str(salary) + " and there's no bonus")
  
# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

#name1= input("What is your name?\n")
#age1= int(input("What is your age?\n"))

#name2= input ("Another person's name\n")
#age2= int(input("Age of second person\n"))

#name3= input ("A name of 3rd person")
#age3= int(input ("Age of 3rd person"))

#if age1 > age2 and age1> age3: print (name1 + " is the oldest at" + str(age1) + " years old")
#elif age2 >age1 and age2> age3: print (name2 + " is the oldest at" + str(age2) + " years old")
#elif age3> age1 and age3 > age2: print (name3 + " is the oldest at" + str(age3) + " years old")
#if age1 <age2 and age1 < age3: print (name1 + "is the youngest at" + str(age1) + " years old")
#elif age2 <age1 and age2 < age3: print (name2 + "is the youngest at" + str(age2) + " years old")
#elif age3 <age2 and age3 < age1: print (name3 + "is the youngest at" + str(age3) + " years old")
#else: print ("All ages are the same")
  
# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson =input("Please provide lesson namenn")
mark1= int(input("marks for lesson 1\n"))
mark2 = int(input("marks for lesson 2\n"))
mark3 = int(input("marks for lesson 3\n"))

if mark1 >80: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of A")
elif mark1 >60: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of B")
elif mark1 >50: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of C")
elif mark1 >45: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of D")
elif mark1 >25: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of E")
elif mark1 <25: print ("Lesson 1 has a mark of" + str (mark1) + " with a grade of F")

else: print("Go see your teacher")


if mark2 >80: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of A")
elif mark2 >60: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of B")
elif mark2 >50: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of C")
elif mark2 >45: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of D")
elif mark2 >25: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of E")
elif mark2 <25: print ("Lesson 1 has a mark of" + str (mark2) + " with a grade of F")

else: print("Go see your teacher")



if mark3 >80: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of A")
elif mark3 >60: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of B")
elif mark3 >50: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of C")
elif mark3 >45: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of D")
elif mark3 >25: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of E")
elif mark3 <25: print ("Lesson 1 has a mark of" + str (mark3) + " with a grade of F")

else: print("Go see your teacher")