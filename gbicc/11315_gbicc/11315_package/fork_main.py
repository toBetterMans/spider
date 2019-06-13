# -*- coding:utf-8 -*-
import os, time


def child(i):
    os.execl("/usr/bin/python", "python", "./spider_child.py", str(i))


if __name__ == '__main__':

    i = 41000000
    while 1:

        pid = os.fork()
        if pid == 0:
            child(i)
        else:
            os.wait3(os.WNOHANG)
            while int(os.popen("ps -e | grep python | wc -l").readlines()[0]) > 18:
                print "The total number of processes is greater than 10 ...."
                time.sleep(1)
                os.wait3(os.WNOHANG)
        i -= 1

        if i == 40000000:
            i = 30000000
	
	if i == 25000000:
	    break


