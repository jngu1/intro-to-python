# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
#items = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]

#print(items[0])
#print(items[1])
#print(items[2])
#print(items[3])
#print(items[4])
#print(items[5])
# 2. Add "Grapes" to the list and print the list.
#items.append("Grapes")
#print(items)

# 3. Change "Pears" to "Strawberries" and print the list.
#items[2]="Strawberries"

#print (items)
# 4. Remove "Apples" from the list and print the list.

#del(items[0])
#print(items)
# 5. Print out the current length of the list.
#print(len(items))


# 6. Order the list alphabetically.
#items.sort()

#print(items)



# 7. Print out the list again.

#print(items)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
#for item in items: print (item)

# 2. Print the numbers 1 to 100 (including the number 100).
#for numbers in range (101): print(numbers)


# 3. Print all odd numbers from 1 to 100.
#for numbers in range (1,100, 2): print(numbers)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
#for years in range(1896,2022, 4):
  #print(years)
 ## not_held = (1916,1940,1944,2020)

#for years in range (1896,2022,4): 
 # if years not in not_held: print(years)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
#numbers = [1,15,16,21,24,26,27,31,33,35]
#even_count = 0
#odd_count = 0

#for n in numbers:
 # if n% 2 == 0:
 #   even_count = even_count + 1
 # else:
  #  odd_count= odd_count + 1
#print(" the number of even numbers are " + str(even_count) + " and the number of odd numbers are " + str(odd_count))

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
#names = ["Anton", "Jeremy", "Pawel", "Roman" , "Zachariah"]
#for n in names:
 # print("Hello, " + n)



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
#word = ["supercalifragilisticexpialidocious"]

#for i in word: print (i)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
#number = [1,3,5,6,9]
#sqr_number = []

#for n in number :
# sqr_number.append(n**2)
# print (sqr_number)
# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

#names = ["Anton", "Jeremy", "Pawel", "Roman" , "Zachariah"]
#dr = []
#for n in names: 
#  dr.append("Dr. " + n)

#print (dr)
# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

for number in range (1, 101):
  if (number % 3 == 0) and (number % 5 == 0):
       print("FizzBuzz")
  elif (number % 3 == 0):
        print("Fizz")
  elif (number % 5 == 0):
        print("Buzz")
  else:
        print(number)

