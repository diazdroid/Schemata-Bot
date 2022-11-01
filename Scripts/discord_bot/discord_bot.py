import os
import discord
from dotenv import load_dotenv
import asyncio
import json
import pathlib

main_folder_path = pathlib.Path(__file__).parent.parent.parent.resolve()

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())
data = json.load(open(str(main_folder_path) + '/config.json', 'r'))
platform = data['Platform']
mail = data['Mail']
mdp = data['Mdp']
alerts = data['Alerts']
max_skip = data['max_skip']
min_skip = data['min_skip']
hyperloop = data['Hyperloop']
device = data['Device']
proxy_mode = data['Proxy_mode']

if alerts == True:
        alerts = "✅"
else:
        alerts = "❌"
if hyperloop == True:
        hyperloop = "✅"
else:
        hyperloop = "❌"
if proxy_mode == True:
        proxy_mode = "✅"
else:
        proxy_mode = "❌"

list = ['CHANNEL_0','CHANNEL_1','CHANNEL_2','CHANNEL_3','CHANNEL_4','CHANNEL_5','CHANNEL_6','CHANNEL_7','CHANNEL_8','CHANNEL_9','CHANNEL_10','CHANNEL_11','CHANNEL_12','CHANNEL_13','CHANNEL_14','CHANNEL_15','CHANNEL_16','CHANNEL_17','CHANNEL_18','CHANNEL_19','CHANNEL_20','CHANNEL_21','CHANNEL_22', 'CHANNEL_23', 'CHANNEL_24', 'CHANNEL_25', 'CHANNEL_26', 'CHANNEL_27', 'CHANNEL_28', 'CHANNEL_29']

CHANNEL_ID = os.getenv(str(list[data['Device_ID']]))

def reset_crash_status():
    with open(str(main_folder_path) + "/config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["Crash_status"] = False
    with open(str(main_folder_path) + "/config.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

reset_crash_status()

with open(str(main_folder_path) + "/config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        crash_status = data['Crash_status']

@client.event
async def on_ready():  #  Called when internal cache is loaded

    channel = client.get_channel(int(CHANNEL_ID)) 
    await channel.send(f"""\n**-------------------------------------------------**\n🤖 **Im launching... I'll be up in a minute** 🤖\n**-------------------------------------------------**
    While waiting here is a recap of your config ⬇️
    - Platform => **{platform}**
    - Device => **{device}**
    **--------------------------**
    - Mail Alerts => {alerts} 
    - Hyperloop =>  {hyperloop}
    - Proxy Mode => {proxy_mode}
    **--------------------------**
    - Mail => **{mail}**
    - Pwd => **{mdp}**
    **--------------------------**
    - Minimum Skip => **{min_skip}s**
    - Maximim Skip => **{max_skip}s**""") 
    await asyncio.sleep(110)

    while True:
        with open(str(main_folder_path) + "/config.json", "r") as jsonFile:
                data = json.load(jsonFile)
                crash_status = data['Crash_status']
                proxy_loc = data['Proxy_loc']

        with open(str(main_folder_path) + "/Scripts/discord_stats.txt", "r") as discord_msg:
                foo = discord_msg.readlines() 
                x1 = foo[0]
                Total = foo[1]
                ram_usage = foo[2]
                cpu_usage = foo[3]
                av_skiptime = foo[4]
                now = foo[5]

        x1 = x1.rstrip('\n')
        Total = Total.rstrip('\n')
        ram_usage = ram_usage.rstrip('\n')
        cpu_usage = cpu_usage.rstrip('\n')
        av_skiptime = av_skiptime.rstrip('\n')
        now = now.rstrip('\n')

        price_stream = 0.004
        session_money = price_stream * int(Total)


        if crash_status == True:
                if hyperloop == "✅":
                        await channel.send("\n**--------------------------------------**\n🚨⚠️🚨   **__@everyone__**   🚨⚠️🚨\n**--------------------------------------**\n\n**" + platform + "** on ***" + str(data['Device']) + '*** **just crashed... ** \n\n 💰 __During your session you made approx. **' + str(session_money)+ f"\nTotal streams: {Total}" + '$**__ 💰\n\n** Hyperloop launched ! **\n\n**--------------------------------------**\n🚨⚠️🚨   **__@everyone__**   🚨⚠️🚨\n**--------------------------------------**')
                        break
                else:
                        await channel.send("\n**--------------------------------------**\n🚨⚠️🚨   **__@everyone__**   🚨⚠️🚨\n**--------------------------------------**\n\n**" + platform + "** on ***" + str(data['Device']) + '*** **just crashed... ** \n\n 💰 __During your session you made approx. **' + str(session_money) + '$**__ 💰\n\n** try to take a look on it ! **\n\n**--------------------------------------**\n🚨⚠️🚨   **__@everyone__**   🚨⚠️🚨\n**--------------------------------------**')
                        break

        else:
                if proxy_mode == "❌":
                        await channel.send(f'\n**------------------- {platform} -------------------**\n🔊 Streams since Random Switch : **{x1}**\n🔊 Total streams : **{Total}**\n\n:gear: *RAM* memory used : **{ram_usage}%**\n:gear: The *CPU* usage is : **{cpu_usage}%**\n\n📈 Average streams by day : **{av_skiptime}**\n💸 Average money generated : **{session_money}$**\n\n🕙 Time : {now}') 
                        await asyncio.sleep(180)
                else:
                        await channel.send(f'\n**------------------- {platform} -------------------**\n🔊 Streams since Random Switch : **{x1}**\n🔊 Total streams : **{Total}**\n\n:gear: *RAM* memory used : **{ram_usage}%**\n:gear: The *CPU* usage is : **{cpu_usage}%**\n\n📈 Average streams by day : **{av_skiptime}**\n💸 Average money generated : **{session_money}$**\n\n🕙 Time : {now}\n🌎 Localisation : {proxy_loc}') 
                        await asyncio.sleep(180)

client.run(str(TOKEN))