###################显示错误具体类型######################
def test1():
    try:
        f = open("一个不存在的文件.txt");
        print(f.read());
    except OSError as reason:
        print("打开文件错误! 原因："+str(reason));
    except TypeError as reason:
        print("文件类型错误! 原因："+str(reason));
    finally:
        if ('f' in dir()):  #注意判断变量是否创建且存在
            f.close();
    print();


###################显示错误具体类型######################
def test2():
    try:
        f = open("不可能存在的文件.txt");
        print(f.read());
    except (OSError, TypeError) as reason:
        print("错误! 原因："+str(reason));
    finally:
        if ('f' in dir()):
            f.close();
    print();

###################捕获所有异常######################
def test3():
    try:
        f = open("不存在的文件.txt");
        print(f.read());
    except :
        print("错误!");
    finally:
        if ('f' in dir()):
            f.close();
    print();

###################手动抛出自定义异常######################
def testme():
    try:
        raise ZeroDivisionError("除数不能为0！！");
    except  ZeroDivisionError as zr:
        print("错误! 原因："+str(zr));
    print();

###################测试with处理文件######################
def testwith():
    try:
        with open("某个文件.txt") as f:
            f.read();
    except :
        print("错误!");
    print();

#########################################
test1();
test2();
test3();
testme();
testwith();
