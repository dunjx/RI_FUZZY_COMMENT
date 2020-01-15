from enum import Enum, unique
import inputParse
import classes
import modifiers
import math
import re


@unique
class Logic(Enum):
    OR = 0
    AND = 1


class MFInput:

    def __init__(self, name, x, y, x0):

        self.name = name
        # list of tuples
        self.points = [(x[i], y[i]) for i in range(len(x))]
        self.mi = self.getMi(x0)

    def getY(self, x1, y1, x2, y2, x0):

        if y1 == y2:
            return y1
        if y1 < y2:
            return (x0 - x1) / (x2 - x1)
        return (x2 - x0) / (x2 - x1)

    def getMi(self, x0):

        if x0 < self.points[0][0]:
            return self.points[0][1]

        if x0 > self.points[-1][0]:
            return self.points[-1][1]

        for i in range(1, len(self.points)):
            x1 = self.points[i - 1][0]
            x2 = self.points[i][0]

            if x0 >= x1 and x0 < x2:
                y1 = self.points[i - 1][1]
                y2 = self.points[i][1]
                return self.getY(x1, y1, x2, y2, x0)

        return -1


class Rule:
    def __init__(self, mfi1, mfi2, mfo, logic):
        self.mfInput1 = mfi1
        self.mfInput2 = mfi2
        self.mfOutput = mfo
        if logic == Logic.OR:
            self.mfOutput.mi = max(self.mfOutput.mi, max(self.mfInput1.mi, self.mfInput2.mi))
        else:
            self.mfOutput.mi = max(self.mfOutput.mi, min(self.mfInput1.mi, self.mfInput2.mi))

class MFOutput:
    def __init__(self, name, x, y):
        self.name = name
        sumX = 0
        nb1 = 0
        self.points = []
        for i in range(len(x)):
            self.points.append((x[i], y[i]))
            if y[i] == 1:
                sumX += x[i]
                nb1 += 1
        self.mi = 0
        self.value = sumX / nb1


badwordFunc = MFInput("FuncOfBad", [0, 60], [1, 0], 9)
goodwordFunc = MFInput("FuncOfGood", [0, 110], [0, 1], 4)


ratings = []
positiveStr = {"so", "very",  "too", "much", "really", "quite", "rather", "especially", "certainly",
                 "extremely", "highly", "relatively", "specifically", "fairly", "completely", "ultimately", "widely",
                 "seriously", "essentially", "significantly", "totally",
                 "truly", "definitely", "deeply",  "strongly", "more", "such"}
negativeStr = {"hardly", "less", "nearly", "almost", "mostly", "slightly", "somewhat"}

sentences = list()
for sentence in inputParse.review.split(". "):
    sentences.append(re.sub(r"[.,!?]", r"", sentence).split(" "))

#print("Recenice cele: ", sentences)

index1 = 0
wordCount = 0
miTotal = 0
notHappened = False

for wordList in inputParse.finalList:
    l2 = sentences[index1]
    index1 += 1
    for word in wordList:
        index2 = l2.index(word)

        if word in classes.goodKeywords and word in classes.badKeywords:

            if classes.goodKeywords[word] >= classes.badKeywords[word]:
                wordCount += 1
                index3 = index2
                mi = goodwordFunc.getMi(classes.goodKeywords[word])
                #print("Dobar Mi: ", mi)
                notHappened = False

                while index3 > 0:
                    if l2[index3 - 1] in negativeStr:
                        val = modifiers.impactMap.get(l2[index3 - 1])
                        mi = math.pow(mi, val)
                        index3 -= 1
                    elif l2[index3 - 1] in positiveStr:
                        val = modifiers.impactMap.get(l2[index3 - 1])
                        mi = math.pow(mi, 1/val)
                        index3 -= 1
                    elif l2[index3 - 1] == "not":
                        mi = 1 - mi
                        index3 -= 1
                        notHappened = not notHappened
                    else:
                        break
                if notHappened:
                    miTotal += (-1)*mi
                    notHappened = False
                else:
                    miTotal += mi
            else:
                wordCount += 1
                index3 = index2
                mi = badwordFunc.getMi(classes.badKeywords[word])
                #print("Los Mi: ", mi)
                notHappened = False

                while index3 > 0:
                    if l2[index3 - 1] in negativeStr:
                        val = modifiers.impactMap.get(l2[index3 - 1])
                        mi = math.pow(mi, 1/val)
                        index3 -= 1
                    elif l2[index3 - 1] in positiveStr:
                        val = modifiers.impactMap.get(l2[index3 - 1])
                        mi = math.pow(mi, val)
                        index3 -= 1
                    elif l2[index3 - 1] == "not":
                        mi = 1 - mi
                        index3 -= 1
                        notHappened = not notHappened
                    else:
                        break
                if notHappened:
                    miTotal += (-1)*mi
                    notHappened = False
                else:
                    miTotal -= 1 - mi

        elif word in classes.goodKeywords:
            wordCount += 1
            index3 = index2
            mi = goodwordFunc.getMi(classes.goodKeywords[word])
            #print("Dobar Mi: ", mi)
            notHappened = False

            while index3 > 0:
                if l2[index3 - 1] in negativeStr:
                    val = modifiers.impactMap.get(l2[index3 - 1])
                    mi = math.pow(mi, val)
                    index3 -= 1
                elif l2[index3 - 1] in positiveStr:
                    val = modifiers.impactMap.get(l2[index3 - 1])
                    mi = math.pow(mi, 1 / val)
                    index3 -= 1
                elif l2[index3 - 1] == "not":
                    mi = 1 - mi
                    index3 -= 1
                    notHappened = not notHappened
                else:
                    break
            if notHappened:
                miTotal += (-1)*mi
                notHappened = False
            else:
                miTotal += mi

        elif word in classes.badKeywords:
            wordCount += 1
            index3 = index2
            mi = badwordFunc.getMi(classes.badKeywords[word])
            #print("Los Mi: ", mi)
            notHappened = False

            while index3 > 0:
                if l2[index3 - 1] in negativeStr:
                    val = modifiers.impactMap.get(l2[index3 - 1])
                    mi = math.pow(mi, 1 / val)
                    index3 -= 1
                elif l2[index3 - 1] in positiveStr:
                    val = modifiers.impactMap.get(l2[index3 - 1])
                    mi = math.pow(mi, val)
                    index3 -= 1
                elif l2[index3 - 1] == "not":
                    mi = 1 - mi
                    index3 -= 1
                    notHappened = True
                else:
                    break
            if notHappened:
                miTotal += (-1)*mi
                notHappened = False
            else:
                miTotal -= 1 - mi

if wordCount == 0:
    wordCount = 1
miTotal = miTotal/wordCount
grade = math.ceil(5 + 5*miTotal)
if grade == 0:
    grade = 1
#print(inputParse.finalList)
#print(miTotal)
print(grade)
