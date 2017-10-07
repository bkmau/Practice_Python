from collections import namedtuple

print("Using regular tuple to represent a RGB")
color = (55, 155, 255)
print(color)
print(color[1])

print("For more readable, i use dictionary to represent a RGB")
color = {"red": 55, "green": 155, "blue": 255}
print(color)
print(color["red"])

print("But i have nametuple that i can represent a RGB easily")
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(55, 155, 255)
print(color)
print(color.blue)