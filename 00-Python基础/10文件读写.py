#################分割十不准函数split_file#################
def split_file(file):
    count = 1;
    bans = "";
    for eachline in file:
        if (eachline[:1] == "第"):
            ban = "第" + str(count) + "条->" +eachline[4:];
            bans += ban;
            count += 1;
            print(ban);
    f = open("bans.txt", "w");
    f.write(bans);
    f.close();

##################将“十不准.txt”拷贝至目录下#################
txt = open("十不准.txt");

print("当前定位指针:"+str(txt.tell()));
print();

print(txt.read());

print("当前定位指针:"+str(txt.tell()));
print();

txt.seek(0,0);
print(txt.read(5));

txt.seek(0,0);
print(txt.readline());

txt.seek(0,0);
split_file(txt);

txt.close();




