print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input ("Do you want to move left or right?")
if direction == "left" or direction == "LEFT" or direction == "Left" or direction == "l" or direction == "L":
    action = input("Want to swim or wait?")
    if action == "wait" or action == "WAIT" or action == "W" or action == "w" or action == "Wait":
        door = input("which door you want to enter into: Red ? Blue? or Yellow?")
        if door == "Red" or door == "R" or door == "r" or door == "RED":
            print("Booo!! you burned by fire!! GAME OVER!!")
        elif door == "Yellow" or door == "Y" or door == "YELLOW" or door == "y" or door == "yellow":
            print("You won!! you won!! GAME OVER!!")
        elif door == "BLUE" or door == "B" or door == "b" or door == "blue" or door == "Blue":
            print("Eaten by Beast!! GAME OVER!!")
        else:
            print("GAME OVER!!")
    elif action == "SWIM" or action == "S" or action == "s" or "swim" or "Swim":
        print("Attacked by trout!! GAME OVER!!")
elif direction == "right" or direction == "RIGHT" or direction == "Right" or direction == "R" or direction == "r":
    print("Fall into a hole!! GAME OVER!!")
