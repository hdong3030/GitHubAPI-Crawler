from datetime import date, timedelta
from github_api import GitHubAPI
import csv


def get_all_repos(startDate, endDate, timeWindow):
    with open('notebooks.csv', mode='a') as csv_file:
        fieldnames = ['id', 'full name', 'created at', 'size', 'forks count', 'authors']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    api = GitHubAPI()
    change = timedelta(days=timeWindow)
    count = 1
    
    while startDate <= endDate:
        newStart = startDate + change
        api.get_repo("Jupyter%20Notebook", str(startDate), str(newStart))
        count = count + 1
        startDate = newStart