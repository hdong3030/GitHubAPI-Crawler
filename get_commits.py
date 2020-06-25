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


def get_files(repo):
    api = GitHubAPI()

    file_list = []

    commits = api.get_commit(repo)
    recent = commits[0]
    comm = recent['commit']

    tree = comm['tree']
    sha = tree['sha']

    files = api.get_file(repo, sha)
    
    arr = files['tree']
        
    for i in range(len(arr)):
        tree = arr[i]
        repo_file = tree['path']
        file_list.append(repo_file)

    return file_list

def parse_file_commits():
    api = GitHubAPI()

    with open('notebooks.csv', newline='') as csvfile:
        with open('commits.csv', mode='a') as csvfile2:
            fieldnames = ['repo', 'file', 'message']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)

            data = csv.DictReader(csvfile)
            
            for row in data:
                repo = row['full name']
                file_list = get_files(repo)

                for i in range(len(file_list)):
                    if '.ipynb' in file_list[i]:
                        commits = api.file_commits(repo, file_list[i])
                        
                        if len(commits) > 2:
                            for commit in commits:
                                comm = commit['commit']
                                
                                writer.writerow({
                                    'repo': repo,
                                    'file': file_list[i],
                                    'message': comm['message']
                                })

                                print(file_list[i])
                                print()



            
            
        



            

    
                            

    