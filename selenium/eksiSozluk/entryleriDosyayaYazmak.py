from selenium import webdriver  
import random  
import time

driver = webdriver.Chrome()  
url = "https://eksisozluk.com/python--109286?p="  
pageCount = 1
entries = list() 
entryCount = 1
while pageCount <= 10: 
    randomPage = random.randint(1, 96) 
    newUrl = url + str(randomPage)
    driver.get(newUrl) 
    elements = driver.find_elements_by_css_selector(".content") 
    for element in elements: 
        entries.append(element.text) 
    pageCount += 1 

with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+".\n"+entry+"\n**************************************\n")
        entryCount+=1

driver.close()  