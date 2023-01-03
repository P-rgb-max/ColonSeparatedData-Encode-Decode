
#!/usr/bin/python3

import sys
import os

csd_file = sys.argv[1]

with open(csd_file, 'r') as csd:
    for line in csd:
        if line.startswith('#'):
            continue

        cols = line.split(':')
        rescols = []
        for col in cols:
            if col.startswith('%'):
                op = os.popen(col.strip('%'))
                rescols.append(op.read())
            elif col.startswith('@'):
                rescols.append(str(exec(col.strip('@'))))
            elif col.startswith('$'):
                rescols.append(os.environ.get(col.strip('$')))
            else:
                rescols.append(col)

        row = ''
        for col in rescols:
            row += col
            row += ','
        row = row[:-1].strip('!').replace('\n', ' ', row.count('\n') - 1).strip('\n')

        print(row)
