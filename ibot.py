from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from insta_cred import username, password



class insta_bot:
    def __init__(self, uname, pw):
        self.uname = uname
        self.passw = pw
        self.path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.uname)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.passw)
        self.driver.find_element_by_css_selector('button[type=submit]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()   #
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()      # NOT NOW

    def send_text(self, targetID):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()  # PROFILE
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click() #FOLLOWING
        time.sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        l_ht, ht = 0, 1
        while l_ht != ht:
            l_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""arguments[0].
                    scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;""", scroll_box)
        self.driver.find_element_by_link_text(targetID).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("button[class='sqdOP  L3NKy    _8A5w5    ']").click()   #MESSAGE BUTTON
        time.sleep(5)
        #TEXT TO SEND
        file = open("text.txt")
        line = file.read()
        word = line.split("\n")
        #print(word)
        file.close()
        for i in range(len(word)):
            text = word[i]
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(text)
            self.driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button").click()
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("ENTER")

targetId = input('Enter receipient ID: ')

mybot = insta_bot(username, password)
mybot.send_text(targetId)