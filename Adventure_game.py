import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def print_list(strings):
    for string in strings:
        print(string)
        time.sleep(2)


def valid_input(prompt, options):
    while True:
        print_pause(prompt)
        for option in range(len(options)):
            print_pause(str(option + 1) + "." + options[option])

        response = input()
        try:
            response_int = int(response)
            for option in range(1, len(options)+1):
                if response_int == option:
                    return response_int
        except ValueError:
            response_string = response.lower()
            response_int = 0
            for option in options:
                response_int += 1
                if option.lower() in response_string:
                    return response_int
        print_pause("\nEnter a valid option\n")


def if_actions(response, options, actions):
    index = 0
    for option in options:
        if option == response:
            print_pause(actions[index])
            return option
        index += 1


def intro():
    print_list(["\n\nHumanity’s last safe city has fallen to an "
                "overwhelming invasion force,",
                "led by Ghaul, the imposing commander of the brutal Red "
                "Legion.",
                "He has stripped the city’s Guardians of their power, and "
                "forced the",
                "survivors to flee. To defeat the Red Legion(Cabal forces) "
                "and confront Ghaul,",
                "you must reunite humanity’s scattered heroes, stand together"
                ", and fight back",
                "to reclaim our home.\n"])
    time.sleep(7)

    print_list(["\nSo, your home has been destroyed, your light’s "
                "been stolen, ",
                "and you’ve just been chucked out the tower with not even"
                "a ghost",
                "for a companion. You are Looking dishevelled and on the"
                "brink of death.\n\n"])

    time.sleep(3)


def nessus():
    if "teleporter" not in inventory and "Cayde-6" not in heroes:
        inventory.append("teleporter")
        heroes.append("Cayde-6")
        print_list(["\nYou fight some of the forces in that planet and manage "
                    "to find Cayde-6,",
                    "one of the scattered heroes, He is a hunter vanguard of "
                    "the city as you",
                    "he will advice you once you find all the remaining "
                    "heroes,",
                    "he has a vex teleporter that you can use later",
                    "You head back to your ship."])
        places(["earth", "io", "titan"])
    else:
        print_pause("\nNothing else to do here. you waisting fuel.")
        places(["earth", "io", "titan"])


def titan():
    if "Zavala" not in heroes:
        heroes.append("Zavala")
        print_list(["\nYou fight some of the forces in that planet and manage "
                    "to find Zavala,",
                    "one of the scattered heroes, He is a titan vanguard of "
                    "the city",
                    "he will advice you once you find all the remaining "
                    "heroes.",
                    "You head back to your ship."])
        places(["earth", "io", "nessus"])
    else:
        print_pause("\nNothing else to do here. you waisting fuel.")
        places(["earth", "io", "nessus"])


def io():
    if "Ikora" not in heroes:
        heroes.append("Ikora")
        print_list(["\nYou fight some of the forces in that planet "
                    "and manage to find Ikora,",
                    "one of the scattered heroes, She is a warlock "
                    "vanguard of the city",
                    "she will advice you once you find all the "
                    "remaining heroes.",
                    "You head back to your ship."])
        places(["earth", "titan", "nessus"])
    else:
        print_pause("\nNothing else to do here. you waisting fuel.")
        places(["earth", "titan", "nessus"])


