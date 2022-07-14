from art import logo
import random
# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card():
    c_1 = random.choice(cards)
    c_2 = random.choice(cards)
    return c_1, c_2


def score(crd):
    sc = 0
    for i in crd:
        sc = sc + i
    return sc


def winner(user, comp):
    if user == 21:
        return 1
    elif comp == 21:
        return 2
    elif user == comp:
        return 3
    if user < 21:
        if comp > 21:
            return 1
        elif user > comp:
            return 1
    if comp < 21:
        if user > 21:
            return 2
        elif comp > user:
            return 2
    else:
        return 3


def play():
    print(logo)
    u_cards = list(card())
    c_cards = list(card())

    u_score = score(u_cards)
    c_score = score(c_cards)

    print(u_cards, end=" ")
    print("the user score is:" + str(u_score))
    print(f"Computer's First Card is={c_cards[0]}")
    while c_score <= 16:
        c_cards.append(random.choice(cards))
        c_score = score(c_cards)

    # print(c_score)
    while 1:
        ch = int(input("Press 1 to add another card and 2 to check your result="))
        if ch != 1:
            break
        u_cards.append(random.choice(cards))
        print(f"\nthe new set of user cards is{u_cards}")
    u_score = 0
    for i in u_cards:
        u_score = u_score + i
    # print(u_cards)
    # print(u_score)
    result = winner(u_score, c_score)
    print(f"\nThe user cards are:{u_cards} and the computer cards are:{c_cards}")
    if result == 1:
        print(f"User wins with score {u_score}")
    elif result == 2:
        print(f"Computer wins with a score of{c_score}")
    elif result == 3:
        print(f"Draw with user score as{u_score} and computer score as {c_score}")


while 1:
    c = int(input("Please enter 1 to Play Blackjack and 2 if you don't want to play Blackjack\n="))
    if c == 1:
        # clear()
        play()
    else:
        print("You Quit")
        break
