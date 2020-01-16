# RI_FUZZY_COMMENT
## Fuzzy classificator for grading film reviews

FUZZY_COMMENT takes an input film review and estimates how that film would be graded from 1 to 10 based on given review. It does this by analizing IMDb comments and grades on romantic films. Comment base contains user reviews of 18 films. This is a classificator that classifies new comment in one of 10 categories. This is done by using fuzzy logic and calculating membership function (returns a value in [0,1] range) and then scaling that to 1-10 grading.
