import random
import sys
import time

line_characters = r'\-|/_'

sys.stdout.write('\r' + (a := random.choice(line_characters)) + '   ')

s = 1

time.sleep(s)

sys.stdout.write('\r ' + (b := random.choice(line_characters)) + '  ')
time.sleep(s)

sys.stdout.write('\r  ' + (c := random.choice(line_characters)) + ' ')
time.sleep(s)

sys.stdout.write('\r   ' + (d := random.choice(line_characters)) + '')
time.sleep(s)

sys.stdout.write('\r    The sequence is revealed after 8 seconds.\n\r    ')

s = 8

time.sleep(s)

sys.stdout.write('\r' + a + b + c + d)
