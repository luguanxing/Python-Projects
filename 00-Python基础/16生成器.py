####################生成器###########################
def myGen():
    print("执行生成器");
    yield "暂停1下";
    yield "暂停2下";

def fibs():
    a = 0;
    b = 1;
    while True:
        t = a;
        a = b;
        b = t + b;
        yield b;

####################测试实例#########################
mg = myGen();
print(next(mg));
print(next(mg));
try:
    print(next(mg));
except StopIteration:
    print("已结束");
print("");

fibs = fibs();
for item in fibs:
    if (item > 100):
        break;
    print(item);
print("");

div2not3 = [i for i in range(100) if not(i%2) and (i%3)];
print("100以内能被2整除不难被3整除的数字");
print(div2not3);
print("");

check1 = [i for i in [1,2,3,3]];
print("check1 = [i for i in [1,2,3,3]];");
print(check1);
print("");

check2 = [i for i in {1,2,3,3}];
print("check2 = [i for i in {1,2,3,3}];");
print(check2);
print("");

check3 = {i for i in [1,2,3,3]};
print("check3 = {i for i in [1,2,3,3]};");
print(check3);
print("");

