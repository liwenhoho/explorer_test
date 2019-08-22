#-*-coding:utf-8-*-
import BaseLog
import time
import os
from time import sleep
import threading
from PalletoneAndroid.Base.BaseAndroidPhone import getPhoneInfo

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Log:
    def __init__(self, devices):
        get_phone = getPhoneInfo(devices)
        phone_name = get_phone["brand"] + "_" + get_phone["model"] + "_" + "android" + "_" + get_phone["release"]
        global logger, resultPath, logPath
        resultPath = PATH("../log")
        #phone_name +
        logPath = os.path.join(resultPath, (time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = BaseLog.getLogger()
        self.logger.setLevel(BaseLog.INFO)

        # create handler,write log
        fh = BaseLog.FileHandler(os.path.join(logPath, "outPut.log"))
        # Define the output format of formatter handler
        formatter = BaseLog.Formatter('%(asctime)s  - %(levelname)s - %(name)s[line:%(lineno)d]: %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def getMyLogger(self):
        return self.logger

    def buildStartLine(self, caseNo):
        startLine = "----  " + caseNo + "   " + "   " + \
                    "  ----"
        self.logger.info(startLine)

    def buildEndLine(self, caseNo):
        endLine = "----  " + caseNo + "   " + "END" + "   " + \
                  "  ----"
        self.logger.info(endLine)
        self.checkNo = 0

    def writeResult(self, result):
        reportPath = os.path.join(logPath, "report.txt")
        flogging = open(reportPath, "a")
        try:
            flogging.write(result + "\n")
        finally:
            flogging.close()
        pass

    def resultPass(self, caseNo):
        self.writeResult(caseNo + ": PASS")

    def resultFail(self, caseNo, reason):
        self.writeResult(caseNo + ": FAIL--" + reason)

    def checkPointOK(self, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": OK")
        print("==用例_%s检查点成功==" % caseName)
        # take shot 默认去掉成功截图
        # self.screenshotPass(driver, caseName)

    def checkPointNG(self, driver, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": NG")
        return self.screenshotNG(driver, caseName)

    def screenshotPass(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_PASS.png"
        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))

    def screenshotNG(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_NG.png"
        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))
        return os.path.join(screenshotPath + screenshotName)

    def screenshotERROR(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "ERROR.png"
        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))

class myLog:
    """
    This class is used to get log
    """
    log = None
    mutex = threading.Lock()
    def __init__(self):
        pass

    @staticmethod
    def getLog(devices):
        if myLog.log is None:
            myLog.mutex.acquire()
            myLog.log = Log(devices)
            myLog.mutex.release()
        return myLog.log

if __name__ == "__main__":
    logTest = myLog.getLog("devices")
    # logger = logTest.getMyLogger()
    logTest.buildStartLine("11111111111111111111111")