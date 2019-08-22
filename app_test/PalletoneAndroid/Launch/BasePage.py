#-*-coding:utf-8-*-
import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PalletoneAndroid.Util import launchDevice

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class BasePage(object):
    def __init__(self):
        desired_caps = launchDevice.setCapbility()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 15)

    def _getProperty(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,"com.hande.wanchain.wallet:id/currency_detail_coin_balance")))
        property = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/currency_detail_coin_balance")
        propertyAmount = int(property.text)
        return propertyAmount

    def getProperty(self):
        propertyAmount = self._getProperty(self)
        return propertyAmount

    def find_element(self, *element):
        try:
            self.wait.until(lambda driver: driver.find_element(*element).is_displayed())
            self.wait.until(EC.visibility_of_element_located(element))
            return self.driver.find_elements(*element)
        except:
            print u"%s 页面中未能找到 %s 元素" % (self, element)

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)