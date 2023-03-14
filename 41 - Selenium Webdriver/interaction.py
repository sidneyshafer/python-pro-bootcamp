from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("C:/Users/shafe/OneDrive/Documents/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount > a")
# print(article_count.text)

site_news = driver.find_element(By.LINK_TEXT, "Site news")
# site_news.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()
