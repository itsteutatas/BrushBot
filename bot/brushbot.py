from twitchio.ext import commands, routines
import asyncio
import dbconfig as dbcfg
import oauthconfig as oauth
import aiomysql


class giveaways():
    async def start(self):
        conn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])

        print("connected")

        cur = await conn.cursor()
        await cur.execute("DROP Table participants")
        await cur.execute(f"CREATE table participants(participantID int NOT NULL AUTO_INCREMENT,participantNAME VARCHAR(60),PRIMARY KEY (participantID))")
        await conn.commit()
        conn.close()

    async def participate(name):

        cn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])
        cr = cn.cursor()

        cr.execute(f"SELECT * from participants where participantNAME = '{name}'")
        if cr.fetchall():
            pass
        else:
            cr.execute(f"INSERT INTO participants(participantID, participantNAME) VALUES (0, '{name}')")

        cn.commit()

        cn.close()

    async def end(self):
        cn = await aiomysql.connect(dbcfg.localconfig["host"], dbcfg.localconfig["user"], dbcfg.localconfig["password"], dbcfg.localconfig["db"])
        cr = cn.cursor()

        cr.execute("SELECT participantNAME FROM participants ORDER BY RAND() LIMIT 1")
        winner = cr.fetchone()
        cn.commit()

        cn.close()
        return winner



# TODO: fix bot not sending messages/responses oauth token is not the problem
class brush(commands.Bot):
    giveaway_bool = False

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=oauth.oauth, prefix='!', initial_channels=['teutatas'])
        # self.event_player = sounds.AudioPlayer(callback=self.player_done)

    # async def player_done(self):
    # print(f'Finished playing song!')

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # final state [shoutout command]
    @commands.command()
    async def so(self, ctx: commands.Context, name: str):
        await ctx.send(f"Check out {name} over at twitch.tv/{name}")

    # teststate [giveaway]
    @commands.command()
    async def giveaway(self, ctx: commands.Context):
        if self.giveaway_bool:
            await ctx.send(f'Giveaway already running')
        else:
            if ctx.author.name == 'teutatas':
                await ctx.send(f'GivePLZ Giveaway TakeNRG')
                await giveaways.start(self)
                self.giveaway_bool = True
                return

    @commands.command()
    async def endgiveaway(self, ctx: commands.Context):
        if ctx.author.name == 'teutatas':
            if not self.giveaway_bool:
                ctx.send(f'No giveaway running')
            else:
                use = str(giveaways.end)
                use = use.replace('(', '')
                use = use.replace(',)', '')
                await ctx.send(f'TakeNRG Congratulations {use} you won the giveaway GivePLZ')
                self.giveaway_bool = False
                return

    @commands.command()
    async def join(self, ctx: commands.Context):
        if self.giveaway_bool == True:
            name = ctx.author.name

            await giveaways.participate(name)

            return name

    # final state preWeb [discord command]
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("https://discord.gg/u2Jk8eBzPv")

    # test state preWeb [discord routine]
    @routines.routine(minutes=1)
    async def discord1(self, ctx: commands.Context):
        await ctx.send("https://discord.gg/u2Jk8eBzPv")

    @commands.command()
    async def docs(self, ctx: commands.Context):
        await ctx.send("Check out the diffrent features over at https://tinyurl.com/3hshdmjs")

    # prestate [custom sound appearance]
    """@commands.command()
    async def hey(self, ctx: commands.Context, message):
        if message.author.name.lower() == 'teutatas':
            sound = sounds.Sound(source='Tene.mp3')
            self.player.play(sound)
            await ctx.send("messages")
    """


"""
    @commands.command()
    async def hello(self) -> None:
        # This is just an example only...
        # Playing a sound on every message could get extremely spammy...
        sound = sounds.Sound(source='Tene.mp3')
        self.event_player.play(sound)
"""

bot = brush()
# bot.discord1.start()
bot.run()

