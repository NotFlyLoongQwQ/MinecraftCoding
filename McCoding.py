from McCodingCore import *
import time
try:
    bb = McCoding版本()
    设置窗口标题("McCoding Core " + bb)
    设置屏幕颜色("08")
    显示("McCoding " + VER + " on Windows." + str(time.time()) + " \n By NotFlyLoong \n Copyright © NotFlyLoong. All rights reserved. \n Built On Python")
    def core():
        while True:
            Temp = 输入数据(">>>")
            if Temp == "退出":
                print('如果要退出，请输入"退出()。"')
            elif Temp == "退出()":
                正常退出程序()
            eval(Temp)
            core()
    core()
except:
    print ("我们在您的代码中发现了一个致命错误，请检查您的语法。")
    core()
