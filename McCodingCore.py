# This Mc Coding Core
import sys,time,os,random
VER = "0.1.0.0"
def 退出():
    sys.exit()
def 延时(intime):
    time.sleep(intime)
    return 0
def 显示(intext):
    print(str(intext))
    return 0
def 设置屏幕颜色(INZ16):
    os.system("color " + INZ16)
    return 0
def 暂停():
    os.system("pause")
    return 0
def 输入数据(tips):
    print(tips,end="")
    temp1 = input()
    return temp1
def 调用系统指令(insystem):
    os.system(insystem)
    return 0
def 设置窗口标题(title_in):
    os.system("title " + title_in)
    return 0
def 取整随机数(ain,bin):
    random.randint(ain,bin)
    return 0
def 正常退出程序():
    sys.exit()
#变量/列表/字典为python内置
def 转换_字符型(cas):
    temp2 = str(cas)
    return cas
def 转换_整数型(cas2):
    temp3 = int(cas2)
    return temp3
def McCoding版本():
    return "McCoding 核心模块,版本：测试版" + VER
def 注释(fbbl):
    return fbbl