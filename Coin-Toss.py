#We're gonna use random module here
import random

#We just gonna use this directly because it doesn't require any input
coin = random.randint (0, 1)
if coin == 0:
    print("Tails")
else:
    print("Heads")