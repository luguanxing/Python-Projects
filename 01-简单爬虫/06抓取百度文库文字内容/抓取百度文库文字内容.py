##############获取百度文库内容######################
import urllib.request as request
import re

file = open("毛概.txt", "w");

for i in range(0,23):
    #打开wap纯文字文库页面各页,这里以毛概内容1-23页为例，代替手工复制
    url = "https://wapwenku.baidu.com/view/0ff3d997650e52ea54189839.html?pn="+str(i+1)+"&pu=";
    response = request.urlopen(url);
    html = response.read();
    html = html.decode("utf-8");

    #获取文库页面文字内容
    index1 = re.search(r'<div class="content bgcolor1">', html);
    index2 = re.search(r'<div class="pagebox">', html);
    data = re.compile('<p class="txt">(.*?)</p>');
    texts = data.findall(html, index1.start(), index2.start());

    #写入文件
    for text in texts:
        file.write(text);
        file.write("\n");

file.close();



