import codecs


def writeFile(name, string1):
    with codecs.open(name, 'w', 'utf-8') as file:
        file.write(string1)

