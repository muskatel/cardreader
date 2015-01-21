#!/usr/bin/python
#

import lcd
import nfc

def main():
    read = 0
    lcd.init()
    nfc.init()
    lcd.screen_write('Ready...', '')
    
    while True:
        card = nfc.read_card()
	read += 1
        lcd.screen_write('Card: ' + card, 'Count: ' + str(read))

if __name__ == '__main__':
    main()
