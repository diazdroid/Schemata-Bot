from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os
import json
import psutil
import random
import datetime
import smtplib, ssl
import time
import statistics
import pathlib
import colorama
from colorama import Fore, Style
import requests

os.system('cls' if os.name == 'nt' else 'clear')
colorama.init()

print(Fore.LIGHTGREEN_EX + '''
███████╗ ██████╗██╗  ██╗███████╗███╗   ███╗ █████╗ ████████╗ █████╗ 
██╔════╝██╔════╝██║  ██║██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗
███████╗██║     ███████║█████╗  ██╔████╔██║███████║   ██║   ███████║
╚════██║██║     ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
███████║╚██████╗██║  ██║███████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                    •°¯`•• v.1.2 by.Haash ••`¯°•''' + Style.RESET_ALL)

### GLOBAL VARIABLES ###
device = ''
ram_usage = 0
cpu_usage = 0
x1 = 0
Total = 0
av_skiptime = 0
Time = datetime.datetime.now()
now = 0
Num_OnOff = 0
main_folder_path = pathlib.Path(__file__).parent.parent.resolve()

options = Options()
options.page_load_strategy = 'eager'
options.add_argument('--disable-blink-features=AutomationControlled')

if os.path.exists(str(main_folder_path) + "/config.json"):
    data = json.load(open(str(main_folder_path) + "/config.json", 'r'))
    print(Fore.GREEN + '================================\n' + Style.RESET_ALL +'[' + Fore.LIGHTGREEN_EX + "*" + Style.RESET_ALL + ']' ' Config.json file detected...' + Fore.GREEN + '\n================================' + Style.RESET_ALL)
    platform = data['Platform']
    device = data['Device']
    hyperloop = data['Hyperloop']
    blue_popup = data['BluePopup']
    mail = data['Mail']
    mdp = data['Mdp']
    alerts = data['Alerts']
    max_skip = data['max_skip']
    min_skip = data['min_skip']
    proxy_mode = data['Proxy_mode']
    proxy_type = data['Proxy_type']
    device_ID = data['Device_ID']
else:
    #### INPUT SETTINGS ####
    print('\n' + Style.RESET_ALL +'[' + Fore.LIGHTGREEN_EX + "*" + Style.RESET_ALL + ']' ' Config.json file not found...')
    sys.exit()

if alerts:
    Mail_Sender = "roboto277@outlook.fr"
    Mail_SenderPwd = "Azerty321@"
    #print("\n=================== \n\n[*] Please be careful to not spam or Outlook will ban your mail. \nYou can unlock it by verifying your account with your phone number or creat a new one. \n\n===================\n")
    Mail_Receiver = "robotboy1800@gmail.com"

if proxy_mode:
    prx_type = str(proxy_type).lower()
    if prx_type not in {"socks5", "socks4", "http", "https"}:
        print('Proxy type not available, please choose a correct type ! (socks5/socks4/http/https)')
        sys.exit()
    rdm_proxy = random.choice(open('Scripts/proxies.txt').readlines())
    PROXY = rdm_proxy
    string = rdm_proxy.split(":")
    ip = string[0]
    chrome_options = webdriver.ChromeOptions()
    if prx_type == "socks5":
        chrome_options.add_argument('--proxy-server='"socks5://"+PROXY)
    elif prx_type == "socks4":
        chrome_options.add_argument('--proxy-server='"socks4://"+PROXY)
    elif prx_type == "http":
        chrome_options.add_argument('--proxy-server='"http://"+PROXY)
    elif prx_type == "https":
        chrome_options.add_argument('--proxy-server='"https://"+PROXY)
    try:
        request_url = 'https://geolocation-db.com/jsonp/' + ip
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result  = json.loads(result)
        proxy_loc = result['country_name']

        print('[' + Fore.LIGHTGREEN_EX + "*" + Style.RESET_ALL + ']' + Fore.GREEN + ' PROXY: '+ Style.RESET_ALL + ip + Fore.GREEN + ' LOCATION: '+ Style.RESET_ALL + proxy_loc + Fore.GREEN + '\n================================' + Style.RESET_ALL)

        with open(str(main_folder_path) + "/config.json", "r") as jsonFile:
                data = json.load(jsonFile)
        data["Proxy_loc"] = proxy_loc
        with open(str(main_folder_path) + "/config.json", "w") as jsonFile:
                json.dump(data, jsonFile, indent=4)
    except:
        print('[' + Fore.LIGHTRED_EX + "*" + Style.RESET_ALL + ']' + Fore.GREEN + ' PROXY: '+ Style.RESET_ALL + ip + Fore.RED + ' LOCATION: '+ Style.RESET_ALL + "API NOT REACHABLE" + Fore.GREEN + '\n================================' + Style.RESET_ALL)
    driver = webdriver.Chrome(options=chrome_options)
