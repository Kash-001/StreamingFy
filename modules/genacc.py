import requests,random,string,time,turtle,selenium
from turtle import tilt
from selenium import webdriver

def generateacc():
    session = requests.Session()
    headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "https://www.spotify.com/"
            }

    email = ("").join(random.choices(string.ascii_letters + string.digits, k = 12)) + "@gmail.com"
    password = ("").join(random.choices(string.ascii_letters + string.digits, k = 12))
    dname = ("").join(random.choices(string.ascii_letters + string.digits, k = 12))

    data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={dname}&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
    session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data)

    return email,password