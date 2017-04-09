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
    # read from url-link
    all_wiki = urllib.request.urlopen(infile)
    with open(trainfile, "a") as train:
        with bz2.open(all_wiki, "r") as corpus:
            # creat a reservoir to which random elements are added
            reservoir = []
            # iterate through the enumerated .xml elements from the corpus
            # all titles are extracted
            for t, (event, element) in enumerate(
                    etree.iterparse(
                        corpus,
                        tag='{http://www.mediawiki.org/xml/export-0.10/}title'
                    )):
                title = element.text
                # algorithm R
                if t < k:
                    reservoir.append(title)
                else:
                    m = random.randint(0, t)
                    if m < k:
                        reservoir[m] = title
                    else:
                        title_add = "{}\n".format(title)
                        train.write(title_add)
                    # if t > 50:        # an option to limit
                    #     break         # the number of iterations
                # save the current result at the end of iteration;
                # enable to interrupt procesing of the code
                # to get current result
                with open(testfile, "w") as test:
                    test.write("\n".join(reservoir))


if __name__ == "__main__":
    infile = "https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2"
    testfile = "testfile.txt"
    trainfile = "trainfile.txt"
    k = 5
    gettitles(infile, testfile, trainfile, k)