else:
    print('[' + Fore.LIGHTRED_EX + "*" + Style.RESET_ALL + ']' + Fore.RED + ' NO PROXY' + Fore.GREEN + '\n================================' + Style.RESET_ALL)
    driver = webdriver.Chrome()

wait = WebDriverWait(driver, 25)
hover = ActionChains(driver)
skip_timing = [min_skip,max_skip]
av_skiptime = round(144000/statistics.mean(skip_timing))

if platform.lower() not in {'spotify', 'amazon'}:
    print("\n[*] You didn't pick an available platform... Please choose Spotify or Amazon")
    sys.exit()

print('[' + Fore.LIGHTGREEN_EX + "*" + Style.RESET_ALL + ']' " Starting..." + Fore.GREEN + '\n================================' + Style.RESET_ALL)

#### Activating crash status Function ####
def crash_status():
    with open(str(main_folder_path) + "/config.json", "r") as jsonFile:
            data = json.load(jsonFile)
    data["Crash_status"] = True
    with open(str(main_folder_path) + "/config.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)

#### Spotify Looping Function #### 
def Spoti_Loop():
    global Total, cpu_usage, ram_usage, x1
    x1 = 0
    RandomRead = randint(180,400)

    for x in range(RandomRead):
        try:
            time.sleep(randint(min_skip,max_skip))

            wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')))
            skip_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
            skip_button.click()

            Total += 1
            x1 += 1
            now = datetime.datetime.now()
            ram_usage = psutil.virtual_memory()[2]
            cpu_usage = psutil.cpu_percent(4)

            message = f'Streams since Random Switch : {x1} \nTotal streams : {Total} \n\nRAM memory used : {ram_usage}% \nThe CPU usage is : {cpu_usage}% \n\nAverage streams by day : {round(av_skiptime)} \nTime : {now} ' + Fore.GREEN + f'\n|============| {platform} N.{device_ID} |=============|' + Style.RESET_ALL
            print(message)
            with open("Scripts/discord_stats.txt", "w") as discord_msg:
                discord_msg.write(f"{x1} \n{Total} \n{ram_usage} \n{cpu_usage} \n{av_skiptime} \n{now}")
        except:
            exit()

#### Amazon Looping Function ####
def Amazon_Loop():
    global Total, cpu_usage, ram_usage, x1
    x1 = 0
    x2 = 0
    RandomRead = randint(150,300)

    for x in range(RandomRead):
        try:
            if (x2 % 15) == 0:
                driver.refresh()
            time.sleep(randint(min_skip,max_skip))

            wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="nextButton"]')))
            skip_button = driver.find_element(By.XPATH, '//*[@id="nextButton"]')
            skip_button.click()

            Total += 1
            x1 += 1
            x2 +=1
            now = datetime.datetime.now()
            ram_usage = psutil.virtual_memory()[2]
            cpu_usage = psutil.cpu_percent(4)

            message = f'Streams since Random Switch : {x1} \nTotal streams : {Total} \n\nRAM memory used : {ram_usage}% \nThe CPU usage is : {cpu_usage}% \n\nAverage streams by day : {round(av_skiptime)} \nTime : {now}'  + Fore.GREEN + f'\n|============| {platform} N.{device_ID} |=============|' + Style.RESET_ALL
            print(message)
            with open("Scripts/discord_stats.txt", "w") as discord_msg:
                discord_msg.write(f"{x1} \n{Total} \n{ram_usage} \n{cpu_usage} \n{av_skiptime} \n{now}")
        except:
            exit()

#### ERROR Function ####
def ERROR_ALERT():

    sender_email = Mail_Sender
    receiver_email = Mail_Receiver
    password = Mail_SenderPwd
    Crash_Time = datetime.datetime.now()

    message = MIMEMultipart("alternative")
    message["Subject"] = f"CRASH {platform} *** {device} ***"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    The {platform} script just crashed on {device}.

    You launched It at {Time}.
    It stopped at {Crash_Time}.

    It made a total of {Total} Streams.

    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

