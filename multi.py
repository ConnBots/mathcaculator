import sys
import time
import random
from random import randrange
from termcolor import colored

# Start

print("First Number:")
fn = input("")
print("Second Number:")
sn = input("")

answer = (int(fn) * int(sn))
time.sleep(1)
print(colored(answer,'yellow'))