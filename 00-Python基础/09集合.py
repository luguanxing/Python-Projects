type1 = {};
type2 = {1,2,3}

print("type1 %s is " % str(type1) + str(type(type1)));
print("type2 %s is " % str(type2) + str(type(type2)));
print();

num = {1,2,3,4,5,4,3,2,1}
print("num = {1,2,3,4,5,4,3,2,1}");
print("set num = "+str(num));
print();

set1 = {"a", "b", "a"};
set2 = set(["b","b","a"]);
print("set1{\"a\", \"b\", \"a\"} == set2set([\"b\",\"b\",\"a\"]) is "+str(set1 == set2));
print();

print("利用集合排序除重复1,3,3,2,5,2,6,5,4,6");
list1 = list(set((1,3,3,2,5,2,6,5,4,6)));
print(list1);
print();

print("in num:");
for each in num:
    print(each, end=" ");
print("\n");

print("6 in num is " + str(6 in num));
print("3 in num is " + str(3 in num));
print("9 not in num is " + str(9 not in num));
print();

num.add(9);
num.remove(2);
print(num);