#!/usr/bin/env python3
# PCL 2, FS 17

# Uebung 04 Aufgabe 01

# Deduplizierung mit Zählen
# von Iuliia Nigmatulina


import glob
from lxml import etree


def getfreqwords(indir, outfile):
    """
    the function gets 20 the most frequent words with the length 6 or
    more words from the collection of .xml files
    """
    all_sentences_count = {}
    hash_sentences = {}
    # to read from the collection of .xml files of one pattern
    for filename in glob.glob(indir, recursive=True):
        # open .xml document to get lemmas
        tree = etree.parse(filename)
        root = tree.getroot()
        # iterate through the sentences to get all the lemmas of each sentence
        for s in root.iter('s'):
            sentence = " ".join(str(w.get("lemma")) for w in s.findall('w'))
            if len(sentence.split(" ")) > 5:
                sentence_hash = hash(sentence)
                hash_sentences[sentence_hash] = sentence
                if sentence_hash in all_sentences_count:
                    all_sentences_count[sentence_hash] += 1
                else:
                    all_sentences_count[sentence_hash] = 1
        # sort sentences by frequency and filter top 20
        frequent_sentences = [fs for fs in sorted(all_sentences_count.items(),
                                                  key=lambda x: x[1],
                                                  reverse=True)][:20]

        with open(outfile, "w") as outf:
            for fs in frequent_sentences:
                freq_sentences_for_print = "{}: {}\n".format(fs[1],
                                                             hash_sentences
                                                             [fs[0]])
                outf.write(freq_sentences_for_print)


if __name__ == "__main__":
    indir = "/Users/inigma/Documents/UZH_Master/Computational_linguistics/PCL/PCL_2/Uebungen/Uebung04/SAC/SAC-Jahrbuch_**_mul.xml"
    outfile = "20_frequent_sentences.txt"
    getfreqwords(indir, outfile)
