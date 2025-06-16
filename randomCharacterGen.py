import random
import time

lineWidth = 120
curLines = {}
chars = ['#', '*', '&', '$', '%', '@']

for i in range(90000):
  for j in range(lineWidth):
    a = False
    if j in curLines:
      print(chars[random.randint(0, len(chars)-1)], end = "")
      a = True
      curLines[j] -=1
      
      if curLines[j] == 0:
        del curLines[j]
    elif random.randint(0, 240) == 0:
      curLines[j] = random.randint(0,50)

    if not a:
      print(" ", end = "")
  print()
  time.sleep(0.02)
      
        
