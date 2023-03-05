from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("#######################################################")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                BOZKURT FLOOD ARAÇI                    ")
print("                İnstagram: @f3rrkan                    ")
print("      Web Site: https://f3rkan.github.io/              ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("#######################################################")
print()

username = input("Kullanıcı Adı: ")

password = input("Şifrenizi Giriniz: ")

metin = input("Metni Giriniz: ")

basılcak = input("Flood Atılcak Kişi: ")
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def singIn(self):
         self.browser.get("https://www.instagram.com/accounts/login/")
         time.sleep(2)

         usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
         passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

         usernameInput.send_keys(self.username)
         passwordInput.send_keys(self.password)
         passwordInput.send_keys(Keys.ENTER)
         time.sleep(4)

    def dm(self):
         dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
         dm.click()
         time.sleep(2)
         dm = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
         dm.click()
         dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
         dm.click()
       
         dmInput = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")

         dmInput.send_keys(f"{basılcak}")
         time.sleep(4)

    def msj(self):
         msj = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button")
         msj.click()
         time.sleep(3)
         msj = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
         msj.click()
         time.sleep(3)
       
    def oldu(self):
         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

         msjInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
   
         msjInput.send_keys(f"{metin}")
         msjInput.send_keys(Keys.ENTER)
         time.sleep(0.5)

instgrm = Instagram(username, password)
instgrm.singIn()
instgrm.dm()
instgrm.msj()
instgrm.oldu()
