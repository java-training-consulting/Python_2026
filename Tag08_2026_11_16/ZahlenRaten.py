from random import random

#versuche zählen
# hinweis größer, kleiner

# computer schumelt  von bis merken
# jedes 2 spiel ist beim 3 mal gewonnen


def zahlenRaten():
    # 1..10
    geheimzahl = int((random() * 10) + 1)
    # print(geheimzahl)
    rateZahl = int(input("welche Zahl ist es:"))

    while geheimzahl != rateZahl:
        print("falsch")
        rateZahl = int(input("welche Zahl ist es:"))

    print("richtig")

if __name__ == '__main__':
    zahlenRaten()