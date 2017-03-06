import os
import sys

nl = '\n'
skip = {'cmds'}
asd=sys.argv[1]

def wordtra(path):

    for root, dir, files in os.walk(path):


                for file in files:

                    if file not in skip and file.endswith('.txt'):
                        fp = os.path.join(root, file)
                        if os.path.isfile(fp):
                            past_header, lines = False, []
                            f = open(fp, encoding="latin-1")
                            for line in f:
                                lines.append(line)

                            f.close()
                            stuff = nl.join(lines)

                            yield fp, stuff


def wordlist(path):
    dic = {}

    for file, text in wordtra(path):
        words = text.split()
        for item in words:


                if item not in dic:
                    dic[item]= [0, 0]

    return dic



def lrnsp(path):

    for root, dir, files in os.walk(path):
        if 'train' in root:
            if 'spam' in root:
                for file in files:
                    if file not in skip and file.endswith('.txt'):
                        fp = os.path.join(root, file)
                        if os.path.isfile(fp):
                            past_header, lines = False, []
                            f = open(fp, encoding="latin-1")
                            for line in f:
                                lines.append(line)

                            f.close()
                            stuff = nl.join(lines)

                            yield fp, stuff


def lrnha(path):

    for root, dir, files in os.walk(path):
        if 'train' in root:
            if 'ham' in root:
                for file in files:
                    if file not in skip and file.endswith('.txt'):
                        fp = os.path.join(root, file)
                        if os.path.isfile(fp):
                            past_header, lines = False, []
                            f = open(fp, encoding="latin-1")
                            for line in f:
                                lines.append(line)

                            f.close()
                            stuff = nl.join(lines)

                            yield fp, stuff




def bdf(path, dic):

    for file, text in lrnha(path):
        words=text.split()
        for item in words:


                val=dic[item]

                val[0]+=1
                dic[item]=val


    for file, text in lrnsp(path):
        words = text.split()
        for item in words:

                val = dic[item]
                val[1] += 1
                dic[item] = val


    return dic



voc=wordlist(asd)

classifier={}
voc=bdf(asd, voc)

f=open('nbmodel.txt', 'w')
f.write(str(voc))
f.close()