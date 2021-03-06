import  urllib.request as request
import  urllib
import random

###############获取一条新IP####################
def getIP():
	ip = '';
	rmd = random.randint(1,34);
	print("========================");
	print("访问第"+str(rmd)+"页");
	response = request.urlopen("http://www.66ip.cn/areaindex_"+str(rmd)+"/1.html");
	html = response.read();
	html = html.decode("raw_unicode_escape");
	ip_1 = html.index("<tr><td>");
	try:
		ip_1 = html.index("<tr><td>", ip_1+1);
		ip_2 = html.index("</td><td>", ip_1+1);
		ip_3 = html.index("</td><td>", ip_2+1);
		ip = html[ip_1+8:ip_2] + ':' + html[ip_2+9:ip_3];
		print("获取该页第1条成功");
		print("========================");
	except ValueError:
		print("获取该页失败");
		print("========================");
	return ip;

###############获取若干IP列表####################
def getIPs(size = 20):
	print("获取"+str(size)+"个代理IP");
	iplist = [];
	while len(iplist) < size:
		iplist = list(set(iplist));
		rmd = random.randint(1,34);
		print("========================");
		print("访问第"+str(rmd)+"页");
		response = request.urlopen("http://www.66ip.cn/areaindex_"+str(rmd)+"/1.html");
		html = response.read();
		html = html.decode("raw_unicode_escape");
		ip_1 = html.index("<tr><td>");
		try:
			while len(iplist) < size:
				ip_1 = html.index("<tr><td>", ip_1+1);
				ip_2 = html.index("</td><td>", ip_1+1);
				ip_3 = html.index("</td><td>", ip_2+1);
				ip = html[ip_1+8:ip_2] + ':' + html[ip_2+9:ip_3];
				iplist.append(ip);
			print("已到数量");
			print("========================");
			print("");
		except ValueError:
			print("第"+str(rmd)+"页已获取完毕");
			print("========================");
			print("");
	return iplist;


###############显示当前IP####################
def showIP(ip):
	proxy_support = request.ProxyHandler({'http': ip});
	opener = request.build_opener(proxy_support);
	opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36')];
	request.install_opener(opener);

	try:
		url = "http://www.baidu.com/s?wd=ip%E6%9F%A5%E8%AF%A2";
		print("========================");
		print("正在验证IP:"+ip+"...");
		response = request.urlopen(url);
		html = response.read().decode('utf-8');
		print("验证代理地址成功");
		index1 = html.index('本机IP:&nbsp;');
		index2 = html.index('</span>',index1);
		index3 = html.index('	    ',index2);
		print("IP:"+html[index1+11:index2]);
		print("地址:"+html[index2+7:index3]);
	except urllib.error.URLError:
		print("验证代理地址出错");
	print("========================");

###############测试函数####################
while True:
	ip = '';
	while (ip == ''):
		ip = getIP();
	print("");
	showIP(ip);
	check = input("是否继续？按Q退出\n\n");
	if (check == 'Q'):
		break;



