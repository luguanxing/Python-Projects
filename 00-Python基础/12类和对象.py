#####################类的使用########################
class Student():
    def __init__(self, *name):
        if (len(name)):
            print("有参数构造函数")
            self.name = name[0];
        else:
            print("无参数构造函数")
            self.name = "无名氏";
    def introduce(self):
        print("我是"+self.name+"\n");

stu1 = Student();
stu1.introduce();

stu2 = Student("Stu");
stu2.introduce();

#####################类的继承########################
class BigStudent(Student):
    def __init__(self, *name):
        Student.__init__(self, *name);
    def introduce(self):
        print("***");
        super().introduce();

bstu1 = BigStudent();
bstu1.introduce();

bstu2 = BigStudent("BigStu");
bstu2.introduce();