from twitchio.ext import commands, routines, sounds
import pyaudio


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token='av9ea9ynv6d1xbturc6zzkiwz5mueu', prefix='!', initial_channels=['frica_friggie'])
        self.event_player = sounds.AudioPlayer(callback=self.player_done)

    async def player_done(self):
        print('Finished playing song!')

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    user = input()
    #final state [shoutout command]
    @commands.command()
    async def so(self, ctx: commands.Context, user):
        user1 = user.replace('@', '')
        await ctx.send(f'check out {user} over at https://www.twitch.tv/{user1}')


    #prestate [giveaway]
    #@commands.command()
    #async def giveaway(self):



    # final state preWeb [discord command]
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("https://discord.gg/u2Jk8eBzPv")

    #prestate [custom sound appearance]
    @commands.command()
    async def hey(self, ctx: commands.Context, message):
        if message.author.name.lower() == 'teutatas':
            sound = sounds.Sound(source='Tene.mp3')
            self.player.play(sound)
            await ctx.send("messages")

    # test state preWeb [discord routine]
    @routines.routine(minutes=20)
    async def discord1(self, ctx: commands.Context):
        await ctx.send("https://discord.gg/u2Jk8eBzPv")
    discord1.start()

    @commands.command()
    async def hello(self) -> None:
        # This is just an example only...
        # Playing a sound on every message could get extremely spammy...
        sound = sounds.Sound(source='Tene.mp3')
        self.event_player.play(sound)



bot = Bot()
bot.run()