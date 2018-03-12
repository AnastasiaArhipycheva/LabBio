#!/usr/bin/python
import sys
import operator

def main():
    pattern = []
    dict = {}
    file = sys.argv[1]
    size = int(sys.argv[2])
    with open(file) as _file:
        for i in _file:
            for j in i:
                if len(pattern) < size:
                    pattern.append(j)
                else:
                    patternString = ''.join(pattern)
                    if patternString in dict:
                        dict[patternString] += 1
                        pattern.pop(0)
                        pattern.append(j)
                    else:
                        dict[patternString] = 1
                        pattern.pop(0)
                        pattern.append(j)
        patternString = ''.join(pattern)
        if patternString in dict:
            dict[patternString] += 1
        else:
            dict[patternString] = 1

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    maxLenPatern = sorted_dict[len(sorted_dict) - 1][1]
    i = 1
    while sorted_dict[len(sorted_dict)-i][1] == maxLenPatern:
        print(sorted_dict[len(sorted_dict) - i][0])
        i += 1


if __name__ == "__main__":
    main()
