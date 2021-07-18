import discord
token = "token"
client = discord.Client()

@client.event
async def on_ready():
    print('판매 준비 끝')
    print(client.user)
    print("==================")


@client.event
async def on_message(message):

    if message.content == "GTA5":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 새계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』 \n\n 에픽 게임즈 새계정 \n\n 『𝑷𝒓𝒊𝒄𝒆』 10,000 \n\n\n 『문화상품권 / 𝐂𝐮𝐥𝐭𝐮𝐫𝐞 𝐋𝐚𝐧𝐝』 \n\n 에픽 게임즈 새계정 \n\n『𝑷𝒓𝒊𝒄𝒆』 13,000 \n\n\n @everyone")

        embed.set_image(url="https://media1.tenor.com/images/a3925c5320d32423b78a1958032f30b4/tenor.gif?itemid=16618310")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "오버워치":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 새계정 / 랜덤계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n[ 해외계정 미배치 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  25,000\n\n[ 오버워치 1레벨 새계정 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  18,000\n\n[ 25레벨 미만 해외 랜덤 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  9000\n\n[ 25레벨 이상 해외 랜덤 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  18,000\n\n\n『문화상품권 / 𝐂𝐮𝐥𝐭𝐮𝐫𝐞 𝐋𝐚𝐧𝐝』\n\n[ 해외계정 미배치 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  28,000\n\n[ 오버워치 1레벨 새계정 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  21,000\n\n[ 25레벨 미만 해외 랜덤 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  13,000\n\n[ 25레벨 이상 해외 랜덤 ]\n\n『𝑷𝒓𝒊𝒄𝒆』  21,000\n\n\n @everyone ")
        embed.set_image(url="https://cdn.discordapp.com/attachments/861261550546321449/861261576840151040/gif.gif")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "발로란트":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 새계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』 150\n 국적 🇯🇵 \n\n\n회수 가능성 0%\n정보 변경 가능\n\n\n@everyone")
        embed.set_image(url="https://cdn.discordapp.com/attachments/861261550546321449/861261583744761876/val.gif")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "발로란트2":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 랜덤계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』 150\n\n\n회수 가능성 ⭕️\n\n\n @everyone")
        embed.set_image(url="https://cdn.discordapp.com/attachments/861261550546321449/861261583744761876/val.gif")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "넷플릭스":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 랜덤계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』 20\n\n\n@everyone")
        embed.set_image(url="https://i.pinimg.com/originals/61/d1/42/61d14291ee3bd48dc9c6a68e4a3a442d.gif")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "배그":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 새계정 ]", description="계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』  15,000\n\n\n『문화상품권 / 𝐂𝐮𝐥𝐭𝐮𝐫𝐞 𝐋𝐚𝐧𝐝』\n\n『𝑷𝒓𝒊𝒄𝒆』  18,000\n\n\n@everyone")
        embed.set_image(url="https://media1.tenor.com/images/82a585aa177c6eb399e2864a509147b3/tenor.gif?itemid=18625783")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "배그2":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 랜덤계정 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』  9000\n\n\n『문화상품권 / 𝐂𝐮𝐥𝐭𝐮𝐫𝐞 𝐋𝐚𝐧𝐝』\n\n『𝑷𝒓𝒊𝒄𝒆』  13,000\n\n\n@everyone")
        embed.set_image(url="https://media1.tenor.com/images/82a585aa177c6eb399e2864a509147b3/tenor.gif?itemid=18625783")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "롤":
        embed = discord.Embed(color=discord.Colour.red(), title = "[ 한국랜계 ]", description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』  3500\n\n\n[ 한국 랜계 x 30 ] \n\n『𝑷𝒓𝒊𝒄𝒆』  5500 \n\n @everyone")
        embed.set_image(url="https://media1.tenor.com/images/d6bc1b52c2f93aa1e59478ef0fba1993/tenor.gif?itemid=8430935")
        embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "롤2":
        embed = discord.Embed(color=discord.Colour.red(), title="[ 해외랜계 ]",description="『계좌 / 𝐀𝐜𝐜𝐨𝐮𝐧𝐭』\n\n『𝑷𝒓𝒊𝒄𝒆』  200\n\n\n[ 해외 랜계 x 30 ] \n\n『𝑷𝒓𝒊𝒄𝒆』  850 \n\n @everyone")
        embed.set_image(url="https://media1.tenor.com/images/d6bc1b52c2f93aa1e59478ef0fba1993/tenor.gif?itemid=8430935")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "컬쳐랜드":
       embed = discord.Embed(color=discord.Colour.red(), title = "매입", description="컬쳐문상⭕️/해피문화상품권 등등❌\n\n환전 비율 알려드립니다👇🏻👇🏻\n최소금액 0.1 백원단위 안받아요.문상 만원단위,천원단위0.5<88%>\n\n0.6~0.9<87%>\n0.1~0.4<86%>\n\n1.1~1.4<87%>/1.6~1.9<87%>/1.5<88%>\n\n\n ❌금지사항❌\n백원,십원단위는 절대 안받습니다.\n\n만약 지속적으로 환전문의하셧다가 취소하시면\n환전에 도움드리기 힘들다는점 알려드립니다.\n\n추후 비율은 바뀔수있으며 / 비율은 고정한다.\n\n@everyone")
       embed.set_image(url="https://play-lh.googleusercontent.com/g3eZ-GTdqSE_XqT1Ghah1-EOabs1xFCytkGMXSRiBjZbwaVinmnMcTBFmLM_nVUeVw")
       embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
       await message.channel.send(embed=embed)

    if message.content == "컬쳐랜드2":
        embed = discord.Embed(color=discord.Colour.red(), title="판매",description="『문화상품권 / 𝐂𝐮𝐥𝐭𝐮𝐫𝐞 𝐋𝐚𝐧𝐝』\n\n소량은 95% 또는 100% 비율 고정합니다.\n\n판매 가격 93%\n\n\n@everyone")
        embed.set_image(url="https://play-lh.googleusercontent.com/g3eZ-GTdqSE_XqT1Ghah1-EOabs1xFCytkGMXSRiBjZbwaVinmnMcTBFmLM_nVUeVw")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
client.run(token)



