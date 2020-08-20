from github_api import GitHubAPI
from datetime import date
import datetime
from read_repos import get_all_repos
from get_commits import get_commits, parse_file_commits
import csv
from get_production_nb import get_production_nb_byEXT, get_production_nb_byFEAT

if __name__ == "__main__":
    api = GitHubAPI()

    #get all jupyter notebooks from start date to end date, increment date

    # print('Getting repos...')
    # get_all_repos(datetime.datetime(2019, 2, 3), datetime.datetime(2019, 6, 1), 6, True)
    # print('done!')

    # print('Getting Commits...')
    # api.repo_commits("hdong3030/Data-Analysis")
    # print('done!')


    #get all notebooks in csv file by keyword (passed into get_commits function)
    
    # print('Getting Commits...')
    # get_commits("ready")
    # print('done!')


    #get commits with a filter
    # print('Getting Commits...')
    # parse_file_commits()
    # print('done!')

    get_production_nb_byEXT()
    



