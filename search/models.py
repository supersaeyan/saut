import operator
import time

from suffixtree import SuffixQueryTree


def _read_dataset():
    with open('/opt/word_search.tsv', 'r') as f:
        words = {line.split()[0]: line.split()[1] for line in f.readlines() if len(line.split())}

    return words


def create_qtree(dataset):
    qtree = SuffixQueryTree(True, list(dataset.keys()))
    qtree.cacheNodes()

    return qtree


dataset = _read_dataset()
qtree = create_qtree(dataset)


def match(word):
    matches = []
    for elem, freq in dataset.items():
        match_idx = elem.find(word)
        if match_idx != -1:
            matches.append((elem, freq, match_idx))

    return matches


def cmatch(word):
    results = qtree.findString(word)
    try:
        freq = dataset[word]
    except KeyError:
        return []

    matches = []
    for match in results:
        match_idx = match.find(word)
        if match_idx != -1:
            matches.append((match, freq, match_idx))

    return matches


def clookup(word):
    t0 = time.time()
    matches = cmatch(word)
    t1 = time.time()
    print('Matches in {}'.format(t1 - t0))

    matches.sort(key=operator.itemgetter(2))
    # Matches found in the beginning of words, ranked higher

    t2 = time.time()
    print('Sorted by index of substring in {}'.format(t2 - t1))

    matches.sort(key=operator.itemgetter(1), reverse=True)
    # Matches that are common, ranked higher

    t3 = time.time()
    print('Sorted by commonality of words in {}'.format(t3 - t2))

    matches.sort(key=lambda t: len(t[0]))
    # Matches that are shorter in length, ranked higher

    t4 = time.time()
    print('Sorted by length of the matches in {}'.format(t4 - t3))

    matches = [match[0] for match in matches[:25]]

    t5 = time.time()
    print('Total time {}'.format(t5 - t0))

    return matches


def lookup(word):
    t0 = time.time()
    matches = match(word)
    t1 = time.time()
    print('Matches in {}'.format(t1 - t0))

    matches.sort(key=operator.itemgetter(2))
    # Matches found in the beginning of words, ranked higher

    t2 = time.time()
    print('Sorted by index of substring in {}'.format(t2 - t1))

    matches.sort(key=operator.itemgetter(1), reverse=True)
    # Matches that are common, ranked higher

    t3 = time.time()
    print('Sorted by commonality of words in {}'.format(t3 - t2))

    matches.sort(key=lambda t: len(t[0]))
    # Matches that are shorter in length, ranked higher

    t4 = time.time()
    print('Sorted by length of the matches in {}'.format(t4 - t3))

    matches = [match[0] for match in matches[:25]]

    t5 = time.time()
    print('Total time {}'.format(t5 - t0))

    return matches
