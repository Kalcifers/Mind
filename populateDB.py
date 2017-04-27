import traceback
import pymysql

# apro una connessione al DB
db = pymysql.connect(host='localhost',
                     user='root',
                     password='carlitos',
                     db='mind',
                     local_infile=1)

# assegno un cursore
cursor = db.cursor()

# operazioni del cursore

sql = """LOAD DATA LOCAL INFILE '/Users/robertopenna/Desktop/Archivio/UNIMIB/Stage/Mind/CleanTweet.csv'
INTO TABLE tweet
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\\r\\n';"""

try:
    # Eseguo il comando
    cursor.execute(sql)
    # Committo i cambiamenti
    db.commit()
except:
    # In caso di errori
    print(traceback.format_exc())

# chiudo la connessione
db.close()
