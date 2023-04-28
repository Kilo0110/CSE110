# TODO:
# Create your own text-based adventure game with at least three levels of choices. It's up to you to determine the scenarios, the choices, and the consequences.


# NOTE: While the code written here is entirely mine, the story was created with help from OpenAI's ChatGPT tool.

intro = "You wake up in a mysterious castle with no memory of how you got there. The door to your room is locked, and there doesn't seem to be anyone around. As you explore the castle, you realize that it's full of secrets and puzzles. You'll need to use your wits and creativity to find a way out and piece together what happened to you. Along the way, you'll encounter strange creatures, hidden passages, and powerful magic. Will you be able to escape the castle and uncover the truth, or will you be trapped forever? The choice is yours."

scenario_one = "You come across a locked door and have to choose how to open it."

scenario_one_first_option = "Pick the lock using a hairpin"
scenario_one_second_option = "Search the room for a key"
scenario_one_third_option = "Kick the door"

scenario_one_input = None

#
print('Stuck In a Castle')

print(f'\n{intro}')


def print_scenario_with_options(scenario_prompt, options_array):
    print(f"\n{scenario_prompt}")
    for option in options_array:
        if options_array.index(option) == 0:
            print(f"\n>>> a. {options_array[0].upper()}")
        elif options_array.index(option) == 1:
            print(f">>> b. {options_array[1].upper()}")
        else:
            print(f">>> c. {options_array[2].upper()}")

    scenario_one_input = input("\n What do you do?: ")
    return scenario_one_input


def checkInputsAgainstOption(scenario_input, present_scenario_options, option_letter, new_scenario, new_scenario_options):
    """
    Purpose: Checks the user's input against the options and outputs a new scenario
    """

    if option_letter == 'A':
        if scenario_input.casefold() == present_scenario_options[0].casefold() or scenario_input.casefold() == option_letter.casefold():
            next_scenario = new_scenario
            next_scenario_first_option = new_scenario_options[0]
            next_scenario_second_option = new_scenario_options[1]
            next_scenario_third_option = new_scenario_options[2]

            next_scenario_input = print_scenario_with_options(next_scenario, [
                next_scenario_first_option, next_scenario_second_option, next_scenario_third_option])
        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif option_letter == 'B':
        if scenario_input.casefold() == present_scenario_options[1].casefold() or scenario_input.casefold() == option_letter.casefold():
            next_scenario = new_scenario
            next_scenario_first_option = new_scenario_options[0]
            next_scenario_second_option = new_scenario_options[1]
            next_scenario_third_option = new_scenario_options[2]

            next_scenario_input = print_scenario_with_options(next_scenario, [
                next_scenario_first_option, next_scenario_second_option, next_scenario_third_option])
        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif option_letter == 'C':
        if scenario_input.casefold() == present_scenario_options[2].casefold() or scenario_input.casefold() == option_letter.casefold():
            next_scenario = new_scenario
            next_scenario_first_option = new_scenario_options[0]
            next_scenario_second_option = new_scenario_options[1]
            next_scenario_third_option = new_scenario_options[2]

            next_scenario_input = print_scenario_with_options(next_scenario, [
                next_scenario_first_option, next_scenario_second_option, next_scenario_third_option])
        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    else:
        print(
            "You have an inputed an invalid option and now you're stuck here forever!!!")
        exit()

# end def


scenario_one_input = print_scenario_with_options(scenario_one, [
    scenario_one_first_option, scenario_one_second_option, scenario_one_third_option])


