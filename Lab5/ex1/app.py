import utils
import sys
while True:
    nr = input("nr: ")
    if nr == 'q':
        sys.exit(1)
    elif nr.isnumeric() == False:
        print("Input not number")
        continue
    nr = int(nr)
    utils.process_item(nr)