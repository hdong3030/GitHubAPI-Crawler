import subprocess
import os
import csv

with open('test.csv', newline='') as csvfile:

    data = csv.DictReader(csvfile)
    
    for row in data:
        repo = row['full name']
        repo_name = repo.split("/")[1]

        #destination dir
        os.chdir("/Users/helendong/Desktop/Research/test_nb")

        #clone repo
        subprocess.run(["git", "clone", "https://github.com/" + repo])

        #make folder
        subprocess.run(["mkdir", repo_name + "_data"])

        os.chdir("/Users/helendong/Desktop/Research/test_nb/" + repo_name)

        #check for .ipynb extension
        p = subprocess.Popen('git ls-tree -r master --name-only', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            line = str(line)
            if '.ipynb' in line:
                line = line.split("'")[1]
                line = line.split("\\")[0]
                os.chdir("/Users/helendong/Desktop/Research/test_nb/" + repo_name + "_data")
                subprocess.run(["wget", "https://raw.githubusercontent.com/" + repo + "/" + "master" + "/" + line])
        
        subprocess.run(["rm", "-rf", "/Users/helendong/Desktop/Research/test_nb/" + repo_name])
