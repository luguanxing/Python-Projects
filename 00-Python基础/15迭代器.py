####################迭代器###########################
class Fibs:
    def __init__(self, n = 25):
        self.a = 0;
        self.b = 1;
        self.n = n;
    def __iter__(self):     #重写__iter__和__next__即重新实现for循环
        return  self;
    def __next__(self):
        if self.b > self.n:
            raise  StopIteration("结束");
        a = self.a;
        b = self.b;
        self.a = b;
        self.b = a + b;
        return  self.a;

####################测试实例#########################
string = "hello";
it = iter(string);
while True:
    try:
        item = next(it);
    except StopIteration:
        break;
    print(item);
print("");

fibs = Fibs();
for fib in fibs:
    print(fib);
print("");

fibs = Fibs(10);
for fib in fibs:
    print(fib);


