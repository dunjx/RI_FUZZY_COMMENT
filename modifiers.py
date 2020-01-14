import pandas as pd
import numpy as np


littleChange = {"nearly", "relatively", "mostly"}
averageChange = {"so", "quite", "rather", "certainly", "fairly", "widely", "essentially", "such", "more", "less", "somewhat"}
bigChange = {"almost", "very", "too", "much", "really", "especially", "extremely", "highly", "specifically",
             "comletely", "ultimately", "seriously", "slightly", "somewhat", "significantly", "totally",
             "truly", "definitely", "deeply", "strongly", "hardly", "slightly"}

impactMap = {}

for l in littleChange:
    impactMap[l] = 2

for a in averageChange:
    impactMap[a] = 3

for b in bigChange:
    impactMap[b] = 4