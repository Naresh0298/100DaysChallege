
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")

choice_01 = input('You\'re at a crossroaf where do you want to go? Type "left" or "right".').lower()

if choice_01 == 'left':
    choice_02 = input('''You arrive at the island unharmed. There is a house with 3 doors. One yellow and one blue.which color do you choose?''').lower()
    if choice_02 == 'wait':
        choice_03 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you chosse?").lower()
        if choice_03 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_03 == "yellow":
            print("You found the treasure! You Win!")
        elif choice_03 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesnt exist. Gameover.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print('You fell into a hole. Game Over.')

