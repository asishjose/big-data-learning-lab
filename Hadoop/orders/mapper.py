# Count Orders Per Product Category

import sys

for line in sys.stdin:
    line = line.strip()

    if line.startswith("order_id"):
        continue

    columns = line.split(",")
    
    product_category = columns[2]
    print(product_category)