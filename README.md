# Assignment-Creator
Python code that automates creating a 314 assignment locally.

## Description
In a Data Structures class at my school, we have to complete programming assignments. The rubric and files for this assingment will be posted online by the proffessor. I realized that each time an assingment was released, I would do the same things:
- Create a new directory in my Coding directory
- Name it the assignment number (1-11)
- wget all of the required files on the assingment webpage (very tedious)
I realized this could be automated with a script, so I took the opportunity to improve my python skills and decided to create a program that would do this for me.

## Usage
python3 assignment.py -l [link]
###Arguments
-l: link. This is the link you want to scan for .java and .txt files to download.

## Future Plans
I want to work on making this more universal as I might have to use it for other classes.
This means changing the naming system as I probably won't have a directory full of subdirectories with numerical names.
(Most likely adding a -n argument for the name of the directory to be created).
This program is quite slow. I'll look for more ways to potentially optimize it as well.
