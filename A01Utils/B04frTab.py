# B04frTab.py
# получение списка ключ '\t' значение
# из таблицы
# tab2list

import codecs

from B03toTable import from2tab

OUT_LIST_TXT = "B04out.txt"
IN_TABLE_TXT = "B04in.txt"

def readFile():
    string1 = ''
    with codecs.open(IN_TABLE_TXT, 'r', 'utf-8') as file:
        string1 = file.read()
    return string1

def writeFile(string1):
    with codecs.open(OUT_LIST_TXT, 'w', 'utf-8') as file:
        file.write(string1)


def tab2list(string1):
    listTr = from2tab(string1, 'tr')

    listTd = []
    listTrTd = []
    k = 0
    countTd = 0
    for strListTr in listTr:
        listTd = from2tab(strListTr, 'td')
        if k == 0:
            countTd = len(listTd)
        listTrTd.append(listTd)
    countTr = len(listTrTd)
    list = []
    strTd = ''
    for i in range(int((countTd+1)/2)):
        for j in range(countTr):
            strTd = listTrTd[j][i*2] + '\t' + listTrTd[j][i*2+1]
            list.append(strTd)

    # print(list, listTrTd)

    string2 = '\r\n'.join(list)
    return string2


print("Welcome...", type('a'))
string1 = readFile()

string2 = tab2list(string1)

writeFile(string2)


