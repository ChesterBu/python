class Room:
    tag = 1
    def __init__(self, owner, name, width, height):
        self.owner = owner
        self.name = name
        self.width = width
        self.height = height

    @property      #静态属性，掉用时不需要加括号，当作一个属性来用。类似vue的computed
    def cal_area(self):
        return self.width * self.height
    
    @classmethod   # 类方法，主要供类来调用,实例可调用，但不建议
    def tell_info(cls,x):
        print(cls)
        print('----->',cls.tag,x)
    
    @staticmethod    # 静态方法，名义上归类管理，其实写外面也一样，类和实例都可以调用。而不加staticmethod的话，一般函数实例无法调用，应为会默认给传一个self参数,不能使用类变量，和实例变量，是个工具包
    def wash_body(x,y,z):
        print('%s %s %s 正在洗澡' %(x,y,z) )
        

    

r1 = Room('alex','wc',100,100)
print(r1.__dict__)  #实例只有数据属性，方法都从类里调用

print(r1.cal_area)

Room.tell_info(10)

Room.wash_body('alex','wupeiqi','yuanhao')
r1.wash_body('alex','wupeiqi','yuanhao')

