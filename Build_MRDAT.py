# importo le librerie
import csv
import Cleaner
import sys

csv.field_size_limit(sys.maxsize)  # risolve il problema di overflow

with open('File_Parsered.csv', 'rt', encoding='utf8') as f, \
        open('/Users/robertopenna/Desktop/Archivio/UNIMIB/Stage/JST-master/data/MR.dat', 'wt', encoding='utf8') as d:
    csv_f = csv.reader(f)
    next(csv_f)

    for row in csv_f:

        idtweet = row[0]
        string = row[1]
        string_clean = Cleaner.clean(string)
        d.write('Tweet' + idtweet + ' ' + string_clean + '\n')
