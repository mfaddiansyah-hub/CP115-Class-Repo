#Imports the math module
import math

#Takes a radius of circle from the user
radius = float(input("Radius (cm): "))

#Print the area and circumference of the circle
area = math.pow(radius, 2) * math.pi
circumference = 2 * radius * math.pi

print (f"\n\nArea : {area}")
print (type(area))

print (f"\nCircumference : {circumference}")
print (type(circumference))