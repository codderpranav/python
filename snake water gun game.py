import random
print("wlcome! to snake water gun game")
print("type'snake','water','gun'")
user=input("please! enter your choice ")
options=("snake","water","gun")
computer=random.choice(options)
print("computer chooses the ",computer)
if user=='snake' and computer=='water':
    print("sorry! the computer wins better luck next time")
elif user=='water'and computer=='gun':
    print("congrats you win")
elif user=='gun' and computer=='water':
    print("sorry! thecomputer wins better luck next time")
elif user=='water' and computer=='snake':
    print("sorry! computer wins better luck next time")
else:
    print("the game is draw")