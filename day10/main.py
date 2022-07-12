# Calculator
from art import logo
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def Calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  ch=True
  c=0
  while ch:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    c=int(input("Enter 1 to continue and 2 to enter a new calculation and 3 to exit ="))
    if c == 1:
      num1=answer
      ch=True
    elif c== 2:
      ch=False
      Calculator()
    else:
      ch=False

Calculator()




