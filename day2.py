#tip calcultor
print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))
per = 1 + (0.01 * tip)
# print(per)
total = bill * per
per_person = round(total / people, 2)
print(f"the per person cost is ${per_person} ")
