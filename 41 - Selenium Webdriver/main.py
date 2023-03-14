from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/shafe/OneDrive/Documents/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/Element-26-Self-Locking-Weightlifting-Crossfit/dp/B074KK9928/ref=sr_1_4?"
           "keywords=weight%2Blifting%2Bbelt&qid=1678103316&s=sporting-goods&sprefix=we%2Csporting%2C371&sr=1-4&th=1")

title = driver.find_element(By.ID, "title")
print(title.text)

price = driver.find_elements(By.CLASS_NAME, "a-price")
print(price[0].text)

# driver.close()
driver.quit()
