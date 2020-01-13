import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Film:

    comments = []
    def __init__(self, path):

        # Regex za <div> jednog komentara.
        ri = re.compile(
            r'<div\s+class="lister-item mode-detail\s+imdb-user-review.+?>.*?</div>\s*(?=<div\s+class="lister-item)',
            re.MULTILINE | re.S)

        # Ovde moze bilo koij html fajl komentara na film da se stavi.
        try:
            f = open(path, "r")
        except IOError:
            sys.error("Fajl ne postoji.")

        # U buf se ucitava cela html stranica, a match je kolekcija svih komentara.
        buf = f.read()
        match = ri.findall(buf)
        length = len(match)

        if match is None:
            sys.exit()

        # Regexi za ocene i za sadrzaj komentara.
        ri_grade = re.compile(r'(?<=<span>)\d{1,2}(?=</span><span class="point-scale">/10</span>)', re.MULTILINE | re.S)
        ri_comment = re.compile(r'(?<=<div class="text show-more__control">).+?(?=</div>)', re.MULTILINE | re.S)

        grades = []
        comments = []

        # Dodaju se u liste ocene i komentari, i iz komentara se izbacuje <br> i ako nema posle interpunkcijskih znakova
        # razmak, stavlja se.
        for i in range(length):
            grade = ri_grade.search(match[i])
            comment = ri_comment.search(match[i])

            if grade is not None and comment is not None:
                grades.append(grade.group())
                comments.append(re.sub(r'<br>', r' ', re.sub(r'([\.,;:])(?!\s)', r'\1 ', comment.group())))

        length = len(grades)

        # Dodaju se stop reci, i na default skup se dodaju nove reci.
        stop_words = set(stopwords.words('english'))
        additional = {"like","one","was","were","While","To","39","like","movie","film","The","A","An","This","this","see","She","Her","something","nobody","His","He","They","it","is","are","am","know","And","and","IMDb","spoilers","spoiler","-","?","[","]","br/","<",">","!",",", ".", "``", "I", "me", "i", "'", '"', "#", "(", ")", "quot", "&", ";", ":", "It", "it", "she",
                      "her", "he", "his", "they", "them"}
        modifiers = {"so", "very", "not", "too", "much", "really", "quite", "rather", "almost", "especially", "certainly", "extremely", "highly", "relatively", "specifically", "fairly", "completely", "ultimately", "widely", "seriously", "mostly", "nearly", "essentially", "slightly", "somewhat", "significantly", "totally", "truly", "definitely", "deeply", "hardly", "strongly", "more", "such", "less"}
        stop_words = stop_words.union(additional)
        stop_words = stop_words.union(modifiers)

        # Izbacuju se stop reci iz komentara i te liste se ubacuju u listu important.
        important = []
        for i in range(length):
            tokens = word_tokenize(comments[i])
            important.append([j.lower() for j in tokens if not j in stop_words])

        # Pravi se mapa bitnih reci i ocena filmova.
        com_map = zip(important, grades)
        self.comments = list(com_map)


#film1 = Film('Zovi_me_svojim_imenom(2017)User_ReviewsIMDb.html')

#print(film1.comments)
