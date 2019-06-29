import pymysql.cursors
import time
import random



# coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(1, 10.0)
#此处fourcc的在MAC上有效，如果视频保存为空，那么可以改一下这个参数试试, 也可以是-1
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
out = cv2.VideoWriter('video/output2.avi', fourcc, 10, (640, 480))

i = 1
while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        a = out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("capture/zz" + str(i) + ".jpg", frame)
            i += 1
            print('捕获一个图片')
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()










'''
import os

file = "C:\\Users\\fuchen\\Desktop\\good_park_test"
for root, dirs, files in os.walk("C:\\Users\\fuchen\\Desktop\\good_park_test"):
    print(files)  # 当前路径下所有非目录子文件
    for name in files:
        print(file + "\\" + name)


# 连接服务器操作
connection = pymysql.connect(host='152.136.105.72',  # 服务器地址
                             user='root',  # 数据库账号
                             password='12345',  # 数据库密码
                             db='tcc',  # 使用的是tcc这个表
                             charset='utf8mb4'
                             )

try:
    with connection.cursor() as cursor:
        # 创建sql语句
        sql = "insert into `tcc_tbl` (`tcc_title`, `tcc_author`, `submission_date`) values (%s, %s, %s)"
        # 执行sql语句
        tmp = time.localtime(time.time() - random.random() * 60 * 60 * 24 * 30)
        dateTime = time.strftime('%Y-%m-%d %H:%M:%S', tmp)
        cursor.execute(sql, ("测试title", "测试author",  dateTime))
        # 提交
        connection.commit()
        print('插入成功!')
finally:
    connection.close()
'''

'''
# 更新python库代码
import pip
# pip V10.0.0以上版本需要导入下面的包
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
from time import sleep
import time

# for dist in get_installed_distributions():
#     call("pip install --upgrade " + dist.project_name, shell=True)
'''