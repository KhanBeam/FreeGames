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

url = "https://www.epicgames.com/store/tr"
driver.get(url)

element = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[6]/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/span/div')
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(1)

free_game = driver.find_element(By.CSS_SELECTOR, "img.css-1dsjpsr")

game_name = free_game.get_attribute("alt")
game_image = free_game.get_attribute("src")

print(f"Oyun Adı: {game_name}")
print(f"Görsel Bağlantısı: {game_image}")