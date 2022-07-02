#!/usr/bin/env python3
#############################
#       MKV BULK SUBS       #
#############################
# Author: Marcos Dos Santos #
# Github: dotvectortech     #
#############################

# Import.
import os

# Yes or No function.
def y_n(question,answer,fail):
    choice = None
    while choice == None:
        print(question)
        choice = input('(y/N): ')
        if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
            print(answer)
        elif choice == '' or choice == 'n' or choice == 'N' or choice == 'no' or choice == 'No':
            print(fail)
            quit()
        else:
            print('Invalid option selected. Exiting')
            quit()

# Creates files for working later.
os.system('ls *.mkv > files.txt')
with open('./files.txt','r') as f:
    files = f.read()
os.system('ls *.srt > subs.txt')
with open('./subs.txt','r') as f:
    subs = f.read()
files = files.rsplit()
subs = subs.rsplit()
if len(files) != len(subs):
    print('No the same amount of MKV files and SRT files')
    quit()

# Creates list, and gives output to check if the script can work.
files_list = list()
subs_list = list()
print('Check for similarity in the MKV and SRT files')
print('Example: This.is.an.example.1e01.mkv AND This is an example s01e01.srt')
for l in range(len(files)):
    f = files[0].split('.mkv')
    files_list.append(f[0])
    s = subs[0].split('.srt')
    subs_list.append(s[0])
    files.pop(0)
    subs.pop(0)
    print(f[0],'AND',s[0])

# Question the user for input about similarity in names of files.
y_n('Are the MKV and SRT similar?','Ok!','Ok, change them and run the script again')

# Creates "no sub" files (Fixing if the files had already subs).
# Creates files with the subs and remove the "no sub" files.
for f,s in zip(files_list,subs_list):
    cmd = 'mkvmerge -o "' + f + '-no-sub.mkv" ' + '--no-subtitles ' + '"' + f + '.mkv"'
    os.system(cmd)
    cmd = 'mkvmerge -o "' + f + '-sub.mkv" ' + '"' + f + '-no-sub.mkv" "' + s + '.srt"'
    os.system(cmd)
    cmd = '/bin/rm "' + f + '-no-sub.mkv"'
    os.system(cmd)

exit()
