import sys

for line in sys.stdin:
    data = line.strip().split(',')

    if len(data) > 2:
        payment_type = data[1]
        print(f"{payment_type}\t1")