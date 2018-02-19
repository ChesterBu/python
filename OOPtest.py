
# 角色:学校、学员、课程、讲师
# 要求:
# *1. 创建北京、上海 2 所学校
# *2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# *3. 课程包含，周期，价格
# *5. 创建学员时，选择学校，关联班级
# *5. 创建讲师角色时要关联学校， 
# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
# 6.3 管理视图，创建讲师， 创建班级，创建课程


class School:
    def __init__(self, place):
        self.place = place
        self.course = []
        self.teacher = []
        self.room = []

    def create_courese(self, name, perid, price):
        cou = Course(name, perid, price)
        self.course.append(cou)
        cou = None

    def recurit_teacher(self, name):
        tea = Teacher(name, self)
        self.teacher.append(tea)
        tea = None
    
    def create_room(self,name,teacher):
        roo = Room(name,teacher)
        self.room.append(roo)
        roo = None



class Course:
    def __init__(self, name, perid, price):
        self.name = name
        self.perid = perid
        self.price = price


class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.room = None
        self.has_paied = False
        self.grade = None
    
    def exam(self):
        import random
        self.grade = random.randint(0, 100)

    def pay_tution(self):
        self.has_paied = True

    def choice_class(self, room):
        self.room = room
        room.student.append(self)

    
    

class Teacher:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.room = None

    def choice_room(self, room):
        self.room = room

    def check_student(self):
        if(self.room):
            print(self.room.student)
        else:
            pass


class Room:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.student = []


python = Course('python', '6m', 9999)
linux = Course('linux', '5m', 8888)
go = Course('go', '6m', 9999)

beijing = School('beijing')
shanghai = School('shanghai')

stu1 = Student('xialv',beijing)

alex = Teacher('alex', beijing)

py15 = Room('py15',alex)

# 6.1 学员视图， 可以注册， 交学费， 选择班级

stu1.pay_tution()
stu1.choice_class(py15)
# print(stu1.__dict__)

# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
alex.choice_room(py15)
print(alex.room.name)
print(alex.room.student[0].name)
# stu1.exam()
# print(stu1.grade)
# alex.room.student[0].grade = 100
# print(stu1.grade)

# 6.3 管理视图，创建讲师， 创建班级，创建课程
beijing.recurit_teacher('wupeiqi')
print(beijing.teacher[0].name)
beijing.create_room('py16',beijing.teacher[0])
print(beijing.room[0].__dict__)
shanghai.create_courese('python','6m',9999)
print(shanghai.course[0].name)

