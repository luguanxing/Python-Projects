################################有道翻译#################################
import urllib.request as request;
import urllib.parse as parse;
import json;
import time;

while True:
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/";
    str = input("请输入要翻译的内容:\n");

    #设置header
    header={};
    header['Referer'] = 'http://fanyi.youdao.com/';
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36';
    header['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';

    #设置提交表单
    data = {};
    data['i'] = str;
    data['type'] = 'AUTO';
    data['doctype'] = 'json';
    data['xmlVersion'] = '1.8';
    data['keyfrom'] = 'fanyi.web';
    data['ue'] = 'UTF-8';
    data['action'] = 'FY_BY_CLICKBUTTON';
    data['typoResult'] = 'true';
    data = parse.urlencode(data).encode('utf-8');
    req = request.Request(url, data, header);
    response = request.urlopen(req);
    html = response.read().decode('utf-8');

    #打印输出结果
    data = json.loads(html);
    print("===============");
    print(data["translateResult"][0][0]["tgt"]);
    print(data["smartResult"]["entries"][1]);
    print("===============");
    print("");
