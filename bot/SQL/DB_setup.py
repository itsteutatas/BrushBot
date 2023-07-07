import aiomysql
import asyncio
import warnings


import bot.SQL.dbconfig as dbcfg



class setup():
    def __init__(self):
        pass

    async def test(self):

        # Checks if we are able to connect to the database in the first place
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"],
                                      dbcfg.localconfig["password"])
        curr = await conn.cursor()

        print("Connection succeeded")

        await conn.commit()
        conn.close()

    async def create_database(self):
        # Connects and creates database if it does not exist
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"],
                                      dbcfg.localconfig["password"])
        curr = await conn.cursor()

        await curr.execute(f"CREATE DATABASE IF NOT EXISTS {dbcfg.localconfig['db']}")

        await conn.commit()
        conn.close()

    async def create_participants(self):
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])
        curr = await conn.cursor()

        await curr.execute("DROP TABLE IF EXISTS participants")
        await curr.execute(f"CREATE TABLE participants(participantID int NOT NULL AUTO_INCREMENT,participantNAME VARCHAR(60),PRIMARY KEY (participantID))")

        await conn.commit()
        conn.close()


async def main():
    warnings.simplefilter("ignore")
    setup_instance = setup()

    await setup_instance.test()
    await setup_instance.create_database()
    print("Database setup complete")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())