from circuit import *
from element import *

main=Circuit("main")#创建电路“main”
s=OnePoleSwitch("s")#开关“s”
m=Motor("M")
r=Ring('r')
#添加从属关系
main.add(s)
s.add(m)
m.add(r)
main.draw()

main.turn_on()
s.close()
print(r.status)