from selenium import webdriver

class Bot:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        # self.user = user
        # self.password = password
        
    def navigate(self):
        self.driver.get(self.url)

    
    def startBot(self):
        return self.driver
        
    