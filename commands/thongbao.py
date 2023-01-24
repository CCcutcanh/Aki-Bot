from discord.ext import commands
import discord
from command.cache.list_color import list_color
import random
class Thongbao(commands.Cog):
    config = {
        "name": "thongbao",
        "desc": "gửi thông báo bằng embed đến 1 kênh của server",
        "use": "thongbao",
        "author": "King.",
        "event": False
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def thongbao(self,ctx):
        try:
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel

            await ctx.send('cậu muốn tiêu đề là gì? 📰')
            title = await self.bot.wait_for('message', check=check)
        
            await ctx.send('cậu muốn nội dung của tin nhắn là gì? 💬')
            desc = await self.bot.wait_for('message', check=check)

            await ctx.send('Nhập id channel cậu muốn gửi đến? 📻')
            channelID1 = await self.bot.wait_for('message',check=check)
            channelID = int(channelID1.content)

            await ctx.send('cậu có muốn muốn gửi ảnh(LINK ẢNH) cùng với tin nhắn không? nếu không muốn gửi cùng thì gõ `none` 📷')
            picurl = await self.bot.wait_for('message', check=check)
            if picurl.content == "none":
                channel = self.bot.get_channel(channelID)
                embed = discord.Embed(title=title.content, description=desc.content, color=random.choice(list_color))
                await channel.send(embed=embed)
            else:
                channel = self.bot.get_channel(channelID)
                embed = discord.Embed(title=title.content, description=desc.content, color=random.choice(list_color))
                embed.set_image(url=picurl.content)
                await channel.send(embed=embed)
        except Exception as e:
            print(e)
    


async def setup(bot):
    await bot.add_cog(Thongbao(bot))
