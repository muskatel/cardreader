import nfc
import lcd
import urllib2
import settings

prompt = '''\n\tOptions:
            Add Member to (G)roup
            Mark (E)vent Attendance
            (Q)uit
            Option (g/e/Q): '''
            
def doAction(c):
    if c == 'g':
        doAddMember()
    elif c == 'e':
        doAttend()
        
def doAddMember():
    group = raw_input('Group Name: ')
    fee = raw_input('Fee: R')
    while True:
        lcd.screen_write('Add Member:', group)
        card = nfc.read_card()
        url = 'http://%s:%s/%s' % (settings.getSettings().parseString('API.Host'),
                                   settings.getSettings().parseString('API.Port'),
                                   settings.getSettings().parseString('API.AddMember') % group,
                                   )
        response = urllib2.urlopen(url, {'group_name' : group,
                                        'user_id' : card,
                                        'paid' : fee,
                                        },
                                  timeout=10)
        print response
        lcd.screen_write('Member added', '')
        option = raw_input('Add Another? (Y/n): ').lower()
        if option == 'n':
            break

def doAttend():
    group = raw_input('Group Name: ')
    event = raw_input('Event ID: ')
    while True:
        lcd.screen_write('Attend Event:', event)
        card = nfc.read_card()
        url = 'http://%s:%s/%s' % (settings.getSettings().parseString('API.Host'),
                                   settings.getSettings().parseString('API.Port'),
                                   settings.getSettings().parseString('API.AttendEvent') % (group, event),
                                   )
        response = urllib2.urlopen(url, {'student_id' : card
                                        },
                                  timeout=10)
        print response
        lcd.screen_write('Attendance', 'Marked')
        option = raw_input('Add Another? (Y/n): ').lower()
        if option == 'n':
            break