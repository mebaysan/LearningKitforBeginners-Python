from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/form/div[3]/div/p/a")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys("****")
password.send_keys("****")

time.sleep(3)


login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")

login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='search-query']") # arama için input alanını yakaladık
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button") # input alanına yazdıktan sonra aramak için tıklayacağımı ara butonunu yakaladık

searchArea.send_keys("#python") # arama alanına key yolladık

searchButton.click() # arama alanına kelime yolladık

time.sleep(3)

browser.back() # bir önceki sayfaya geliyoruz
time.sleep(2)

browser.quit()