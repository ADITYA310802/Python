


from art import logo
# from replit import clear
import random


def guessing(num,rnge):
  for i in range(0,rnge):
    print(f"\nNumber of attempts remaining is={rnge}")
    n=int(input("Please guess a number="))
    if n<num:
      print("\nToo Low")
      rnge=rnge-1
    elif n>num:
      print("\nToo High")
      rnge=rnge-1
    elif n==num:
      print("You guessed the correct number")
      break
  if rnge==0:
    print(f"The number of attempts is over!You lose,the correct answer is {num}")


while 1:
  ch=int(input("\nEnter 1 to play and 2 to quit="))
  if ch==1:
    guess = random.randint(1,100)
    # clear()
    print(logo)
    c=int(input("select the difficulty level:\n1)Easy\n2)hard="))
    if c==1:
      guessing(guess,10)
    elif c==2:
      guessing(guess,5)
  else:
    break;


