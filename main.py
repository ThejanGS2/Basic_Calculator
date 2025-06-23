def add(a, b):
  """Adds two numbers."""
  return a + b

def subtract(a, b):
  """Subtracts two numbers."""
  return a - b

def multiply(a, b):
  """Multiplies two numbers."""
  return a * b

def divide(a, b):
  """Divides two numbers, handling division by zero."""
  try:
      return a / b
  except Exception as e:
      print(e)
      return None

def power(a, b):
  """Calculates the power of a number."""
  return a ** b

def remainder(a, b):
  """Calculates the remainder of a division."""
  return a % b

def get_number_input(prompt):
  """Gets a valid number input from the user."""
  while True:
      num_str = input(prompt)
      print(num_str)
      if num_str.endswith('$'):
          return '$'
      if num_str.endswith('#'):
          return '#'
      try:
          return float(num_str)
      except ValueError:
          print("Not a valid number, please enter again")

def select_op(choice):
  """Selects the operation and handles user input."""
  if choice == '#':
      return -1
  elif choice == '$':
      return 0
  elif choice in ('+', '-', '*', '/', '^', '%'):
      num1 = get_number_input("Enter first number: ")
      if num1 in ('$', '#'):
          return 0 if num1 == '$' else -1

      num2 = get_number_input("Enter second number: ")
      if num2 in ('$', '#'):
          return 0 if num2 == '$' else -1

      if choice == '+':
          print(num1, "+", num2, "=", add(num1, num2))
      elif choice == '-':
          print(num1, "-", num2, "=", subtract(num1, num2))
      elif choice == '*':
          print(num1, "*", num2, "=", multiply(num1, num2))
      elif choice == '/':
          print(num1, "/", num2, "=", divide(num1, num2))
      elif choice == '^':
          print(num1, "^", num2, "=", power(num1, num2))
      elif choice == '%':
          print(num1, "%", num2, "=", remainder(num1, num2))
      return 1
  else:
      print("Unrecognized operation")
      return 1

# Main loop
while True:
  print("\nSelect operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  result = select_op(choice)

  if result == -1:
      print("Done. Terminating")
      exit()
  elif result == 0:
      continue
