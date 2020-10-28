sum = 0

with open('editedspydata.csv') as f:
    content = f.readlines()[-200:]
    for line in content:
        split = line.split(',')
        close = split[3]

        sum += float(close)

print(sum)
