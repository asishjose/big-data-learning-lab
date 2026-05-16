from collections import defaultdict

def map_phase(document):
    result = []
    for word in document.lower().split():
        result.append((word, 1))
    return result

def shuffle(mapped_pairs):
    grouped = defaultdict(list)
    for key, value in mapped_pairs:
        grouped[key].append(value)
    return grouped

def reduce_phase(grouped):
    result = {}
    for key, values in grouped.items():
        result[key] = sum(values)
    return result


# Running Map Reduce

documents = [
    "the cat sat on the mat",
    "the cat sat on the hat",
    "the cat ate the rat",
]

mapped = []
for doc in documents:
    mapped.extend(map_phase(doc))

grouped = shuffle(mapped)
output = reduce_phase(grouped)

print(sorted(output.items(), key=lambda x: -x[1]))