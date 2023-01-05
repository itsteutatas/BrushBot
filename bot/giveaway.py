import asyncio
import aiomysql
import time
import datetime
from mysql.connector import Error
localConfig = {
        'user': 'test',
        'password': '',
        'host': '127.0.0.1',
        'db': 'giveawaydb'
}


async def start():
    cn = await aiomysql.connect(**localConfig)
    cr = cn.cursor()
    cr.execute(f"CREATE table participants(participantID int NOT NULL AUTO_INCREMENT,participantNAME VARCHAR(60),PRIMARY KEY (participantID))")
    cn.commit()
    cn.close()

async def participate(name):

    cn = await aiomysql.connect(**localConfig)
    cr = cn.cursor()

    cr.execute(f"SELECT * from participants where participantNAME = '{name}'")
    if cr.fetchall():
        pass
    else:
        cr.execute(f"INSERT INTO participants(participantID, participantNAME) VALUES (0, '{name}')")

    cn.commit()

    cn.close()


async def end():
    cn = await aiomysql.connect(**localConfig)
    cr = cn.cursor()

    cr.execute("SELECT participantNAME FROM participants ORDER BY RAND() LIMIT 1")
    winner = cr.fetchone()

    cr.execute("DROP Table participants")
    cn.commit()

    cn.close()
    return winner

if __name__ == '__main__':
    participate()
    end()
    start()
