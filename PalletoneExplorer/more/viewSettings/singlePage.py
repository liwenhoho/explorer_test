#-*-coding:utf-8-*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilFunc.utilFunc import utilFunc
from Config import Config
import HTMLTestRunner
import time
import os

class singlePage(unittest.TestCase):
    def setUp(self):
        #chrome_driver = "D:\Python2.7\chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        #self.url = "http://123.126.106.89:8000/"
        #self.url = "http://123.57.60.155:8545"
        self.url = "http://123.126.106.84:8000/"

    def getRowsData(self):
        #self.driver.get(self.url+"viewSettings")
        tableTitle1= self.driver.find_elements_by_css_selector('tr[role="row"] > th.sorting_disabled.dt-head-center')
        for n in range(len(tableTitle1)):
            print tableTitle1[n].text
        lines = self.driver.find_elements_by_css_selector('tr[role="row"]')
        #rows = self.driver.find_elements_by_css_selector('tr[role="row"] > td.dt-head-center')
        dictList = []
        for l in range(1,len(lines)):
            sysConfig = dict()
            row = lines[l].find_elements_by_css_selector("td.dt-head-center")
            line_text = lines[l].text
            key_value =line_text.split(' ')
            key_value[1] = str(key_value[1])
            key_value[2] = str(key_value[2])
            sysConfig['key'] = key_value[1]
            sysConfig['value'] = key_value[2]
            #print sysConfig
            dictList.append(sysConfig)
        print dictList
        #for r in range(len(rows)):
        #    print rows[r].text
        utilFunc().sysConfigList()

    def test_assertElements(self):
        result = utilFunc().sysConfigList()
        pageAdd = utilFunc().settings_paging(result, 1, Config.Settings_PagingAmount)

        dictList = [{'value': '15000', 'key': 'GenerateUnitReward'}, {'value': '288745000', 'key': 'PledgeDailyReward'},
                    {'value': '100', 'key': 'RewardHeight'}, {'value': '5242880', 'key': 'UnitMaxSize'},
                    {'value': 'P1HBfefWUpWm3aVrhCsEDe1MwBkYexBHLt7', 'key': 'FoundationAddress'},
                    {'value': '5000000000', 'key': 'DepositAmountForMediator'},
                    {'value': '1000000000', 'key': 'DepositAmountForJury'},
                    {'value': '100000000', 'key': 'DepositAmountForDeveloper'},
                    {'value': '5', 'key': 'ActiveMediatorCount'}, {'value': '1', 'key': 'MaximumMediatorCount'}]

        for num in range(len(pageAdd)):
            try:
                self.assertEqual(dictList[num]['key'], pageAdd[num]['key'])
                self.assertEqual(dictList[num]['value'], pageAdd[num]['value'])
            except AssertionError:
                print dictList[num]['key'] + " FAIL.Expect: " + dictList[num]['value']
            else:
                print dictList[num]['key'] + " PASS"

    def test_ccc(self):
        self.driver.get(self.url + "viewSettings")
        #pages = self.wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, "li.paginate_button > a.page-link"))
        self.wait = WebDriverWait(self.driver, 10)
        paginate = self.driver.find_elements_by_css_selector("li.paginate_button > a.page-link")
        #print str(len(paginate)-1)
        for i in range(1,len(paginate)-1):
            paginate = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.paginate_button > a.page-link")))
            #pages = self.driver.find_elements_by_css_selector("li.paginate_button > a.page-link")
            paginate[i].click()
            self.getRowsData()
            time.sleep(3)
            #print paginate[i].text

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main()
    print("main-start")
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(singlePage))
    now = time.strftime('%Y-%m-%d%H%M%S')
    print("main-getcwd")
    print(os.getcwd())
    filename = open(os.getcwd() + '/TestResult_' + now + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title=u'单元测试报告',description =u'单元测试报告')
    runner.run(suite)
    print("main-stop")
    filename.close()