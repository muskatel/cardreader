import sqlite3 as sql
import encrypt

DB_INIT = False
conn = None

def init():
    global conn, DB_INIT
    conn = sql.connect('data.db')
    conn.row_factory = sql.Row
    drop_records()
    create_table()
    DB_INIT = True
    
def drop_records():
    conn.executescript(open('sql/purge.sql', 'r').read())
    
def create_table():
    conn.executescript(open('sql/create.sql', 'r').read())
    conn.commit()

# I am aware that this is horribly insecure, don't bitch at me about it
def get_record(**kwargs):
    if not DB_INIT:
        init()
    if kwargs['card']:
        cur = conn.execute("SELECT * FROM `User` WHERE 1=1 AND `card_id` LIKE '%s'" % encrypt.encrypt(kwargs['card']))
        return cur.fetchone()
    elif kwargs['studno']:
        cur = conn.execute("SELECT * FROM `User` WHERE 1=1 AND `student_id` LIKE '%s'" % kwargs['studno'])
        return cur.fetchone()

def create_record(**kwargs):
    if not DB_INIT:
        init()
    if kwargs['name'] and kwargs['surname'] and kwargs['studno'] and kwargs['card'] and kwargs['pin']:
        data = (kwargs['name'], kwargs['surname'], kwargs['studno'], encrypt.encrypt(kwargs['card']), encrypt.encrypt(kwargs['pin']))
        conn.execute("INSERT INTO `User` (name, surname, student_id, card_id, pin) VALUES ('%s', '%s', '%s', '%s', '%s');" % data)
        conn.commit()
        return True
    else:
        return False
    
def auth_pin(user, pin):
    secret = user['pin']
    return secret == encrypt.encrypt(pin)

def auth_card(card, pin):
    user = get_record(card=card)
    if user:
        return auth_pin(user, pin)
    return False
    
def log_scan(card, pin):
    if not DB_INIT:
        init()
    if card:
        user = get_record(card=card)
        if not user:
            return None
        if auth_pin(user, pin):
            conn.execute("INSERT INTO `Log` (card_id, timecode) VALUES ('%s', datetime('now'));" % encrypt.encrypt(card))
            conn.commit()
            return user
        else:
            return None
    else:
        return None
        
def cleanup():
    if conn:
        conn.commit()
        conn.close()