import random

rock = '''
    ______
---'   ___)
      (_____)
      (______)
      (_____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       __________)
      (____)
---.__(___)
'''
hand=[rock,paper,scissors]
print("-------------------------------------")
print("Welcome to ROCK PAPER SCISSORS GAME!!")
print("-------------------------------------")
print("know your symbols")
print("-----------------ROCK----------------")
print( hand[0])
print("----------------PAPER----------------")
print( hand[1])
print("---------------SCISSORS--------------")
print( hand[2])
print("-------------------------------------")
usern = int(input("please choose a number from the following:\n0)Rock\n1)Paper\n2)Scissors\n"))
compn = random.randint(0,2)
print(f"Your option is\n{hand[usern]}")
print(f"computer option is \n{hand[compn]}")

#winning condition check

if (usern == 0 and compn == 2) or (usern == 1 and compn == 0) or (usern == 2 and compn == 1):
  print("user won!!Yayy")

elif  (compn == 0 and usern == 2) or (compn == 1 and usern == 0) or (compn == 2 and usern == 1):
  print("Oops!You lose")

else:
  print("Its a Draw")