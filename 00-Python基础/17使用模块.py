####################使用模块###########################
import timeit;
print("导入timeit模块");
print("文件位于"+timeit.__file__);

t = timeit.Timer("x=range(100)");
print("执行1000次'x=range(500)'耗时="+str(t.timeit(number=1000)));
print("");

t = timeit.Timer("sum(range(1,10))");
print("执行默认（1000000）次sum(range(1,500))耗时="+str(t.timeit()));
print("");

t = timeit.Timer("4295824985694.28659464*987659231343.5425");
print("执行默认（1000000）次42958249856942865.9464*98765923134354.25耗时="+str(t.timeit()));
print("");

####################使用自定义模块###########################
import hello as hello
import my.myfunction as mf;
hello.sayhello();
mf.say();
