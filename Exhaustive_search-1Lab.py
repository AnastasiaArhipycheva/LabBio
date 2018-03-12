#!/usr/bin/python
import sys


def main():
    pattern = []
    sequenceAll = []
    sequence = []
    result = []
    listMotive = []
    size = int(sys.argv[1])
    t = int(sys.argv[2])
    file = sys.argv[3]
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

    for i in range(len(sequenceAll[0])):
        listMotive.append(sequenceAll[0][i])
        for q in range(1, t):
            listMotive.append(findMotiveInString(sequenceAll[0][i], sequenceAll, q, size))
        listMotive.append(score(listMotive, t, size))
        result.append(listMotive.copy())
        listMotive.clear()
    finalResult = []
    maxScore = 0
    for i in range(len(result)):
        if result[i][len(result[i]) - 1] > maxScore:
            maxScore = result[i][len(result[i]) - 1]
            finalResult = result[i]
    finalResult.pop(len(result[i]) - 1)
    print(finalResult)

def findMotiveInString(first, list, t, l):
    listTemp = []
    listTemp.append(first)
    scoreMax = 0
    tempMotive = []
    for j in range(len(list[0])):
        listTemp.append(list[t-1][j])
        scoreTemp = score(listTemp, 2, l)
        if scoreTemp > scoreMax:
            scoreMax = scoreTemp
            tempMotive = listTemp[1]
        listTemp.pop(1)
    return tempMotive


def score(list, t, l):
    score = 0
    tmp = []
    for i in range(l):
        for j in range(t):
            tmp.append(list[j][i])
        score += max(check(tmp, t))
        tmp.clear()
    return score

def check(list, t):
    listOut = [0,0,0,0]
    for i in range(t):
        if list[i] == 'A':
           listOut[0] += 1
        elif list[i] == 'C':
           listOut[1] += 1
        elif list[i] == 'G':
           listOut[2] += 1
        elif list[i] == 'T':
           listOut[3] += 1
        else:
            raise Exception('Wrong symbol')
    return listOut


if __name__ == "__main__":
    main()
