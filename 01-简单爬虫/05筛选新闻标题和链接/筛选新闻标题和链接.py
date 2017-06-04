##############获取网站新闻标题和地址######################
import urllib.request as request
import re

#下载网页
response = request.urlopen("http://www.163.com");
html = response.read();
html = html.decode("gbk");

#截取要问内容
index1 = re.search(r'<div class="yaowen_news">', html);
index2 = re.search(r'<div class="yaowen_dada_news">', html);
data = re.compile('<a href="(.*?)">(.*?)</a>');
yaowen = data.findall(html, index1.start(), index2.start());

#排除重复
set = set();
for new in yaowen:
    if (new not in set):
        set.add(new);
        print(new);

