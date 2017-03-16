# importo le librerie
import csv
import Cleaner
import sys

csv.field_size_limit(sys.maxsize)

i = -1

with open('File_Parsered.csv', 'rt', encoding='utf8') as f, \
         open('/Users/robertopenna/Desktop/Archivio/UNIMIB/Stage/JST-master/data/MR.dat', 'wt', encoding='utf8') as d:
    csv_f = csv.reader(f)

    for row in csv_f:

        i += 1
        if i > 0:
            k = str(i)
            string = row[0]
            string_clean = Cleaner.clean(string)
            d.write('Tweet' + k + ' ' + string_clean + '\n')
