import selenium
import modules.useragenting

from modules.getproxy import getrandomproxy
from modules.useragenting import GetRandomUserAgent
from selenium import webdriver

def create_driver():   
   chromeOptions = webdriver.ChromeOptions()
   chromeOptions.add_argument(f'--proxy-server=http://{getrandomproxy()}')
   chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
   chromeOptions.add_argument(f'--user-agent={GetRandomUserAgent()}')
   chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
   chromeOptions.add_argument("--disable-logging")
   chromeOptions.add_argument("--log-level=3")
   return webdriver.Chrome('modules/chromedriver',options=chromeOptions)