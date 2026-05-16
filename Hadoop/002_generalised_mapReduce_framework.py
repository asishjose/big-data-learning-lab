from collections import defaultdict
from functools import reduce as functools_reduce

def mapreduce(data, mapper, reducer, combiner=None):
    """
    Args:
        data     : iterable of input records
        mapper   : fn(record)  - list of (key, value) pairs
        reducer  : fn(key, values) - (key, result)
        combiner : optional local reducer to run before shuffle
    """

    pairs = []
    for record in data:
        pairs.extend(mapper(record))

    if combiner:
        grouped = defaultdict(list)
        for k, v in pairs:
            grouped[k].append(v)
        pairs = []
        for k, vs in grouped.items():
            _, combined = combiner(k, vs)
            pairs.append((k, combined))

    grouped = defaultdict(list)
    for k, v in pairs:
        grouped[k].append(v)

    return dict(reducer(k, vs) for k, vs in grouped.items())

# Using framework  - word count:

documents = [
    "the cat sat on the mat",
    "the cat sat on the hat",
    "the cat ate the rat",
]

def word_mapper(line):
    return [(word, 1) for word in line.lower().split()]

def word_reducer(word, counts):
    return (word, sum(counts))

result = mapreduce(documents, word_mapper, word_reducer, combiner=word_reducer)
#print(result)


# Using framework - average score per student:

records = [
    ("Alice", 85), ("Bob", 90), ("Alice", 92),
    ("Bob", 78),   ("Alice", 88), ("Bob", 95),
]

def score_mapper(record):
    name, score = record
    return [(name, score)]

def avg_reducer(name, scores):
    return (name, sum(scores) / len(scores))

result = mapreduce(records, score_mapper, avg_reducer)
print(result)