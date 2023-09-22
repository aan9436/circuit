from element import *
import define
import math
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
        #print(lst)
        l1,l2,l3,l4=[],[],[],[]
        each=math.ceil(num/4)
        r=min(25,150/(2*each+1))
        slice1=max(2*r,(400-2*r*each)/(each+1))
        slice2=max(2*r,(300-2*r*each)/(each+1))
        for i in range(each):
            l1.append([lst[i][0],600-slice1-r,450,lst[i][1]])
        for i in range(each):
            l2.append([lst[each+i][0],200,450-slice2-r,lst[each+i][1]])
        for i in range(each):
            l3.append([lst[each*2+i][0],200+slice1+r,150,lst[each*2+i][1]])
        if num>3:
            for i in range(each):
                l4.append([lst[each*3 + i], 600, 150 + slice2 + r])
        dic={
            "radius":r,
            "lst":[l1,l2,l3,l4]
        }
        return dic


if __name__=="__main__":
    circuit = Circuit("main")  # 创建电路“main”
    s = OnePoleSwitch("s")  # 创建单刀开关“s”
    circuit.add(s)  # 把开关“s”添加到电路“main”下
    l = Light("l")  # 创建灯泡“l1”
    s.add(l)  # 把灯泡“l1”添加到开关“l”下
    print(circuit.to_series())
