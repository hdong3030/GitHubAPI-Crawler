from github_api import GitHubAPI
import csv
import json

def get_commits(keyword):
    api = GitHubAPI()

    with open('notebooks.csv', newline='') as csvfile:
        with open('commits.csv', mode='a') as csvfile2:
            fieldnames = ['repo', 'message']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)

            data = csv.DictReader(csvfile)
            
            for row in data:
                repo = row['full name']
                commits = api.repo_commits(repo)

                count = 0
                for commit in commits:
                    comm = str(commit).replace("\'", "\"")
                    
                    if "\"message\"" in comm:
                        if keyword in (commit['message']):
                            message = str(commit['message']).replace(',', '.')
                            print(repo + ': ' + message)
                            
                            writer.writerow({
                                'repo': repo,
                                'message': message
                            })