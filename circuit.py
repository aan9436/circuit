
import define

class Cirsuit:
    def __init__(self,name):
        self.name=name
        self.have=[]
        self.status=False
    def add(self,ele):
        ele.parent=self
        ele.belongs=self
        self.have.append(ele)
    def turn_on(self):
        self.status=True
        for i in self.have:
            i.update(self.status)

    def check(self):
        lst=self.have
        if lst:
            for i in lst:
                if i.type==define.ELECTRICAL_APPLIANCES:
                    return False
                return i.check()
        return True
