from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()
num = random.randint(0,len(fonts))

if (len(sys.argv) == 1):
    input = input("Input: ")
    figlet.setFont(font = fonts[num])
    print(figlet.renderText(input))

elif (len(sys.argv) > 1 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in fonts)):
    input = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(input))

else:
    sys.exit("invalid input")


