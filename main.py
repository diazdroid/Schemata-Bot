from multiprocessing import Process
import os
import time

def Discord_script():
    os.system('py Scripts/discord_bot/discord_bot.py' if os.name == 'nt' else 'python3 Scripts/discord_bot/discord_bot.py')   
def Schemata_script():
    os.system('py Scripts/Schemata.py' if os.name == 'nt' else 'python3 Scripts/Schemata.py')


if __name__ == '__main__':
    p = Process(target=Discord_script)
    q = Process(target=Schemata_script)
    p.start()
    time.sleep(2)
    q.start()
    p.join()
    q.join()