#-*-coding:utf-8-*-
import unittest
from viewSettingsPage import viewSettingsPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilFunc.utilFunc import utilFunc
from Config import Config
from report_template import HTMLTestRunner_cn
import time
import os
import sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print BASE_DIR
libPath = os.path.abspath('../../')
#libPath = os.path.abspath('../../Config')
sys.path.append(libPath)
#print sys.path

class viewSettings(unittest.TestCase):
    def setUp(self):
        #option = webdriver.ChromeOptions()
        #option.add_argument('headless')
        #option.add_argument('no-sandbox')
        #option.add_argument('--disable-gpu')
        #option.add_argument('disable-dev-shm-usage')
        #self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://123.126.106.84:8080/"
        #self.url = "http://123.57.60.155:8545"
        #self.url = "http://123.126.106.84:8000/"

    def test_viewSettings(self):
        settings_page = viewSettingsPage(self.driver,self.url)
        settings_page.open()
        #self.assertElements()
        self.wait = WebDriverWait(self.driver, 15)
        #'''''
        pages =settings_page.find_element(*settings_page.pages)
        for i in range(1,len(pages)-1):
            #print pages[i].text
            pages = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.paginate_button > a.page-link")))
            pages[i].click()
            dictList = settings_page.getRowsData()
            print dictList
            self.assertElements(dictList,i)
            time.sleep(1)
        #'''

    def assertElements(self,dictList,current_page):
        result = utilFunc().sysConfigList()
        pageAdd = utilFunc().settings_paging(result, current_page, Config.Settings_PagingAmount)
        '''
        dictList = [{'value': '15000', 'key': 'GenerateUnitReward'}, {'value': '288745000', 'key': 'PledgeDailyReward'},
                    {'value': '100', 'key': 'RewardHeight'}, {'value': '5242880', 'key': 'UnitMaxSize'},
                    {'value': 'P1HBfefWUpWm3aVrhCsEDe1MwBkYexBHLt7', 'key': 'FoundationAddress'},
                    {'value': '5000000000', 'key': 'DepositAmountForMediator'},
                    {'value': '1000000000', 'key': 'DepositAmountForJury'},
                    {'value': '100000000', 'key': 'DepositAmountForDeveloper'},
                    {'value': '5', 'key': 'ActiveMediatorCount'}, {'value': '1', 'key': 'MaximumMediatorCount'}]
        '''
        for num in range(len(dictList)):
            try:
                self.assertEqual(dictList[num]['key'], pageAdd[num]['key'])
            except AssertionError:
                print dictList[num]['key'] + " FAIL.Expect key: " + dictList[num]['key']
            try:
                self.assertEqual(dictList[num]['value'], pageAdd[num]['value'])
            except AssertionError:
                print dictList[num]['key'] + " FAIL.Expect value: " + dictList[num]['value']
            else:
                print dictList[num]['key'] + " PASS"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
#if __name__ == "viewSettings":
    current_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    #suite = unittest.TestLoader().discover("viewSettings")
    print("Test start")
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(viewSettings))
    #now = time.strftime('%Y-%m-%d')
    print("test getcwd")
    print(os.getcwd())
    filename = open(os.getcwd()+'/Report/TestResult_' + current_time + '.html', 'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=filename,title=u'PalletExplorer测试报告',description =u'测试报告')
    runner.run(suite)
    print("test stop")
    filename.close()