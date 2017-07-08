import threading
import time

def action(arg):
    time.sleep(1);
    print( '子线程%s' % threading.currentThread().getName());

for i in range(10):
    t =threading.Thread(target=action, args=(i,));
    #前台线程serDeamon(False)，则等待前台线程也执行完成后，主线程才停止
    #后台线程serDeamon(True)，则后台线程不论成功完成与否，主线程均停止
    t.setDaemon(False);
    t.start();

print("主线程");