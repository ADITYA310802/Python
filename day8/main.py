import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(msg,value,choice):
  new_msg = ""
  for i in msg:
    if i in alphabet:
      pos = alphabet.index(i)
      if choice == 1:
        new_pos = pos + value
        if new_pos > 25:
          new_pos = new_pos - 26
      elif choice == 2:
        new_pos = pos - value
        if new_pos < 0:
          new_pos = new_pos + 26
      else:
        print("invalid choice")
      new_msg += alphabet[new_pos]
    else:
      new_msg += i
  print("the converted message is="+new_msg)

c=1
while c == 1:
  choice = int(input("Type 1 to encrypt, type 2 to decrypt:\n"))
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
  caesar(text,shift,choice)
  c = int(input("Do you want to repeat?\n1)Yes\n2)No"))




