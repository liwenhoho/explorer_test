#-*- coding=utf-8 -*-
import requests
import json
from time import time
import random
import re
from time import sleep
from Config import Config
import os
import sys
libPath = os.path.abspath('../')
sys.path.append(libPath)

class utilFunc(object):
    #host = 'http://123.57.60.155:8545/'
    host = 'http://123.126.106.82:8545/'

    def __init__(self):
        self.domain = utilFunc.host
        self.headers = {'Content-Type': 'application/json'}

    def runTest(self):
        pass

    def getBalance(self, address, domain=host):
        data = {
            "jsonrpc": "2.0",
            "method": "ptn_getBalance",
            "params": [address],
            "id": 1
        }
        data = json.dumps(data)
        print "Current URL:" + domain
        response = requests.post(url=domain, data=data, headers=self.headers)
        result1 = json.loads(response.content)
        try:
            result = result1['result']
        except KeyError, error:
            print "key " + error.message + " not found.\n"
        else:
            print 'Current Balance: ' + str(result) + '\n'
            return result

    def sysConfigList(self, domain=host):
        data = {
            "jsonrpc": "2.0",
            "method": "ptn_listSysConfig",
            "params": [""],
            "id": 1
        }
        data = json.dumps(data)
        print "Current URL:" + domain
        response = requests.post(url=domain, data=data, headers=self.headers)
        result1 = json.loads(response.content)
        try:
            result = result1['result']
            print 'Sys Config List: ' + str(result) + '\n'
            return result
        except KeyError, error:
            print "key " + error.message + " not found.\n"

    def settings_paging(self,data,current_page,pageSize):
        total = len(data)
        totalPage = total/pageSize
        print "totalPage is: " +str(totalPage)
        print "total is: " + str(total)+"\n"
        k = 0
        pageArr = []
        if current_page > totalPage:
            current_page = totalPage
        if current_page < 1:
            current_page = 1
        i = (current_page - 1) * pageSize
        while i < total:
            if k < pageSize:
                pageArr.append(data[i])
                k+=1
            i+=1
        return pageArr

    def generateReport(self,testunit,classsName):
        pass

if __name__ == '__main__':
    pass