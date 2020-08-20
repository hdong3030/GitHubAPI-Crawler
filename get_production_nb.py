from github_api import GitHubAPI
import csv
import json
from get_commits import get_commits, get_files
import subprocess
import os
import csv

def get_production_nb_byEXT():
    api = GitHubAPI()

    with open('notebooks_10k.csv', newline='') as csvfile:
        with open('classifier.csv', mode='a') as csvfile2:
            fieldnames = ['repo', 'production', 'sharing', 'personal']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            data = csv.DictReader(csvfile)

            for row in data:
                production = "False"
                sharing = "False"
                personal = "False"
                
                repo = row['full name']
                print(repo)
                try:
                    file_list = get_files(repo)
                    parser = api.repo_details(repo)
                    if parser["watchers_count"] > 100:
                        print(parser["watchers_count"])
                        sharing = "True"
                
                    for elem in file_list:
                        if ".py" in elem:
                            production = "True"
                            break

                    if (production == "False") and (sharing == "False"):
                        personal = "True"
                    
                    writer.writerow({
                        'repo': repo,
                        'production': production, 
                        'sharing': sharing,
                        'personal': personal
                    })
                except:
                    continue
                
                                
         

def get_production_nb_byFEAT():

    os.chdir("/home/feature/helen/GitHubAPI-Crawler/data/notebooks/Drug_Review_NLP")
    subprocess.run(["nbgrep", "import", "01_Drug_Review_Dataset_Exploration.ipynb"])