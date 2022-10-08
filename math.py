from termcolor import colored
import math
import time
import sys
import random

# Start
print(text(Color.BLUE) + "Homework Helper")
print(Formatting.END + "Algebra 1 + Geometry")

# Options
print(text(Color.INDIGO) + "[1]" + Formatting.END + "- Addition")
print(text(Color.INDIGO) + "[2]" + Formatting.END + "- Multiplication")
print(text(Color.INDIGO) + "[3]" + Formatting.END + "- Factorials")
print(text(Color.INDIGO) + "[4]" + Formatting.END + "- Pythagorean theorem")
print(
  text(Color.INDIGO) + "[5]" + Formatting.END +
  "- String Stats (Mean, Median, Mode)")
print(text(Color.INDIGO) + "[6]" + Formatting.END + "- Quadratic Formula")
print(" ")
type = input("Which would you like to choose? ")


def addition():
  print("Addition Selected")
  a1 = input("Input your first value ")
  a2 = input("Input your second value ")
  # Convert string into int
  aa1 = int(a1)
  aa2 = int(a2)
  # Output
  aanswer = aa1 + aa2
  print(aa1, "+", aa2, "=", aanswer)


def multiplication():
  print("Multiplication Selected")
  m1 = input("Input your first value ")
  m2 = input("Input your second value ")
  # Convert string into int
  am1 = int(m1)
  am2 = int(m2)
  # Output
  manswer = am1 * am2
  print(am1, "*", am2, "=", manswer)


def factorials():
  print("Factorials Selected")
  print("Type in your value without the !")
  fac = input()
  fac = int(fac)

  # Begin
  product = 1
  count = fac

  while count != 1:
    product = product * count
    count = count - 1

  print(product)

  # END


def ptheorem():
  print("Pythagorean Theorem Selected")
  print(" ")
  typ = input("Which side are you trying to find? (A, B, C) ")

  if typ == "a":
    abb = input("What is your B value? ")
    abb = int(abb)
    ac = input("What is your C value? ")
    ac = int(ac)
    print("a^2  + ", abb, "^2  = ", ac, "^2")
    b = abb**2
    c = ac**2
    bc = c - b
    asb = math.sqrt(bc)
    print(back(Color.GREEN_DARK) + "Answer: ", asb)


# Run

if type == "1":
  addition()

if type == "2":
  multiplication()

if type == "3":
  factorials()

if type == "4":
  ptheorem()
