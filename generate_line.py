import random
import csv 
from io import StringIO


filesize = 8558                

f = open('notebooks.csv')

with open('random_notebooks.csv', mode='a') as csv_file:
    fieldnames = ['link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    for i in range(10):
        offset = random.randrange(filesize)
        f.seek(offset)                  #go to random position
        f.readline()                    
        random_line = f.readline() 
        arr = list(csv.reader([random_line]))[0]
        
        writer.writerow({'link' : 'http://github.com/' + arr[1]})
