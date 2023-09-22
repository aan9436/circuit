
import define

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
