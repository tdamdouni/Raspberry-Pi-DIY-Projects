# https://forums.pimoroni.com/t/enviro-phat-pymysql-logging/7263

import time
import json
import datetime
import pymysql.cursors
from envirophat import motion

timestamp = datetime.datetime.now()

out = open('enviro.log', 'w')
out.write('motion\ttimestamp\n')

conn = pymysql.connect(user="root",passwd="mersea",host="localhost",database="sensor")
cursor = conn.cursor()

try:
    while True:
        acc2 = motion.accelerometer()
        acc = str(motion.accelerometer())[1:-1]
        
        #json.dump(acc2, out)
        
        out.write('%s\t%s\n' % (acc2, timestamp))
        #acc = acc.split(' ')
        
        #insert="""insert into tbl_name (%s,%s,%s) values (%s, %s, %s);"""

        cursor.executemany("insert into sensor(axis-x, axis-y, axis-z) values (%s, %s, %s)", acc2 )
        conn.commit()

        #cursor.execute(insert % (strList1 + acc2))
        #conn.commit()
        cursor.close()
        conn.close()
        #acc = str(motion.accelerometer())
        #heading = motion.heading()
        #out.write('%s\t%f\t%s\n' % (acc, heading, timestamp))

        time.sleep(0.1)

except KeyboardInterrupt:
    out.close()

import time
import pymysql.cursors
from envirophat import motion
# Import libraries 

conn = pymysql.connect(user="root",passwd="mersea",host="localhost",database="sensor")
cursor = conn.cursor()
# Open a connection to mysql

# Loop 
try:
	while True:

		acc = str(motion.accelerometer())[1:-1]
		# strip square braces form either end of output 

		axisx, axisy, axisz = acc.split(", ")
		# Split the string into three variabes 

		sql = "INSERT INTO `sensor` (`axis-x`, `axis-y`, `axis-z`) VALUES (%s, %s, %s)"
		cursor.execute(sql, (axisx, axisy, axisz))
		# Do our INSERT into mysql 

		conn.commit()
		# Confirm we want to commit this data? 

		time.sleep(0.1)
		# Sleep for 1 millisecond, then get new values 

except KeyboardInterrupt:
	conn.close()