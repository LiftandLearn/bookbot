def countWords(text):
    return len(text.split())


def countCharacters(text):
    makeLower = text.lower()
    counts = {}
    for char in makeLower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sortOn(item):
    return item["num"]


def sortedDict(dictionary):
    dictList = []
    for char, num in dictionary.items():
        dictList.append({"char": char, "num": num})
    dictList.sort(reverse=True, key=sortOn)
    return dictList


# def toSort(counts):
#    listDicts = []
#    for char, num in counts.items
#    sorted = countCharacters(dict).sort()
