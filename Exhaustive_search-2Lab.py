#!/usr/bin/python
import sys


def main():
    pattern = []
    sequenceAll = []
    sequence = []
    result = []
    listMotive = []
    size = int(sys.argv[1])
    t = 0
    file = sys.argv[2]
    with open(file) as _file:
        for i in _file:
            sequence.clear()
            for j in i:
                if len(pattern) < size:
                    pattern.append(j)
                else:
                    patternString = ''.join(pattern)
                    sequence.append(patternString)
                    pattern.pop(0)
                    pattern.append(j)
            pattern.clear()
            sequenceAll.append(sequence.copy())
            t += 1

    for q in range(4 ** size):
        distTmp = 0
        for i in range(len(sequenceAll)):
            tmp = findMotiveInString(replaceWord(q , size), sequenceAll, i, size)
            distTmp += tmp[1]
            tmp.pop(1)
            listMotive.append(tmp)
        listMotive.append(distTmp)
        result.append(listMotive.copy())
        listMotive.clear()

    print (findMin(result, t, size))

def findMotiveInString(first, list, t, l):
    listTemp = []
    listTemp.append(first)
    distMin = l
    tempMotive = []
    for j in range(len(list[t])):
        listTemp.append(list[t][j])
        distTemp = checkTotalDistance(listTemp, l)
        if distTemp < distMin:
            tempMotive.clear()
            distMin = distTemp
            tempMotive.append(listTemp[1])
            tempMotive.append(distMin)
        listTemp.pop(1)
    if not tempMotive:
        tempMotive.append(list[t][0])
        tempMotive.append(distMin)
    return tempMotive

def findMin(list, t, l):
    minTmp = l * t
    out = 0
    for i in range(len(list)):
        if list[i][t] < minTmp:
            minTmp = list[i][t]
            out = i
    return replaceWord(out, l)

def checkTotalDistance(list, l):
    countTmp = 0
    for i in range(l):
        if list[0][i] != list[1][i]:
            countTmp += 1
    return countTmp

# Принимаем число, на выход набор буквы
def replaceWord(number, l):
    result = ''
    out = ''
    while number > 0:
        y = str(number % 4)
        result = y + result
        number = int(number / 4)
    if len(result) < l:
        for q in range(l - len(result)):
            result = '0' + result
    for i in range(l):
        if result[i] == '0':
           out += 'A'
        elif result[i] == '1':
           out += 'C'
        elif result[i] == '2':
           out += 'G'
        elif result[i] == '3':
           out += 'T'
    return out


if __name__ == "__main__":
    main()
