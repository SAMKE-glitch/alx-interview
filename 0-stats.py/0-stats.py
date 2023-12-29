#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""

import sys

# store the count of all status codes in a directory
statusCodesDict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                   '404': 0, '405': 0, '500': 0}

totalSize = 0
# keep count of the number lines counted
count = 0

try:
    for line in sys.stdin:
        lineList = line.split(" ")

        if len(lineList) > 4:
            status_code = lineList[-2]
            fileSize = int(lineList[-1])

            # check if the status code receive exists in the dictionary ans
            # increment its count
            if status_code in statusCodesDict.keys():
                statusCodesDict[status_code] += 1

            # update total size
            totalSize += fileSize

            # update count of lines
            count += 1

        if count == 10:
            # reset count
            count = 0
            print('File size: {}'.format(totalSize))

            # print out status codes counts
            for key, value in sorted(statusCodesDict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except Exception as err:
    pass
finally:
    print('File Size: {}'.format(totalSize))
    for key, value in sorted(statusCodesDict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
