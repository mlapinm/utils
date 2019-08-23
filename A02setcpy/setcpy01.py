#setcpy01.py
#если нет файла huishu01.txt, то он его создает
# netbean082.txt	04install
# netbean083.txt	04install
#из содержимого директория игнорируя
# setcpy01.py
# ignore.txt
# huishu01.txt
#  из ignore.txt
# имя файла директрия и куда записать в папку
# на уровень выше
# порождает следующий logout04.txt
# freonpc	..\04install\netbean082.txt
# freonpc	..\04install\netbean083.txt
# freonpc	..\04install\netbean084.txt
# 2019-08-23 14:56:10.663600
#
# freonpc	..\04install\netbean085.txt
# 2019-08-23 15:03:21.964269


import codecs
import os
from datetime import time, datetime
import socket
import shutil

import errno

INSTALL_DIR = "04install"
LOGOUT__TXT = "logout01.txt"
HUISHU = "huishu01.txt"

string1 = ""
string2 = ""

def readFile(name):
    string1 = ''
    with codecs.open(name, 'r', 'utf-8') as file:
        string1 = file.read()
    return string1

def writeFile(name, string1):
    with codecs.open(name, 'w', 'utf-8') as file:
        file.write(string1)

def makeHuis():
    string1 = ""
    file_list1 = os.listdir()
    strIgnore = readFile("ignore.txt")
    listIgnore1 = strIgnore.split("\r\n")
    listIgnore = []
    for i in listIgnore1:
        if i != "":
            listIgnore.append(i)
    file_list = []
    for i in file_list1:
        bis = False
        for j in listIgnore:
            if i == j:
                bis = True
                break
        if bis == False \
                and i[:3]!="log"\
                and i[0]!='.':
             file_list.append(i)
    for i in file_list:
            string1 += i + "\t" + INSTALL_DIR + "\r\n"
    writeFile(HUISHU, string1)
    # writeFile(HUISHU,strIgnore)

def lastLog():
    string1 = ""
    list = os.listdir()
    list2 = []
    for i in list:
        if i[:3] == "log":
            list2.append(i)
    list2.sort()
    if len(list2)<1:
        return ""
    else:
        string1 = list2[len(list2)-1]
    return string1

def nextLog():
    string1 = lastLog()
    if len(string1) == 0:
        return "logout01.txt"
    string2 = string1[6:8]
    i = int(string2) + 1
    string2 = "" + str(i)
    if len(string2) < 2:
        string2 = '0' + string2
    string2 = "logout" + string2 + ".txt"
    return string2

def readHuis():
    string1 = readFile(HUISHU)
    list1 = string1.split("\r\n")
    list = []
    for i in list1:
        if i != "":
            list.append(i)
    return list

def appendLog(logName):
    if lastLog() == "":
        list = []
        for i in copy.arrayTo:
            list.append(socket.gethostname() + '\t' + i)
        writeFile(logName, '\r\n'.join(list))
        return
    textLastLog = readFile(lastLog())
    listLast1 = textLastLog.split("\r\n")
    listLast = []
    for i in listLast1:
        if i != "":
            listLast.append(i)
    listAdd = []
    listHost=[]
    for i in copy.arrayTo:
        listHost.append(socket.gethostname()+'\t'+i)
    for i in listHost:
        boolIs = False
        for j in listLast:
            if i == j:
                boolIs = True
                break
        if boolIs == False:
            listAdd.append(i)
    if len(listAdd)>0:
        textAdd = '\r\n'.join(listAdd)
        text = textLastLog + '\r\n' + '\r\n' \
                + textAdd + '\r\n' \
                + str(datetime.now())
        writeFile(logName, text)

class ClCopy:
    arrayName = []
    arrayPath = []
    arrayTo = []

    @classmethod
    def setArrays(self, list):
        if len(list) == 0:
            return
        for i in list:
            lrow = i.split("\t")
            while len(lrow)<2:
                lrow.append("")
            self.arrayName.append(lrow[0])
            self.arrayPath.append(lrow[1])
            k = 0
        for i in self.arrayName:
            self.arrayTo.append("..\\"
                                + self.arrayPath[k] + "\\"
                                + self.arrayName[k])
            k += 1

    @classmethod
    def copyDirFile(cls, src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                print('Directory not copied. Error: %s' % e)
    @classmethod
    def copy(self):
        for i in range(len(self.arrayName)):
            self.copyDirFile(self.arrayName[i], self.arrayTo[i])

file_list = os.listdir()
if file_list.count(HUISHU) == 0:
    makeHuis()
# print(file_list.count(HUISHU))
logName = nextLog()
list = readHuis()
copy = ClCopy
copy.setArrays(list)
copy.copy()
string1 = '\r\n'.join(copy.arrayTo)

appendLog(logName)

print(__file__)



