import sys

current_category = ""
count = 0

for line in sys.stdin:

    category = line.strip()

    if current_category == category:
        count += 1

    else:

        if current_category:
            print(current_category, count)

        current_category = category
        count = 1

print(current_category, count)