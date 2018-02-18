# 组合：类和类之间进行关联


class School:
    def __init__(self,name,addr,course):
        self.name = name
        self.addr = addr
        self.course = course


class Course:
    def __init__(self,name,price,teacher):
        self.name = name
        self.price = price
        self.teacher = teacher

class Teacher:
    def __init__(self,name):
        self.name = name

alex = Teacher('alex')
python = Course('python',1000,alex)
oldboy = School('oldboy','beijing',python)

print(python.teacher.name)
print(oldboy.course.name)

