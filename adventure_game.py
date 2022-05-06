import time
import random
enemy = random.choice(["Bear", "Pirate", "Troll", "Ogre"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def intro():
    print_pause("You are taking a nature hike in the woods.")
    print_pause("You are taking pictures of all sorts of beautiful "
                "wildlife until you come across something shiny.")
    print_pause("Sparking your curiosity, you decide to investigate it.")
    print_pause("You move away a bunch of vines to reveal a door!")
    print_pause("The shiny object you saw was a golden door knob!")
    print_pause("You decide to turn the knob and go through the door.")
    print_pause("The door is a portal to a new world!")
    print_pause("You decide to explore this new magical "
                "world taking in the beauty of it.")
    print_pause("After a few moments, you find a cute "
                "fairy stuck in tree sap.")
    print_pause("'Help me please! I am stuck!' The fairy said.")


def decision(item):
    while True:
        choice = input("Would you help the fairy? Or ignore the fairy? "
                       "Press [1] to help, Press [2] to ignore:").rstrip()
        if choice == "1":
            print_pause("You decide to help the fairy, "
                        "freeing her from the sap.")
            print_pause("The fairy thanks you for the help by rewarding "
                        "you with a magical amulet.")
            print_pause("'Take this as a token of my appreciation.' "
                        "The fairy said.")
            print_pause("'Use this amulet to call for "
                        "help whenever you need it'")
            print_pause("You graciously accept the gift "
                        "and continue to walk along.")
            item.append("amulet")
            break

        elif choice == "2":
            print_pause("You decide to ignore the fairy "
                        "and continue to walk along your path.")
            break

        else:
            print_pause("Please choose one of the choices provided")


def action(item, enemy):
    print_pause("As you was walking, you encounter a scary "
                "" + enemy + " they approach you!")
    print_pause("They want to attack you!")
    print_pause("What should you do?")
    while True:
        choice2 = input("Do you decide to call for help "
                        "with the power of your amulet? Or fight? "
                        "Press [1] to call, Press [2] to fight")
        if choice2 == "1":
            if "amulet" in item:
                print_pause("You chose to call for help "
                            "with the use of your mighty amulet")
                print_pause("The fairy comes to help you defeat "
                            "the " + enemy + " and you win the game!")
                play_again()
                break
            elif choice2 == "2":
                print_pause("You chose to fight but you lose. "
                            "You are too weak to fight the"
                            "" + enemy + " alone")
                play_again()
                break
            else:
                print("Please choose one of the choices provided")
        if choice2 == "1":
            if "amulet" not in item:
                print_pause("You do not have the amulet, "
                            "therefore you cannot call for help")
                print_pause("You are alone and cannot defeat "
                            "the " + enemy + " by yourself")
                print_pause("You lose")
                play_again()
                break
        elif choice2 == "2":
            print_pause("You chose to fight but you lose. "
                        "You are too weak to fight the " + enemy + " alone")
            play_again()
            break
        else:
            print_pause("Please choose one of the choices provided")


def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    enemy = random.choice(["Bear", "Pirate", "Troll", "Ogre"])
    intro()
    decision(item)
    action(item, enemy)


play_game()
