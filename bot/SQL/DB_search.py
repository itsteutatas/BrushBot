import aiomysql
import asyncio


import bot.SQL.dbconfig as dbcfg




class search():
    def __init__(self):
        pass

    async def get_winner(self):
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])
        curr = await conn.cursor()

        await curr.execute("SELECT participantNAME FROM participants ORDER BY RAND() LIMIT 1")
        winner = await curr.fetchone()

        await conn.commit()
        conn.close()

        return winner