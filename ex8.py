###############################################################################
#  Program Name   : ex8.py
#  Author         : Parnika Bhat
#  Task           : it asks to write a program that keeps asking the user for words until they type exit. 
###############################################################################
"""count = 1
while count <= 5:
    print(count)
    count += 1
    password = "hi"

while password != "tiger123":
    password = input("Enter password: ")
print("Access granted")

while True:
    word = input("Type stop to end: ")
    if word == "stop":
        break
count=1
while count <= 5:
    print(count,"Cookies")
    count += 1

Enter a number: 5
5 is not an even number. Try again.
Enter a number: abc
Invalid input. Please enter a valid integer.
Enter a number: 8
8 is an even number. Program
"""
# Initialize an empty list to store words
story = []
while True:
   # Prompt the user for input
   word = input("Please type in a word: ")
   # Check if the user wants to end the input
   if word.lower() == "end":
       break
   # Add the word to the story
   story.append(word)
# Join and print the story
print("The story formed is:")
print(" ".join(story))
