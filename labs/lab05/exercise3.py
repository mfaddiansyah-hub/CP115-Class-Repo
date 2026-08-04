#Imports the random module
import random

#Takes the student's class name from the user
className = input("Class : ")

#Generates a random number and displays class information
num = random.randint(0,100)

print (f"\nNumber : {num}")
print (f"Class : {className}")