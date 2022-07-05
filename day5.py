#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
l=[]
s=[]
n=[]
for i in range(nr_letters):
  l= random.sample(letters,nr_letters)
for j in range(nr_symbols):
  s= random.sample(symbols,nr_symbols)
for k in range(nr_numbers):
  n = random.sample(numbers,nr_numbers)
password = l+s+n
random.shuffle(password)
# print(password)
print("the generated password is:")
# for i in range(0,len(password)):
#   print (password[i],end="")
pw=""
for char in password:
  pw += char
print(pw)