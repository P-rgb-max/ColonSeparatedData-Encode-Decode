
#!/usr/bin/python3

import sys
import os

csv_file = sys.argv[1]

with open(csv_file, 'r') as csv:
    first_row = True

    for line in csv:
        row = line.replace(',', ':')
        if first_row:
            first_row = False
            row = '!' + row

        row = row.replace('\n', ' ', row.count('\n') - 1).strip('\n')

        chars = row.split(';')
        if len(chars) > 0:
            lines = []
            for char in chars:
                lines.append(char)
            for nl in lines:
                print(nl)
            continue

        print(row)
