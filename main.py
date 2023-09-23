from circuit import *
from element import *

main=Circuit("main")#创建电路“main”
s=OnePoleSwitch("s")#开关“s”
l1=Light("L1")#灯泡“L1”
l2=Light("L2")#灯泡“L2”
# l3=Light("L3")
# l4=Light("L4")
# l5=Light("L5")
# l6=Light("L6")
# l7=Light("L7")
# l8=Light("L8")
# l9=Light("L9")
# l10=Light("L10")

#添加从属关系
main.add(s)
s.add(l1)
l1.add(l2)
# l2.add(l3)
# l3.add(l4)
# l4.add(l5)
# l5.add(l6)
# l6.add(l7)
# l7.add(l8)
# l8.add(l9)
# l9.add(l10)
main.draw()