import define



class Element:
    def __init__(self,name,tp):
        self.name=name
        self.type=tp
        self.status=False
        self.have=[]
        self.belongs=None
        self.parent=None
        self.given=None
    def update(self,status):
        self.given=status
        self.operation(status)
        self.give()
    def give(self):
        if self.have:
            for i in self.have:
                i.status = self.status
    def operation(self):
        pass
    def add(self,ele):
        ele.parent=self
        ele.belongs=self.belongs
        self.have.append(ele)
    def check(self):
        lst=self.have
        if lst:
            for i in lst:
                if i.type==define.ELECTRICAL_APPLIANCES:
                    return False
                return i.check()
        return True
class Light(Element):
    def __init__(self,name):
        super().__init__(name=name,tp=define.ELECTRICAL_APPLIANCES)
        self.is_broken=False
    def operation(self,status):
        if not self.is_broken:
            self.status=status
        else:
            self.status=False
    def broken(self):
        self.is_broken=True
        self.update(self.given)
    def repair(self):
        self.is_broken=False
        self.update(self.status)
class OnePoleSwitch(Element):
    def __init__(self,name,):
        super().__init__(name=name,tp=define.SWITCH,)
        self.is_closed=False
    def operation(self,status):
        if self.is_closed:
            self.status=status
        else:
            self.status=False
    def open(self):
        self.is_closed=False
        self.update(self.given)
    def close(self):
        self.is_closed=True
        self.update(self.given)