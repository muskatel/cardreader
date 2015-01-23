#!/usr/bin/python
#

import lcd
import nfc
import db

def main():
    lcd.init()
    nfc.init()
    db.init()
    lcd.screen_write('Ready...', '')
    
    try:
        while True:
            c = raw_input('\n\tOptions\n(C)reate new record\n(S)can card\nOption (c/S): ')
            if c.lower() is 'c':
                lcd.screen_write('Enter details', '')
                name, surname, studno, card, pin = '', '', '', '', ''
                while True:
                    name, surname, studno, card, pin = promptCreateRecord()
                    b = raw_input ('Is this information correct? (Y/n): ')
                    if b.lower() == 'n':
                        continue
                    else:
                        break
                ret = db.create_record(name=name, surname=surname, studno=studno, card=card, pin=pin)
                if ret:
                    lcd.screen_write('Record "%s"' % studno, 'created.') 
                else:
                    lcd.screen_write('Database error')
                    break

            else:
                count = 0
                while count < 10:
                    lcd.screen_write('Scanning...')
                    card = nfc.read_card()
                    data = db.get_record(card=card)
                    lcd.screen_write(data['name'], data['surname'])
                    count += 1
    finally:
        lcd.cleanup()
        nfc.cleanup()
        db.cleanup()

def promptCreateRecord():
    a = raw_input('Name: ')
    b = raw_input('Surname: ')
    c = raw_input('Student Number: ')
    print 'Please scan your card'
    d = nfc.read_card()
    e = raw_input('Please enter your pin: ')
    return (a, b, c, d, e)
        
    

if __name__ == '__main__':
    main()
