import re
from nltk.corpus import stopwords


class rev:
    review = ""
    finalList = []

    def __init__(self, rein):
        self.review = str(rein).lower()

    def getfinalList(self):
        finalList = []
        premiseList = []
        premises = self.review.split(". ")

        for premise in premises:
            premiseList.append(re.sub(r"[,.!?]", r"", premise).split(" "))

        stop_words = set(stopwords.words('english'))
        additional = {"like","one","was","were","While","To","39","like","movie","film","The","A","An","This","this","see","She","Her","something","nobody","His","He","They","it","is","are","am","know","And","and","IMDb","spoilers","spoiler","-","?","[","]","br/","<",">","!",",", ".", "``", "I", "me", "i", "'", '"', "#", "(", ")", "quot", "&", ";", ":", "It", "it", "she",
                              "her", "he", "his", "they", "them"}
        modifiers = {"so", "very", "not", "too", "much", "really", "quite", "rather", "almost", "especially", "certainly", "extremely", "highly", "relatively", "specifically", "fairly", "completely", "ultimately", "widely", "seriously", "mostly", "nearly", "essentially", "slightly", "somewhat", "significantly", "totally", "truly", "definitely", "deeply", "hardly", "strongly", "more", "such", "less"}
        stop_words = stop_words.union(additional)
        stop_words = stop_words.union(modifiers)

        workingList = []

        for wordList in premiseList:
            for word in wordList:
                if word not in stop_words:
                    workingList.append(word)
            finalList.append(workingList)
            return finalList



#ROV = rev(input())
#print(ROV.review)
#print(ROV.finalList)