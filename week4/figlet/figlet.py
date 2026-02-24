import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

fonts_list = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = random.choice(fonts_list)
    figlet.setFont(font=random_font)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f","--font"]:
        if sys.argv[2] in fonts_list:
            figlet.setFont(font=sys.argv[2])
        else:
            print("Invalid usage")
            sys.exit()   
    else:
        print("Invalid usage")
        sys.exit()
else:
    print("Invalid useage")
    sys.exit()
str_input = input("Input:")
print(figlet.renderText(str_input))