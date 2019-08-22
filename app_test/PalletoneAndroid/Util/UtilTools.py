# -*- coding:utf-8 -*-
__author__ = 'miho'
import os
import sys

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def getGain(before,after,keyName='PTN'):
    print("Before " + keyName + " is: %s" % str(before))
    print("After " + keyName + " is: %s" % str(after))
    gain = after-before
    print("Gain value is: %s\n" % str(gain))
    return gain

if __name__=="__main__":
    getGain(899.33333,11.2222222277777999)