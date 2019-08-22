# -*- coding:utf-8 -*-
import logging
import sys
import os
import time

#root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0]))))
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
root_dir = PATH("../log")
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(name)s[line:%(lineno)d]: %(message)s"
LOG_FILE_NAME = root_dir + "log.log"
LOG_ERROR_FILE_NAME = root_dir + "error.log"

class LogUtil:
    def __init__(self):
        global logger, resultPath, logPath
        resultPath = PATH("../log")
        # phone_name +
        logPath = os.path.join(resultPath, (time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = LogUtil.getLogger()
        self.logger.setLevel(LogUtil.INFO)

    @staticmethod
    def get_logger(class_name):
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
        logger = logging.getLogger(class_name)
        logger.setLevel(logging.INFO)
        rf_handler = logging.FileHandler(LOG_FILE_NAME, encoding='utf-8')
        # rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
        rf_handler.setLevel(logging.DEBUG)
        rf_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        f_handler = logging.FileHandler(LOG_ERROR_FILE_NAME, encoding="utf-8")
        f_handler.setLevel(logging.ERROR)
        f_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)
        return logger

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

    def checkPointPass(self, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": PASS")
        print("==用例_%s检查点成功==" % caseName)
        # self.screenshotPass(driver, caseName)

    def checkPointNG(self, driver, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": FAIL")
        return self.screenshotNG(driver, caseName)

    def screenshotPass(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_PASS.png"
        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))

    def screenshotFAIL(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_FAIL.png"
        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))
        return os.path.join(screenshotPath + screenshotName)

    def screenshotERROR(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "ERROR.png"
        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))

if __name__ == "__main__":
    logger = LogUtil.get_logger('LogUtil')
    logger.debug('debug message')
    info = 'info message', 'critical into'
    logger.info(info)


