from twitchio.ext import commands
import aiomysql

import bot.oauthconfig as oauth
import bot.config as cfg
import bot.SQL.DB_setup as DB_setup
import bot.SQL.DB_search as DB_search
import bot.SQL.DB_query as DB_query



class brushbot(commands.Bot):


    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=oauth.oauth, prefix='!', initial_channels=cfg.i_channel_list)
        self.giveaway_bool = False


        # Set up the database connection and create the DataBase if it doesn't exist
        self.loop.create_task(DB_setup.main())

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


    # final state [shoutout command]
    @commands.command(name='so')
    async def shoutout(self, ctx: commands.Context, name: str):
        await ctx.send(f'Check out {name} over at twitch.tv/{name}')

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send(f'test')

    # final state [discord command]
    @commands.command()
    async def discord(self, ctx: commands.Context):
        print('test')
        await ctx.send("None")

    # teststate [giveaway]
    @commands.command()
    async def giveaway(self, ctx: commands.Context):
        if self.giveaway_bool:
            if ctx.author.name in cfg.admin_n_list:
                await ctx.send(f'Giveaway already running')
                # TODO: think on this idea needs to exclude x streamer on their stream only

            else:
                await ctx.send(f'There is a giveaway running right now')
            """
            else:
                participant_name = ctx.author.name
                await DB_query.query.add_participant(participant_name)
            """
        else:
            if ctx.author.name in cfg.admin_n_list:
                await DB_setup.setup().create_participants()
                await ctx.send(f'GivePLZ Giveaway TakeNRG')
                self.giveaway_bool = True
                return
            else:
                ctx.send(f'There is no giveaway running')

    @commands.command()
    async def endgiveaway(self, ctx: commands.Context):
        if ctx.author.name in cfg.admin_n_list:
            # Check if a giveaway is currently active
            if not self.giveaway_bool:
                await ctx.send('There is currently no active giveaway.')
                return

            # Pick a winner from the list of participants
            winner = await DB_search.search().get_winner()
            winner = str(winner).translate( { ord(i): None for i in "'(),"} )
            # Announce the winner in chat
            await ctx.send(f'Congratulations {winner}! You have won the test!')

            # Reset the giveaway state
            self.giveaway_bool = False


    @commands.command(name='join')
    async def join_giveaway(self, ctx: commands.Context):
        participant_name = ctx.author.name
        await DB_query.query().add_participant(participant_name)




bot = brushbot()
bot.run()