#!/usr/bin/env python3
# PCL 2, FS 17

# Uebung 04 Aufgabe 02

# Randomisierung
# von Iuliia Nigmatulina


import urllib.request
import bz2
from lxml import etree
import random


def gettitles(infile, testfile, trainfile, k):
    """
    The function gets and saves k number of random elements in testfile
    and all other elements in trainfile.
    Infile - das Korpus,
    testfile - die Ausgabedatei für k zufällig ausgesuchte Artikeltitel,
    und trainfile - die Ausgabedatei für alle anderen Titel
    """
    all_wiki = urllib.request.urlopen(infile)
    with open(trainfile, "a") as train:
        with bz2.open(all_wiki, "r") as corpus:
            reservoir = []
            for t, (event, element) in enumerate(
                    etree.iterparse(
                        corpus,
                        tag='{http://www.mediawiki.org/xml/export-0.10/}title'
                    )):
                title = element.text
                if t < k:
                    reservoir.append(title)
                else:
                    m = random.randint(0, t)
                    if m < k:
                        reservoir[m] = title
                    else:
                        title_add = "{}\n".format(title)
                        train.write(title_add)
                    # if t > 50:
                    #     break
                with open(testfile, "w") as test:
                    test.write("\n".join(reservoir))


if __name__ == "__main__":
    infile = "https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2"
    testfile = "testfile.txt"
    trainfile = "trainfile.txt"
    k = 5
    gettitles(infile, testfile, trainfile, k)
