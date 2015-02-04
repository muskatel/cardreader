#!/usr/bin/python
#

import prompts
import lcd
import nfc

def main():
    lcd.init()
    nfc.init()
    
    try:
        while True:
            lcd.screen_write('Ready...', '')
            c = raw_input(prompts.prompt).lower()
            if c == 'q':
                break
            prompts.doAction(c)
    finally:
        lcd.cleanup()
        nfc.cleanup()

if __name__ == '__main__':
    main()
