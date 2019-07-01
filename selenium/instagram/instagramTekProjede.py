from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.get("https://www.instagram.com/")

time.sleep(2)

girisYap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")

girisYap.click() # yakaladığımız butona tıklıyoruz

time.sleep(2)

username = browser.find_element_by_name("username") # input alanını yakaladık
password = browser.find_element_by_name("password")

username.send_keys("***") # input alanlarına parametre yolladık
password.send_keys("*****")


loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")

loginButton.click() # yakaladığımız login butonuna tıkladık

time.sleep(5)

profileButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a") # kendi profilimize giden butonu yakaladık


profileButton.click() # kendi profilimze giden butona tıkladık

time.sleep(3)


buttons = browser.find_elements_by_css_selector("._bnq48") # profilim sayfasındaki butonları aldık

followersButton = buttons[1] # takipçiler butonunu yakalıyoruz. buttons Listesindeki butonlardan 2. olanı aldık

followersButton.click() # yakaladığımız butona tıkladık

time.sleep(5)

jscommand = """
followers = document.querySelector("._gs38e");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

""" # js scripti (scroll için) bir değere atadık
lenOfPage = browser.execute_script(jscommand) # js scripti çalıştırdık
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
followersList = []

followers = browser.find_elements_by_css_selector("._2g7d5.notranslate._o5iw8") # takipçileri yakaladık



for follower in followers: # takkipçiler listesindeki her takipçi için
    
    followersList.append(follower.text) # takipçi adını yazdırdık
    
with open("followers.txt","w",encoding = "UTF-8") as file: # takipçileri dosyaya yazdık
    for follower in followersList:
        file.write(follower + "\n")
        











          
browser.close()


