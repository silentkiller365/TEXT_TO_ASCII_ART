import pyfiglet

print(' /$$$$$$$$ /$$$$$$$$ /$$   /$$ /$$$$$$$$       /$$$$$$$$  /$$$$$$         /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$        /$$$$$$  /$$$$$$$  /$$$$$$$$      ')
print('|__  $$__/| $$_____/| $$  / $$|__  $$__/      |__  $$__/ /$$__  $$       /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/|_  $$_/       /$$__  $$| $$__  $$|__  $$__/      ') 
print('   | $$   | $$      |  $$/ $$/   | $$            | $$   | $$  \ $$      | $$  \ $$| $$  \__/| $$  \__/  | $$    | $$        | $$  \ $$| $$  \ $$   | $$   ')
print('   | $$   | $$$$$    \  $$$$/    | $$            | $$   | $$  | $$      | $$$$$$$$|  $$$$$$ | $$        | $$    | $$        | $$$$$$$$| $$$$$$$/   | $$   ')
print('   | $$   | $$__/     >$$  $$    | $$            | $$   | $$  | $$      | $$__  $$ \____  $$| $$        | $$    | $$        | $$__  $$| $$__  $$   | $$   ')
print('   | $$   | $$       /$$/\  $$   | $$            | $$   | $$  | $$      | $$  | $$ /$$  \ $$| $$    $$  | $$    | $$        | $$  | $$| $$  \ $$   | $$   ')
print('   | $$   | $$$$$$$$| $$  \ $$   | $$            | $$   |  $$$$$$/      | $$  | $$|  $$$$$$/|  $$$$$$/ /$$$$$$ /$$$$$$      | $$  | $$| $$  | $$   | $$         ')
print('   |__/   |________/|__/  |__/   |__/            |__/    \______/       |__/  |__/ \______/  \______/ |______/|______/      |__/  |__/|__/  |__/   |__/         ')
print('\n')
print('                                                    >> V1.0           ')  
print('                                                           >> By Silentkiller365            ')  
text = input("Enter text: ")


print("Select a style:")
print("1. Standard")
print("2. Slant")
print("3. 3D")
print("4. Banner")
print("5. Bubble")
style = int(input("Enter a number to select: "))


if style == 1:
    ascii_art = pyfiglet.figlet_format(text)
elif style == 2:
    ascii_art = pyfiglet.figlet_format(text, font="slant")
elif style == 3:
    ascii_art = pyfiglet.figlet_format(text, font="3-d")
elif style == 4:
    ascii_art = pyfiglet.figlet_format(text, font="banner")
elif style == 5:
    ascii_art = pyfiglet.figlet_format(text, font="bubble")


print(ascii_art)
