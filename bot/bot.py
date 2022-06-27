from irc.bot import SingleServerIRCBot
from requests import get

NAME="BrushBot"
OWNER="teutatas"
class Bot(SingleServerIRCBot):
    def  __init__(self):
        self.HOST="irc.chat.twitch.tv"
        self.PORT=6667
        self.USERNAME=NAME.lower()
        self.CLIENT_ID="7n9tcv2652ggjo96meo6p199opqd3h"
        self.TOKEN="851l4q6i3cnzmfrzcyfm2wynodzmvw"
        self.CHANNEL="#{OWNER}"

        url = "https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID":self.CLIENT_ID,"Accept":"application/vnd.twitchtv.v5+json"}
        resp = get(url,headers-headers).json()
        self.channel_idresp["users"][0]["_id"]

        super().__init__([(self.HOST,self.PORT,"oauth:{self.TOKEN")],self.USERNAME,self.USERNAME)

    def on_welcome(self, cxn, event):
        for rep in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)

if __name__ == "__main__":
    bot = Bot()
    bot.start()