if scenario_one_input.casefold() == scenario_one_first_option.casefold() or scenario_one_input.casefold() == 'A'.casefold():
    scenario_two = "You encounter a strange creature in the castle."
    scenario_two_first_option = "Attack it with the sword you found earlier."
    scenario_two_second_option = "Try to sneak past it undetected."
    scenario_two_third_option = "Attempt to communicate with it."

    scenario_two_input = print_scenario_with_options(scenario_two, [
        scenario_two_first_option, scenario_two_second_option, scenario_two_third_option])

    if scenario_two_input.casefold() == scenario_two_first_option.casefold() or scenario_two_input.casefold() == 'A'.casefold():
        scenario_three = "You succeed in killing it but now its screams have brought many creatures."
        scenario_three_first_option = "Face all the creatures in valiant battle."
        scenario_three_second_option = "Turn back and run away."
        scenario_three_third_option = "Lay down your weapon and plead for mercy."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])

        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You managed to defeat the creatures but as you catch your breath, you notice that the room you're in has several exits, but you don't know which one to take."
            scenario_four_first_option = "Take the door on the left, as it seems to be the safest and easiest route"
            scenario_four_second_option = "Take the door on the right, as it may lead to a shortcut or a hidden treasure."
            scenario_four_third_option = "Take the door straight ahead, as it looks like the most direct route out of the castle."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print('You have made the wrong choice and are now stuck here forever!!!')
            else:
                print('You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "As you hurry back down the hallway, you hear the creatures getting closer and closer. You turn a corner and come across a stairway leading up and another leading down."
            scenario_four_first_option = "Go up the stairs, as higher ground may provide a better view of the surrounding area"
            scenario_four_second_option = "Go down the stairs, as it may lead to a lower level and a chance to hide from the creatures"
            scenario_four_third_option = "Stand your ground and prepare for a fight, as running may not be an option."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print('You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print('You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "To your surprise, the creatures stop their approach and form a circle around you. One of them, larger and more imposing than the rest, steps forward."
            scenario_four_first_option = "Attempt to communicate with the creature, hoping to find a peaceful resolution."
            scenario_four_second_option = "Take advantage of the situation and attack the creature, hoping to catch it off guard."
            scenario_four_third_option = "Wait and see what the creature does, as you have no means of escape and no weapons to defend yourself."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print('You have made the right choice and have reached safety but beware lest you be caught again!!!')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_second_option.casefold() or scenario_two_input.casefold() == 'B'.casefold():
        scenario_three = "You succeed in sneaking past and enter a courtyard."
        scenario_three_first_option = "Make a run for the gate 300m away."
        scenario_three_second_option = "Scale the fence with a rope."
        scenario_three_third_option = "Scream for help."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])

        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You make a run for the gate 300m away. However, as you approach the gate, you see two guards standing in front of it, talking to each other."
            scenario_four_first_option = "Attempt to sneak past the guards and make a run for the gate."
            scenario_four_second_option = "Try to distract the guards and create an opening to slip past them."
            scenario_four_third_option = "Turn back and look for another way out of the castle."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "You quickly grab the rope you have with you and begin to scale the fence, hoping to get over it quickly and quietly. You're making good progress, but just as you're about to reach the top, you hear a loud shout. One of the guards has noticed you!"
            scenario_four_first_option = "Keep climbing and hope to get over the fence before the guard can catch you."
            scenario_four_second_option = "Jump down from the fence and try to make a run for it."
            scenario_four_third_option = "Surrender to the guard and hope for leniency."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "To your surprise, your scream is answered by a group of friendly rebels who were hiding in the castle, waiting for the right moment to strike. They hear your call and come to your rescue, taking you to their secret hideout."
            scenario_four_first_option = "Join the rebels and fight against the evil ruler of the castle."
            scenario_four_second_option = "Thank the rebels for their help and leave to find another way to escape the castle."
            scenario_four_third_option = "Stay in the hideout and wait for further instructions from the rebels."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_third_option.casefold() or scenario_two_input.casefold() == 'C'.casefold():
        scenario_three = "The creature understands you and you become friends. Now you must decide what to do."
        scenario_three_first_option = "Ride the monster's back and try to escape."
        scenario_three_second_option = "Tell the creature to stand guard while you try to escape."
        scenario_three_third_option = "Ask the creature to call his friends for help."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])

        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You climb onto the monster's back, gripping tightly as it takes off into the air, eventually landing in a remote clearing where you dismount and make a run for it. You run for hours until you reach a small village where you collapse from exhaustion."
            scenario_four_first_option = "Rest in the village and try to continue your journey when you have recovered."
            scenario_four_second_option = "Leave the village immediately and try to find another way to escape the castle."
            scenario_four_third_option = "Ask for help in the village and try to find a way to rescue the creature."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        if scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "You tell the creature to stand guard while you make your way to the nearest exit. You finally reach the exit and slip out into the night, grateful for your unexpected ally. However, you soon realize that you are lost in a vast and unfamiliar wilderness, with no idea how to reach safety."
            scenario_four_first_option = "Find a high vantage point and try to spot any landmarks or signs of civilization."
            scenario_four_second_option = "Start walking in a random direction and hope for the best."
            scenario_four_third_option = "Go back into the castle and try to find the creature."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        if scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "They offer to help you escape the castle and take you to a secret underground network of tunnels that lead out of the castle. You make your way through the dark and twisting passages, dodging traps and avoiding patrols, until you finally emerge into a moonlit forest."
            scenario_four_first_option = "Head for the nearest town or village and try to find help."
            scenario_four_second_option = "Try to find the creature's lair and thank them for their help."
            scenario_four_third_option = "Stay in the forest and build a shelter, hoping to avoid detection."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')
            
        else:
            print("You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    else:
        print("You have an inputed an invalid option and now you're stuck here forever!!!")
        exit()


elif scenario_one_input.casefold() == scenario_one_second_option.casefold() or scenario_one_input.casefold() == 'B'.casefold():
    scenario_two = "You come across a room filled with treasure."
    scenario_two_first_option = "Take as much as you can carry."
    scenario_two_second_option = "Leave it be, as it may be guarded by traps."
    scenario_two_third_option = "Take only what you need to progress on your journey."

    scenario_two_input = print_scenario_with_options(scenario_two, [
        scenario_two_first_option, scenario_two_second_option, scenario_two_third_option])

    if scenario_two_input.casefold() == scenario_two_first_option.casefold() or scenario_two_input.casefold() == 'A'.casefold():
        scenario_three = "You have a wagon full of treasures but moving it will make a hell of noise."
        scenario_three_first_option = "Attempt to escape by buying your way out."
        scenario_three_second_option = "Drop the treasure and go empty-handed."
        scenario_three_third_option = "Take only a handful."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])

        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You attempt to buy your way out and offer gold to the guards. They agree to let you go, but demand you leave the wagon behind."
            scenario_four_first_option = "Surrender the wagon and leave"
            scenario_four_second_option = "Negotiate for the wagon"
            scenario_four_third_option = "Draw weapons and fight"

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "You abandon the wagon and escape, but soon realize that you need money to survive. You must find a way to earn back what you lost."
            scenario_four_first_option = "Find work in the city"
            scenario_four_second_option = "Rob a wealthy merchant"
            scenario_four_third_option = "Join a band of thieves"

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and will now spend the rest of your days  in the dungeons!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "You grab a handful of gold coins and escape, but now must decide what to do with your newfound wealth."
            scenario_four_first_option = "Spend it all on luxury"
            scenario_four_second_option = "Invest in a business"
            scenario_four_third_option = "Hide it away for a rainy day."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])

            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have wasted a chance to be wealthy and comfortable and will now live a life of little!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        else:
            print("You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_second_option.casefold() or scenario_two_input.casefold() == 'B'.casefold():
        scenario_three = "You continue your search for a key and come across a hidden passage."
        scenario_three_first_option = "Follow the passage and see where it leads."
        scenario_three_second_option = "Keep searching for a key."
        scenario_three_third_option = "Give up and lay down to meet your fate."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You follow the hidden passage and find yourself in a large room filled with treasure. The room is guarded by two fierce beasts."
            scenario_four_first_option = "Fight the beasts and take the treasure."
            scenario_four_second_option = "Try to sneak past the beasts and escape with a small amount of treasure."
            scenario_four_third_option = "Surrender and ask the beasts for mercy."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be stuck here forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "You continue your search for the key and eventually find it hidden in a small crevice. You unlock the door and escape to freedom."
            scenario_four_first_option = "Keep the key as a souvenir."
            scenario_four_second_option = "Return with the key to try and save others who might be imprisoned."
            scenario_four_third_option = "Throw the key into the ocean, never to be found again."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have made the wrong choice and will now either die in battle or be found and returned to captivity forever!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "You resign yourself to your fate and await your end. However, a kind-hearted person finds you and takes you to safety."
            scenario_four_first_option = "Thank the person and go on your way."
            scenario_four_second_option = "Stay with the person and help them in any way you can."
            scenario_four_third_option = "Run away and continue your journey alone."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and have fallen into a group of raiders who snaps your neck')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_third_option.casefold() or scenario_two_input.casefold() == 'C'.casefold():
        scenario_three = "You find a key tucked away under the bed. You also find a hidden cellar."
        scenario_three_first_option = "Take the key and open the door."
        scenario_three_second_option = "Leave the key and open the cellar."
        scenario_three_third_option = "Take some more treasure to help you on your way."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You use the key to open the door and find a treasure room."
            scenario_four_first_option = "Take all the treasure you can carry."
            scenario_four_second_option = "Leave some behind for whoever lives here."
            scenario_four_third_option = "Leave everything as it is and escape quickly."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'The treasure you have carried slows you down and you are eventually caught and your neck snapped')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')


        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "You open the cellar and find a dark, musty room."
            scenario_four_first_option = "Light a torch and explore."
            scenario_four_second_option = "Turn back and leave the house."
            scenario_four_third_option = "Stay and hide, hoping no one will find you."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'You have made the wrong choice and have being caught by guards. This is your end!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')


        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "You grab some of the treasure and head for the door but you see guards guarding the exit"
            scenario_four_first_option = "Attempt to escape unnoticed."
            scenario_four_second_option = "Confront anyone who tries to stop you."
            scenario_four_third_option = "Offer a share of the treasure as a bribe."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have made the wrong choice and have being caught by guards. This is your end!!!')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')


        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()


    else:
        print("You have an inputed an invalid option and now you're stuck here forever!!!")
        exit()


