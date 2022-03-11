import datetime
import easygui as gui
import os
import random
import sys
print('欢迎使用倍率抽选助手\n这是上层图形化界面的底层窗口，请勿关闭。')
beilv = [1,2,3,4,5,6,7,8,9,10,'超级加']
banben = 'V3.1'
print('软件版本'+banben)
print('下方显示抽选历史记录：')
shuchu = random.choice(beilv)
wenzi = '倍\n你希望继续嘛？'
shuchuwenzi = str(shuchu)
gui.msgbox("欢迎使用简易倍率抽选助手 GUI For 906""\n此程序提供简易倍率抽选功能\n可选倍率1-10.",'软件介绍',ok_button='开始抽选')
while True:
    shuchu = random.choice(beilv)
    shuchuwenzi = str(shuchu)
    print(shuchuwenzi+'倍')
    if gui.ccbox(shuchuwenzi+wenzi,'简易倍率抽选助手 GUI For 906',choices = ('重新抽选','退出')):
        pass   
        
    else:
        break
        sys.exit
