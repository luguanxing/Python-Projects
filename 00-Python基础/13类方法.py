####################类的方法#########################
class Test(object):
    def __new__(cls, *args, **kwargs):
        print("我是__new__方法");
        return  object.__new__(cls, *args); #需返回object实例
    def __init__(self, *args):
        print("我是__init__方法");
    def __del__(self):
        print("我是__del__方法");

class Vector():
    def __init__(self, *args):
        length = len(args);
        if (length):
            print("有%d个参数构造函数，即%s:"% (length, str(args)));
            self.x = args[0];
            if (length >= 2):
                self.y = args[1];
            else:
                self.y = 0;
        else:
            print("无参数构造函数")
            self.x = 0;
            self.y = 0;
    def __add__(self, other):
        newx = self.x + other.x;
        newy = self.y + other.y;
        return Vector(newx, newy);
    def __sub__(self, other):
        newx = self.x - other.x;
        newy = self.y - other.y;
        return Vector(newx, newy);
    def __mul__(self, value):
        newx = self.x * value;
        newy = self.y * value;
        return Vector(newx, newy);
    def __rmul__(self, value):
        return self * value;
    def show(self):
        str = ("(%d, %d)" % (self.x, self.y));
        return str;

####################测试实例#########################
t1 = Test();
del t1;
print("");

v0 = Vector();
print("v0 = "+v0.show());
v1 = Vector(1);
print("v1 = "+v1.show());
v2 = Vector(3,5);
print("v2 = "+v2.show());
v5 = Vector(6,7,8,9,0);
print("v5 = "+v5.show());
print("");

vadd = v2 + v5;
print("v2 + v5 = " + vadd.show());
vsub = v2 - v5;
print("v2 - v5 = " + vsub.show());
vcon1 = v2 * 3;
print("v2 * 3 = " + vcon1.show());
vcon1 = 5 * v2;
print("5 * v2 = " + vcon1.show());