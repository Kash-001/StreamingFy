from cgi import print_arguments
import time,selenium,colorama
from venv import create

import modules.close_chrome
import modules.genacc
import modules.driverscript
import modules.useragenting
import random

from time import sleep
from random import randint
from modules.close_chrome import tkill
from modules.genacc import generateacc
from colorama import Fore
from modules.driverscript import create_driver

colorama.init()

while True:
    raw_creds=generateacc()
    email=raw_creds[0]
    password=raw_creds[1]
    with open("Created.txt", "a") as lines:
       lines.write(f'{email}:{password}\n')
    print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} CREATED ACCOUNT {Fore.RED}:')
    print(f'{Fore.RED}-> {Fore.WHITE}email {Fore.RED}: {Fore.WHITE}{email}')
    print(f'{Fore.RED}-> {Fore.WHITE}password {Fore.RED}: {Fore.WHITE}{password}\n')

    driver = create_driver()
    driver.get('https://accounts.spotify.com/en/login/')
    print(f'{Fore.RED}--> {Fore.WHITE}driver opened on {Fore.RED}: {Fore.WHITE}https://accounts.spotify.com/en/login/')
    sleep(1)

    username_elem = driver.find_element_by_id('login-username').send_keys(email)
    username_elem
    password_elem = driver.find_element_by_id('login-password').send_keys(password)
    login_button_elem = driver.find_element_by_id('login-button').click()
    print(f'{Fore.RED}--> {Fore.WHITE}user logged in successfully')
    sleep(1)

    driver.get('https://open.spotify.com/track/4ZCdEpoQpx3LXGLUVuHbUW?si=7edf9349acaa428a')
    print(f'{Fore.RED}--> {Fore.WHITE}driver opened on {Fore.RED}: {Fore.WHITE}https://open.spotify.com/track/4ZCdEpoQpx3LXGLUVuHbUW?si=7edf9349acaa428a')
    sleep(2)

    js_string = "var element = document.getElementById('onetrust-banner-sdk');element.remove();"
    driver.execute_script(js_string)
    sound_button_eleme = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/button').click()
    print(f'{Fore.RED}--> {Fore.WHITE}cookie removed successfully')
    sleep(1)

    print(f'{Fore.RED}--> {Fore.WHITE}Streaming started')
    play_button_eleme = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div/div/button/div').click()
    
    playtime = randint(35,40)
    print(f'{Fore.RED}--> {Fore.WHITE}chosen stream time : {playtime}')
    sleep(playtime)
    print(f'{Fore.RED}--> {Fore.WHITE}Streaming ended')

    tkill()
    print(f'{Fore.RED}--> {Fore.WHITE}Google.exe successfully closed')

