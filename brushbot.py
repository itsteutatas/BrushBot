from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token='q0ti5qlqia4bxuuiruy4ua76gn8hn8', prefix='!', initial_channels=['frica_friggie'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        if ctx.auther.name == 'MiniMatties':
            

        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()