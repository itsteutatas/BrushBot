import mysql.connector
import time
import datetime
from mysql.connector import Error
localConfig = {
        'user': 'test',
        'password': '',
        'host': '127.0.0.1',
        'database': 'giveawaydb'
}


def start():
    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()
    cr.execute(f"CREATE table participants(participantID int NOT NULL AUTO_INCREMENT,participantNAME VARCHAR(60),PRIMARY KEY (participantID))")
    cn.commit()
    time.sleep(2)
    cn.close()
def participate(name):

    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()

    cr.execute(f"SELECT * from participants where participantNAME = '{name}'")
    if cr.fetchall():
        pass
    else:
        cr.execute(f"INSERT INTO participants(participantID, participantNAME) VALUES (0, '{name}')")

    cn.commit()
    time.sleep(2)

    cn.close()


def end():
    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()

    cr.execute("SELECT participantNAME FROM participants ORDER BY RAND() LIMIT 1")
    winner = cr.fetchone()

    cr.execute("DROP Table participants")
    cn.commit()
    time.sleep(2)

    cn.close()
    return winner

if __name__ == '__main__':
    participate()
    end()
    start()
