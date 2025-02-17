from  selenium import webdriver
import os 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
audience = ['rohit sharma', 'virat kohli']
message = "U are great sir!"

class bot:
    def __init__(self,username,password, audience, message):
        self.username = "username"
        self.password = "password"
        
        self.audience = audience
        self.message = message

        self.base_url = "https://instagram.com"
        self.bot = driver
        self.login()
    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME,'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)


        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

       
        self.bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button').click()

        time.sleep(4)
        
        self.bot.find_element_by_xpath(
            '//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
  
       
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(2)
        for i in audience:
  
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)
  
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div[2]/div').click()
            time.sleep(2)
  
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)
  
           
            send = self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
  
            
            send.send_keys(self.message)
            time.sleep(1)
  
         
            send.send_keys(Keys.RETURN)
            time.sleep(2)
  
     
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)
  
  
def init():
    bot('username', 'password', message, audience)
 
    input("DONE")
  
  
init()