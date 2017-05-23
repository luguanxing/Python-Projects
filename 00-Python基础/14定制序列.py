####################定制序列#########################
class myList:
    def __init__(self, * args):
        self.values = [x for x in args];                               #列表值
    def __len__(self):
        return  len(self.values);
    def __getitem__(self, key):
        return self.values[key];
    def pop(self):
        val = 0;
        if (len(self.values) > 0):
            val = self.values[0];
            self.values = self.values[1:];
        return val;
    def show(self):
        print(self.values);

####################测试实例#########################

c1 = myList();
c1.show();
print("c1.len="+str(len(c1)));
print("");

c2 = myList(1,2,3);
c2.show();
print("c2.len="+str(len(c2)));
print("");

for i in range(5):
    print("c2.pop="+str(c2.pop()));
    c2.show();
    print("");
