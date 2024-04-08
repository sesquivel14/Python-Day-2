# #order of execution
# # in python 

# #strings are surrounded by quoes
# #single or double quotes ' ' or ""
# #be consistent with the quotes you use 
# print("Hello World")
# print ("order of execution")
# print ("in python")
# print ("*"*20)

# #variables are used to store data
# #variables are created when you assign a value to it
# #variables are vase sensitive 

# price= 10 #intefer variable
# name = "John" #string variable
# rating = 4.9 #float variable
# is_published = True #boolean variable 
# #start all variables with a lower case letter or underscore 
# #Use underscore to seperate words
# #use camel case og you want to start a capital letter
# #on the next word
# playerBulls =  "micheal jordan"

# #Concatenation to join variables in a sentence
# print(name + " is a basketball player")
# print(name + "has a arating of" + str(rating))
# #use the str() function to convert a nuber to a strong
# #the plus (+) sign is used to concatenate strings
# print(price "of the book" + str(price))
# #getting input from the user
name = input ("What is your name?")
age = input("What is your age?")
print("Hello" + name + "you are" + age + "years old")

#ask two questions from the user
#person's name and favorite color
#then print a message like "Moses likes blue"

personName = input("What is your name?")
favoriteColor = input("What is your favorite color?")
print(personName + "likes" + favoriteColor)
