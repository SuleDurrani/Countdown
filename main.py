import time


def importFile():
    with open('words.txt') as f:
        lines = f.readlines()
        newList = [s.replace("\n", "") for s in lines]
        returnList = []
        count = 0
        for i in newList:
            if '-' not in i:
                # print(newList[count])
                returnList.append(newList[count])
            count += 1
        return returnList


def compare(words, letters):
    inPromptList = []
    for i in range(len(words)):
        allValidLetters = True
        x = letters
        for j in range(len(words[i])):

            if words[i][j] in x:
                tempPrompt = ""
                for k in range(len(x)):
                    if x[k] == words[i][j]:
                        tempPrompt = x[:k] + x[k + 1:]
                x = tempPrompt
                allValidLetters = True

            else:
                allValidLetters = False
                break

        if allValidLetters:
            inPromptList.append(words[i])

    return inPromptList


def generateLetters():
    while True:
        val = input("Enter 9 letters, or 8 for the 8/10 version: ")
        if len(val) == 8 or len(val) == 9:
            break

    return val


def reduceWordCount(words):
    temp = []
    for i in range(len(words)):
        if 4 < len(words[i]) < 10:
            temp.append(words[i])
    return temp


def sortWords(words):
    li = sorted(words, key=len, reverse=True)
    return li[:5]


def countWordsAtLength(words):
    length9, length8, length7 = 0, 0, 0
    for i in words:
        if len(i) == 9:
            length9 += 1
        elif len(i) == 8:
            length8 += 1
        elif len(i) == 7:
            length7 += 1

    print(f"\nIn your input string there are {length9} nines, {length8} eights, and {length7} seven letter words.\n")


def main():
    letters = generateLetters()
    t0 = time.time()
    words = importFile()
    words = reduceWordCount(words)

    finalWordList = compare(words, letters)

    countWordsAtLength(finalWordList)

    fiveBestWord = sortWords(finalWordList)

    print(f"5 best words are: {fiveBestWord}")
    t1 = time.time()
    print(f"\nTotal execution time is: {round(t1 - t0, 3)}")


if __name__ == '__main__':
    main()