#### SWITCH ALBUM SPOTIFY ####
def SWITCH_ALBUM_SPOTIFY():
    rdm_album_spotify = random.choice(open( 'Scripts/albums_spotify.txt').readlines())
    time.sleep(0.5)
    driver.get('https://open.spotify.com/album/' + rdm_album_spotify)
    if blue_popup:
            wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="tippy-1"]/div/div[1]/div/div/div[2]/button[2]')))
            blue_button = driver.find_element(By.XPATH, '//*[@id="tippy-1"]/div/div[1]/div/div/div[2]/button[2]')
            blue_button.click() # -> Pop-Up Blue
            time.sleep(1)

    time.sleep(0.5)
    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')))
    play_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
    play_button.click() # -> Loop Button
    
    time.sleep(0.5)
    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')))
    play_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
    play_button.click() # -> Play Button
    
#### SWITCH ALBUM AMAZON ####
def SWITCH_ALBUM_AMAZON():
    time.sleep(0.5)
    rdm_album_amazon = random.choice(open( 'Scripts/albums_amazon.txt').readlines())
    driver.get('https://music.amazon.fr/albums/' + rdm_album_amazon)

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="detailHeaderButton1"]')))
    play_button = driver.find_element(By.XPATH, '//*[@id="detailHeaderButton1"]')
    hover.move_to_element(play_button).click().perform()
    
    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="root"]/music-app/div[4]')))
    bandeau = driver.find_element(By.XPATH, '//*[@id="root"]/music-app/div[4]')
    hover.move_to_element(bandeau).perform()

    #Loop Button
    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="transport"]/div[2]/music-button[1]')))
    loop_button = driver.find_element(By.XPATH, '//*[@id="transport"]/div[2]/music-button[1]')
    hover.move_to_element(loop_button).click().perform()

# === SPOTIFY_CONNECTION Function === #
def SPOTIFY_CONNECTION():

        driver.get("https://open.spotify.com/collection/tracks")
        driver.maximize_window()
        
        wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        time.sleep(0.5)
        accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()

        wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')))
        connect_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
        connect_button.click()

        wait.until(cond.presence_of_element_located((By.XPATH, '//*[@id="login-username"]')))
        username_input = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        username_input.send_keys(mail) #mail

        password_input = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        password_input.send_keys(str(mdp)) #password

        wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

        SWITCH_ALBUM_SPOTIFY()

#### AMAZON CONNECTION Function ####
def AMAZON_CONNECTION():
    driver.get('https://www.amazon.fr/music/unlimited')
    driver.maximize_window()

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="sp-cc-rejectall-link"]')))
    time.sleep(0.5)
    accept_cookie = driver.find_element(By.XPATH, '//*[@id="sp-cc-rejectall-link"]')
    accept_cookie.click()

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="nav-subnav"]/a[9]')))
    web_player_button = driver.find_element(By.XPATH, '//*[@id="nav-subnav"]/a[9]')
    web_player_button.click()

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="signInButton"]')))
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="signInButton"]')
    sign_in_button.click()

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="ap_email"]')))
    username_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    username_input.send_keys(mail)

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="ap_password"]')))
    pwd_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    pwd_input.send_keys(mdp)

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="signInSubmit"]')))
    login_button = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    login_button.click()

    time.sleep(0.5)

    #2nd Time
    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="ap_email"]')))
    username_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    username_input.send_keys(mail)

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="ap_password"]')))
    pwd_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    pwd_input.send_keys(mdp)

    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="signInSubmit"]')))
    login_button = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    login_button.click()
    
    SWITCH_ALBUM_AMAZON()


##########################################################################################################################
#####################  SCRIPT ############################################################################################
##########################################################################################################################


if platform.lower() == 'spotify':
#### Spotify Connexion ####
    try:
        SPOTIFY_CONNECTION()
    except:
        driver.quit()
        print('\n' + Fore.RED + '=============================\n\n' + Style.RESET_ALL +'[' + Fore.RED +'*' + Style.RESET_ALL + ']' + ' DEPLOYING ERROR - Please restart by paying attention to the informations you have given !\n\n' + Fore.RED + '=============================' + Style.RESET_ALL)
        sys.exit()

    #### Infinit LOOP #### 
    while True:
            try:
            #### Normal Playlist reading #####
                Spoti_Loop()

                try:
                    driver.refresh()
                    print('\n\n[' + Fore.GREEN + '*' + Style.RESET_ALL + ']' ' Refreshing the page...\n\n')
                except:
                    print('\n\n[' + Fore.RED + '*' + Style.RESET_ALL + ']' ' Not able to refresh... \n\n')
                    break

            #### Clicking the random Button ####
                time.sleep(1)
                try:
                    wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]')))
                    rdm_btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]')
                    rdm_btn.click()
                    if (Num_OnOff % 2) == 0:
                        print(Fore.GREEN + "##### Random Switch: ON #####" + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + "##### Random Switch: OFF #####" + Style.RESET_ALL)
                    Num_OnOff += 1
                    time.sleep(2)
                    SWITCH_ALBUM_SPOTIFY()
                except:
                    try:
                        driver.refresh()
                        print('\n\n[*] Problem with the Random Button --> Refreshing the page...\n\n')
                    except:
                        print('\n\n[*] Not able to refresh... \n\n')
                        break

            except:
                break
