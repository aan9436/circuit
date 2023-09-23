from element import *
import define
import math
from draw import *
class Circuit:
    def __init__(self,name,voltage=4.5,resistance=1e-3):
        self.name=name
        self.have=[]
        self.status=False
        self.voltage=voltage
        self.resistance=resistance
    def add(self,ele):
        ele.parent=self
        ele.belongs=self
        self.have.append(ele)
    def turn_on(self):
        self.status=True
        for i in self.have:
            i.update(self.status)#,self.voltage,self.resistance)

    def is_short(self):
        lst=self.have
        if lst:
            for i in lst:
                if i.type==define.ELECTRICAL_APPLIANCES:
                    return False
                return i.check()
        return True
    def to_series(self):
        num=1
        i=self
        lst=[["power",self.name]]
        while i.have!=[]:
            num+=1
            i=i.have[0]
            lst.append([i.element,i.name])
        print(lst)
        l1,l2,l3,l4=[],[],[],[]
        one=math.ceil(num/4)
        two=round((num-one)/3)
        three=math.ceil((num-one-two)/2)
        four=num-one-two-three
        print(one,two,three,four)
        r=30
        r1=min(r,150/(2*one+1))
        r2=min(r,150/(2*two+1))
        r3=min(r,150/(2*three+1))
        r4=min(r,150/(2*four+1))
        # print(r1,r2,r3,r4)
        slice1=max(2*r1,(400-2*r1*one)/(one+1))
        slice2=max(2*r2,(300-2*r2*two)/(two+1))
        slice3=max(2*r3,(400-2*r3*three)/(three+1))
        slice4=max(2*r4,(300-2*r4*four)/(four+1))
        # print(slice1,slice2,slice3,slice4)
        # print(each)
        for i in range(one):
            l1.append([lst[i][0],600-(i+1)*(slice1+r1)-i*r1,450,lst[i][1]])
        for i in range(two):
            l2.append([lst[one+i][0],200,450-(i+1)*(slice2+r2)-i*r2,lst[one+i][1]])
        for i in range(three):
            l3.append([lst[one+two+i][0],200+(i+1)*(slice3+r3)+i*r3,150,lst[one+two+i][1]])
        if num>3:
            for i in range(four):
                l4.append([lst[one+two+three + i][0], 600, 150+(i+1)*(slice4+r4)+i*r4,lst[one+two+three + i][1]])
        dic={
            "radius":[r1,r2,r3,r4],
            "lst":[l1,l2,l3,l4]
        }
        return dic
    def draw(self):
        draw=Draw()
        draw.to_draw(self)
        run()

if __name__=="__main__":
    circuit = Circuit("main")  # 创建电路“main”
    s = OnePoleSwitch("s")  # 创建单刀开关“s”
    circuit.add(s)  # 把开关“s”添加到电路“main”下
    l = Light("l")  # 创建灯泡“l1”
    s.add(l)  # 把灯泡“l1”添加到开关“l”下
    l1 = Light("l1")  # 创建灯泡“l1”
    l.add(l1)  # 把灯泡“l1”添加到开关“l”下
    l2 = Light("l2")  # 创建灯泡“l1”
    l1.add(l2)  # 把灯泡“l1”添加到开关“l”下
    l3 = Light("l3")  # 创建灯泡“l1”
    l2.add(l3)  # 把灯泡“l1”添加到开关“l”下
    print(circuit.to_series())
