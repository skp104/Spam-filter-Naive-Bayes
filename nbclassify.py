import os
import sys
import math


nl = '\n'
skip = {'cmds'}
asd2=sys.argv[1]

def wordtra(path):

    for root, dir, files in os.walk(path):
        if 'train' in root:

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



def wordte(path):

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
def wordlistte(path, dic, h ,s,tot,alpha):

    w=0

    f = open('nboutput.txt', 'w')
    for file, text in wordte(path):
        w+=1
        probsp=math.log(s/tot)
        probha=h/tot

        words = text.split()


        for item in words:
            values=dic.get(item, [0,0])

            numh=values[0]+alpha
            denh=htot*(alpha+1)
            probha+=math.log(float(numh)/denh)

            nums = values[1] + alpha
            dens = stot * (alpha+1)
            probsp += math.log(float(nums) / dens)

        if probha>probsp:
            cla = 'HAM'

        if probha<probsp:
            cla = 'SPAM'

        f.write(str(cla+' '+ file+'\n'))

    f.close()

f=open('nbmodel.txt', 'r')
voc=eval(f.read())
f.close()


tot=0
htot=0
stot=0
for key in voc:
    val=voc[key]
    tot+=(val[0]+val[1])
    htot+=val[0]
    stot+=val[1]
pspa=stot/tot
pham=htot/tot

classifier={}
alpha=1
for key in voc:
    item=key
    val=voc[key]
    wno=val[0]+val[1]

    pw=wno/tot


    classifier[key]=[val[0], val[1]]





wordlistte(asd2,classifier, htot, stot, tot,alpha )