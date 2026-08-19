import termios
import tty
from sys import stdin, stdout
from time import sleep

attrs = termios.tcgetattr(stdin)

tty.setcbreak(0)

try:
  while True:
    value = stdin.read(1)

    if value == '':
      continue

    value_ascii_code = ord(value)

    if value_ascii_code == 3:
      break

    if 49 <= value_ascii_code <= 57:
      for _ in range(value_ascii_code - 48):
        stdout.write('\7')
        stdout.flush()
        sleep(0.2)
finally:
  termios.tcsetattr(stdin, termios.TCSADRAIN, attrs)
