import random
import word
import ascii_art

# random words list
# word_list = ["aardvark", "baboon", "camel","apple","banana",]

print(ascii_art.logo)

index = random.randint(1, len(word.word_list))

word = word.word_list[index - 1]

blank = []
for n in range(len(word)):
    blank.extend("_")

# the representation of lives

print("********************************RULES**********************************")
print("\t1)You can save a man from getting hanged.")
print("\t2)Please choose random letters to fill this blank.")
print("\t3)Each wrong attempt would cost you 1 life.")
print("\t4)You have lives until the man dies. please save him from dying.")
print("\t5)If you enter an incorrect letter twice, 2 lives will be deducted.")
print("\t6)No life would be deducted when you enter the correct letter twice")
print("***********************************************************************")
for n in range(0, len(word)):
    print(blank[n], end=" ")
print("\n")

# for i in word:
#   if guess == i:
#     print("\nright")
#   else:
#     print("\nwrong")

lives = 6
while '_' in blank:
    g = input("enter a charecter=")
    guess = g.lower()
    for pos in range(len(word)):
        letter = word[pos]
        if letter == guess:
            blank[pos] = letter
    if guess not in word:
        print(ascii_art.stages[lives])
        lives = lives - 1
        if lives >= 0:
            print("\nremaining lives=", lives)

    for n in range(0, len(word)):
        print(blank[n], end=" ")
    if lives < 0:
        print("\nOops you lose! ")
        break

    print("\n")

if lives > 0:
    print("yay!! you won. The man is alive now ")

print("the answer is-", word)