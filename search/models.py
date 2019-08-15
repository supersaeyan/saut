import operator
import time


def _read_dataset():
    # dataset_path = os.path.join(os.getcwd(), os.path.abspath('word_search.tsv'))
    # print(os.getcwd())
    # print(dataset_path)

    dataset_path = '/home/arpit/projects/home/saut/search/word_search.tsv'

    with open(dataset_path, 'r') as f:
        dataset = f.readlines()
        dataset = [line.split() for line in dataset if len(line.split())]

    return dataset


dataset = _read_dataset()


def lookup(word):
    t0 = time.time()

    matches = []
    for elem, freq in dataset:
        match_idx = elem.find(word)
        if match_idx != -1:
            matches.append((elem, freq, match_idx))

    t1 = time.time()
    print('Matches in {}'.format(t1 - t0))

    matches = sorted(matches, key=operator.itemgetter(2))
    # Matches found in the beginning of words, ranked higher

    t2 = time.time()
    print('Sorted by index of substring in {}'.format(t2 - t1))

    matches = sorted(matches, key=operator.itemgetter(1), reverse=True)
    # Matches that are common, ranked higher

    t3 = time.time()
    print('Sorted by commonality of words in {}'.format(t3 - t2))

    matches = sorted(matches, key=lambda t: len(t[0]))
    # Matches that are shorter in length, ranked higher

    t4 = time.time()
    print('Sorted by length of the matches in {}'.format(t4 - t3))

    matches = [match[0] for match in matches[:25]]

    t5 = time.time()
    print('Total time {}'.format(t5 - t0))

    print(len(matches))

    return matches
