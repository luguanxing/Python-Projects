province = {"北京":"京",
             "天津":"津 ",
             "上海":"沪",
             "广东":"粤",
             "广西":"桂",
             "四川":"川"
            };

captial = dict(
            中国="北京",
            美国="华盛顿",
            日本="东京",
            俄罗斯="莫斯科",
            英国="伦敦"
        );

print("省份字典="+str(province));
print("广东简称:" +province["广东"]);
print();

print("首都字典="+str(captial));
print("中国首都:" +captial["中国"]);
print();


dict1 = dict.fromkeys((1,2,3));
print("dict1="+str(dict1));
dict2 = dict.fromkeys(('a', 'b', 'c'), "test");
print("dict2="+str(dict2));
dict3 = dict.fromkeys(range(10), "赞");
print("dict3="+str(dict3));
print()

print(dict3.keys());
print("dict3.get(5)="+str(dict3.get(5)));
print("dict3.get(15)="+str(dict3.get(15)));
print()

print("dict1="+str(dict1));
dict1.clear();
print("dict1.clear();\ndict1="+str(dict1));
print();

dict1 = dict2.copy();
print("dict1 = dict2.copy();\ndict1="+str(dict1));
print();

print("dict1.popitem() = "+str(dict1.popitem()));
print("dict1="+str(dict1));
print();

print("dict1.pop('a') = "+str(dict1.pop('a')));
print("dict1="+str(dict1));
print();


dict1.update(b="haha");
dict1.update(x="666");
print("dict1="+str(dict1));
print();
