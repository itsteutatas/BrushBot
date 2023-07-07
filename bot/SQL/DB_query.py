import aiomysql
import asyncio


import bot.SQL.dbconfig as dbcfg




class query():
    def __init__(self):
        pass

    async def add_participant(self, participant_name):
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])
        curr = await conn.cursor()

        # Check if the participant already exists in the table
        await curr.execute("SELECT * FROM participants WHERE participantNAME = %s", (participant_name,))
        result = await curr.fetchall()
        if len(result) > 0:
            # Participant already exists, do nothing
            pass
        else:
            # Participant does not exist, add them to the table
            await curr.execute(f"INSERT INTO participants(participantID, participantNAME) VALUES (0, %s)", (participant_name,))

        await conn.commit()
        conn.close()