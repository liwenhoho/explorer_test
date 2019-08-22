import os
from PalletoneAndroid.Util import analysisYaml
import platform

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def setCapbility(deviceNum=0):
    content = analysisYaml.analysisYaml("../Config/env_params.yml")
    kwargs = systemInfo()
    item = whichSystem(content, **kwargs)
    desired_caps = {}
    desired_caps['deviceName'] = content['devices'][deviceNum]['deviceName']
    desired_caps['platformName'] = content['devices'][deviceNum]['platformName']
    desired_caps['platformVersion'] = content['devices'][deviceNum]['platformVersion']
    desired_caps['app'] = PATH(item)
    desired_caps['appPackage'] = content['devices'][deviceNum]['appPackage']
    desired_caps['appActivity'] = content['devices'][deviceNum]['appActivity']
    return desired_caps

def systemInfo():
    #plat_tuple=platform.architecture()
    system = platform.system()
    plat_version = platform.platform()
    print("System is: %s, Version is: %s\n" %(system,plat_version))
    kwargs = {'system':system,'plat_version':plat_version}
    #print("System info is: %s\n" %kwargs)
    return kwargs

def whichSystem(content,**sysInfo):
    item = content['system'][0]['package_path']
    return item

if __name__ == '__main__':
    pass
    #setCapbility()