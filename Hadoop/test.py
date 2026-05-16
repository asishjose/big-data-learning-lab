grouped = {'the': [1, 1, 1, 1, 1, 1], 'cat': [1, 1, 1], 'sat': [1, 1], 'on': [1, 1], 'mat': [1], 'hat': [1], 'ate': [1], 'rat': [1]}

print(grouped)

result = {}
for key, values in grouped.items():
    result[key] = sum(values)

print(result)