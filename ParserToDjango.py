# apro il documento .newtwords e creo il documento Ready4Django.txt

with open('/Users/robertopenna/Desktop/Archivio/UNIMIB/Stage/JST-master/Results/inference/final_final.newtwords', 'rt',
          encoding='utf8') as f, \
        open('/Users/robertopenna/Desktop/Archivio/UNIMIB/Stage/TCG/static/files/Ready4Django.txt', 'wt', encoding='utf8') as d:
    text = f.readlines()  # ritorna una lista che contiene le righe lette
    cont = []

    for line in text:
        for word in line.split():
            diz = {}
            if word == 'Label' or word == 'Topic':
                break
            else:
                print(word)
                diz['weight'] = line.split()[1]
                diz['text'] = line.split()[0]
                cont.append(diz)
    print(cont)

    listofdict = ','.join(str(x) for x in cont)
    d.write('[' + listofdict + ']')
