import pandas as pd
import re

df = pd.read_csv('comments.csv')
df = pd.DataFrame(df)
df.columns = ["comment", "grade"]

dfTest = pd.read_csv('testComs.csv')
dfTest = pd.DataFrame(dfTest)
dfTest.columns = ["comment", "grade"]

#elseFilms = df[3 < df["grade"] < 8]
badFilms = df[df["grade"] <= 3]
goodFilms = df[df["grade"] >= 8]
testFilms = dfTest[dfTest["grade"] < 8]
testFilms = testFilms[testFilms["grade"] > 3]
testFilms.to_csv("From4TO7.csv",index=False,header=False)

ri = re.compile(r"\'|]|\[|\s")
badKeywords = {}

for comment in badFilms["comment"]:
    comment = str(comment)
    comment = ri.sub(r"", comment).split(",")

    for com in comment:
        if com not in badKeywords:
            badKeywords[com] = 1
        else:
            badKeywords[com] = badKeywords.get(com) + 1

goodKeywords = {}

for comment in goodFilms["comment"]:
    comment = str(comment)
    comment = ri.sub(r"", comment).split(",")

    for com in comment:
        if com not in goodKeywords:
            goodKeywords[com] = 1
        else:
            goodKeywords[com] = goodKeywords.get(com) + 1

reviews = []
for review in testFilms["comment"]:
    reviews.append(review)
