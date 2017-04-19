import pymysql

# apro una connessione al DB
db = pymysql.connect(host='localhost',
                     user='root',
                     password='carlitos')

# assegno un cursore
cursor = db.cursor()

# operazioni del cursore
cursor.execute("USE mind;")

sql = """"""

try:
    # Eseguo il comando
    cursor.execute(sql)
    # Committo i cambiamenti
    db.commit()
except:
    # In caso di errori
    db.rollback()

# chiudo la connessione
db.close()
