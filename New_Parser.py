# importo le librerie
import json
import csv

# Chiedo all'utente il percorso del file che devo parsare
input_user = input("immettere percorso File .json: ")

# apro e parso il file .json
data = open(input_user).read()
data_parsed = json.loads(data)

# creo e apro un file .csv per scrivere
csv_file = open("File_Parsered.csv", 'w')
# creo il writer
csvwriter = csv.writer(csv_file)

# ciclo per tradurre il file .json in quello .csv
# scrivo l'header
header = ['id', 'text', 'sentiment']
csvwriter.writerow(header)

idtweet = 0

# vado a cercare i values() corrispondenti a text e sentiment
for tweet in data_parsed:
    mylist = []
    idtweet += 1
    mylist.append(idtweet)
    header_1Lev = tweet.keys()

    for keys1lev in header_1Lev:
        if "text" in keys1lev:
            mylist.append(tweet["text"])

    for temp in tweet.values():
        if isinstance(temp, dict) == 1:
            header_2Lev = temp.keys()

            for keys2lev in header_2Lev:
                if "sentiment" in keys2lev:
                    mylist.append(temp["sentiment"])

    if len(mylist) != 3:
        mylist.append("N/A")

    csvwriter.writerow(mylist)

# salvo e chiudo il file .csv
csv_file.close()
