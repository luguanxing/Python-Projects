##################正则表达式使用########################
import re

#编译正则表达式
p = re.compile("[a-z]");
res = p.search("123 abc edf");
print('p.search("123 abc edf")');
print(res, end='\n\n');

#使用编译标志,?:表示不处理子组
test = re.compile(r"""
    (?:                                      #重复3次数字加小数点匹配
        (?:                                  #数字匹配
            [01]? \d? \d |                  #百位为0或1时十位个位任意,百位十位可有可无
            2 [0-4] \d |                     #百位为2十位为0-4时,个位任意
            2 5 [0-5]                        #百位为2十位为5时,个位0-5
        )
        \.                                   #小数点
    ) {3}
    (?:                                      #最后一次数字匹配，不带小数点
        [01]? \d? \d |
        2 [0-4] \d |
        2 5 [0-5]
    )
 """, re.VERBOSE)
res = test.findall("local192.168.0.1 baidu14.14.14.14 google8.8.8.8")
print('test.findall("local192.168.0.1 baidu14.14.14.14 google8.8.8.8")');
print(res, end='\n\n');

#使用参数
p = re.compile("[a-z]");
res = p.search("123 abc edf", 6);
print('p.search("123 abc edf", 6)');
print(res, end='\n\n');

#使用返回对象
res = re.search(r"(\w+) (\w+)", "hello 123.ads");
print('re.search(r"(\w+) (\w+)", "hello 123.ads")');
print(res);
print('res.group()');
print(res.group());
print("res.start()=" + str(res.start()));
print("res.end()=" + str(res.end()));
print("res.span()=" + str(res.span()));