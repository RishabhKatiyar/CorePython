from collections import namedtuple
print('Named tuple')
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 100)

print(color)    # Color(red=55, green=155, blue=100)
print(color.red)
print(color.green)
print(color.blue)

print()
# normal tuple
print('Normal Tuple')

color = (100, 55, 155) 

print(color)    # (100, 55, 155)
print(color[0])
print(color[1])
print(color[2])
