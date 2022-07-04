print('''


                  .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
dirn = input("You are at a T-end. please choose left or right? ")
if dirn == "Right" or dirn == "right" or dirn == "RIGHT":
    print("\nYou enter the wrong hallway. GAME OVER")
elif dirn == "Left" or dirn == "left" or dirn == "LEFT":
  river = input("\n You have a river in your way. Would you like to swim or wait? ")
  if river == "swim" or river == "Swim" or river == "SWIM":
    print("You couldn't swim and sink in the water. GAME OVER")
  elif river == "wait" or river == "Wait" or river == "WAIT":
    box = int(input("You crossed the river. You now have 3 boxes 1,2,3 and 1 key for all 3 boxes. which one would you choose?"))
    if box == 1:
      print("Hiss. You have opened a box of Cobras. GAME OVER")
    elif box == 2:
      print("Yayy! you won the tressure game. WINNER WINNER CHICKEN DINNER")
    elif box == 3:
      print("A ghost attacked you. GAME OVER")
    else:
      print("you lose the chance of treasure. GAME OVER")
  else:
     print("you lose the chance of treasure. GAME OVER")
else:
   print("you lose the chance of treasure. GAME OVER")