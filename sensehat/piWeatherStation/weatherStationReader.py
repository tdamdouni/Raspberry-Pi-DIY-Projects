# Programmed by Robert B. Please do not use and claim it is your own. I spent many hours working on this.
# However, feel free to use it to your advantage. I programmed this code to work with CPANEL and Namecheap.
# Enjoy! I had a lot of fun working on this project and it is my pleasure. You can find the end result at: http://robdev.tech/weather

import MySQLdb
import datetime
import time
from random import randint

now = datetime.datetime.now()
dayCheck = str(now.strftime("%B%d%Y"))
last_temperature = 30

# Connects to mySQL database. I could've added arguments such as port, user, etc.
def connectToSQL():
    db = MySQLdb.connect(host="localhost",    # Hostname, which is usually local host.
                 user="USERNAME",         # The username in which you use to log into your database.
                 passwd="****",  # The password.
                 db="DATABASENAME", # The name of the database you are reading/writing to.
                 port=3306)        # The port you are connecting to. In my case, this is port 3309. 3306 is default, however Namecheap forced me to use an SSH tunnel with port 3309.

    return db

'''
This function is used to update the table. There are two seperate tables, one for PHP to read the current data, and the other
is a log of all of the weather data for that specific day. The current_Weather table will only store one value. As you do not want php to have
to read a million values as it loops through. The second table is a complete log of all of the weather data from that day. This
data, at least in my case, will be used to plot graphs.

Function updateTable takes arguments tableList, which is all of the tables to be updated to, and c, an annoying variable I had to 
add because of local and global variable issues.

The function will write data to two tables.
'''
def updateTable(tableList, c):
    
    # Function is used to calculate the difference between two numbers that are given. Specifically for the temperatures recorded.
    # This function will return a string.
    def calculateDifference(numberOne, numberTwo):
        if int(numberOne) > int(numberTwo):
            return ("+" + str(numberOne - numberTwo))
        elif int(numberOne) > int(numberTwo):
            return ("-" + str(numberTwo - numberOne))
 
    # Checks if code has been run before, if not, last_temperature is initialized at 50.
    if c == 0:
        last_temperature = 50
        count = count + 1
    else:   
        last_temperature = last_temperature
    database = connectToSQL()
    cur = database.cursor()
    
    currentTemperature = randint(0, 100)
    currentTime = 948 # Use datetime?
    difference_from_last = calculateDifference(last_temperature, currentTemperature)

    print currentTemperature, last_temperature

    deleteFromCurrent = "DELETE FROM current_Weather LIMIT 1"
    cur.execute(deleteFromCurrent)
    
    valuesToInsertCurrent = "insert into %s VALUES(%d, %d, %s)" % (tableList[0], currentTemperature, currentTime, difference_from_last)
    valuesToInsertLog = "insert into %s VALUES(%d, %d, %s)" % (tableList[1], currentTemperature, currentTime, difference_from_last)

    last_temperature = currentTemperature
    cur.execute(valuesToInsertCurrent)
    cur.execute(valuesToInsertLog)
    
    database.close()

# Function will create a new table. Is used to create a new table at the start of every day. The format is: 'MONTHDAY,YEAR', or 'May12,2017'
def createTable():

    database = connectToSQL()
    cur = database.cursor()

    # Updates using the Datetime function.    
    date = str(now.strftime("%B%d%Y"))
    dayCheck = date

    cur.execute('''CREATE TABLE %s
                 (loggedTemperature int, loggedTime int, loggedDifference text)''' % (date))

    database.close()

# Function will run the script every minute to read and write new temperatures. Checks if there is a new day or not. If so, a new table is created.
def runScript():
    count = 0
    while True:
        if dayCheck != str(now.strftime("%B%d%Y")):
            createTable()
            # Need to add current temperature, time, for real. Maybe add barometric pressure?
            updateTable(["current_Weather", str(now.strftime("%B%d%Y"))], count)
            print "Added - Date is different!"
            last_temperature = currentTemperature        
            time.sleep(60)        
        else:       
            updateTable(["current_Weather", str(now.strftime("%B%d%Y"))], count)
            print "Added - Date is the same!"
            time.sleep(60)

runScript()
