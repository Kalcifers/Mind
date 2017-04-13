import pymysql
import csv

mydb = pymysql.connect(host='localhost',
                       user='co302mc',
                       passwd='mafol597',
                       db='co302mc_bike_theft')
cursor = mydb.cursor()