elif scenario_one_input.casefold() == scenario_one_third_option.casefold() or scenario_one_input.casefold() == 'C'.casefold():
    scenario_two = "You encounter a powerful mage in the castle."
    scenario_two_first_option = "Fight them with your sword."
    scenario_two_second_option = "Try to reason with them and gain their help."
    scenario_two_third_option = "Attempt to sneak past them."

    scenario_two_input = print_scenario_with_options(scenario_two, [
        scenario_two_first_option, scenario_two_second_option, scenario_two_third_option])

    if scenario_two_input.casefold() == scenario_two_first_option.casefold() or scenario_two_input.casefold() == 'A'.casefold():
        scenario_three = "The mage is too powerful for you and knocks you to the ground."
        scenario_three_first_option = "Plead for mercy."
        scenario_three_second_option = "Keep your head up and prepare to die with honour."
        scenario_three_third_option = "Attempt one last kick to destabilize the mage."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "The mage listens to your pleas. He gives you a chance to prove your worth and offers you a task."
            scenario_four_first_option = "Accept the task."
            scenario_four_second_option = "Decline the task and try to fight the mage."
            scenario_four_third_option = "Attempt to escape."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])

            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'You have made the wrong choice and the mage ends your life with one final blow!')
            else:
                print(
                    'The task is to live a good and productive life and you pledge to do so.')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "The mage nods and ends your life swiftly and respectfully."
            print("You have played valiantly, you have faced terrifying situations and you have had to battle mages. You die a brave soul and your name will be the stuff of legends.")
            exit()

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "You surprise the mage with your bravery and quick thinking, knocking him off balance."
            scenario_four_first_option = "Take advantage of the situation and try to flee."
            scenario_four_second_option = "Finish off the mage while he's down."
            scenario_four_third_option = "Show mercy and spare the mage's life."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'The mage counters and regains control ending your life with one final blow.')
            else:
                print(
                    'You have made the right choice and have reached safety but beware lest you be caught again!!!')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_second_option.casefold() or scenario_two_input.casefold() == 'B'.casefold():
        scenario_three = "The mage agrees to help only if you pledge your life to them."
        scenario_three_first_option = "Pledge your life."
        scenario_three_second_option = "Refuse to pledge your life."
        scenario_three_third_option = "Pledge him treasures from your estate."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "The mage casts a spell and you are under his control. You must carry out his bidding until your life's end. Your options are now limited to what he permits."
            scenario_four_first_option = "Face the consequences of your pledge and serve him for the rest of your life."
            scenario_four_second_option = "Break your pledge and face the mage's wrath."
            scenario_four_third_option = "Try to renegotiate the pledge with the mage."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have angered the mage and he sends you to the dungeons.')
            else:
                print(
                    'The mage agrees to change the terms of the agreement giving you your freedom')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "The mage casts a spell, but you manage to resist its power. You are now hunted by the mage and must flee for your life. Your options are now limited to finding a way to survive and escape."
            scenario_four_first_option = "Hide in the nearby forest."
            scenario_four_second_option = "Ask for help from a friendly tribe."
            scenario_four_third_option = "Make a deal with another mage to protect you."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_second_option.casefold() or scenario_four_input.casefold() != 'B'.casefold():
                print(
                    'The mage finds you and casts you into the dungeons.')
            else:
                print(
                    'The friendly tribe protects you from the mage and assimilates you into their society.')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "The mage agrees and provides the requested help. You are now without much of your wealth and must find a way to regain it. Your options are limited to what you can afford or acquire by other means."
            scenario_four_first_option = "Steal from nearby merchants."
            scenario_four_second_option = "Start a small business and trade goods."
            scenario_four_third_option = "Beg for money from passing travelers."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You have made the wrong choice and will now be condemned to a life of imprisonment.')
            else:
                print(
                    'Your business flourishes and you become successful')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()

    elif scenario_two_input.casefold() == scenario_two_third_option.casefold() or scenario_two_input.casefold() == 'C'.casefold():
        scenario_three = "The mage sees you and stops you on your tracks."
        scenario_three_first_option = "Attack it with the sword you found earlier."
        scenario_three_second_option = "Plead for mercy."
        scenario_three_third_option = "Try to distract the mage."

        scenario_three_input = print_scenario_with_options(scenario_three, [
            scenario_three_first_option, scenario_three_second_option, scenario_three_third_option])
        
        if scenario_three_input.casefold() == scenario_three_first_option.casefold() or scenario_three_input.casefold() == 'A'.casefold():
            scenario_four = "You attack the mage with the sword, and a battle ensues. Your goal is to defeat the mage and escape safely."
            scenario_four_first_option = "Focus on defending yourself."
            scenario_four_second_option = "Try to disarm the mage."
            scenario_four_third_option = "Go on the offensive and aim for a quick kill."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_third_option.casefold() or scenario_four_input.casefold() != 'C'.casefold():
                print(
                    'You are too slow and the mage finishes you up.')
            else:
                print(
                    'You succeed in killing the mage and can escape to freedom.')

        elif scenario_three_input.casefold() == scenario_three_second_option.casefold() or scenario_three_input.casefold() == 'B'.casefold():
            scenario_four = "The mage is pleased by your mercy and decides to help you."
            scenario_four_first_option = "Accept the mage's help gratefully."
            scenario_four_second_option = "Refuse the mage's help and continue on your own."
            scenario_four_third_option = "Bargain for the mage's help in exchange for something else."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])

            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'The mage is angered by your decision to ignore his offer of help and snaps your neck.')
            else:
                print(
                    'The mage helps you escape to freedom.')

        elif scenario_three_input.casefold() == scenario_three_third_option.casefold() or scenario_three_input.casefold() == 'C'.casefold():
            scenario_four = "The distraction works, and the mage's attention is diverted."
            scenario_four_first_option = "Take advantage of the opportunity and escape."
            scenario_four_second_option = "Steal some of the mage's treasure."
            scenario_four_third_option = "Stay and continue your conversation with the mage."

            scenario_four_input = print_scenario_with_options(scenario_four, [
                scenario_four_first_option, scenario_four_second_option, scenario_four_third_option])
            
            if scenario_four_input.casefold() != scenario_four_first_option.casefold() or scenario_four_input.casefold() != 'A'.casefold():
                print(
                    'Your decision angers the mage and he snaps your neck immediately.')
            else:
                print(
                    'You escape to freedom finally!!!.')

        else:
            print(
                "You have an inputed an invalid option and now you're stuck here forever!!!")
            exit()


    else:
        print("You have an inputed an invalid option and now you're stuck here forever!!!")
        exit()

else:
    print("You have an inputed an invalid option and now you're stuck here forever!!!")
    exit()
