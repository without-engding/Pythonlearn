'''class Cup:
    capacity = 450
    color = '红色'
    def __init__(self,capacity,color)://构造函数
        self.capacity=capacity
        self.color=color
    def retain_water(self)://代表对象自己
        print(self.color+'我正在装水')
    def keep_water(self):
        print(self.color+'我正在保温')
cup1=Cup(450,'red')
cup2=Cup(370,'green')
print(cup1.capacity)
cup1.keep_water()
cup2.keep_water()'''

'''
class Cup:
    capacity = 450
    color = '红色'
    def __init__(self,capacity,color):#构造函数
        self.capacity=capacity
        self.color=color
    def retain_water(self):#代表对象自己
        print(self.color+'我正在装水')
class Luminous_cup(Cup):
    def __init__(self,capacity,color):
        super().__init__(capacity,color)
    def glow(self):
        print('我在发光')
cup1=Cup(450,'red')
cup2=Luminous_cup(110,'green')
cup1.retain_water()
cup2.glow()
cup2.retain_water()'''
'''
class Cup:
    capacity = 450
    color = '红色'
    def __init__(self,capacity,color):#构造函数
        self.capacity=capacity
        self.color=color
    def retain_water(self):#代表对象自己
        print(self.color+'我正在装水')
class Luminous_cup(Cup):
    def __init__(self,capacity,color):
        super().__init__(capacity,color)
    def glow(self):
        print('我在发光')
    def retain_water(self):
        print('我正在装水，容量为'+str(self.capacity)+'ml')

cup=Luminous_cup(110,'green')
cup.retain_water()
super(Luminous_cup,cup).retain_water()'''

class Cup:
    def __init__(self,capacity,color):#构造函数
        self.__capacity=capacity
        self.color=color
    def __heat(self):
        print('我开始加热')
    def retain_water(self):#代表对象自己
        print(str(self.__capacity)+'的'+self.color+'我正在装水')
        self.__heat()
cup1=Cup(110,'green')
cup1.retain_water()