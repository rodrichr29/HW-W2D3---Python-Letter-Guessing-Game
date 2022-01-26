# before testing code, make sure to type this in your command/terminal, [pip install colorama].
# as well reload vscode.
from colorama import Fore, Back, Style
import threading
event = threading.Event()
import random

def guessing_game():
    # Variables
    start = ""
    insert = ""
    quit = ""
    chances = 0
    insert_pool = ""

    # Array
    words = ['cake','terraria','smell','hell','chill','fill','cities','ringing','food','minecraft']
    word = random.choice(words)

    #START
    print("\nWelcome to guessing_game TM!\n")
    event.wait(1.50)
    print("Here are the rules of the game.")
    event.wait(1.50)
    print("You have to guess the chosen word, which will not be revealed.")
    event.wait(1.50)
    print("You only have seven chances to guess that word.")
    event.wait(1.50)
    print("And if all seven chances have been used...\n")
    event.wait(3)
    print(Fore.RED + "###############")
    print(Fore.RED + "# YOU ARE OUT #")
    print(Fore.RED + "###############")
    event.wait(1)

    while start != "y":
      print(Fore.WHITE + "\nUnderstood? [y/n]")
      start = input("> ")
      
      if start == "n":
        print("\nThat's quite unforunate, maybe another time.")
        event.wait(1.50)
        print("Thanks for playing!")
        event.wait(1.50)
        exit(guessing_game)
      if start != "y":
        print("\nType something that is defined...")
        event.wait(1.50)

    event.wait(.50)
    print(Fore.RED + "\nPERFECT")
    #START
    #MAIN
    while chances < 8:
      end_goal = 0
      event.wait(.50)
      print(Fore.WHITE + "\n#############################################################################\n")
      event.wait(.50)
      print("The word has been chosen...")
      print("(The word is lowercased.)\n")
      event.wait(.50)

      for char in word:
        if char in insert_pool:
            print(char)
        else:
            print("_")
            end_goal += 1

      if end_goal == 0:
        print("\nCongratulations!\n")
        event.wait(1.5)
        print(Fore.GREEN + "###########")
        print(Fore.GREEN + "# YOU WON #")
        print(Fore.GREEN + "###########")
        event.wait(3)
        print(Fore.WHITE + "\nThe word was", word, ".")
        event.wait(1)
        exit(guessing_game)

      event.wait(.50)
      print("\nIf you want to give up enter [quit]")
      print("\n\n\n\nEnter a Character...")
      insert = input("> ")
      insert_pool += insert
      event.wait(.50)
      print(Fore.WHITE + "\n#############################################################################\n")
      event.wait(.50)
      #QUIT
      if insert == "quit":
        print("Are you sure you want to leave? [y/n]")
        quit = input("> ")

        if quit == "y":
          print("\nThat's quite unforunate, maybe another time.")
          event.wait(1.50)
          print("Thanks for playing!")
          event.wait(1.50)
          exit(guessing_game)
        else:
          print("\nOkay sending you back...")
          event.wait(1)
      #QUIT
      #WIN/WRONG
      elif insert in word:
        print("Congratulations!")
        event.wait(.50)
        print("You got one of the characters right!")
        event.wait(1.50)
      else:
        print("That character isn't in the word...")
        chances += 1
        event.wait(1.50)
      #WIN/WRONG
    #MAIN
    #LOSE
    print("\nLooks like you ran of chances to guess the word...\n")
    event.wait(1)
    print("The word was", word + ".\n")
    event.wait(3)
    print(Fore.RED + "###############")
    print(Fore.RED + "# NOW GET OUT #")
    print(Fore.RED + "###############")
    event.wait(1)
    exit(guessing_game)
    #LOSE
guessing_game()
print(guessing_game)