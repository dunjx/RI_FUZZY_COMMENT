import re
from nltk.corpus import stopwords

review = input()
print("Your review: ", review)
review = review.lower()

premises = review.split(". ")

premiseList = list()

for premise in premises:
    premiseList.append(re.sub(r"[,.!?]", r"",premise).split(" "))

stop_words = set(stopwords.words('english'))
additional = {"one","like", "was","were","While","To","39","like","movie","film","The","A","An","This","this","see","She","Her","something","nobody","His","He","They","it","is","are","am","know","And","and","IMDb","spoilers","spoiler","-","?","[","]","br/","<",">","!",",", ".", "``", "I", "me", "i", "'", '"', "#", "(", ")", "quot", "&", ";", ":", "It", "it", "she",
                      "her", "he", "his", "they", "them"}
modifiers = {"so", "very", "not", "too", "much", "really", "quite", "rather", "almost", "especially", "certainly", "extremely", "highly", "relatively", "specifically", "fairly", "completely", "ultimately", "widely", "seriously", "mostly", "nearly", "essentially", "slightly", "somewhat", "significantly", "totally", "truly", "definitely", "deeply", "hardly", "strongly", "more", "such", "less"}
stop_words = stop_words.union(additional)
stop_words.union(modifiers)

for wordList in premiseList:
    for word in wordList:
        if word in stop_words:
            wordList.remove(word)