import subprocess
import os
import csv

#for performance increase, clone the file, and remove all that do not have .ipynb extension.
#remove .git also

with open('notebooks_10k.csv', newline='') as csvfile:

    data = csv.DictReader(csvfile)
    
    for row in data:
        repo = row['full name']
        repo_name = repo.split("/")[1]
        folder = repo.replace("/", "~")

        #destination dir
        os.chdir("/DATA/jupyter_data/GITHUB_NOTEBOOKS_DATA")

        #clone repo
        subprocess.run(["git", "clone", "https://github.com/" + repo])

        #make folder
        subprocess.run(["mkdir", folder + "_nb"])

        #back to repo folder
        os.chdir("/DATA/jupyter_data/GITHUB_NOTEBOOKS_DATA/" + repo_name)

        #check for .ipynb extension
        p = subprocess.Popen('git ls-tree -r master --name-only', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            line = str(line)
            if '.ipynb' in line:
                line = line.split("'")[1]
                line = line.split("\\")[0]
                os.chdir("/DATA/jupyter_data/GITHUB_NOTEBOOKS_DATA/" + folder + "_nb")
                subprocess.run(["wget", "https://raw.githubusercontent.com/" + repo + "/" + "master/" + line])
        
        subprocess.run(["rm", "-rf", "/DATA/jupyter_data/GITHUB_NOTEBOOKS_DATA/" + repo_name])