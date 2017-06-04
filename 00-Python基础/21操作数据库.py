##############操作mysql######################
import pymysql

# 创建连接
conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='student',
        charset='utf8'
);

# 创建游标
cursor = conn.cursor();

# 执行SQL，并返回受影响行数
effect_row = cursor.execute("select * from score");

# 查看数据
results = cursor.fetchmany(effect_row);
for result in results:
    print(result);

# 执行SQL，并返回受影响行数,执行多次
effect_row = cursor.execute("INSERT INTO student.score (NAME, math, physics, english)VALUES('测试名字', '90', '90', '90');");
if (effect_row > 1):
    print("添加数据成功");

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close();

# 关闭连接
conn.close();