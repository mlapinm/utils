#strqu - string quantity
#количество строк в "html" файлах
import codecs
import os

import lib01

TYPE_FILE_HTML = "html"
WRITE_FILE_TXT = "count.txt"

file_list = os.listdir()
text1 = __file__ + '\r\n'
sum = 0
string2 = ''
for filename in file_list:
    string2 = ""
    if filename.find(TYPE_FILE_HTML)>0:
        count = 0
        with codecs.open(filename,'r','utf-8') as file:
            strings = file.readlines()
            count = len(strings)
            string2 = filename + "\t" + str(count)
        text1 += string2 + "\r\n"
        print(string2)
        sum += count

print("This written to file: " + WRITE_FILE_TXT)
print( sum )
text1 += str(sum)
lib01.writeFile(WRITE_FILE_TXT, text1)


