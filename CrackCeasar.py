import sys

f = open(sys.argv[1], "r")
contents = f.read().lower()

f.close()
# print contents
contents.lower()
fin = open(sys.argv[2], "r")
d = fin.readlines()
fin.close()

letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(letters)):
    translated = ''

    for symbol in contents:
        if symbol in letters:
            num = letters.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(letters)

            translated = translated + letters[num]
        else:
            translated = translated + symbol

    if translated.find('the') != -1:
        print('%s' % (key))
        print('%s' % (translated))

