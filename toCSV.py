import htmlClass
import glob
import pandas as pd

# All files from current directory with extention html.
films = glob.glob("*.html")

allComments = []
for film in films:
    htmlFilm = htmlClass.Film(film)
    allComments.extend(htmlFilm.comments)

data = pd.DataFrame(allComments)
data.to_csv("comments.csv",index=False,header=False)