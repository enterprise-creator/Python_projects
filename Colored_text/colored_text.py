import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset = True)

print(Fore.BLUE + Back.YELLOW + "It rains a lot in Vancouver")
print(Back.CYAN + "Hello world!")
print(Fore.WHITE + Back.RED + "Xbox is better than PlayStation")
print(Fore.CYAN + Back.LIGHTBLACK_EX + "Halo is an amazing game!")