def earth():
    if (("Zavala" and "Cayde" and "Ikora" and "Cayde-6") in heroes and
       ("teleporter" and "light") in inventory):
        print_list(["\nYou have all you need to fight Ghaul and "
                    "finish the invasion,",
                    "the scattered heroes advice you to use",
                    "the vex teleporter to travel through a portal that will",
                    "take you to Ghaul's location in the traveler.",
                    "you take their advice and use the vex teleporter."])

        print_pause("\nYou can use you super or you weapon to take down Ghaul")
        final_traveler()

    elif 'light' not in inventory:
        options = [1, 2]
        action1 = ("\nYou were brutally killed by the red legion army in "
                   "combat,"
                   "\nbecause you didn't have the light of the traveler.")
        action2 = ("\nYou find you ghost. He tells you that he won’t be"
                   "\nable to revive you anymore,because ghaul capture the "
                   "traveler light"
                   "\nhe recommends to find help.")
        actions = [action1, action2]
        response = valid_input("You are hurt, standing in the ruins of the "
                               "city."
                               "\nyou can see cabal forces far away."
                               "\n\nWhat do you"
                               " want to do?\n", ["Fight the forces", "F"
                                                  "ind a way out there."])

        option_picked = if_actions(response, options, actions)
        if option_picked == 1:
            reset_game()
        else:
            response = valid_input("\nYou see some cabal forces around you "
                                   "but it's so dark they can't see you."
                                   "\n\nWhat do you "
                                   "want to do?\n", ["Fight", "Keep the path "
                                                     "and find help."])

            action2 = ("\nYou found Suraya Hawthorne one of the "
                       "scattered heroes,"
                       "\nshe guides you to a refuge place that "
                       "she calls the farm."
                       "\nnow you heal and plan a way to recover your light.")

            actions = [action1, action2]

            option_picked = if_actions(response, options, actions)
            if option_picked == 1:
                reset_game()
            else:
                print_pause("\nSuraya Hawthorne gives you one of her most "
                            "valuable weapon.")
                poweritems.append(random.choice(["Whisper of the worm exotic"
                                                 " Sniper weapon",
                                                 "Nameless midnight Scout "
                                                 "rifle",
                                                 "Better devils hand "
                                                 "cannon"]))
                print_pause(f"Now you have the {poweritems[0]}")
                time.sleep(3)
                print_list(["\nHaving narrowly escaped the clutches of the "
                            "Cabal,"
                            "\nit’s time to see if you can get your light "
                            "back,"
                            "\nand a fallen piece(shard) of the Traveler "
                            "seems like the perfect place to look."])

                options = [1, 2]
                action2 = ("you did't even make it, you died, you couldn't "
                           "past the red legion forces.")
                action1 = ("\nYou travel through the a cave and come out the "
                           "other side to get a nice view"
                           "\nof the shard, before jumping down into the "
                           "wooded area to fight through "
                           f"\nsome Forces with your {poweritems[0]}.")
                actions = [action1, action2]

                response = valid_input("\n\nWhat do"
                                       " you want to do?", ["Get your "
                                                            "light "
                                                            "back.", "Find"
                                                            " and "
                                                            "confront "
                                                            "Ghaul"])
                option_picked = if_actions(response, options, actions)
                if option_picked == 2:
                    reset_game()
                else:
                    inventory.append("light")
                    poweritems.append(random.choice(["Spectral blades "
                                                     "Super", "Golden "
                                                     "Gun Super", "Arc"
                                                     "strider Super"]))
                    time.sleep(5)
                    print_list(["\n\nYou get tho the shard of the traveler,"
                                " and you get your light back.",
                                "your Guardian will now be empowered with "
                                "all a bunch",
                                f"of abilities of the {poweritems[1]}, now "
                                "you head back the farm.",
                                "\n\nGhaul is in the traveler. you can't "
                                "get there",
                                "without a vex teleporter and the advice "
                                "of the scattered heroes.",
                                "They fled away during invasion, Suraya "
                                "tells you that they might be in",
                                "these places:(titan,io or nessus) in the"
                                " solar system.",
                                "you can use her ship to travel around the"
                                " solar system."])

                    places(["titan", "io", "nessus"])
    else:
        print_pause("\nNothing else to do here. you need to find "
                    "all the heroes")
        places(["nessus", "io", "titan"])


def places(places):
    response = valid_input("\n\nWhere would you like to go?", places)

    place = places[response-1]

    if place == "earth":
        earth()
    elif place == "io":
        io()
    elif place == "nessus":
        nessus()
    elif place == "titan":
        titan()


def final_traveler():
    ghaul = 100
    print_list(["\n\nYou are now face to face with Dominus Ghaul",
                "you have to attack him!!!!!."])

    print_pause("\nYou have three rifts of light you can use to get"
                "\nyour super and shoot him. be careful!")
    for riftuse in range(3):
        response = valid_input("\nwhat do you "
                               "want to do?", ["Use your "
                                               f"{poweritems[1]}.", "shoot "
                                               f"him with {poweritems[0]}."])

        if response == 1:
            if poweritems[1] == "Spectral blades Super":
                ghaul -= random.randint(30, 35)
            elif poweritems[1] == "Golden Gun Super":
                ghaul -= random.randint(35, 40)
            elif poweritems[1] == "Arcstrider Super":
                ghaul -= random.randint(34, 38)
            if ghaul < 0:
                ghaul = 0
            print_pause(f"\nYou use your {poweritems[1]} and "
                        f"now ghauls health is at {ghaul}")
        elif response == 2:
            if poweritems[0] == "Whisper of the worm exotic Sniper weapon":
                ghaul -= random.randint(30, 35)
            elif poweritems[0] == "Nameless midnight Scout rifle":
                ghaul -= random.randint(10, 20)
            elif poweritems[0] == "Better devils hand cannon":
                ghaul -= random.randint(10, 20)
            if ghaul < 0:
                ghaul = 0
            print_pause(f"\nYou use your {poweritems[0]} and "
                        f"now ghauls health is at {ghaul}")

        if ghaul == 0:
            break
        else:
            print_pause(f"\nYou have {2-riftuse} more chances")

    if ghaul > 0:
        print_list(["\n\nGhaul is alive impossible!!!!! now he detroys"
                    " your ghost and you died.",
                    "You couldn't beat Ghaul with all the resources"
                    " you had. Shame!"])
        reset_game()
    else:
        print_list(["\n\nYou kill Ghaul now the humanity is safe, and "
                    "the order will be reestablish",
                    "Now you are a scattered heroe.",
                    "Congratulations you won!!!!!"])
        reset_game()


def reset_game():
    inventory.clear()
    heroes.clear()
    poweritems.clear()
    response = valid_input("\n\nWould you like to play again?", ["yes", "no"])

    if response == 1:
        game()
    else:
        print_pause("\nThanks for playing my game.")


def game():
    intro()
    earth()


inventory = []
heroes = []
poweritems = []
game()
