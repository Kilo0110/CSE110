
from colorama import Fore, Style

name = input("Hello, what's your name?")
colour = input(
    "Hi " + name + "! It's nice to meet you. What's your favourite colour?")
if colour == 'blue' or colour == 'Blue' or colour == 'BLUE':
  print("That's great! Your favourite colour is " +
        Fore.BLUE + " and its one of my favourite colours as well")
elif colour == 'purple' or colour == 'Purple' or colour == 'PURPLE':
    print("That's great! Your favourite colour is " +
          Fore.MAGENTA + " and its one of my favourite colours as well")
else:
  print("That's great! Your favourite colour is " + colour + " My favourite colours are " +
        Fore.BLUE + "blue" + Style.RESET_ALL + ' and ' + Fore.MAGENTA + "purple")
