from circuit import *
from element import *

main=Cirsuit("main")#创建电路“main”
s=OnePoleSwitch("s")#创建单刀开关“s”
main.add(s)#把开关“s”添加到电路“main”下
l1=Light("l1")#创建灯泡“l1”
s.add(l1)#把灯泡“l1”添加到开关“l”下
l2=Light("l2")#创建灯泡“l2”
s.add(l2)#把灯泡“l2”添加到开关“l”下
main.turn_on()#开启电源
s.close()#闭合开关“s”
print(l1.status)#显示灯泡“l1”状态（工作）
print(l2.status,end="\n\n")#显示灯泡“l2”状态（工作）
l1.broken()#破坏灯泡“l1”
print(l1.status)#显示灯泡“l1”状态（不工作）
print(l2.status)#显示灯泡“l2”状态（工作）
print(main.check())#检测是否短路（未短路）