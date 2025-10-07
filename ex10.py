###############################################################################
#  Program Name   : ex10.py
#  Author         : Parnika Bhat
#  Task           :  it asks to write a program that asks for 3 friends’ names, stores them in a list, and prints them all.
###############################################################################
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
numbers.remove(2)

animals = ["cat", "dog", "bird"]
for a in animals:
    print(a)

colours = [ "green", "black", "blue"]
for c in colours:
    print(c)

# Prompt the user to enter their favorite movies
movies = []
for movie in input("Enter the name of your favorite movie: "):
    movies.append(movie)
    # Display the list
    for movie in movies:
        print(movie)

Enter your top 5 favorite numbers:
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50

Your favorite numbers are: [10, 20, 30, 40, 50]
The sum of your favorite numbers is: 150
"""
friendsList=[]
while len(friendsList)< 3:
    friends=input ("type your top 3 best friends list ")
    friendsList.append(friends)


#print(letterList)

for friends in friendsList:
    print(friendsList)

