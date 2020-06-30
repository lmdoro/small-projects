#!/usr/bin/python3

'''
    Script that I wrote to copy all the pictures and videos from my Google Photos archive
    to another folder. Since the files are stored in multiple directories and sub-directories, 
    it would've been cumbersome to copy them manually, especially if the archive size is big
'''
import os
import shutil


SRC = "/mnt/f/Pictures/source"
TARGET = "/mnt/f/Pictures/target"

'''
    Since the photos and videos have the extensions .jpg, .JPG, .MOV, .mp4 or .HEIC
    I chose to rather create a list of the type of files I am not interested in
    because they are just two 
'''

extensions_to_skip = ['.json', '.html']

count = 0
duplicate_file_counter = 1

for root, subdirs, files in os.walk(SRC):
    for file in files:
        if file.endswith(extensions_to_skip[0]) or file.endswith(extensions_to_skip[1]):
            print(file, " skipped")
        elif os.path.isfile(os.path.abspath(os.path.join(TARGET, file))):
            # Replace the dot with the incremented duplicate file counter + another dot and convert the integer to string
            slug = str(duplicate_file_counter) + '.'
            duplicate = file.replace('.', slug)
            # Rename the iterated file and provide the path to it, otherwise it will just rename the variable value
            os.rename(os.path.abspath(os.path.join(root, file)), os.path.abspath(os.path.join(root, duplicate)))
            # Increment the counter and the duplicate file counter
            duplicate_file_counter += 1
            count +=1
            # Copy the renamed file
            shutil.copy(os.path.abspath(os.path.join(root, duplicate)), TARGET)
            print(duplicate, "copied")
        else:
            count += 1
            shutil.copy(os.path.abspath(os.path.join(root, file)), TARGET)
            print(file, "copied")

print(count, " files copied")
print('Done')
