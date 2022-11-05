#a simple script to create a new 314 assignment folder
import argparse
import mimetypes
import os
import requests
from bs4 import BeautifulSoup
import wget

#intake link as command argument
parser = argparse.ArgumentParser(description='python password cracker')
parser.add_argument('-l', '--link', help = 'link to get files from', required= True)
args = parser.parse_args()        
#get link HTML      
reqs = requests.get(args.link)
soup = BeautifulSoup(reqs.text, 'html.parser')

#loop through links and get links for java and txt files
files = []
for link in soup.find_all('a'):
    file = link.get('href')
    if(file is not None):
        if (".java" in file or '.txt' in file):
            file = file.replace('..', 'https://www.cs.utexas.edu/~scottm/cs314/')
            files.append(file)

#go to target directory from root
os.chdir(r"/home/sahana/Coding/314-assignments")

#find the latest subdir in dir and increment it
all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d) and d.isnumeric()]
latest_subdir = max(all_subdirs, key=os.path.getmtime)
print(all_subdirs)
num = int(latest_subdir) +1
print(num)

#make directory under that name and wget all files in list
os.mkdir(str(num))
os.chdir(str(num))
for file in files:
    wget.download(file)


