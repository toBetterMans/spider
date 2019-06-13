import os
import time

# from db import single_mysql

def child(i):
    os.execl("/usr/bin/python", "python", "./spider_child.py", str(i))


if __name__ == '__main__':
    ll = range(0, 100000)
    print(ll)
    # max_sql='SELECT Max(company_number) FROM 11315_company {}'
    # sql_1=' where company_number > 100000000 and company_number < 110000000 '
    # sql_2=' where company_number>110000000 '
    # sql_3 = ' where company_number<100000000 '
    # max=single_mysql.mysql_find_by_param(max_sql.format(sql_3))
    # if max[0]>100000000:
    #     max=single_mysql.mysql_find_by_param(max_sql.format(sql_1))
    # if max[0]>110000000:
    #     max = single_mysql.mysql_find_by_param(max_sql.format(sql_2))
    # i =max[0]
    # while 1:
    #
    #     pid = os.fork()
    #     #print 'pid=',pid
    #     if pid == 0:
    #         child(i)
    #     else:
    #         os.wait3(os.WNOHANG)
    #         while int(os.popen("ps -e | grep python | wc -l").readlines()[0]) >7:
    #             print "The total number of processes is greater than 7 ...%s"%str(i)
    #             time.sleep(1)
    #             os.wait3(os.WNOHANG)
    #     i += 1
    #
    #
    #
    #     if i == 155000000:
    #         break

    max_sql = 'SELECT Max(company_number) FROM 11315_company {}'
    sql_1 = ' where company_number > 100000000 and company_number < 110000000 '
    sql_2 = ' where company_number>110000000 '
    sql_3 = ' where company_number<100000000 '
    max = single_mysql.mysql_find_by_param(max_sql.format(sql_3))
    if max[0] > 100000000:
        max = single_mysql.mysql_find_by_param(max_sql.format(sql_1))
    if max[0] > 110000000:
        max = single_mysql.mysql_find_by_param(max_sql.format(sql_2))
    i = max[0]
    while True:
        pid = os.fork()
        #print 'pid=',pid
        if pid == 0:
            child(i)
        else:
            os.wait3(os.WNOHANG)
            while int(
                    os.popen("ps -e | grep python | wc -l").readlines()[0]) > 7:
                print ("The total number of processes is greater than 7 ...%s") % str(
                    i)
                time.sleep(1)
                os.wait3(os.WNOHANG)
        i += 1

        if i == 155000000:
            break
