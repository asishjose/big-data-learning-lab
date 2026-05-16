import sys

current_type = None
current_count = 0

for line in sys.stdin:
    payment_type, count = line.strip().split('\t')
    count = int(count)

    if current_type == payment_type:
        current_count += count
    else:
        if current_type:
            print(current_type, current_count)

        current_type = payment_type
        current_count = count

if current_type:
    print(current_type, current_count)