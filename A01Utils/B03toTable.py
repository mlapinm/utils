#B03toTable.py
# python in_txt out_txt sort
# строки ключ '\t' значение
# сортирует по ключу string2 = sort(string1)
# переводит в таблицу string2 = listNtab(string1, NCOLUMN)
# из NCOLUMN колонок поколоночно

#IN_TXT
# actions	действия
# brief	краткий
# caret	курсор
# collapse	свернуть
# completion	завершение
# implement	реализовать
# intention	намерение
# join	присоединяться
# lookup	просмотр
# override	переопределение
# OUT_TXT
# <table>
# <tr>
# 	<td>actions</td>
# 	<td>действия </td>
# 	<td>collapse</td>
# 	<td>свернуть </td>
# 	<td>intention</td>
# 	<td>намерение </td>
# 	<td>override</td>
# 	<td>переопределение </td>
# </tr>
# <tr>
# 	<td>brief</td>
# 	<td>краткий </td>
# 	<td>completion</td>
# 	<td>завершение </td>
# 	<td>join</td>
# 	<td>присоединяться </td>
# 	<td></td>
# 	<td></td>
# </tr>
# <tr>
# 	<td>caret</td>
# 	<td>курсор </td>
# 	<td>implement</td>
# 	<td>реализовать </td>
# 	<td>lookup</td>
# 	<td>просмотр </td>
# 	<td></td>
# 	<td></td>
# </tr>
# </table>
# <div style="display: none">
# actions	действия
# brief	краткий
# caret	курсор
# collapse	свернуть
# completion	завершение
# implement	реализовать
# intention	намерение
# join	присоединяться
# lookup	просмотр
# override	переопределение
# </div>

import codecs

NCOLUMN = 4
OUT_TXT = "B03out.txt"
IN_TXT = "B03in.txt"

string1 = ""
string2 = ""

def readFile():
    string1 = ''
    with codecs.open(IN_TXT, 'r', 'utf-8') as file:
        string1 = file.read()
    return string1

def writeFile(string1):
    with codecs.open(OUT_TXT, 'w', 'utf-8') as file:
        file.write(string1)

def sort(string1):
    string1 = string1.lower()
    list = string1.split('\r\n')
    list.sort()
    string2 = '\r\n'.join(list)
    return string2

def to2tab(string1):
    string1 = string1.strip()
    list1 = string1.split('\r\n')
    list2 = []
    for i in list1:
        # i = '<tr>' + i + '</tr>'
        isplit = i.split('\t')
        if len(isplit) < 2:
            isplit.append('')
        td1 = isplit[0]
        td2 = isplit[1]
        td1 = '<td>' + td1 + '</td>'
        td2 = '<td>' + td2 + '</td>'
        tr = '\t' + td1 + '\r\n\t' + td2
        tr = '<tr>\r\n' + tr + '\r\n</tr>'
        list2.append(tr)
    string2 = '\r\n'.join(list2)
    string2 = '<table>\r\n' + string2 + '\r\n</table>'
    return string2

def from2tab(string1, strMask):

    strMask1 = '<' + strMask + '>'
    strMask2 = '</' + strMask + '>'
    list=[]
    n1 = -1
    n2 = -1
    while(True):
        n1 = string1.find(strMask1, n1+1)
        n2 = string1.find(strMask2, n2+1)
        if(n1==-1 or n2==-1):
            break
        strFind = string1[(n1 + NCOLUMN):n2]
        strFind = strFind.strip()
        list.append(strFind)
    return list



def listNtab(string1, nColumn):
    list1 = string1.split('\r\n')
    list2 = []
    k = 0
    #10/4 => 3
    count = int(len(list1)/nColumn)
    temp = 1 if len(list1)%nColumn>0 else 0
    count += temp
    for i in range(nColumn):
        list2.append([])
        for j in range(count):
            if k<len(list1):
                list2[i].append(list1[k])
            else:
                list2[i].append('')
            k += 1
    # print(list2)
    # print(len(list2),len(list2[0]))
    icount = len(list2)
    jcount = len(list2[0])
    stringRow = ''
    string2 = ''
    for j in range(jcount):
        stringRow = ''
        listRow = []
        stringRowTr = ''
        whilecount = icount*2
        for i in range(icount):
            if i<icount-1:
                stringRow += list2[i][j] + '\t'
            else:
                stringRow += list2[i][j]

        listRow = stringRow.split('\t')
        for i in range(len(listRow),whilecount):
            listRow.append('')
        for i in listRow:
            stringRowTr += '\t<td>' + i + '</td>\r\n'
        stringRowTr =  '\t' + stringRowTr.strip()
        stringRowTr = '<tr>\r\n' + stringRowTr + '\r\n</tr>'
        string2 += stringRowTr + '\r\n'
    string2 = string2.strip()
    string2 = '<table>\r\n' + string2 + '\r\n</table>'

    return string2

string1 = readFile()

string2 = sort(string1)
string1 = string2

string2 = listNtab(string1, NCOLUMN)


def appDivList(string1):
    string2 = "<div style=\"display: none\">\r\n" \
                + string1\
                + '\r\n</div>'
    return string2

string2 += '\r\n' + appDivList(string1)
writeFile(string2)

