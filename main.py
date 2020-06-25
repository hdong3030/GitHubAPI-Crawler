from github_api import GitHubAPI
from datetime import date
import datetime
from read_repos import get_all_repos
from get_commits import get_commits, parse_file_commits
import csv
from github import Github
import pygit2


if __name__ == "__main__":
    api = GitHubAPI()

    #get all jupyter notebooks from start date to end date, increment date

    # print('Getting repos...')
    # get_all_repos(datetime.datetime(2019, 2, 3), datetime.datetime(2019, 6, 1), 6, True)
    # print('done!')


    #get all notebooks in csv file by keyword (passed into get_commits function)
    
    # print('Getting Commits...')
    # get_commits("ready")
    # print('done!')


    #get commits with a filter
    # print('Getting Commits...')
    # parse_file_commits()
    # print('done!')


repoClone = pygit2.clone_repository(github.com/hdong3030/GitHubAPI-Crawler, '.')
    



