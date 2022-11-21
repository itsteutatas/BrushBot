import mysql.connector
import time
import datetime
from mysql.connector import Error

def participate():
    localConfig = {
        'user': 'test',
        'password': '',
        'host': '127.0.0.1',
        'database': 'giveawaydb'
    }

    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()


    name = ''
    cr.execute(f"INSERT INTO participants(participantID, participantNAME) VALUES (1, '{name}')")
    cr.execute("SELECT * FROM participants")
    res = cr.fetchall()
    print(res[-1])
    cn.commit()
    time.sleep(2)

    cn.close()
    exit()

if __name__ == '__main__':
    participate()
