import os
import random
import sys
import easygui as gui
from datetime import datetime
dt = datetime.today()
banben = 'V3.1'
mima = ['zt','zt']
print('欢迎使用此程序')
print('软件版本'+banben)
print('下方显示软件运行记录：')
def chouxuan(username='临时用户'):    
    gui.msgbox(("欢迎使用抽选助手\n此程序由谢思远授权给\n"+username),'抽选助手',ok_button='开始抽选')
    beilv = [1,2,3,4,5,6,7,8,9,10,'超级加']
    shuchu = random.choice(beilv)
    wenzi = '倍\n恭喜你'
    shuchuwenzi = str(shuchu)
    if username == '临时用户':
        shuchu = random.choice(beilv)
        shuchuwenzi = str(shuchu)
        print(shuchuwenzi+'倍')
        gui.msgbox(shuchuwenzi+'倍',ok_button='退出')
    elif username == '曾甜':
        while True:
            dt = datetime.today()
            shuchu = random.choice(beilv)
            shuchuwenzi = str(shuchu)
            xiaoshi = str(dt.hour)
            fenzhong = str(dt.minute)
            miaozhong = str(dt.second)
            print('在'+xiaoshi+'时'+fenzhong+'分'+miaozhong+'秒'+'VIP用户曾甜抽中了'+shuchuwenzi+'倍')   
            if gui.ccbox(shuchuwenzi+wenzi,('抽选助手 GUI For '+username),choices = ('重新抽选','退出')):
                pass
                
            else:
                break
xuanze  = gui.buttonbox(choices=('登录软件','以游客身份使用','关于软件'),title='功能选择',msg='请选择功能\n未登录状态下仅可抽选一次\n登录账号可连续抽选')
if xuanze == '登录软件':
    yonghushurumima = gui.multpasswordbox(msg='请输入用户名与密码',title='登录软件',fields=('用户名：','密码：'))
    if yonghushurumima == mima:
        dt = datetime.today()
        xiaoshi = str(dt.hour)
        fenzhong = str(dt.minute)
        miaozhong = str(dt.second)
        print('在'+xiaoshi+'时'+fenzhong+'分'+miaozhong+'秒'+'VIP用户曾甜登录成功')   
        chouxuan('曾甜')
    else:
        gui.msgbox('用户名或密码错误','错误信息',ok_button='退出')
        sys.exit
elif xuanze == '以游客身份使用':
    chouxuan()
elif xuanze == '关于软件':
    gui.msgbox('此软件是谢思远于华中师大一附中福星学校九年级时开发的\n主要功能是从1到10以及超级加倍中随机抽取一个\n软件开源地址github.com/AlanGitee/A-Tool','关于软件',ok_button='退出')

