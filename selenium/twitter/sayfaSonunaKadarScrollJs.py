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

searchArea = browser.find_element_by_xpath("//*[@id='search-query']") 
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button") 

searchArea.send_keys("#python") 

searchButton.click() 

time.sleep(3)

elements = browser.find_element_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text") 

time.sleep(1)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") # içeri yazdığımız scripti çalıştırır
match=False
while(match==False):
    lastCount = lenOfPage # az önce atadığımız mesafeyi lastCount'a atadık
    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") # bir defa daha scroll için script çalıştırdık
    if lastCount == lenOfPage: # sayfa uzunluğu ile döngüde atadığımız uzunluk eşit olursa
        match=True # match değerini true yap. Bu sayede döngü sona erecek

browser.quit()