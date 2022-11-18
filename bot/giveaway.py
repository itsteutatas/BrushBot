import mysql.connector
import time
import datetime


def collect():
    localConfig = {
        'user': 'test',
        'password': '',
        'host': '127.0.0.1',
        'database': 'giveawaydb'
    }

    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()
    print('connected')
    name = 0
    follower = 1
    cr.execute(f"INSERT INTO participants(participantID, participantNAME, follower) VALUES (1, '{name}', {follower})")
    cr.execute("SELECT * FROM participants")
    res = cr.fetchall()
    print(res[-1])
    cn.commit()
    time.sleep(2)

    cn.close()
    exit()
