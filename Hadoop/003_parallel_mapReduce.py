from multiprocessing import Pool
from collections import defaultdict

def mapper_worker(chunk):
    """Runs in a separate process."""
    pairs = []
    for line in chunk:
        for word in line.lower().split():
            pairs.append((word, 1))
    return pairs

def parallel_mapreduce(data, num_workers=4):
    # Split data into chunks
    chunk_size = max(1, len(data) // num_workers)
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    # MAP in parallel
    with Pool(num_workers) as pool:
        mapped_chunks = pool.map(mapper_worker, chunks)

    # SHUFFLE
    grouped = defaultdict(list)
    for chunk in mapped_chunks:
        for key, value in chunk:
            grouped[key].append(value)

    # REDUCE
    return {key: sum(values) for key, values in grouped.items()}

lines = ["the cat sat", "the dog ran", "the cat ran", "a dog sat"]
result = parallel_mapreduce(lines, num_workers=2)
print(result)