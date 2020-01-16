import sys
import re
class FilmMiddle:

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

        com_map = zip(comments, grades)
        self.comments = list(com_map)


#cCOM = FilmMiddle("Tell_It_to_the_Bees(2018)_User_ReviewsIMDb.html")
#print(cCOM.comments)
