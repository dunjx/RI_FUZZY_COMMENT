import htmlClass
import test
import glob
import pandas as pd

# All files from current directory with extention html.
films = glob.glob("*.html")

allComments = []
averageCom = []
for film in films:
    htmlFilm = htmlClass.Film(film)
    allComments.extend(htmlFilm.comments)
    testFilm = test.FilmMiddle(film)
    averageCom.extend(testFilm.comments)

data = pd.DataFrame(allComments)
data.to_csv("comments.csv",index=False,header=False)

data = pd.DataFrame(averageCom)
data.to_csv("testComs.csv",index=False,header=False)


