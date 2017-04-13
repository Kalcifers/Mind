# importo le librerie
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)  # risolve il problema di overflow

with open('File_Parsered.csv', 'rt', encoding='utf8') as f,\
        open('CleanTweet.csv', 'wt', encoding='utf8') as d:
    csv_f = csv.reader(f)
    csvwriter = csv.writer(d)
    next(csv_f)

    for row in csv_f:
        mylist = []
        mylist.append(row[0])

        k = row[1].lower()
        k = re.sub("[\n\t\n\s]*<[^>]*>[\n\t\s]*", " ", k)  # remove html tags
        k = re.sub("[\n]+", " ", k)  # remove newline
        k = re.sub("[\s]*https?/?/?\S+", "", k)  # remove links
        k = re.sub("[\s]*-&\S+", "", k)  # remove indentation
        k = re.sub("[\s]{2,}", " ", k)  # remove multiple spaces
        k = re.sub("^\s+", "", k)

        mylist.append(k)

        if k != "":
            csvwriter.writerow(mylist)

