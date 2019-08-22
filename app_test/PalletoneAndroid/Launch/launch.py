__author__ = 'miho'

import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from PalletoneAndroid.Util import analysisYaml
from PalletoneAndroid.Util import launchDevice
from PalletoneAndroid.Util import UtilTools


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class LaunchMainActivity(unittest.TestCase):
    def setUp(self):
        desired_caps = launchDevice.setCapbility()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver,15)
        #self.printLog = LogUtil()

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        content = analysisYaml.analysisYaml("../Senario/recover_wallet.yml")
        print content['senario'][0]['title']
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,content['testcase'][0]['element_location'])))
        print(self.driver.current_activity)
        el1 = self.driver.find_element_by_id(content['testcase'][0]['element_location'])
        el1.click()
        el2 = self.driver.find_element_by_id(content['testcase'][1]['element_location'])
        el2.click()
        sleep(3)
        for i in range(len(content['testcase'][2]['text'])):
            el3 = self.driver.find_element_by_id(content['testcase'][2]['element_location']+str(i+1))
            el3.send_keys(content['testcase'][2]['text'][i])
        el15 = self.driver.find_element_by_id(content['testcase'][3]['element_location'])
        el15.click()
        sleep(3)
        el16 = self.driver.find_element_by_id(content['testcase'][4]['element_location'])
        el16.send_keys(content['testcase'][4]['text'])
        el17 = self.driver.find_element_by_id(content['testcase'][5]['element_location'])
        el17.send_keys(content['testcase'][5]['text'])
        el18 = self.driver.find_element_by_id(content['testcase'][6]['element_location'])
        el18.click()
        el19 = self.driver.find_element_by_id(content['testcase'][7]['element_location'])
        el19.click()
        #self.driver.press_button("com.hande.wanchain.wallet:id/next_step")
        #self.wait.until(EC.visibility_of_all_elements_located((By.ID,content['testcase'][8]['element_location'])))
        sleep(5)
        #el20 = self.driver.find_element_by_id(content['testcase'][9]['element_location'])
        #el20.click()
        self.tap_location(780, 1835)
        sleep(1)
        self.tap_location(780, 1835)
        sleep(2)
        #self.record()
        self.transferToken()

    def createAddr(self):
        content = analysisYaml.analysisYaml("../Senario/create_address.yml")
        el24 = self.driver.find_element_by_id(content['testcase'][0]['element_location'])
        el24.click()
        el25 = self.driver.find_element_by_id(content['testcase'][1]['element_location'])
        el25.click()
        el26 = self.driver.find_element_by_id(content['testcase'][2]['element_location'])
        el26.send_keys("P1EVkpaTCgcWZT4uSkd3vM3sVF8RAY7Gc1A")
        el27 = self.driver.find_element_by_id(content['testcase'][3]['element_location'])
        el27.click()
        #el28 = self.driver.find_element_by_xpath(
            #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
        el28 =self.driver.find_element_by_name(content['testcase'][4]['element_location'])
        el28.click()
        el29 = self.driver.find_element_by_xpath(content['testcase'][5]['element_location'])
        el29.click()
        el30 = self.driver.find_element_by_xpath(content['testcase'][6]['element_location'])
        el30.click()
        el31 = self.driver.find_element_by_id(content['testcase'][7]['element_location'])
        el31.send_keys("P1EVkpaTCgcWZT4uSkd3vM3sVF8RAY7Gc1A")
        el32 = self.driver.find_element_by_id(content['testcase'][8]['element_location'])
        el32.click()

    def transferToken(self):
        content = analysisYaml.analysisYaml("../Senario/transfer_token.yml")
        el1 = self.driver.find_element_by_id(content['testcase'][0]['element_location'])
        el1.click()
        el2 = self.driver.find_element_by_xpath(content['testcase'][1]['element_location'])
        el2.click()
        sleep(2)
        PTN1 = self.getProperty()
        el3 = self.driver.find_element_by_id(content['testcase'][2]['element_location'])
        el3.click()
        el4 = self.driver.find_element_by_id(content['testcase'][3]['element_location'])
        el4.send_keys("P1EVkpaTCgcWZT4uSkd3vM3sVF8RAY7Gc1A")
        el5 = self.driver.find_element_by_id(content['testcase'][4]['element_location'])
        el5.send_keys(content['testcase'][4]['text'])
        fee = self.driver.find_element_by_id(content['testcase'][5]['element_location'])
        fee.clear()
        fee.send_keys(content['testcase'][5]['text'])
        self.driver.hide_keyboard()
        sleep(1)
        el6 = self.driver.find_element_by_id(content['testcase'][6]['element_location'])
        el6.click()
        el7 = self.driver.find_element_by_id(content['testcase'][7]['element_location'])
        el7.click()
        el8 = self.driver.find_element_by_id(content['testcase'][8]['element_location'])
        el8.send_keys(content['testcase'][8]['text'])
        el9 = self.driver.find_element_by_id(content['testcase'][9]['element_location'])
        el9.click()
        #txHashText = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/tx_data")
        #print(txHashText.text.split(": ")[1])
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,content['testcase'][10]['element_location'])))
        sleep(4)
        PTN2 = self.getProperty()
        PTNGAIN = UtilTools.getGain(PTN1,PTN2)
        self.assertEqual(PTNGAIN,21)

    def _getProperty(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,"com.hande.wanchain.wallet:id/currency_detail_coin_balance")))
        property = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/currency_detail_coin_balance")
        propertyAmount = int(property.text)
        return propertyAmount

    def getProperty(self):
        propertyAmount = self._getProperty()
        return propertyAmount

    def record(self):
        main_bottom = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/main_bottom_text_3")
        main_bottom.click()
        self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")))
        record = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")
        record.click()
        self.wait.until(
            EC.visibility_of_all_elements_located((By.ID, "com.hande.wanchain.wallet:id/tx_record_detail_name")))
        el1 = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/tx_record_detail_name")
        self.assertEqual(el1.text,"PalletOneToken")
        el2 = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/rv_from_tx_eth")
        self.assertEqual(el2.text,"P1AuNMS3dSa4vQMpuGPvTjsFSkbKneWRNwC")
        el3 = self.driver.find_element_by_id("com.hande.wanchain.wallet:id/rv_to_tx_eth")
        self.assertEqual(el3.text,"P1EVkpaTCgcWZT4uSkd3vM3sVF8RAY7Gc1A")

    def tap_location(self,x,y,duration=500):
        window_width = self.driver.get_window_size()['width']
        window_height = self.driver.get_window_size()['height']
        x1 = int((float(x)/window_width) * window_width)
        y1 = int((float(y) / window_height) * window_height)
        self.driver.tap([(x, y), (x1, y1)], duration)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LaunchMainActivity)
    unittest.TextTestRunner(verbosity=2).run(suite)