from selenium import webdriver
import time

class login:
    def driverSetup(context):
        context.driver=webdriver.Chrome("C:\\Users\\hp\\Desktop\\featurefiles\\venv\\chromedriver.exe")

    def url(context):
        context.driver.get('https://www.phptravels.net/login')
    def element(context):
        time.sleep(5)
        a=context.driver.find_element_by_xpath("//div[@class='logo']//img[@src='https://phptravels.net/api/uploads/global/logo.png']").is_displayed()
        assert a==True
    def closeDriver(context):
        context.driver.close()
