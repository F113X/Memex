#!/usr/bin/env python3

from datetime import date, datetime
from os import listdir
from os.path import isfile, join
import os, sys, getopt

file = open('subjects.txt')
directory = 'Notes/'


files = [f for f in listdir(directory) if isfile(join(directory, f))]
print(files)


def review():

    for i in range(len(files)-1):
        path = directory + files[i]
        file = open(path, 'r', encoding = 'utf-8')
        temp = file.readline()

        dateCreated = datetime.strptime(temp.strip(), '%Y-%m-%d').date()
        print(dateCreated)

review()



# if __name__ == '__main__':

#     try:
#         opts, args = getopt.getopt(sys.argv[1:], 'he:r', ['help','edit=','review'])

#     except getopt.GetoptError:
#         print('Error: Invalid argument(s)\n')
#         help()
#         sys.exit(2)
    
#     for opt, arg in opts:
#         if opt in ['-r', '--review']:
#             review()