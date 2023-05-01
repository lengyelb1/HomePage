from distutils.spawn import find_executable
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

bongeszo = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#Oldal megnyitás
bongeszo.get('https://fashion-shop2.netlify.app/')
bongeszo.maximize_window()
time.sleep(3)


btn = bongeszo.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul/li[1]/a')
btn.click()
time.sleep(1)
bongeszo.save_screenshot('printscreen1.png')

btn = bongeszo.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul/li[2]/a')
btn.click()
time.sleep(1)
bongeszo.save_screenshot('printscreen2.png')

btn = bongeszo.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul/li[3]/a')
btn.click()
time.sleep(1)
bongeszo.save_screenshot('printscreen3.png')

btn = bongeszo.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul/li[4]/a')
btn.click()
time.sleep(1)
bongeszo.save_screenshot('printscreen4.png')

btn = bongeszo.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul/li[5]/a')
btn.click()
time.sleep(1)
bongeszo.save_screenshot('printscreen5.png')