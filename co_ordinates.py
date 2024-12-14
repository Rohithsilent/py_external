from enum import Flag
import math

def co_ordinates(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2-(y2-y1)**2)

    return distance

x1 = float(input("enter x1:"))
y1 = float(input("enter y1:"))
x2 = float(input("enter x2:"))
y2 = float(input("enter y2:"))

d = co_ordinates(x1,y1,x2,y2)
print(f"distance is:{d:.2f}")
