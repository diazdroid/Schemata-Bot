# Schemata Streaming Bot
This is a streaming python script for Spotify and Amazon Unlimited.

I addded a lot of features to train different skills. You'll find them in config.json file:
- Spotify and Amazon Unlimited
- Proxy mode
- Proxy type
- Email Alerts system
- Hyperloop mode
- Randomly switching albums and proxies
- Discord Bot to send outputs and stats
- RAM/CPU monitoring
- Average Streams by day and aprx. revenue of your session <br/>
<img src= "/IMG/Script_Launch.png" width="300"/>
<img src="/IMG/Script_Output.png" width="300"/>
<img src="/IMG/Discord_bot_launchmsg.png" width="300"/>
<img src="/IMG/Discord_bot_outputmsg.png" width="300"/>
<img src="/IMG/Discord_bot_crashmsg.png" width="300"/>

# **Installation**

1. Get the chromedriver corresponding to the version you are currently using and put it in your PATH.

2. ```pip3 install -r requirements.txt```

3. Edit ```config.json```

4. Edit ```.env``` with you Discord Bot Token and channels ID

5. Edit ```albums_<platform>.txt``` with the characters you see at the end of the URL when you naviguate on an album:
<img src="/IMG/url.png" width="500"/>


5. MacOS: ```python3 main.py```
   Windows: ```py main.py```

# **config.json**
   ```
   {
    "Platform": "Amazon",
    "Device": "PC 1",
    "Device_ID": 1,
    "Hyperloop": true,
    "BluePopup": false,
    "Mail": "",
    "Pwd": "",
    "Alerts": false,
    "Proxy_mode": false,
    "Proxy_type": "Socks5",
    "min_skip": 35,
    "max_skip": 60,
    "Crash_status": false,
    "Proxy_loc": ""
}
```
**Details =>**
   
- Platform: Choose between "Spotify" or "Amazon" platforms.
- Device: Name your device. ("PC 1")
- Device ID: ID for the discord bot to know on wich channel it needs to send the info. (1 => Channel 1)
- Hyperloop: Will automatically restart the script if it crashes. (True/False)
- BluePop: Sometime spotify make a bluepop up appear when connecting, put True if it's the case.
- Mail/Pwd: Credentials of your account.
- Alerts: Will send you an email with informations about your session when the script crashes. (True/false)
- ProxyMode: Use proxy for your session. (True/False)
- Type: Choose wich type of proxy you will use. (socks4/socks5/http/https)
- Min/Max_skip: Choose minimum and maximum skip time. (45/75)
<br/>
- Crash_status/Proxy_loc: No need to put anything.


# Legal
 This is illegal if you use this without the consent of the owners (in this case, the Spotify and Amazon teams).<br/>
 The software designed to perform website security testing.<br/>
 The author is not responsible for any illegal use of these programs.<br/>
 I am not accountable for anything you get into.<br/>
 I am not accountable for any of your actions.<br/>
 This is 100% educational, please do not misuse this tool.
