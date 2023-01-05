from twitchio import http
from twitchio.ext import commands, routines, sounds
import pyaudio
import random
import sys
import time
import asyncio
from giveaway import participate, end, start


oauth = "av9ea9ynv6d1xbturc6zzkiwz5mueu"


class brush(commands.Bot):

    giveaway_bool = False
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=oauth, prefix='!', initial_channels=['teutatas'])
        #self.event_player = sounds.AudioPlayer(callback=self.player_done)

    #async def player_done(self):
        #print(f'Finished playing song!')

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
            ctx.send(f'Giveaway already running')
        else:
            await ctx.send(f'GivePLZ Giveaway TakeNRG')
            if ctx.author.name == 'teutatas':
                await start()
                self.giveaway_bool = True
                return

    @commands.command()
    async def endgiveaway(self, ctx: commands.Context):
        if ctx.author.name == 'teutatas':
            if not self.giveaway_bool:
                ctx.send(f'No giveaway running')
            else:
                use = str(end())
                use = use.replace('(', '')
                use = use.replace(',)', '')
                await ctx.send(f'TakeNRG Congratulations {use} you won the giveaway GivePLZ')
                self.giveaway_bool = False
                return

    @commands.command()
    async def join(self, ctx: commands.Context):
        if self.giveaway_bool == True:

            name = ctx.author.name
            await participate(name)

            return

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
#bot.discord1.start()
bot.run()

