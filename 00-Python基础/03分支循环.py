score = int(input("请输入成绩:"))
if (90 <= score <= 100):
    print("A")
elif (80 <= score < 90):
    print("B")
elif (70 <= score < 80):
    print("C")
elif (60 <= score < 70):
    print("D")
elif (0 <= score < 60):
    print("不及格")
else:
    print("数值有误")
    
print("\n")
gpa = (score-50)/10 if score > 60 else 0
print("GPA="+str(gpa))

print("\n")
print("1-10奇数:")
for i in range(1,10,2):
    print(i)

print("\n")
print("分值循环测试")
for i in range(10):
    if (i%2):
        print(i)
        continue
    i+=2
    print(i)