elif platform.lower() == 'amazon':
    #### AMAZON CONNECTION ####
    try:
        AMAZON_CONNECTION()
    except:
        driver.quit()
        print('\n' + Fore.RED + '=============================\n' + Style.RESET_ALL +'[' + Fore.RED +'*' + Style.RESET_ALL + ']' + ' DEPLOYING ERROR - Please restart by paying attention to the informations you have given !\n' + Fore.RED + '=============================' + Style.RESET_ALL)
        sys.exit()

    #### Infinit LOOP #### 
    while True:
        try:
        #### Normal Playlist reading #####
            Amazon_Loop()

            try:
                driver.refresh()
                print('\n\n[' + Fore.GREEN + '*' + Style.RESET_ALL + ']' ' Refreshing the page...\n\n')
            except:
                print('\n\n[' + Fore.RED + '*' + Style.RESET_ALL + ']' ' Not able to refresh... \n\n')
                break

    #### Clicking the random Button ####
            time.sleep(1)
            try:
                wait.until(cond.element_to_be_clickable((By.CSS_SELECTOR, '<button type="button" class="button music-t1 no-text" tabindex="-1"></rect><use fill-rule="nonzero" xlink:href="#ic_playback_shuffle-a" fill="currentColor"></use></g></svg></span></music-icon><span><slot></slot></span></button>')))
                randomb = driver.find_element(By.CSS_SELECTOR, '<button type="button" class="button music-t1 no-text" tabindex="-1"></rect><use fill-rule="nonzero" xlink:href="#ic_playback_shuffle-a" fill="currentColor"></use></g></svg></span></music-icon><span><slot></slot></span></button>')
                hover.move_to_element(randomb).click().perform()
                if (Num_OnOff % 2) == 0:
                    print(Fore.GREEN + "##### Random Switch: ON #####" + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "##### Random Switch: OFF #####" + Style.RESET_ALL)
                Num_OnOff += 1
                time.sleep(2)
                SWITCH_ALBUM_AMAZON()
            except:
                try:
                    driver.refresh()
                    print('\n\n[*] Problem with the Random Button --> Refreshing the page...\n\n')
                except:
                    print('\n\n[*] Not able to refresh... \n\n')
                    break
        except:
            break

#### END OF SCRIPT / ERROR MSGs ####
if alerts:
    if hyperloop:
        print(Fore.RED + '====================' + Style.RESET_ALL + '\n\nFATAL ERROR ----- MAIL SENT ---- RESTARTING...\n\n' + Fore.RED +'====================' + Style.RESET_ALL)
        ERROR_ALERT()
        crash_status()
        driver.quit()
        time.sleep(240)
        if os.name == 'nt':
            os.system('py ' + str(main_folder_path) + "/main.py")
        else: 
            os.system('python3 ' + str(main_folder_path) + "/main.py")
    else:
        print(Fore.RED + '====================' + Style.RESET_ALL + '\n\nFATAL ERROR ----- MAIL SENT ---- EXITING...\n\n' + Fore.RED +'====================' + Style.RESET_ALL)
        ERROR_ALERT()
        crash_status()
        sys.exit()
    
else:
    if hyperloop:
        print(Fore.RED + '====================' + Style.RESET_ALL + '\n\nFATAL ERROR ----- RESTARTING...\n\n' + Fore.RED +'====================' + Style.RESET_ALL)
        driver.quit()
        crash_status()
        time.sleep(240)
        if os.name == 'nt':
            os.system('py ' + str(main_folder_path) + "/main.py")
        else: 
            os.system('python3 ' + str(main_folder_path) + "/main.py")
    else:
        print(Fore.RED + '====================' + Style.RESET_ALL + '\n\nFATAL ERROR ----- EXITING...\n\n' + Fore.RED +'====================' + Style.RESET_ALL)
        crash_status()
        sys.exit()