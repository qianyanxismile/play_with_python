# coding:utf8

import pymysql

conn = pymysql.connect(user="read_yu",password="1234_qazxsw",port=11813,host="139.199.37.27")
cursor = conn.cursor()            #获取游标
cursor.execute("use wh_toshop")
sql = "INSERT INTO ts_recharge_card_user_record (fans_id,recharge_card_no,recharge_card_attr_id,shop_id,seller_id,card_name,order_no,create_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"  #sql语句
for i in range(1,10000):  #传值
    cursor.execute(sql,(10, 24,203,1496,1192,15 + int(i),20180124145900391823,1538218783))

    conn.commit()   #提交事务
conn.close()   #关闭数据连接
