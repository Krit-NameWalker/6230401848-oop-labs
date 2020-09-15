with open('kku.txt', 'r', encoding='utf8') as namefile:
    oldfile = namefile.read()

with open('kku2.txt', 'w', encoding='utf8') as newfile:
    newfile.write(oldfile)
    newfile.write("\nMotto: วิทยา จริยา ปัญญา\nMotto in English: Knowledge, Virtues, Wisdom")

with open('kku2.txt', 'r', encoding='utf8') as pen:
    print(pen.read())
