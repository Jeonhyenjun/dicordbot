import discord #모듈 불러옴
token = "Token" #토큰설정하기
client = discord.Client()  #client 설정

@client.event
async def on_ready(): #봇이 준비될때
    print("현준이 준비 끝!")
    print(client.user)
    print("현준이랑 놀아보자!!")
@client.event
async def on_message(message): #사용자가 말을 걸었을때
    if message.content == "야": #만약 사용자가 '야' 라고 입력한다면
        await message.channel.send("현준이 불렀어?") #현준이 불렀어 라고 답한다
    if message.content == "하이":  # 만약 사용자가 'ㅎㅇ' 라고 입력한다면
        await message.channel.send("바이")  # ㅂㅇ라고 답한다
    if message.content == "ㅎㅇ":  # 만약 사용자가 'ㅎㅇ' 라고 입력한다면
        await message.channel.send("ㅂㅇ")  # ㅂㅇ 라고 답한다
    if message.content == "전현준 탈모":  # 만약 사용자가 '전현준 탈모' 라고 입력한다면
        await message.channel.send("뒤질래? 탈모 아니다")  # 뒤질래? 라고 답한다
    if message.content == "야 돈줘":  # 만약 사용자가 '야' 라고 입력한다면
        await message.channel.send("돈 준다고? 카카오뱅크 7777010792145 전현준")  # 돈준다고? 카카오뱅크 ;;라고 답한다
    if message.content == "굿모닝":  # 만약 사용자가 '야' 라고 입력한다면
        await message.channel.send("웅 잘잤어?")# 현준이 불렀어 라고 답한다
    if message.content == "뭐":  # 만약 사용자가 '야' 라고 입력한다면
        await message.channel.send("어쩌라는거야;;")  # 현준이 불렀어 라고 답한다
    if message.content == "응 아니야":
        await message.channel.send("응 맞아")
    if message.content == "샌드 어떰?":
        await message.channel.send("돼지 바보똥꾸멍")
    if message.content == "빈츄 어떰?":
        await message.channel.send("케미 여자친구라 감히 말할수 없어!")
    if message.content == "케미 어떰?":
        await message.channel.send("웅 베릴짱")
    if message.content == "야":
        await message.channel.send("외 수영장 할꺼지 ㅋㅋㅋㅋㅋㅋㅋㅋ?")
    if message.content == "박재민 어떰?":
        await message.channel.send("아기 돼지 꿀꿀이")
    if message.content == "쭈구미 어떰?":
        await message.channel.send("나는 오징어가 좋아")
    if message.content == "리저 어떰?":
        await message.channel.send("NYX에서 가장 바보")
    if message.content == "야야":
        await message.channel.send("어어 왜불러?")
    if message.content == "숨결 어떰?":
        await message.channel.send("매우 좋아 최소 샌드보단 좋지")
    if message.content == "미친":
        await message.channel.send("도친레친미친")
    if message.content == "ㅁㅊ":
        await message.channel.send("마차?")
    if message.content == "ㅋ":
        await message.channel.send("나도 같이 웃자 ㅋㅋㅋㅋㅋㅋㅋㅋ")
    if message.content == "빈츄 어때?":
        await message.channel.send("케미 여친이라 내가 함부로 말하면 안됭")
    if message.content == "쭈꾸미 어때?":
        await message.channel.send("오징어 미만잡 ㅅㄱ")
    if message.content == "케미 어때?":
        await message.channel.send("나는 AKM보다 베릴이야")
    if message.content == "샌드 어때?":
        await message.channel.send("모쏠 쉐기 ㅋ")
    if message.content == "야야야":
        await message.channel.send("응으응응 흐응~")
    if message.content == "전현준 어때?":
        await message.channel.send("ㅋ 말이 되냐 짱이지 ㅋ")
    if message.content == "전현준 어떰?":
        await message.channel.send("개좋음 ㄹㅇ")
    if message.content == "현준 어떰":
        await message.channel.send("존나 똑똑")
    if message.content == "전현준 어때":
        await message.channel.send("짱이야")
    if message.content == "?":
        await message.channel.send("??")
    if message.content == "??":
        await message.channel.send("???")
    if message.content == "돈줘":
        await message.channel.send("시렁")
    if message.content == "ㅇ":
        await message.channel.send("ㅇ")
    if message.content == "수준":
        await message.channel.send("너보단 똑똑함ㅋ")
    if message.content == ".":
        await message.channel.send(".")
    if message.content == "정신차려":
         await message.channel.send("나 정신 차리고있어")
    if message.content == "현준아 자폭해":
        await message.channel.send("시러 죽기 싫어")
    if message.content == "리저 바보":
        await message.channel.send("ㅇㅈ")

    if message.content == "!후원":
        embed = discord.Embed(Colur=discord.Colour.red(), title="후원",description="후원은 계좌는 7777010792145 카카오뱅크로 받고있고 문상은 현준#1266으로 보내주시면됩니다. 한번 후원하러 가보실까요?")
        embed.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fnewstream.kr%2Fposts%2F3193888&psig=AOvVaw3XCGEYpu3TJ5OPTY8KPIOy&ust=1613716576681000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCICa6YPp8u4CFQAAAAAdAAAAABAN")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="금액 메뉴",value="5천원:빵 사먹음 , 1만원: 영어학원 쉬는시간 간식먹음",inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswich(f"!채널메세지"):
        ch = client.get_channel(int(message.content[6:24]))
        await ch.send(message.content[25:])
        
client.run(token)
