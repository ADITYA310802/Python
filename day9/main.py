import os
import art
print(art.logo)
bid_values = {}
print("********WELCOME TO BLIND AUCTION********")
name = input("enter your name-")
bid = int(input("enter your bid value="))
bid_values[name]=bid


ch = 1
while(ch==1):
  print("Do you want to continue?")
  ch = int(input("enter\n1)yes\n2)no\n"))
  if ch != 1:
    break
  os.system('cls')
  name = input("enter your name-")
  bid = int(input("enter your bid value="))
  bid_values[name]=bid

maxm=0
print(bid_values)
for name in bid_values:
  if bid_values[name] > maxm:
    maxm = bid_values[name]
    winner = name
print(f"\nThe winner is {name} with amount {maxm}")


