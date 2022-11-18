import mysql.connector
import time
import datetime

def collect(times):
    localConfig = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'senseDB'
    }

    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()
    cr.execute(f"INSERT INTO data (collectorID, temp, humidity, date) VALUES (1, {temp}, {humidity}, '{date}')")
    cr.execute("SELECT * FROM data")
    res = cr.fetchall()
    print(res[-1])
    cn.commit()
    time.sleep(2)


    cn.close()
