from behave import *
import time
from selenium import webdriver
from feature.PAGES.loginpage import login


class stepDefinition:
    #obj=loginpage()
    @given(u'i launched the browser')
    def loginlogo(context):
        login.driverSetup(context)
    @when(u'i open the PHPtravel loginpage url')
    def loginlogo1(context):
        login.url(context)
    @then(u'check whether logo is present on page')
    def loginlogo2(context):
        login.element(context)
    @then(u'close browser')
    def loginlogo3(context):
        login.closeDriver(context)




