string = 'Hello anh em nha !'
emptystring = ''

for i in range(0, len(string)):

    if string[i] == ' ':
        emptystring = emptystring + ' '
    else:
        emptystring= emptystring+string[i]+str('\u0332')

print(emptystring)
print(string)
x="the solution"
print("\033[4m" + x + "\033[0m")
from simple_colors import *
a= green('hello anh em', 'underlined')
print(a)

# import required module
import fontstyle

# display formatted text
print(fontstyle.apply('Hello anh em',
                      'bold/Italic/UNDERLINE'))

print(fontstyle.apply('GEEKSFORGEEKS',
                      'bold/Italic/red/INVERSE/UNDERLINE/GREEN_BG'))
