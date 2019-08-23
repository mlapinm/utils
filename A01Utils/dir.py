#в dir.txt содержимое директория
import codecs
import os

import lib01

DIR_TXT = 'dir.txt'

listFilesDirs = os.listdir()
teList = '\r\n'.join(listFilesDirs)
lib01.writeFile(DIR_TXT, teList)
