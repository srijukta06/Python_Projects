'''
Your target time is 4 seconds.
---Press Enter to Begin---
...Press Enter again after 4 seconds...
'''

import time
import random

def waiting_game():
  target = random.randint(2, 4) # target seconds to wait 
  print(f'\nYour target time is {target} seconds')

  input(' ---Press Enter to Begin--- ')
  start = time.perf_counter()

  input(f'\n...Press Enter again after {target} seconds...') 
  elapsed = time.perf_counter() - start

  print(f'\nElapsed time: {elapsed :.3f} seconds')
    if elapsed == target:
      print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
      print(f'({target - elapsed :.3f} seconds too fast)')
    else:
      print(f'({elapsed - target :.3f} seconds too slow)')
