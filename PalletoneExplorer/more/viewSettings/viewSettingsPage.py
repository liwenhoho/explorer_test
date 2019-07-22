#-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from BasePage import BasePage

class viewSettingsPage(BasePage):
        page_url = 'viewSettings'
        Sequence = (By.CSS_SELECTOR,'input.form-control')
        tableTitle1 = (By.CSS_SELECTOR, 'tr[role="row"] > th.sorting_disabled.dt-head-center')
        logo = (By.CSS_SELECTOR, 'a.navbar-brand.mr-1')
        lines = (By.CSS_SELECTOR, 'tr[role="row"]')
        rows = (By.CSS_SELECTOR, 'td.dt-head-center')
        pages = (By.CSS_SELECTOR, 'li.paginate_button > a.page-link')
        disableButton = (By.CSS_SELECTOR, 'li.paginate_button.disabled')

        def open(self):
            url=self.base_url+self.page_url
            self._open(url)

        def getRowsData(self):
            #self.open()
            tableTitle= self.find_element(*self.tableTitle1)
            for n in range(len(tableTitle)):
                print tableTitle[n].text
            lines = self.find_element(*self.lines)
            # rows = self.driver.find_elements_by_css_selector('tr[role="row"] > td.dt-head-center')
            dictList = []
            for l in range(1, len(lines)):
                sysConfig = dict()
                #row = lines[l].find_element(*self.rows)
                line_text = lines[l].text
                key_value = line_text.split(' ')
                key_value[1] = str(key_value[1])
                key_value[2] = str(key_value[2])
                sysConfig['key'] = key_value[1]
                sysConfig['value'] = key_value[2]
                # print sysConfig
                dictList.append(sysConfig)
            print dictList
            return dictList
            #for pageItem,dictItem in zip(pageAdd,dictList):
            #    #print pageItem
            #    print dictList