#-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from BasePage import BasePage

class viewSettingsPage(BasePage):
        #page_url = 'viewSettings'
        Sequence = (By.CSS_SELECTOR,'input.form-control')
        tableTitle1 = (By.CSS_SELECTOR, 'tr[role="row"] > th.sorting_disabled.dt-head-center')
        logo = (By.CSS_SELECTOR, 'a.navbar-brand.mr-1')
        lines = (By.CSS_SELECTOR, 'tr[role="row"]')
        rows = (By.CSS_SELECTOR, 'td.dt-head-center')
        pages = (By.CSS_SELECTOR, 'li.paginate_button > a.page-link')
        disableButton = (By.CSS_SELECTOR, 'li.paginate_button.disabled')
