#-*-coding:utf-8-*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver,15)

    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open(self):
        self._open(self.base_url)

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