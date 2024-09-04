#!/usr/bin/env python3

from datetime import date, datetime
from os import listdir
from os.path import isfile, join
import os, sys, getopt

directory = '/Users/YOUROWNDIR/memex/Notes/'
fileDir = '/Users/YOUROWNDIR/memex/'

file = open(fileDir+'subjects.txt')
subjects = file.readlines()
intervalDays = []

VERSION = '0.1.0'

currentDate = date.today()
tempCurrentDate = str(currentDate)
files = [f for f in listdir(directory) if isfile(join(directory, f))]
if '.DS_Store' in files:
    files.remove('.DS_Store')

def help():
    print('memex -h -e <subject> -r -V -v\n')
    print('\t-h --help\t\tGet help')
    print('\t-e --edit <subject>\tEdit notes')
    print('\t-r --review\t\tReview')
    print('\t-V --version\t\tDisplay Version')
    print('\t-v --view <subject>\tView Notes')


def edit(subject):
    #subject = input('Input subject: ')
    temp = []
    for i in range(len(subjects)):
        temp.append(subjects[i].strip())

    if subject in temp:
        path = directory + subject + tempCurrentDate + '.txt'
        if os.path.isfile(path):
            file = open(path, 'a', encoding = 'utf-8')
            print('enter changes')
            notes = input()
            file.write(notes)
        else:
            file = open(path, 'a', encoding = 'utf-8')
            file.write(tempCurrentDate)
            file.write('\n\n')
            print('enter notes:')
            notes = input()
            file.write(notes)
    else:
        print('subject not found:', subject)

def review():
    for i in range(15):
        intervalDays.append(pow(2, i+1) - 1)

    for i in range(len(files)):
        path = directory + files[i]
        file = open(path, 'r', encoding = 'utf-8')
        temp = file.readlines()

        dateCreated = datetime.strptime(temp[0].strip(), '%Y-%m-%d').date()
        yearCreated = dateCreated.year
        monthCreated = dateCreated.month
        dayCreated = dateCreated.day

        currentYear = currentDate.year
        currentMonth = currentDate.month
        currentDay = currentDate.day

        yearDifference = currentYear - yearCreated
        monthDifference = currentMonth - monthCreated
        dayDifference = currentDay - dayCreated

        if monthDifference > 0:
            dayDifference += 30
        
        if yearDifference > 0:
            dayDifference += 365
        
        if dayDifference in intervalDays:
            for i in range(len(temp)):
                if  temp[i]!= '\n':
                    contents = temp[i].strip()
                else:
                    contents = temp[i]
                print(contents)
            input('press enter when ready')
        else:
            print('No notes in to review today!')

def view(subject):
    print(subject)
    print('(view function is not available yet)')


if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'he:rVv:', ['help','edit=','review','version','view='])

    except getopt.GetoptError:
        print('Error: Invalid argument(s)\n')
        help()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            help()
            sys.exit(2)
        elif opt in ['-e', '--edit']:
            edit(arg)
        elif opt in ['-r', '--review']:
            review()
        elif opt in ['-V', '--version']:
            print('memex prerelease version',VERSION)
        elif opt in ['-v','--view']:
            view(arg)