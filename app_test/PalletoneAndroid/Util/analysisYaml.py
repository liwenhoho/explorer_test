# -*- coding:utf-8 -*-
__author__ = 'miho'

import yaml
import os
import sys

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def analysisYaml(yamlPathStr):
    filePath = PATH(yamlPathStr)
    print(filePath)
    try:
        #opened_file = file(recover_path, 'r')
        with file(filePath, 'r') as opened_file:
            recover_wallet = opened_file.read()
            content = yaml.load(recover_wallet, Loader=yaml.FullLoader)
            print(content)
            return content
    except Exception,e:
        print Exception, ":", e
        print("Yaml file not found.")