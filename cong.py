import time
import pyfiglet
from colorama import init, Fore, Style

def display_congratulations():
    init(autoreset=True) 

    congrats_text = "Congratulations! Vivek Kumar Sir and Sunil Sir"
    ascii_art = pyfiglet.figlet_format(congrats_text, font="slant")
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for i in range(3):
        for color in colors:
            styled_text = color + Style.BRIGHT + ascii_art
            print(styled_text)
            time.sleep(0.2)

    styled_text = Fore.RED + Style.BRIGHT + ascii_art
    print(styled_text)

display_congratulations()
