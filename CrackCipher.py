import sys
import collections
import string
import operator

f = open(sys.argv[1], "r")
contents = f.read().lower()

f.close()
# print contents
contents.lower()
fin = open(sys.argv[2], "r")
d = fin.read().lower()
fin.close()

Alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
]

hits = [
    (Alphabet[i], contents.count(Alphabet[i]))
    for i in range(len(Alphabet))
    if contents.count(Alphabet[i])
]

# for letter, frequency in hits:
#   print(letter.lower(), frequency)


print("\n")
dic = [
    (Alphabet[i], d.count(Alphabet[i]))
    for i in range(len(Alphabet))
    if d.count(Alphabet[i])
]

# for letter, frequence in dic:
#   print(letter.lower(), frequence)

print
hits, "\n", dic

hits.sort(key=operator.itemgetter(1))
dic.sort(key=operator.itemgetter(1))

hitter = [i[0] for i in hits]
dics = [i[0] for i in dic]

# print hitter
# print("\n")
# print dics
fname = sys.argv[1]
with open(fname) as f:
    while True:
        c = f.read(1).lower()

        if not c:
            break
        if c not in hitter:
            sys.stdout.write(c)
        else:
            new = hitter.index(c)
            sys.stdout.write(dics[new])

f.close()


