from selenium import webdriver
import time


driver = webdriver.Chrome()


driver.get("https://twitter.com/")
time.sleep(2)

giris_yap = driver.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]") # ana sayfadaki giriş yap elementini seçtik
giris_yap.click() # giriş yap elementine tıkladık
time.sleep(1)

user_name = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input") # girişyap'a tıklayınca yönlendirildiğimiz sayfadaki username input alanını aldık
password = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input") # password input alanını aldık

user_name.send_keys("***") # user_name değişkenine (input alanına)  kullanıcı adını yolladık
password.send_keys("****") # password değişkenine (input alanına) şifre yolladık


login = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button") # 2. aşamadaki giriş yap butonunu yakaladık
login.click() # oraya tıkladık
time.sleep(3)


driver.quit()