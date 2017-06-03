##################正则表达式练习########################
import re

#使用正则表达式
res = re.search(r"llo", "hello world");
print('re.search(r"llo", "hello world")');
print(res, end='\n\n');

#通配符
res = re.search(r".", "hello world");
print('re.search(r".", "hello world")');
print(res, end='\n\n');

#反斜杠转义字符匹配.
res = re.search(r"\.", "hell. world");
print('re.search(r"\.", "hell. world")');
print(res, end='\n\n');

#反斜杠转义字符匹配数字
res = re.search(r"\d", "hell123 world");
print('re.search(r"\d", "hell123 world")');
print(res, end='\n\n');

#字符类
res = re.search(r"[aeiou]", "hell123 world");
print('re.search(r"[aeiou]", "hell123 world")');
print(res, end='\n\n');

#多个字符类
res = re.search(r"[0-9][0-9][0-9]", "hell123 world");
print('re.search(r"[0-9][0-9][0-9]", "hell123 world")');
print(res, end='\n\n');

#重复匹配
res = re.search(r"l{2}", "hell123 world");
print('re.search(r"el{2}", "hell123 world")');
print(res, end='\n\n');

#重复匹配范围
res = re.search(r"el{1,3}", "hell123 world");
print('re.search(r"el{1,3}", "hell123 world")');
print(res, end='\n\n');

#匹配一个IP地址
res = re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "hello 192.168.0.1 world");
print('re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "hello 192.168.0.1 world")');
print(res, end='\n\n');

#匹配子组
res = re.search(r"(hello)\1", "helle hellohello");
print('re.search(r"(hello)\1", "helle hellohello")');
print(res, end='\n\n');

#匹配子组八进制ASCII
res = re.search(r"(hello)\060", "helle hellohello0");
print('re.search(r"(hello)\060", "helle hellohello0")');
print(res, end='\n\n');

#贪婪匹配
res = re.search(r"<.+>", "<html><div></div></html>");
print('re.search(r"<.+>", "<html><div></div></html>")');
print(res, end='\n\n');

#非贪婪匹配
res = re.search(r"<.+?>", "<html><div></div></html>");
print('re.search(r"<.+?>", "<html><div></div></html>")');
print(res, end='\n\n');

#匹配边界
res = re.findall(r"\bhello\b", "hello hello_(这个不匹配) hello..");
print('re.findall(r"\bhello\b", "hello hello_(这个不匹配) hello..")');
print(res, end='\n\n');

#匹配单词
res = re.findall(r"\w", "我爱北京天安门, 天安门上太阳升");
print('re.findall(r"\w", "我爱北京天安门, 天安门上太阳升")');
print(res, end='\n\n');



