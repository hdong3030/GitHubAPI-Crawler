from github_api import GitHubAPI
import csv
import json
from get_commits import get_commits, get_files

def get_production_nb():
    api = GitHubAPI()

    with open('notebooks_alot.csv', newline='') as csvfile:
        with open('production_nb.csv', mode='a') as csvfile2:
            fieldnames = ['repo']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)

            data = csv.DictReader(csvfile)
            jupyter = False
            python = False
            dvc = False

            for row in data:
                repo = row['full name']
                file_list = get_files(repo)
                print(repo)
            
                for elem in file_list:
                    # if ".py" in elem:
                    #     python = True
                    if "dvc" in elem:
                        dvc = True

                if dvc:
                    writer.writerow({
                        'repo': repo
                    })
                    print("this repository had a dvc file\n")
                    #remove this break for continuous cycle
                    break