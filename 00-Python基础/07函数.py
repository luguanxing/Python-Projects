################函数定义段#####################
def hello():
    print("hello world!\n");

def sayhelloto(name):
    print("hello "+name+"!\n");

def add(num1, num2):
    return num1+num2;

def showlist(*params):
    print("有%d个参数" %len(params));
    print("参数为");
    for each in params:
        print(each, end=' ');
    print("\n");

def showParam(*params, param):
    print("参数数组为");
    for each in params:
        print(each, end=' ');
    print("\n参数为"+str(param)+"\n");

def returnlist():
    return 1,2,3;

def returntuple():
    return [1,2,3];

count = 10;

def showlocal():
    count = 5;
    print("local count = "+str(count)+"\n");

def showglobal():
    global count;
    print("global count = "+str(count)+"\n");

def father():
    print("正在调用父函数");
    def son():
        print("正在调用子函数");
    son();

def closure1(x):
    print("外层closure1中x="+str(x));
    def closure2(y):
        print("内层closure2中y="+str(y));
        return x*y;
    return closure2;

add2 = lambda a,b:a+b;

def oddfilter(x):
    return x % 2

def showodd(n):
    return list(filter(oddfilter, range(n)));



################程序段#####################
hello();

sayhelloto("lgx");

print("2+3=%d\n" % add(2,3));

print("a=[1,2,3]");
a=[1,2,3];
showlist(a);

print("a=1,2,3传参用*解包");
a=[1,2,3];
showlist(*a);

print("a=(1,2,3)");
a=(1,2,3);
showlist(a);

print("a=(1,2,3)传参用*解包");
a=(1,2,3);
showlist(*a);

showParam(1,2,3,4,5, param=6);

print("returnlist");
print(returnlist());

print("returntuple");
print(returntuple());
print();

showlocal();
showglobal();

father();
print();

print("closure1(5)(6)");
ret = closure1(5)(6);
print(ret);
print();

print("lambda表达式add2(2,3)");
print(add2(2,3));

print("使用filter和lambda构造技术过滤器");
odds = showodd(20);
print(odds);