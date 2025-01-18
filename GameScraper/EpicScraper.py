from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def game_scraper():
    url = "E-P-I-C-HomeLink"
    driver.get(url)
    element = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[6]/div/div/div[2]/div[1]/div/div[2]/div[1]/a/h5/div/div')
    driver.execute_script("arguments[0].scrollIntoView();",element)
    time.sleep(1)
    

    game_status_element = driver.find_element(By.CSS_SELECTOR, "div.css-82y1uz").text

    if game_status_element == "ŞIMDI ÜCRETSIZ":
        game = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[7]/div/div/section/div/div[1]/div/div/div/a/div/div[1]/div[1]/div/div/div/img')
        game_name = game.get_attribute("alt")
        game_image = game.get_attribute("src")

        game_link_element = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[7]/div/div/section/div/div[1]/div/div/div/a')
        game_link = game_link_element.get_attribute("href")


    game_status_element2 = driver.find_element(By.CSS_SELECTOR, "div.css-gyjcm9").text

    if game_status_element2 == "ŞIMDI ÜCRETSIZ":
        game2 = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[7]/div/div/section/div/div[2]/div/div/div/a/div/div[1]/div[1]/div/div/div/img')
        game_name2 = game2.get_attribute("alt")
        game_image2 = game2.get_attribute("src")

        game_link_element2 = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[7]/div/div/section/div/div[2]/div/div/div/a')
        game_link2 = game_link_element2.get_attribute("href")
        
    
game_scraper()
