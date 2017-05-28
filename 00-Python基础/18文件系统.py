####################文件系统##################
import  os;

def BFS(dirpath, blank):
	os.chdir(dirpath);
	files = os.listdir();
	for file in files:
		for i in range(0, int(blank/4)):
			print("║  ", end='');
		print("╚═"+str(file));
		if (os.path.isdir(dirpath+'\\'+file)):
			BFS(dirpath+'\\'+file, blank+4);


####################测试函数##################
print("当前目录为:"+os.getcwd());
print("当前目录文件为:"+str(os.listdir()));
print("遍历当前目录:");
BFS(str(os.getcwd()), 2);
os.mkdir("haha");
os.rmdir("haha");
